#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <time.h>
#include <string>

using namespace std;

int majority_num(vector<int> nums) {

    srand(time(NULL));

    map<int, int> sel;
    int idx;

    // 확률적으로 전체중에서 랜덤으로 한 개의 숫자를 뽑았을 때, 절반 이상을 차지하고있는 수를 V라 할 때, V를 뽑을 확률이 50퍼센트 이상이므로
    // 랜덤으로 뽑은 숫자를 빈도수 배열을 만들어서 가장 많이 나온 값을 반환하는 함수이다.
    // 많이 뽑으면 뽑을수록 정확도가 높아지는 알고리즘이다.
    // 이 방법의 시간 복잡도는
    // 랜덤으로 100회 뽑는 반복문 -> O(100)
    // 100회마다 find함수(선형적으로 탐색) -> 최악의 경우 -> O(2475)
    // 가장 많이 나온 수를 탐색 -> 최악의 경우 -> O(99)
    // 이므로 어떤 길이의 nums가 전달되어도 O(2674)에 해결할 수 있다.

    for (int i = 0; i < 100; i++) {
        idx = rand() % nums.size();
        if (sel.find(nums[idx]) == sel.end()) {
            sel[nums[idx]] = 1;
        }
        else {
            sel[nums[idx]] += 1;
        }
    }

    int val = 0;
    int cnt = 0;
    for (auto i = sel.begin(); i != sel.end(); ++i) {
        if (i->second > cnt) {
            val = i->first;
            cnt = i->second;
        }
    }
    return val;

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
        int result = majority_num(nums);
        cout << result << "\n";
    }

}