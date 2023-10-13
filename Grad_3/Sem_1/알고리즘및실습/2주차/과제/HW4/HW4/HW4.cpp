#include <iostream>
#include <vector>

using namespace std;

int countsum(int m, vector<int> nums) {
	if (m < 0) return 0;
	if (m == 0) return 1;
	int cnt = 0;
	for (int i = 0; i < nums.size(); i++) {
		cnt += countsum(m - nums[i], nums);
	}
	return cnt;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		cout << countsum(N, nums) << "\n";
	}
	
}