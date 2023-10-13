#include <iostream>
#include <vector>
#include <time.h>

using namespace std;

int partition(vector<int>& a, int left, int right) {
	srand(time(NULL));
	int pivot_index = rand() % (right + 1 - left) + left;
	int pivot_value = a[pivot_index];

	int temp = a[pivot_index];
	a[pivot_index] = a[right];
	a[right] = temp;

	int store_index = left;
	for (int i = left; i < right; i++) {
		if (a[i] < pivot_value) {
			int buf = a[i];
			a[i] = a[store_index];
			a[store_index] = buf;
			store_index += 1;
		}
	}

	temp = a[right];
	a[right] = a[store_index];
	a[store_index] = temp;

	return store_index;

}

void quick_sort(vector<int>& a, int left, int right) {
	if (left < right) {
		int p = partition(a, left, right);
		quick_sort(a, left, p - 1);
		quick_sort(a, p + 1, right);
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
		quick_sort(nums, 0, N - 1);
		for (int j = 0; j < N; j++) {
			cout << nums[j] << " ";
		}
		cout << "\n";
	}

}