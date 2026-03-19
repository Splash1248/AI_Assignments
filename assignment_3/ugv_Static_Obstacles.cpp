#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

const int GRID_SIZE = 70;

// 8-way movement vectors and their corresponding costs (1 for straight, 1.414 for diagonal)
const int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
const int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
const double cost[] = {1.0, 1.0, 1.0, 1.0, 1.414, 1.414, 1.414, 1.414};

struct Point { int x, y; };
bool operator==(const Point& a, const Point& b) { return a.x == b.x && a.y == b.y; }

struct Node {
    Point pos;
    double g, f;
    bool operator>(const Node& other) const { return f > other.f; }
};

double heuristic(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

bool isValid(int x, int y, const vector<vector<int>>& grid) {
    return (x >= 0 && x < GRID_SIZE && y >= 0 && y < GRID_SIZE && grid[x][y] == 0);
}

void runAStar(const vector<vector<int>>& grid, Point start, Point goal) {
    auto start_time = high_resolution_clock::now();

    vector<vector<double>> min_g(GRID_SIZE, vector<double>(GRID_SIZE, 1e9));
    priority_queue<Node, vector<Node>, greater<Node>> open_set;

    open_set.push({start, 0.0, heuristic(start, goal)});
    min_g[start.x][start.y] = 0.0;

    int nodes_expanded = 0;
    bool found = false;
    double final_cost = 0.0;

    while (!open_set.empty()) {
        Node current = open_set.top();
        open_set.pop();

        if (current.g > min_g[current.pos.x][current.pos.y]) continue;

        nodes_expanded++;

        if (current.pos == goal) {
            found = true;
            final_cost = current.g;
            break;
        }

        for (int i = 0; i < 8; i++) {
            int nx = current.pos.x + dx[i];
            int ny = current.pos.y + dy[i];

            if (isValid(nx, ny, grid)) {
                double new_g = current.g + cost[i];
                if (new_g < min_g[nx][ny]) {
                    min_g[nx][ny] = new_g;
                    double f = new_g + heuristic({nx, ny}, goal);
                    open_set.push({{nx, ny}, new_g, f});
                }
            }
        }
    }

    auto stop_time = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop_time - start_time);

    cout << "--- Measures of Effectiveness ---\n";
    if (found) {
        cout << "Status: Success\n";
        cout << "Path Cost: " << final_cost << "\n";
    } else {
        cout << "Status: Failure (No path exists)\n";
    }
    cout << "Nodes Expanded: " << nodes_expanded << "\n";
    cout << "Execution Time: " << duration.count() << " ms\n\n";
}

vector<vector<int>> generateGrid(double density) {
    vector<vector<int>> grid(GRID_SIZE, vector<int>(GRID_SIZE, 0));
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);

    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (dis(gen) < density) grid[i][j] = 1;
        }
    }

    // Ensure start and goal cells are always free
    grid[0][0] = 0;
    grid[GRID_SIZE-1][GRID_SIZE-1] = 0;
    return grid;
}

int main() {
    Point start = {0, 0};
    Point goal = {GRID_SIZE - 1, GRID_SIZE - 1};

    cout << "Testing Low Density (15%)..." << endl;
    runAStar(generateGrid(0.15), start, goal);

    cout << "Testing Medium Density (30%)..." << endl;
    runAStar(generateGrid(0.30), start, goal);

    cout << "Testing High Density (45%)..." << endl;
    runAStar(generateGrid(0.45), start, goal);

    return 0;
}
