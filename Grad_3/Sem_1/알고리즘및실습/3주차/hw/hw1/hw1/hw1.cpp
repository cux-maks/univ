#include <iostream>
#include <vector>

using namespace std;

pair<vector<int>, int> merge(vector<int>& left, vector<int>& right) {
    int i = 0, j = 0;
    vector<int> result;
    int inversions = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            result.push_back(left[i]);
            i++;
        }
        else {
            result.push_back(right[j]);
            j++;
            inversions += left.size() - i;
        }
    }

    result.insert(result.end(), left.begin() + i, left.end());
    result.insert(result.end(), right.begin() + j, right.end());

    return make_pair(result, inversions);
}

pair<vector<int>, int> count_inversions(vector<int>& arr) {
    if (arr.size() <= 1) {
        return make_pair(arr, 0);
    }

    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    auto left_result = count_inversions(left);
    auto right_result = count_inversions(right);
    auto merged_result = merge(left_result.first, right_result.first);

    int inversions = left_result.second + right_result.second + merged_result.second;
    return make_pair(merged_result.first, inversions);
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<int> arr(N);
        for (int j = 0; j < N; j++) cin >> arr[j];
        auto result = count_inversions(arr);
        cout << result.second << endl;

    }


    return 0;
}