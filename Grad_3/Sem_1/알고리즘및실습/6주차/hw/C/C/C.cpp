#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

vector<int> dijkstra(vector<vector<pair<int, int>>> graph, int N, int start) {
	vector<int> dist(N, INT_MAX);
	priority_queue<pair<int, int>> heap;

	dist[start] = 0;
	heap.push(make_pair(0, start));

	while (!heap.empty()) {
		int cost = -heap.top().first;
		int cur = heap.top().second;
		heap.pop();

		for (int i = 0; i < graph[cur].size(); i++) {
			int next = graph[cur][i].first;
			int nCost = graph[cur][i].second;
			if (dist[next] > cost + nCost) {
				dist[next] = cost + nCost;
				heap.push(make_pair(-1 * dist[next], next));
			}
		}
	}

	return dist;

}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K, start, end_Num;
		cin >> N >> K >> start >> end_Num;
		vector<int> end(end_Num);
		for (int j = 0; j < end_Num; j++) cin >> end[j];
		vector<vector<pair<int, int>>> graph(N);
		for (int j = 0; j < K; j++) {
			int a, b, c;
			cin >> a >> b >> c;
			graph[a].push_back(make_pair(b, c));
		}

		vector<int> result(dijkstra(graph, N, start));
		for (int j = 0; j < end_Num; j++) {
			if (result[end[j]] == INT_MAX) cout << "-1 ";
			else cout << result[end[j]] << " ";
		}
		cout << "\n";

	}
	return 0;
}