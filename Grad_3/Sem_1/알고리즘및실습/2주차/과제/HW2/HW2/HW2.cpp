#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool cansum(int m, vector<int> nums) {
	if (m < 0) return false;
	if (m == 0) return true;
	for (int i = 0; i < nums.size(); i++) {
		if (cansum(m - nums[i], nums) == true) return true;
	}
	return false;
}

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		bool result = cansum(N, nums);
		if (result) cout << "true\n";
		else cout << "false\n";
	}

	return 0;
}