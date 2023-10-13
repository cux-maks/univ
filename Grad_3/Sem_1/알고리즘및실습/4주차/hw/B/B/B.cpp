#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <time.h>

using namespace std;

/*
������ ����� �������� �� ��������� ������̴�.
�⺻�� ����� �������� �����̳� ���ĵ� �迭�� ��� ��Ͱ� �ʹ� ����� �����÷θ� ����ų �� �ִ�. 
�� ��������� ������ ��� ���ȣ���� ���ְ� ���� ������ ����� ���ÿ� start, end�� �ε��� ���� �߰��ϸ� �����Ѵ�.
���� ������ ����� �����ĺ��� �ӵ��� �����ȴ�.

���� Ȯ���� �˰����̱� ������ ������ left pivot �Ǵ� right pivot �˰��򺸴� �ǹ��� ���ÿ� �־� ���� ȿ�����̴�.
���� ������ left pivot, right pivot �����ĺ��� �� ������.
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