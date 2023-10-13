#### 1주차 과제
## A번 문제
```c++
// set자료구조 미사용

#include <iostream>
 
using namespace std;
 
int main() {
 
    int T = 0;
    cin >> T;
 
    for (int i = 0; i < T; i++) {
        int cnt = 0;
        string S;
        cin >> S;
        for (int j = 3; j < S.length() + 1; j++) {
            if (S[j - 3] != S[j - 2] && S[j - 2] != S[j - 1] && S[j - 3] != S[j - 1]) {
                cnt += 1;
            }
        }
        cout << cnt << endl;
    }
 
    return 0;
}
```
```c++
// set자료구조 사용
#include <iostream>
#include <set>
 
using namespace std;
 
int main() {
 
    int T = 0;
    cin >> T;
 
    for (int i = 0; i < T; i++) {
        int cnt = 0;
        string S;
        cin >> S;
        for (int j = 3; j < S.length() + 1; j++) {
            set<char> s;
            s.insert(S[j - 3]);
            s.insert(S[j - 2]);
            s.insert(S[j - 1]);
            if (s.size() == 3) cnt++;
        }
        cout << cnt << endl;
    }
 
    return 0;
}
```

## B번 문제
```c++
// 합병정렬
#include <iostream>
using namespace std;
 
void merge(int* arr, int left, int mid, int right) {
    int* nums_sorted = new int[right - left + 1];
    int i = left;
    int j = mid + 1;
    int k = 0;
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) nums_sorted[k++] = arr[i++];
        else nums_sorted[k++] = arr[j++];
    }
    if (i > mid) {
        while (j <= right) nums_sorted[k++] = arr[j++];
    }
    else {
        while (i <= mid) nums_sorted[k++] = arr[i++];
    }
    for (i = left, k = 0; i <= right; i++, k++) arr[i] = nums_sorted[k];
    delete[] nums_sorted;
}
 
void mergeSort(int* arr, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
 
int main() {
 
    int T = 0;
    cin >> T;
 
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        int *nums = new int[N];
        for (int j = 0; j < N; j++) cin >> nums[j];
        mergeSort(nums, 0, N - 1);
        for (int j = 0; j < N; j++) cout << nums[j] << " ";
        cout << "\n";
    }
 
    return 0;
}
 
/*
합병정렬의 공간복잡도
 
line 4, line 23, line 40 참고
 
line 4를 보면, 함수의 매개변수로 int *arr을 받고있다. 이는 포인터로 변수의 주소값을 나타낸다.
여기에서는 정수 배열의 이름을 전달함으로써 배열의 주소값을 전달하는것으로 해석할 수 있다.
따라서 해당 함수에서는 추가적인 공간을 사용하지 않는다.
 
line 23을 보면, 함수의 매개변수로 int *arr을 받고있다. line 4와 마찬가지로 배열의 주소값을 전달하는것으로 해석할 수 있다.
따라서 해당 함수에서도 추가적인 공간을 사용하지 않는다.
 
line 40을 보면, int *nums = new int[N];을 통해 N개의 정수형 변수를 저장할 수 있는 배열을 동적할당 하고있다.
따라서 이 부분에서는 N개의 추가 공간을 사용하고 있다.
 
위의 내용을 종합해보았을 때, 이 코드의 공간 복잡도는 O(N)이라고 할 수 있다.
*/
```
```c++
// 팀정렬
#include <iostream>
using namespace std;
const int RUN = 32;
 
void insertionSort(int *arr, int left, int right)
{
    for (int i = left + 1; i <= right; i++) {
        int temp = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
}
 
void merge(int *arr, int l, int m, int r)
{
    int len1 = m - l + 1;
    int len2 = r - m;
    int* left = new int[len1];
    int* right = new int[len2];
    for (int i = 0; i < len1; i++) left[i] = arr[l + i];
    for (int i = 0; i < len2; i++) right[i] = arr[m + 1 + i];
 
    int i = 0;
    int j = 0;
    int k = l;
 
    while (i < len1 && j < len2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        }
        else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }
 
    while (i < len1) {
        arr[k] = left[i];
        k++;
        i++;
    }
 
    while (j < len2) {
        arr[k] = right[j];
        k++;
        j++;
    }
}
 
void timSort(int *arr, int n)
{
 
    for (int i = 0; i < n; i += RUN) insertionSort(arr, i, min((i + RUN - 1), (n - 1)));
    for (int size = RUN; size < n; size = 2 * size) {
        for (int left = 0; left < n; left += 2 * size) {
 
            int mid = left + size - 1;
            int right = min((left + 2 * size - 1), (n - 1));
            if (mid < right) merge(arr, left, mid, right);
        }
    }
}
 
int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        int* nums = new int[N];
        for (int j = 0; j < N; j++) cin >> nums[j];
        timSort(nums, N);
        for (int j = 0; j < N; j++) cout << nums[j] << " ";
        cout << "\n";
    }
    return 0;
}
```
#### 2주차 과제
## A번 문제
```c++
#include <iostream>
#include <algorithm>

using namespace std;

int dx[4][3] = { {0, 1, 1}, {0, 0, 1}, {0, 0, 1}, {0, 1, 1} };
int dy[4][3] = { {0, -1, 0}, {0, 1, 0}, {0, 1, 1}, {0, 0, 1} };
char grid[21][21];
int ans, N, M;

void dfs(int x, int y) {
	if (grid[x][y] != '.') {
		int flag = 0;
		for (int i = 0; !flag && i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (grid[i][j] == '.') {
					dfs(i, j);
					flag = 1;
					break;
				}
			}
		}
		if (!flag) {
			ans += 1;
			return;
		}
	}
	for (int i = 0; i < 4; i++) {
		int can = 1;
		for (int j = 0; j < 3; j++) {
			int nx = x + dx[i][j];
			int ny = y + dy[i][j];
			if (nx < 0 || ny < 0 || nx >= N || ny >= M || grid[nx][ny] != '.') {
				can = 0;
				break;
			}
		}
		if (can) {
			for (int j = 0; j < 3; j++) {
				int nx = x + dx[i][j];
				int ny = y + dy[i][j];
				grid[nx][ny] = '0';
			}
			dfs(x, y);
			for (int j = 0; j < 3; j++) {
				int nx = x + dx[i][j];
				int ny = y + dy[i][j];
				grid[nx][ny] = '.';
			}
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
		cin >> N >> M;
		ans = 0;
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin >> grid[j][k];
			}
		}
		dfs(0, 0);
		cout << ans << "\n";
	}
}
```

## B번 문제
```c++
#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool cansum(int m, vector<int> nums) {
	if (m < 0) return false;
	if (m == 0) return true;
	for (int i = 0; i < nums.size(); i++) {
		if (cansum(m - nums[i], nums) == true) return true;
	}
	return false;
}

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		bool result = cansum(N, nums);
		if (result) cout << "true\n";
		else cout << "false\n";
	}

	return 0;
}
```
## C번 문제
```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> howsum(int m, vector<int> nums) {
	if (m < 0) {
		vector<int> result(1, NULL);
		return result;
	}
	if (m == 0) {
		vector<int> result;
		return result;
	}
	for (int i = 0; i < nums.size(); i++) {
		vector<int> list = howsum(m - nums[i], nums);
		if (find(list.begin(), list.end(), NULL) == list.end()) {
			list.push_back(nums[i]);
			return list;
		}
	}
	vector<int> result(1, NULL);
	return result;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		vector<int> result(howsum(N, nums));
		if (find(result.begin(), result.end(), NULL) == result.end()) {
			cout << result.size() << " ";
			for (int j = 0; j < result.size(); j++) cout << result[j] << " ";
		}
		else {
			cout << "-1";
		}
		cout << "\n";
	}
}
```
## D번 문제
```c++
#include <iostream>
#include <vector>

using namespace std;

int countsum(int m, vector<int> nums) {
	if (m < 0) return 0;
	if (m == 0) return 1;
	int cnt = 0;
	for (int i = 0; i < nums.size(); i++) {
		cnt += countsum(m - nums[i], nums);
	}
	return cnt;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		cout << countsum(N, nums) << "\n";
	}
	
}
```
## E번 문제
```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> bestsum(int m, vector<int> nums) {
	if (m < 0) {
		vector<int> result(1, NULL);
		return result;
	}
	if (m == 0) {
		vector<int> result;
		return result;
	}
	vector<int> best(1, NULL);
	for (int i = 0; i < nums.size(); i++) {
		vector<int> list = bestsum(m - nums[i], nums);
		if (find(list.begin(), list.end(), NULL) == list.end()) {
			if (find(best.begin(), best.end(), NULL) != best.end() || best.size() > list.size() + 1) {
				list.push_back(nums[i]);
				best = list;
			}
		}
	}
	return best;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<int> nums(M);
		for (int j = 0; j < M; j++) cin >> nums[j];
		vector<int> result(bestsum(N, nums));
		if (find(result.begin(), result.end(), NULL) == result.end()) {
			cout << result.size() << " ";
			for (int j = 0; j < result.size(); j++) cout << result[j] << " ";
		}
		else {
			cout << "-1";
		}
		cout << "\n";
	}
}
```
## F번 문제
```c++
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
```

#### 3주차 과제
## A번 문제
```c++
#include <iostream>
#include <vector>
 
using namespace std;
 
pair<vector<int>, int> merge(vector<int>& left, vector<int>& right) {
    int i = 0, j = 0;
    vector<int> result;
    int inversions = 0;
 
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            result.push_back(left[i]);
            i++;
        }
        else {
            result.push_back(right[j]);
            j++;
            inversions += left.size() - i;
        }
    }
 
    result.insert(result.end(), left.begin() + i, left.end());
    result.insert(result.end(), right.begin() + j, right.end());
 
    return make_pair(result, inversions);
}
 
pair<vector<int>, int> count_inversions(vector<int>& arr) {
    if (arr.size() <= 1) {
        return make_pair(arr, 0);
    }
 
    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
 
    auto left_result = count_inversions(left);
    auto right_result = count_inversions(right);
    auto merged_result = merge(left_result.first, right_result.first);
 
    int inversions = left_result.second + right_result.second + merged_result.second;
    return make_pair(merged_result.first, inversions);
}
 
int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<int> arr(N);
        for (int j = 0; j < N; j++) cin >> arr[j];
        auto result = count_inversions(arr);
        cout << result.second << endl;
 
    }
     
 
    return 0;
}
```

## B번 문제
```c++
#include <iostream>
#include <string>
#include <unordered_map>
 
using namespace std;
 
int longestSubstring(string s, int k) {
    int n = s.length();
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    int left = 0, right = n - 1;
    while (left <= right && freq[s[left]] < k) {
        left++;
    }
    while (left <= right && freq[s[right]] < k) {
        right--;
    }
    if (left > right) {
        return 0;
    }
    for (int i = left; i <= right; i++) {
        if (freq[s[i]] < k) {
            return max(longestSubstring(s.substr(left, i - left), k), longestSubstring(s.substr(i + 1, right - i), k));
        }
    }
    return right - left + 1;
}
 
int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int result = longestSubstring(s, k);
        cout << result << "\n";
    }
    return 0;
}
```

## C번 문제
```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
 
using namespace std;
 
struct point {
    int x, y;
};
 
double distance(point a, point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}
 
bool compareX(point a, point b) {
    if (a.x != b.x) return a.x < b.x;
    else if(a.x == b.x) return a.y < b.y;
}
 
bool compareY(point a, point b) {
    if (a.y != b.y) return a.y < b.y;
    else if (a.y == b.y) return a.x < b.x;
}
 
pair<point, point> bfsp(vector<point> p) {
 
    double min = INFINITY;
    pair<point, point> ret;
    for (int i = 0; i < p.size() - 1; i++) {
        for (int j = i + 1; j < p.size(); j++) {
            double d = distance(p[i], p[j]);
            if (min > d && i != j) {
                min = d;
                ret.first = p[i];
                ret.second = p[j];
            }
        }
    }
    return ret;
}
 
pair<point, point> closestSplitPair(vector<point> px, vector<point> py, double d, pair<point, point> ret) {
 
 
    double x = px[px.size() / 2].x;
    vector<point> S;
    for (int i = 0; i < py.size(); i++) {
        if (py[i].x > x - d && py[i].x < x + d) {
            S.push_back(py[i]);
        }
    }
    double best = d;
    if (S.size() != 0) {
        for (int i = 0; i < S.size(); i++) {
            for (int j = 0; j < min(7, int(S.size()) - i); j++) {
                if (i != i + j) {
                    double di = distance(S[i], S[i + j]);
                    if (di < best) {
                        best = di;
                        ret.first = S[i];
                        ret.second = S[i + j];
                    }
                }
            }
        }
    }
     
    return ret;
}
 
pair<point, point> closestPair(vector<point> px, vector<point> py) {
 
 
    if (px.size() <= 3) {
        return bfsp(px);
    }
 
    vector<point> Lx(px.begin(), px.begin() + (px.size() / 2));
    vector<point> Ly;
 
    vector<point> Rx(px.begin() + (px.size() / 2), px.end());
    vector<point> Ry;
 
    for (int i = 0; i < py.size(); i++) {
        if (py[i].x < Lx[Lx.size() - 1].x) {
            Ly.push_back(py[i]);
        }
        else if (py[i].x > Lx[Lx.size() - 1].x) {
            Ry.push_back(py[i]);
        }
        else {
            if (py[i].y <= Lx[Lx.size() - 1].y) {
                Ly.push_back(py[i]);
            }
            else {
                Ry.push_back(py[i]);
            }
        }
    }
 
    pair<point, point> L = closestPair(Lx, Ly);
    pair<point, point> R = closestPair(Rx, Ry);
    double d = min(distance(L.first, L.second), distance(R.first, R.second));
  
    pair<point, point> ret;
    if (d == distance(L.first, L.second)) {
        ret = L;
    }
    else {
        ret = R;
    }
    return closestSplitPair(px, py, d, ret);
 
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
        vector<point> points(N);
        for (int j = 0; j < N; j++) {
            cin >> points[j].x >> points[j].y;
        }
        sort(points.begin(), points.end(), compareX);
        vector<point> Px(points);
        sort(points.begin(), points.end(), compareY);
        vector<point> Py(points);
        pair<point, point> ret = closestPair(Px, Py);
        double result = distance(ret.first, ret.second);
        printf("%.2f\n", result);
 
    }
    return 0;
}
```
#### 4주차 과제
## A번
```c++
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
```
## B번
```c++
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
```
## C번
```c++
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
```