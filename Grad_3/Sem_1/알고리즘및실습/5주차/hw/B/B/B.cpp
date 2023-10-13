#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>
#include <climits>

using namespace std;

int secondMax(std::vector<int>& A) {
    int n = A.size();
    std::vector<int> S(n);
    for (int i = 0; i < n; i++) S.push_back(A[i]);

    int L = S.size() - 1;
    int R = S.size() - 2;

    for (int i = n - 1; i >= 1; i--) {
        
        if (S[L] > S[R]) {
            S[i] = S[L];
        }
        else {
            S[i] = S[R];
        }
        L -= 2;
        R -= 2;

    }

    int m = S[1];
    int ret = INT_MIN;
    int left = 2;

    int curr, maxLoc;

    while (left <= n * 2 - 1) {
        
        if (S[left] == m) {
            curr = S[left + 1];
            maxLoc = left;
        }
        else {
            curr = S[left];
            maxLoc = left + 1;
        }
        if (curr == m) return m;
        ret = max(ret, curr);
        left = 2 * maxLoc;
    }

    return ret;

}

int main() {

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        cout << secondMax(A) << "\n";
    }

    return 0;
}