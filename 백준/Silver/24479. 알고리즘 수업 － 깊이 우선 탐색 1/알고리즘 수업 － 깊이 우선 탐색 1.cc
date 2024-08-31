#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void dfs(int node, int& order, vector<int> graph[], vector<int>& visited) {
    visited[node] = order;
    order++;

    for (int next : graph[node]) {
        if (visited[next] == 0) {
            dfs(next, order, graph, visited);
        }
    }
}

int main() {
    int N, M, R;
    cin >> N >> M >> R;

    vector<int> graph[N + 1];
    vector<int> visited(N + 1, 0);

    int u, v;
    for (int i = 0; i < M; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);  // 양방향 간선 추가
    }

    // 각 노드의 인접 리스트를 오름차순으로 정렬
    for (int i = 1; i <= N; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    int order = 1;
    dfs(R, order, graph, visited);

    // 방문 순서를 출력
    for (int i = 1; i <= N; i++) {
        printf("%d\n", visited[i]);
    }

    return 0;
}
