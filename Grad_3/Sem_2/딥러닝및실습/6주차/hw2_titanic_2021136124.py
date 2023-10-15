import torch
from torch import nn, optim
from torch.utils.data import random_split, DataLoader, Dataset
from datetime import datetime
import wandb
import argparse
import pandas as pd
import os
# from pathlib import Path
# BASE_PATH = str(Path(__file__).resolve().parent.parent.parent) # BASE_PATH: /Users/yhhan/git/link_dl
# import sys
# sys.path.append(BASE_PATH)

class TitanicDataset(Dataset):
  def __init__(self, X, y):
    self.X = torch.FloatTensor(X)
    self.y = torch.LongTensor(y)

  def __len__(self):
    return len(self.X)

  def __getitem__(self, idx):
    feature = self.X[idx]
    target = self.y[idx]
    return {'input': feature, 'target': target}

  def __str__(self):
    str = "Data Size: {0}, Input Shape: {1}, Target Shape: {2}".format(
      len(self.X), self.X.shape, self.y.shape
    )
    return str

class TitanicTestDataset(Dataset):
  def __init__(self, X):
      self.X = torch.FloatTensor(X)

  def __len__(self):
      return len(self.X)

  def __getitem__(self, idx):
      feature = self.X[idx]
      return {'input': feature}

  def __str__(self):
      str = "Data Size: {0}, Input Shape: {1}".format(
          len(self.X), self.X.shape
      )
      return str

def get_preprocessed_dataset():
    CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))

    train_data_path = os.path.join(CURRENT_FILE_PATH, "train.csv")
    test_data_path = os.path.join(CURRENT_FILE_PATH, "test.csv")

    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    all_df = pd.concat([train_df, test_df], sort=False)
    all_df = get_preprocessed_dataset_1(all_df)
    all_df = get_preprocessed_dataset_2(all_df)
    all_df = get_preprocessed_dataset_3(all_df)
    all_df = get_preprocessed_dataset_4(all_df)
    all_df = get_preprocessed_dataset_5(all_df)
    all_df = get_preprocessed_dataset_6(all_df)

    train_X = all_df[~all_df["Survived"].isnull()].drop("Survived", axis=1).reset_index(drop=True)
    train_y = train_df["Survived"]

    test_X = all_df[all_df["Survived"].isnull()].drop("Survived", axis=1).reset_index(drop=True)

    dataset = TitanicDataset(train_X.values, train_y.values)
    test_dataset = TitanicTestDataset(test_X.values)
    train_dataset, validation_dataset = random_split(dataset, [0.8, 0.2])

    return train_dataset, validation_dataset, test_dataset


def get_preprocessed_dataset_1(all_df):
    # Pclass별 Fare 평균값을 사용하여 Fare 결측치 메우기
    Fare_mean = all_df[["Pclass", "Fare"]].groupby("Pclass").mean().reset_index()
    Fare_mean.columns = ["Pclass", "Fare_mean"]
    all_df = pd.merge(all_df, Fare_mean, on="Pclass", how="left")
    all_df.loc[(all_df["Fare"].isnull()), "Fare"] = all_df["Fare_mean"]
    return all_df


def get_preprocessed_dataset_2(all_df):
    # name을 세 개의 컬럼으로 분리하여 다시 all_df에 합침
    name_df = all_df["Name"].str.split("[,.]", n=2, expand=True)
    name_df.columns = ["family_name", "honorific", "name"]
    name_df["family_name"] = name_df["family_name"].str.strip()
    name_df["honorific"] = name_df["honorific"].str.strip()
    name_df["name"] = name_df["name"].str.strip()
    all_df = pd.concat([all_df, name_df], axis=1)

    return all_df


def get_preprocessed_dataset_3(all_df):
    # honorific별 Age 평균값을 사용하여 Age 결측치 메우기
    honorific_age_mean = all_df[["honorific", "Age"]].groupby("honorific").median().round().reset_index()
    honorific_age_mean.columns = ["honorific", "honorific_age_mean", ]
    all_df = pd.merge(all_df, honorific_age_mean, on="honorific", how="left")
    all_df.loc[(all_df["Age"].isnull()), "Age"] = all_df["honorific_age_mean"]
    all_df = all_df.drop(["honorific_age_mean"], axis=1)

    return all_df


def get_preprocessed_dataset_4(all_df):
    # 가족수(family_num) 컬럼 새롭게 추가
    all_df["family_num"] = all_df["Parch"] + all_df["SibSp"]

    # 혼자탑승(alone) 컬럼 새롭게 추가
    all_df.loc[all_df["family_num"] == 0, "alone"] = 1
    all_df["alone"].fillna(0, inplace=True)

    # 학습에 불필요한 컬럼 제거
    all_df = all_df.drop(["PassengerId", "Name", "family_name", "name", "Ticket", "Cabin"], axis=1)

    return all_df


def get_preprocessed_dataset_5(all_df):
    # honorific 값 개수 줄이기
    all_df.loc[
    ~(
            (all_df["honorific"] == "Mr") |
            (all_df["honorific"] == "Miss") |
            (all_df["honorific"] == "Mrs") |
            (all_df["honorific"] == "Master")
    ),
    "honorific"
    ] = "other"
    all_df["Embarked"].fillna("missing", inplace=True)

    return all_df


def get_preprocessed_dataset_6(all_df):
    # 카테고리 변수를 LabelEncoder를 사용하여 수치값으로 변경하기
    category_features = all_df.columns[all_df.dtypes == "object"]
    from sklearn.preprocessing import LabelEncoder
    for category_feature in category_features:
        le = LabelEncoder()
        if all_df[category_feature].dtypes == "object":
            le = le.fit(all_df[category_feature])
            all_df[category_feature] = le.transform(all_df[category_feature])
    return all_df


class MyModel(nn.Module):
  def __init__(self, n_input, n_output, func):
    super().__init__()

    self.model = nn.Sequential(
        nn.Linear(n_input, wandb.config.n_hidden_unit_list[0]),
        func(),
        nn.Linear(wandb.config.n_hidden_unit_list[0], wandb.config.n_hidden_unit_list[1]),
        func(),
        nn.Linear(wandb.config.n_hidden_unit_list[1], n_output),
        nn.Softmax(dim=1)
    )

  def forward(self, x):
    x = self.model(x)
    return x


def get_model_and_optimizer(f):
  my_model = MyModel(n_input=11, n_output=2, func=f)
  optimizer = optim.SGD(my_model.parameters(), lr=wandb.config.learning_rate)

  return my_model, optimizer


def training_loop(model, optimizer, train_data_loader, validation_data_loader):
  n_epochs = wandb.config.epochs
  loss_fn = nn.CrossEntropyLoss()  # Use a built-in loss function
  next_print_epoch = 100
  best_validation_loss = float('inf')
  patience = int(n_epochs * 0.1)
  no_improvement = 0
  for epoch in range(1, n_epochs + 1):
    loss_train = 0.0
    num_trains = 0
    for train_batch in train_data_loader:
      output_train = model(train_batch['input'])
      loss = loss_fn(output_train, train_batch['target'])
      loss_train += loss.item()
      num_trains += 1

      optimizer.zero_grad()
      loss.backward()
      optimizer.step()

    loss_validation = 0.0
    num_validations = 0
    with torch.no_grad():
      for validation_batch in validation_data_loader:
        output_validation = model(validation_batch['input'])
        loss = loss_fn(output_validation, validation_batch['target'])
        loss_validation += loss.item()
        num_validations += 1

    if loss_validation < best_validation_loss:
        best_validation_loss = loss_validation
        no_improvement = 0
    else:
        no_improvement += 1

    if no_improvement >= patience:
        print(f'Early stopping after {epoch + 1} epochs.')
        break

    wandb.log({
      "Epoch": epoch,
      "Training loss": loss_train / num_trains,
      "Validation loss": loss_validation / num_validations,
    })

    if epoch >= next_print_epoch:
      print(
        f"Epoch {epoch}, "
        f"Training loss {loss_train / num_trains:.4f}, "
        f"Validation loss {loss_validation / num_validations:.4f}, "
      )
      next_print_epoch += 100


def main(args):
    for func in [nn.ReLU, nn.PReLU, nn.ELU, nn.LeakyReLU]:
        current_time_str = datetime.now().astimezone().strftime('%Y-%m-%d_%H-%M-%S')
        for i in range(1):
          config = {
            'epochs': args.epochs,
            'batch_size': args.batch_size,
            'learning_rate': 1e-3,
            'n_hidden_unit_list': [20, 20],
          }

          wandb.init(
            mode="online" if args.wandb else "disabled",
            project= func.__name__ + current_time_str,
            # project="my_model_training " + current_time_str,
            notes=func.__name__ + " performance",
            tags=["my_model", "titanic"],
            name=func.__name__ + " " + current_time_str,
            config=config
          )
          print(args)
          print(wandb.config)

          train_dataset, validation_dataset, test_dataset = get_preprocessed_dataset()

          train_data_loader = DataLoader(dataset=train_dataset, batch_size=16, shuffle=True)
          validation_data_loader = DataLoader(dataset=validation_dataset, batch_size=16, shuffle=True)
          test_data_loader = DataLoader(dataset=test_dataset, batch_size=len(test_dataset))

          linear_model, optimizer = get_model_and_optimizer(func)

          wandb.watch(linear_model)

          print("#" * 50, i, func.__name__)

          training_loop(
            model=linear_model,
            optimizer=optimizer,
            train_data_loader=train_data_loader,
            validation_data_loader=validation_data_loader
          )

          batch = next(iter(test_data_loader))
          output_batch = linear_model(batch['input'])
          prediction_batch = torch.argmax(output_batch, dim=1)
          result = pd.DataFrame(prediction_batch, columns=['Survived'])
          result['PassengerId'] = [i for i in range(892, 1310)]
          result = result[['PassengerId', 'Survived']]
          result.to_csv("submission.csv", index=False)
          wandb.finish()


# https://docs.wandb.ai/guides/track/config
if __name__ == "__main__":
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "--wandb", action=argparse.BooleanOptionalAction, default=True, help="True or False"
        )

        parser.add_argument(
            "-b", "--batch_size", type=int, default=512, help="Batch size (int, default: 512)"
        )

        parser.add_argument(
            "-e", "--epochs", type=int, default=1_000, help="Number of training epochs (int, default:1_000)"
        )

        args = parser.parse_args()

        main(args)
