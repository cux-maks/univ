#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iterator>

using namespace std;

vector<int> result;
vector<int> sel;
int sel_visit[101] = { 0 };
int visit[1000] = { 0 };

void dfs(vector<int> nums, int depth) {
    if (depth == 4) {
        int x;
        x = nums[sel[0]] * 100 + nums[sel[1]] * 10 + nums[sel[2]];
        if (nums[sel[0]] != 0 && x % 2 == 0 && !visit[x]) {
            visit[x] = 1;
            result.push_back(x);
        }
    }
    else {
        for (int i = 0; i < nums.size(); i++) {
            if (!sel_visit[i]) {
                sel.push_back(i);
                sel_visit[i] = 1;
                dfs(nums, depth + 1);
                sel_visit[i] = 0;
                sel.pop_back();
            }
        }
    }
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string t;
    getline(cin, t);
    int T = stoi(t);
    for (int i = 0; i < T; i++) {
        string n;
        getline(cin, n);
        int N = stoi(n);
        vector<int> nums;
        int check[10] = { 0 };
        string s;
        getline(cin, s);
        stringstream num(s);
        int new_n;
        while (num >> new_n) {
            if (check[new_n] < 3) {
                check[new_n] += 1;
                nums.push_back(new_n);
            }
        }
        
        sort(nums.begin(), nums.end());
        dfs(nums, 1);
        
        ostringstream ors;
        if (!result.empty()) {
            copy(result.begin(), result.end(), ostream_iterator<int>(ors, " "));
        }
        cout << ors.str();
        cout << "\n";
        ors.clear();
        for (int j = 0; j < result.size(); j++) {
            visit[result[j]] = 0;
        }
        
        result.clear();
        sel.clear();
    }
}