/*
 * Q: In a real world, obstacles can be dynamic and not known a priori. How do you make the UGV navigate and find the optimal path in a dynamic obstacles environment?
 * A: It is in the README.md file under the same folder. Check the answer there.
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

const int GRID_SIZE = 70;
const int SENSOR_RANGE = 5;

const int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
const int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
const double cost[] = {1.0, 1.0, 1.0, 1.0, 1.414, 1.414, 1.414, 1.414};

struct Point { int x, y; };
bool operator==(const Point& a, const Point& b) { return a.x == b.x && a.y == b.y; }
bool operator!=(const Point& a, const Point& b) { return !(a == b); }

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

vector<Point> findPath(const vector<vector<int>>& knownGrid, Point start, Point goal) {
    vector<vector<double>> min_g(GRID_SIZE, vector<double>(GRID_SIZE, 1e9));
    vector<vector<Point>> parent(GRID_SIZE, vector<Point>(GRID_SIZE, {-1, -1}));
    priority_queue<Node, vector<Node>, greater<Node>> open_set;

    open_set.push({start, 0.0, heuristic(start, goal)});
    min_g[start.x][start.y] = 0.0;

    while (!open_set.empty()) {
        Node current = open_set.top();
        open_set.pop();

        if (current.pos == goal) {
            vector<Point> path;
            Point curr = goal;
            while (curr != start) {
                path.push_back(curr);
                curr = parent[curr.x][curr.y];
            }
            return path;
        }

        if (current.g > min_g[current.pos.x][current.pos.y]) continue;

        for (int i = 0; i < 8; i++) {
            int nx = current.pos.x + dx[i];
            int ny = current.pos.y + dy[i];

            if (isValid(nx, ny, knownGrid)) {
                double new_g = current.g + cost[i];
                if (new_g < min_g[nx][ny]) {
                    min_g[nx][ny] = new_g;
                    parent[nx][ny] = current.pos;
                    double f = new_g + heuristic({nx, ny}, goal);
                    open_set.push({{nx, ny}, new_g, f});
                }
            }
        }
    }
    return {};
}

void updateKnownGrid(vector<vector<int>>& knownGrid, const vector<vector<int>>& trueGrid, Point current) {
    for (int i = -SENSOR_RANGE; i <= SENSOR_RANGE; i++) {
        for (int j = -SENSOR_RANGE; j <= SENSOR_RANGE; j++) {
            int nx = current.x + i;
            int ny = current.y + j;
            if (nx >= 0 && nx < GRID_SIZE && ny >= 0 && ny < GRID_SIZE) {
                knownGrid[nx][ny] = trueGrid[nx][ny];
            }
        }
    }
}

void runDynamicAStar(const vector<vector<int>>& trueGrid, Point start, Point goal) {
    vector<vector<int>> knownGrid(GRID_SIZE, vector<int>(GRID_SIZE, 0));
    Point current = start;
    int steps = 0;

    while (current != goal) {
        updateKnownGrid(knownGrid, trueGrid, current);

        vector<Point> path = findPath(knownGrid, current, goal);

        if (path.empty()) {
            cout << "Failure: UGV is trapped by dynamic obstacles!\n";
            return;
        }

        Point next_step = path.back();

        current = next_step;
        steps++;
    }

    cout << "--- Dynamic Navigation MoEs ---\n";
    cout << "Status: Goal Reached!\n";
    cout << "Total Execution Steps Taken: " << steps << "\n";
}

int main() {
    vector<vector<int>> trueGrid(GRID_SIZE, vector<int>(GRID_SIZE, 0));

    // Simulate an unknown "dynamic" wall appearing in the middle of the map
    for(int i = 0; i < 40; i++) trueGrid[30][i] = 1;

    Point start = {0, 0};
    Point goal = {GRID_SIZE - 1, GRID_SIZE - 1};

    runDynamicAStar(trueGrid, start, goal);

    return 0;
}
