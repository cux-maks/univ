#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <time.h>
#include <string>

using namespace std;

int majority_num(vector<int> nums) {

    srand(time(NULL));

    map<int, int> sel;
    int idx;

    // Ȯ�������� ��ü�߿��� �������� �� ���� ���ڸ� �̾��� ��, ���� �̻��� �����ϰ��ִ� ���� V�� �� ��, V�� ���� Ȯ���� 50�ۼ�Ʈ �̻��̹Ƿ�
    // �������� ���� ���ڸ� �󵵼� �迭�� ���� ���� ���� ���� ���� ��ȯ�ϴ� �Լ��̴�.
    // ���� ������ �������� ��Ȯ���� �������� �˰����̴�.
    // �� ����� �ð� ���⵵��
    // �������� 100ȸ �̴� �ݺ��� -> O(100)
    // 100ȸ���� find�Լ�(���������� Ž��) -> �־��� ��� -> O(2475)
    // ���� ���� ���� ���� Ž�� -> �־��� ��� -> O(99)
    // �̹Ƿ� � ������ nums�� ���޵Ǿ O(2674)�� �ذ��� �� �ִ�.

    for (int i = 0; i < 100; i++) {
        idx = rand() % nums.size();
        if (sel.find(nums[idx]) == sel.end()) {
            sel[nums[idx]] = 1;
        }
        else {
            sel[nums[idx]] += 1;
        }
    }

    int val = 0;
    int cnt = 0;
    for (auto i = sel.begin(); i != sel.end(); ++i) {
        if (i->second > cnt) {
            val = i->first;
            cnt = i->second;
        }
    }
    return val;

}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<int> nums(N);
        for (int j = 0; j < N; j++) {
            cin >> nums[j];
        }
        int result = majority_num(nums);
        cout << result << "\n";
    }

}