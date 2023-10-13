#include <iostream>
#include <vector>
#include <time.h>
#include <algorithm>

using namespace std;

pair<int, int> selectMinMax(vector<int> A) {
	int max, min;
	if (A[0] < A[1]) {
		min = A[0]; max = A[1];
	}
	else {
		min = A[1]; max = A[0];
	}
	int n = A.size();
	for (int i = 2; i < n; i += 2) {
		if (A[i] < A[i + 1]) {
			if (A[i] < min) min = A[i];
			if (A[i + 1] > max) max = A[i + 1];
		}
		else {
			if (A[i + 1] < min) min = A[i + 1];
			if (A[i] > max) max = A[i];
		}
	}
	return make_pair(max, min);
}

int main() {

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		srand(time(NULL));
		int N;
		cin >> N;
		vector<int> nums(N);
		for (int j = 0; j < N; j++) cin >> nums[j];
		pair<int, int> result = selectMinMax(nums);
		cout << result.first << " " << result.second << "\n";
	}

	return 0;
}