#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

int bfs(vector<vector<int>> grid, int N, int M) {
	int dx[] = { 0, 1 };
	int dy[] = { 1, 0 };
	vector<vector<int>> visit(N, vector<int>(M, false));
	int ret = INT_MAX;
	priority_queue<pair<int, pair<int, int>>> q;
	q.push(make_pair(-1 * grid[0][0], make_pair(0, 0)));
	visit[0][0] = true;
	while (!q.empty()) {
		int val = -1 * q.top().first;
		int x = q.top().second.first;
		int y = q.top().second.second;
		q.pop();
		if (x == N - 1 && y == M - 1) {
			ret = min(ret, val);
		}
		for (int i = 0; i < 2; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if ((0 <= nx && nx < N) && (0 <= ny && ny < M)) {
				if (visit[nx][ny] == false) {
					q.push(make_pair(-1 * (val + grid[nx][ny]), make_pair(nx, ny)));
					visit[nx][ny] = true;
				}
			}
		}
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;
		vector<vector<int>> grid(N, vector<int>(M, 0));
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin >> grid[j][k];
			}
		}
		int result = bfs(grid, N, M);
		cout << result << "\n";
	}
	return 0;
}