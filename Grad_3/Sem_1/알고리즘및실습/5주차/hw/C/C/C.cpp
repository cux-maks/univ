#include <iostream>
#include <vector>
#include <time.h>
#include <cstdlib>
#include <algorithm>

using namespace std;

int partition(vector<int>& arr, int left, int right) {

    int pivot_index = left + rand() % (right - left + 1);
    int pivot = arr[pivot_index];

    while (left <= right) {
        while (arr[left] < pivot) left++;
        while (arr[right] > pivot) right--;
        if (left <= right) {
            swap(arr[left], arr[right]);
            left++;
            right--;
        }
    }
    return left;
}

int random_select(vector<int>& arr, int left, int right, int k) {
    if (left == right) return arr[left];

    int pivot_index = partition(arr, left, right);
    if (k <= pivot_index - left) {
        return random_select(arr, left, pivot_index - 1, k);
    }
    else {
        return random_select(arr, pivot_index, right, k - (pivot_index - left));
    }
}

int main() {

    srand(time(NULL));
    
    int T;
    cin >> T;

    while (T--) {
        int N, k, a;
        cin >> N >> k;

        vector<int> freq(2001, 0);
        vector<int> arr(2001, 0);
        for (int i = 0; i < N; i++) {
            cin >> a;
            freq[a + 1000] += 1;
            arr[a + 1000] += 1;
        }

        vector<int> result;

        for (int i = 0; i < k; i++) {
            int cnt = random_select(freq, 0, 2000, 2001 - i);
            for(int j = 0; j < 2001; j++){
                if (arr[j] == cnt) {
                    if (find(result.begin(), result.end(), j - 1000) == result.end()) {
                        result.push_back(j - 1000);
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < k; i++) {
            cout << result[i] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}