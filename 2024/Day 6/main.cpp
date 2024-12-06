#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <set>
#include <algorithm>
#include <thread>
#include <atomic>
#define MAX 500

using namespace std;

typedef struct Point {
    int x;
    int y;

    Point() {}
    Point(int x, int y) : x(x), y(y) {}

    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
    bool operator<(const Point& other) const {
        return x < other.x || (x == other.x && y < other.y);
    }
} Point;

typedef struct Position {
    Point point;
    char direction;

    Position() {}
    Position(Point point, char direction) : point(point), direction(direction) {}
} Position;

vector<Point> grid;
vector<Point> obstacles;
vector<array<Point, MAX>> possible_spots;
Position guard;
int MAX_X, MAX_Y;

void readInput() {
    ifstream file("input.txt");
    string line;
    int y = 0;
    array<Point, MAX> spots;
    int i = 0;
    while (std::getline(file, line)) {
        MAX_X = line.size();
        for (int x = 0; x < line.size(); x++) {
            grid.emplace_back(x, y);

            if (line[x] == '^' || line[x] == 'v' || line[x] == '<' || line[x] == '>') {
                guard = Position{{x, y}, line[x]};
            } else if (line[x] == '#') {
                obstacles.emplace_back(x, y); 
            } else {
                if (i < MAX) {
                    spots[i] = {x, y};
                    i++;
                } else {
                    possible_spots.push_back(spots);
                    i = 0;
                    spots[i] = {x, y};
                    i++;
                }
            }     
        }
        y++;
    }
    possible_spots.push_back(spots);     
    MAX_Y = y;
}

Point getNextPoint(Position position) {
    Point point = position.point;
    char direction = position.direction;
    switch (direction) {
        case '^':
            return {point.x, point.y - 1};
        case '>':
            return {point.x + 1, point.y};
        case 'v':
            return {point.x, point.y + 1};
        case '<':
            return {point.x - 1, point.y};
        default:
            return point;
    }
}

char getNextDirection(char direction) {
    switch (direction) {
        case '^':
            return '>';
        case '>':
            return 'v';
        case 'v':
            return '<';
        case '<':
            return '^';
        default:
            return direction;
    }
}

bool pointInGrid(Point point) {
    return point.x >= 0 && point.x < MAX_X && point.y >= 0 && point.y < MAX_Y;
}

int simulate(Position guard, vector<Point>& obstacles) {
    set<Point> visited = {guard.point};
    int duplicates = 0;
    Point nextPoint = getNextPoint(guard);
    while (pointInGrid(nextPoint) && duplicates < visited.size()) {
        if (find(obstacles.begin(), obstacles.end(), nextPoint) != obstacles.end()) {
            char nextDirection = getNextDirection(guard.direction);
            nextPoint = getNextPoint({guard.point, nextDirection});
            while (pointInGrid(nextPoint) && find(obstacles.begin(), obstacles.end(), nextPoint) != obstacles.end()) {
                nextDirection = getNextDirection(nextDirection);
                nextPoint = getNextPoint({guard.point, nextDirection});
            }
            guard = {nextPoint, nextDirection};
        } else {
            guard.point = nextPoint;
        }
        if (visited.find(guard.point) != visited.end()) duplicates++;
        else visited.insert(guard.point);
        nextPoint = getNextPoint(guard);
    }
    if (duplicates >= visited.size()) return -1;
    return visited.size();
}

void worker(const array<Point, MAX>& lst, const vector<Point>& obstacles, atomic<int>& count) {
    for (Point spot : lst) {
        vector<Point> new_obstacles = obstacles;
        new_obstacles.push_back(spot);
        int result = simulate(guard, new_obstacles);
        if (result == -1) count++;
    }
}

int main() {
    readInput();
    printf("Part 1: %d\n", simulate(guard, obstacles));
    atomic<int> count(0);
    vector<thread> threads;
    
    for (int i = 0; i < possible_spots.size(); ++i) {
        threads.emplace_back(worker, cref(possible_spots[i]), cref(obstacles), ref(count));
    }

    for (thread& thread : threads) {
        thread.join();
    }
    printf("Part 2: %d\n", count.load());
    return 0;
}