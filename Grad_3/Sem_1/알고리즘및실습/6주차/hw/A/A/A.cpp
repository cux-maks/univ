#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int bfs(vector<vector<int>> graph, vector<bool>& visited, int G, int s) {
	int result = 1;
	queue<int> q;
	visited[s] = true;
	q.push(s);

	while (!q.empty()) {
		
		int v = q.front();
		q.pop();
		for (int i = 0; i < graph[v].size(); i++) {
			if (visited[graph[v][i]] == false) {
				result += 1;
				visited[graph[v][i]] = true;
				q.push(graph[v][i]);
			}
		}
	}

	return result;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K;
		cin >> N >> K;
		vector<vector<int>> graph(N);
		for (int j = 0; j < K; j++) {
			int a, b;
			cin >> a >> b;
			graph[a].push_back(b);
			graph[b].push_back(a);
		}

		int result = 0;
		int cnt = 0;

		vector<bool> visited(N, false);

		for(int j = 0; j < N; j++){

			if (visited[j] == false) {
				int val = bfs(graph, visited, N, j);
				result = max(result, val);
				cnt += 1;
			}
		}

		cout << cnt << " " << result << "\n";
	}
	return 0;
}