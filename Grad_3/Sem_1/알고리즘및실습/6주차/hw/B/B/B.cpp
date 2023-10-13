#include <iostream>
#include <vector>
#include <stack>

using namespace std;

bool DFS(int start, vector<vector<int>>& graph, vector<bool>& visited, vector<bool>& recursive_stack) {
    visited[start] = true;
    recursive_stack[start] = true;

    for (int i = 0; i < graph[start].size(); i++) {
        int next = graph[start][i];
        if (!visited[next]) {
            if (DFS(next, graph, visited, recursive_stack))
                return true;
        }
        else if (recursive_stack[next])
            return true;
    }

    recursive_stack[start] = false;
    return false;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, E;
        cin >> N >> E;

        vector<vector<int>> graph(N);

        for (int i = 0; i < E; i++) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
        }

        bool result = false;

        vector<bool> visited(graph.size(), false);
        vector<bool> recursive_stack(graph.size(), false);

        for (int i = 0; i < graph.size(); i++) {
            if (!visited[i]) {
                if (DFS(i, graph, visited, recursive_stack))
                    result = true;
            }
        }

        if (result)
            cout << "true" << endl;
        else
            cout << "false" << endl;
    }

    return 0;
}
