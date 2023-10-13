#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void wiggleSort(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	vector<int> arr = nums;
	int p = (nums.size() - 1) / 2, q = nums.size() - 1;
	for (int i = 0, j = 1; i < nums.size(); i += 2, j += 2) {
		nums[i] = arr[p--];
		if (j < nums.size()) nums[j] = arr[q--];
	}
}

int main() {

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		vector<int> nums(N);
		for (int j = 0; j < N; j++) {
			cin >> nums[j];
		}
		wiggleSort(nums);
		cout << N << "\n";
		for (int j = 0; j < N; j++) {
			cout << nums[j] << " ";
		}
		cout << "\n";
	}


}