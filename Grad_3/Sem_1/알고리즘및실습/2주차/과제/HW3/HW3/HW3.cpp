#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> howsum(int m, vector<int> nums) {
	if (m < 0) {
		vector<int> result(1, NULL);
		return result;
	}
	if (m == 0) {
		vector<int> result;
		return result;
	}
	for (int i = 0; i < nums.size(); i++) {
		vector<int> list = howsum(m - nums[i], nums);
		if (find(list.begin(), list.end(), NULL) == list.end()) {
			list.push_back(nums[i]);
			return list;
		}
	}
	vector<int> result(1, NULL);
	return result;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		vector<int> result(howsum(N, nums));
		if (find(result.begin(), result.end(), NULL) == result.end()) {
			cout << result.size() << " ";
			for (int j = 0; j < result.size(); j++) cout << result[j] << " ";
		}
		else {
			cout << "-1";
		}
		cout << "\n";
	}
}