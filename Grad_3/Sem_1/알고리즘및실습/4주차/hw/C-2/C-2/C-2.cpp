#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>

using namespace std;

int partition(int arr[], int p, int r) {
    int x = arr[r];
    int i = p - 1;
    for (int j = p; j <= r - 1; j++) {
        if (arr[j] <= x) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[r]);
    return i + 1;
}

int randomized_partition(int arr[], int p, int r) {
    if (p <= r) {
        int i = rand() % (r - p + 1) + p;
        swap(arr[r], arr[i]);
        return partition(arr, p, r);
    }
}

int randomized_select(int arr[], int p, int r, int i) {
    if (p == r) {
        return arr[p];
    }
    int q = randomized_partition(arr, p, r);
    int k = q - p + 1;
    if (i == k) {
        return arr[q];
    }
    else if (i < k) {
        return randomized_select(arr, p, q - 1, i);
    }
    else {
        return randomized_select(arr, q + 1, r, i - k);
    }
}

int new_index(int i, int n) {
    return (2 * i + 1) % (n | 1);
}

void wiggle_sort(int arr[], int n) {
    int mid = randomized_select(arr, 0, n - 1, (n + 1) / 2);

    int i = 0, j = 0, k = n - 1;
    while (j <= k) {
        if (arr[new_index(j, n)] > mid) {
            swap(arr[new_index(i, n)], arr[new_index(j, n)]);
            i++;
            j++;
        }
        else if (arr[new_index(j, n)] < mid) {
            swap(arr[new_index(j, n)], arr[new_index(k, n)]);
            k--;
        }
        else {
            j++;
        }
    }
}

int main() {

    srand(time(NULL));

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        int* nums = new int[N];
        for (int j = 0; j < N; j++) {
            cin >> nums[j];
        }
        wiggle_sort(nums, N);
        cout << N << "\n";
        for (int j = 0; j < N; j++) {
            cout << nums[j] << " ";
        }
        cout << "\n";
        delete[] nums;
    }

}