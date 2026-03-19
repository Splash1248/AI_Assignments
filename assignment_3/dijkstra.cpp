#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <climits>
#include <algorithm>

#include <fstream>
#include <sstream>

using namespace std;


struct Edge {
    string to;
    int distance;
};

typedef unordered_map<string, vector<Edge>> GRAPH;

string toLower(string s) {
    for (char &c : s) c = tolower(c);
    return s;
}


void findShortestPath(GRAPH& G, string start, string goal) {
    unordered_map<string, int> min_dist;
    unordered_map<string, string> parent;

    for (auto const& [city, neighbors] : G) {
        min_dist[city] = INT_MAX;
    }

    if (min_dist.find(start) == min_dist.end()) {
        cout << "Error: Start city not found in dataset." << endl;
        return;
    }

    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;
    min_dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int d = pq.top().first;
        string u = pq.top().second;
        pq.pop();

        if (d > min_dist[u]) continue;
        if (u == goal) break;

        for (auto& edge : G[u]) {
            if (min_dist[u] + edge.distance < min_dist[edge.to]) {
                min_dist[edge.to] = min_dist[u] + edge.distance;
                parent[edge.to] = u;
                pq.push({min_dist[edge.to], edge.to});
            }
        }
    }

    if (min_dist.find(goal) == min_dist.end() || min_dist[goal] == INT_MAX) {
        cout << "No path found from " << start << " to " << goal << endl;
    }
    else {
        cout << "Shortest Distance: " << min_dist[goal] << " km" << endl;
        vector<string> path;
        for (string v = goal; v != ""; v = parent[v]) path.push_back(v);
        reverse(path.begin(), path.end());

        cout << "Path: ";
        for (size_t i = 0; i < path.size(); i++)
            cout << path[i] << (i == path.size() - 1 ? "" : " -> ");
        cout << endl;
    }
}



void loadCSV(GRAPH& G, string filename) {
    ifstream file(filename);
    string line, origin, destination, distStr;

    if (!file.is_open()) {
        cout << "Error: Could not open file " << filename << endl;
        return;
    }

    getline(file, line);

    while (getline(file, line)) {
        stringstream ss(line);

        if (getline(ss, origin, ',') &&
            getline(ss, destination, ',') &&
            getline(ss, distStr, ',')) {

            try {
                int distance = stoi(distStr);
                G[origin].push_back({destination, distance});
                if (G.find(destination) == G.end()) G[destination] = {};
            }
            catch (...) {
                continue;
            }
        }
    }

    file.close();
}



int main() {
    GRAPH G;

    loadCSV(G, "indian-cities-dataset.csv");

    string start, goal;
    cout << "Enter starting city: "; cin >> start;
    cout << "Enter destination city: "; cin >> goal;
    cout << endl;

    start = toLower(start);
    goal = toLower(goal);
    start[0] = start[0] + 'A' - 'a';
    goal[0] = goal[0] + 'A' - 'a';

    findShortestPath(G, start, goal);

    return 0;
}
