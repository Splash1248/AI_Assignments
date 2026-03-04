#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void dijkstra(int s, int n, vector<vector<pair<int, int>>> &adj) {
  vector<int> dist(n, 1e9);
  priority_queue< pair<int,int>, vector<pair<int, int>>, greater<pair<int, int>> > pq;
  dist[s] = 0;
  pq.push({0, s});

  while (!pq.empty()) {
    int d = pq.top().first;
    int u = pq.top().second;
    pq.pop();

    if (d > dist[u])
      continue;

    for (auto edge : adj[u]) {
      int v = edge.first;
      int w = edge.second;
      if (dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w;
        pq.push({dist[v], v});
      }
    }
  }

  for (int i = 0; i < n; i++) {
    if (dist[i] == 1e9)
      cout << "-1 ";
    else
      cout << dist[i] << " ";
  }
  cout << endl;
}

int main() {
  int n, e;
  cout << "Enter the number of vertices and edges: ";
  cin >> n >> e;

  vector<vector<pair<int, int>>> adj(n);
  cout << "Enter the edges (u v weight): ";
  for (int i = 0; i < e; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].push_back({v, w});
    adj[v].push_back({u, w});
  }

  int source;
  cout << "Enter source vertex: ";
  cin >> source;

  dijkstra(source, n, adj);

  return 0;
}
