#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <map>
#include <tuple>

using namespace std;

vector<char> jets;
int highest_point = 0;
int idx = 1;
int period;
int start;
typedef pair<int, int> coordinates;
vector<coordinates> chamber;
vector<int> diff;

class Rock {
public:
    vector<coordinates> shape;
    vector<coordinates> foot;
    map<coordinates, coordinates> position;

    Rock(vector<coordinates> s) {
        shape = s;
        for (auto point : shape) {
            if (point.first == 0) {
                foot.push_back(point);
            }
            position[point] = make_pair(point.first + 3, point.second + 4 + highest_point);
        }
    }

    int fall(int idx) {
        position.clear();
        for (auto point : shape) {
            position[point] = make_pair(point.first + 3, point.second + 4 + highest_point);
        }
        while (true) {
            char jet = jets[(idx - 1) % jets.size()];
            int shift = (jet == '>') ? 1 : -1;
            bool all_inside = true;
            bool all_free = true;
            for (auto point : position) {
                if (point.second.first + shift < 1 || point.second.first + shift > 7) {
                    all_inside = false;
                    break;
                }
                if (find(chamber.begin(), chamber.end(), make_pair(point.second.first + shift, point.second.second)) != chamber.end()) {
                    all_free = false;
                    break;
                }
            }
            if (all_inside && all_free) {
                for (auto& point : position) {
                    point.second.first += shift;
                }
            }
            bool all_fall = true;
            for (auto point : position) {
                if (find(chamber.begin(), chamber.end(), make_pair(point.second.first, point.second.second - 1)) != chamber.end()) {
                    all_fall = false;
                    break;
                }
            }
            if (all_fall) {
                for (auto& point : position) {
                    point.second.second--;
                }
                idx++;
            } else {
                idx++;
                for (auto point : position) {
                    chamber.push_back(make_pair(point.second.first, point.second.second));
                    highest_point = max(highest_point, point.second.second);
                }
                break;
            }
        }
    return idx;
    }
};

long long int calculate_height(long long int n) {
    long long int N = n - start * 5;
    vector<int> initial;
    vector<int> temp;
    for (int i = 0; i < start * 5; i++) {
        initial.push_back(diff[i]);
        if (i < n) {
            temp.push_back(diff[i]);
        }
    }
    long long int actual_period = period * 5;
    vector<int> interval;
    for (int i = start * 5; i < (start + period) * 5; i++) {
        interval.push_back(diff[i]);
    }
    long long int remainder = N % actual_period;
    long long int sum = accumulate(temp.begin(), temp.end(), 0);
    if (n <= start * 5) {
        return sum;
    }
    else {
        sum += (N / actual_period) * accumulate(interval.begin(), interval.end(), 0);
        for (int i = 0; i < remainder; i++) {
            sum += interval[i];
        }
        return sum;
    }
}

int main() {
    ifstream infile("input.txt");
    char c;
    while (infile >> c) {
        jets.push_back(c);
    }

    for (int i = 1; i <= 7; i++) {
        chamber.push_back(make_pair(i, 0));
    }

    vector<coordinates> r1; r1.push_back(make_pair(0, 0)); r1.push_back(make_pair(1, 0)); r1.push_back(make_pair(2, 0)); r1.push_back(make_pair(3, 0));
    vector<coordinates> r2; r2.push_back(make_pair(1, 0)); r2.push_back(make_pair(0, 1)); r2.push_back(make_pair(1, 1)); r2.push_back(make_pair(2, 1)); r2.push_back(make_pair(1, 2));
    vector<coordinates> r3; r3.push_back(make_pair(0, 0)); r3.push_back(make_pair(1, 0)); r3.push_back(make_pair(2, 0)); r3.push_back(make_pair(2, 1)); r3.push_back(make_pair(2, 2));
    vector<coordinates> r4; r4.push_back(make_pair(0, 0)); r4.push_back(make_pair(0, 1)); r4.push_back(make_pair(0, 2)); r4.push_back(make_pair(0, 3));
    vector<coordinates> r5; r5.push_back(make_pair(0, 0)); r5.push_back(make_pair(1, 0)); r5.push_back(make_pair(0, 1)); r5.push_back(make_pair(1, 1));

    Rock rock1 = Rock(r1); Rock rock2 = Rock(r2); Rock rock3 = Rock(r3); Rock rock4 = Rock(r4); Rock rock5 = Rock(r5);
    Rock rocks[5] = {rock1, rock2, rock3, rock4, rock5};

    vector<int> H;
    for (int i = 1; i <= 8000; i++) {
        Rock rock = rocks[(i - 1) % 5];
        idx = rock.fall(idx);
        H.push_back(highest_point);
    }

    vector<int> heights;
    for (int i = 1; i <= H.size() / 5; i++) {
        heights.push_back(H[5 * i] - H[5 * i - 5]);
    }
    period = 3;
    vector<int> interval1;
    vector<int> interval2;
    vector<int> interval3;

    while (true) {
        start = 3;
        while (start + period < heights.size()) {
            interval1.clear(); interval2.clear(); interval3.clear();
            for (int i = start; i < start + period; i++) {
                interval1.push_back(heights[i]);
            }
            for (int i = start + period; i < start + period * 2; i++) {
                interval2.push_back(heights[i]);
            }
            for (int i = start + period * 2; i < start + period * 3; i++) {
                interval3.push_back(heights[i]);
            }
            if (interval1 == interval2 && interval2 == interval3) {
                break;
            }
            else {
                start++;
            }
        }
        if (interval1 == interval2 && interval2 == interval3) {
            break;
        }
        else {
            period++;
        }
    }

    for (int i = 1; i < H.size(); i++) {
        diff.push_back(H[i] - H [i-1]);
    }

    cout << "Part 1: " << calculate_height(2022) - 1 << endl;
    long long int num = pow(10, 12);
    cout << "Part 2: " << calculate_height(num) << endl;

    return 0;
}
