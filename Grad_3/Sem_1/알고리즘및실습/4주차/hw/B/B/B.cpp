#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <time.h>

using namespace std;

/*
기존의 재귀적 퀵정렬을 비 재귀적으로 만든것이다.
기본의 재귀적 퀵정렬은 역순이나 정렬된 배열의 경우 재귀가 너무 깊어져 오버플로를 일으킬 수 있다. 
비 재귀적으로 구현할 경우 재귀호출을 없애고 직접 스택을 만들어 스택에 start, end의 인덱스 값을 추가하며 진행한다.
따라서 기존의 재귀적 퀵정렬보다 속도가 개선된다.

또한 확률적 알고리즘이기 때문에 기존의 left pivot 또는 right pivot 알고리즘보다 피벗의 선택에 있어 더욱 효율적이다.
따라서 기존의 left pivot, right pivot 퀵정렬보다 더 빠르다.
*/

void quick_sort(vector<int>& nums, int n) {
    srand(time(NULL));
    int pivot_val, tmp;
    int i, j;
    int r = n - 1;
    int l = 0;
    stack<int> s;
    s.push(r);
    s.push(l);

    while (!s.empty()) {
        l = s.top();
        s.pop();
        r = s.top();
        s.pop();
        if (r - l + 1 > 1) {
            int t = rand() % (r - l + 1) + l;
            pivot_val = nums[t];
            nums[t] = nums[r];
            nums[r] = pivot_val;
            i = l - 1;
            j = r;
            while (true) {
                while (nums[++i] < pivot_val);
                while (nums[--j] > pivot_val);
                if (i >= j) break;
                tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }
            tmp = nums[i];
            nums[i] = nums[r];
            nums[r] = tmp;
            s.push(r);
            s.push(i + 1);
            s.push(i - 1);
            s.push(l);
        }
    }
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
        quick_sort(nums, N);
        int res = (N - 1) / 2;
        cout << nums[res] << "\n";
    }

}