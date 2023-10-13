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