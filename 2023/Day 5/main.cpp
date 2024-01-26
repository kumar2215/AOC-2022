#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class range {
public:
    int64_t lower, upper;

    range(int64_t lower, int64_t upper) : lower(lower), upper(upper - 1) {}

    bool contains(int64_t x) {
        return x >= this->lower && x <= this->upper;
    }
};

class Function {
public:
    vector<pair<range, int64_t>> ranges;

    explicit Function (vector<pair<range, int64_t>> ranges) : ranges(ranges) {}

    int64_t operator()(int64_t x) {
        for (auto &it : this->ranges) {
            if (it.first.contains(x)) {
                return x + it.second;
            }
        }
        return x;
    }

    int64_t inv(int64_t y) {
        for (auto &it : this->ranges) {
            const int64_t c = it.second;
            if (it.first.contains(y - c)) {
                return y - c;
            }
        }
        return y;
    }

};

fstream Input;
vector<string> lines;
vector<int64_t> seeds;
vector<range> seeds2;
typedef pair<string, string> category;
vector<pair<category, Function>> mappings, mappings2;

int64_t minimum(const vector<int64_t>& nums) {
    return *min_element(nums.begin(), nums.end());
}

vector<string> split(const string &str, char separator) {
    int startIndex = 0, endIndex = 0;
    vector<string> result;
    for (int i = 0; i <= str.size(); i++) {
        if (str[i] == separator || i == str.size()) {
            endIndex = i;
            string temp;
            temp.append(str, startIndex, endIndex - startIndex);
            result.push_back(temp);
            startIndex = endIndex + 1;
        }
    }
    return result;
}

void initialisation() {
    string line;
    Input.open("input.txt");
    while (getline(Input, line)) {
        lines.push_back(line);
    }
    lines.push_back("");
    Input.close();
    string s = lines[0];
    s = s.replace(s.find("seeds: "), 7, "");
    for (const string& str: split(s, ' ')) {
        seeds.push_back(stoll(str));
    }
    category curr;
    vector<string> temp;
    int64_t DR, SR, RL;
    vector<pair<range, int64_t>> ranges;
    for (int i = 2; i < lines.size(); i++) {
        line = lines[i];
        if (line.find('-') != string::npos) {
            temp = split(line, '-');
            s = temp[2];
            curr = {temp[0], s.replace(s.find(" map:"), 5, "")};
        } else if (!line.empty()) {
            temp = split(line, ' ');
            DR = stoll(temp[0]);
            SR = stoll(temp[1]);
            RL = stoll(temp[2]);
            range r {SR, SR + RL};
            ranges.push_back({r, DR - SR});
        } else {
            mappings.push_back({curr, Function {ranges} });
            ranges.clear();
        }
    }
    for (auto &it : mappings) {
        curr = it.first;
        mappings2.push_back({{curr.second, curr.first}, it.second});
    }
    for (int i = 0; i < seeds.size() / 2; i++) {
        SR = seeds[2 * i]; RL = seeds[2 * i + 1];
        range r = {SR, SR + RL};
        seeds2.push_back(r);
    }
}

int64_t inv(int64_t x) {
    string curr = "location";
    category cat;
    while (curr != "seed") {
        for (auto &it: mappings2) {
            if (it.first.first == curr) {
                x = it.second.inv(x);
                curr = it.first.second;
                break;
            }
        }
    }
    return x;
}

bool inside_seeds2(int64_t x) {
    for (auto &it : seeds2) {
        if (it.contains(x)) {
            return true;
        }
    }
    return false;
}

int64_t get_min_location() {
    vector<int64_t> locations = seeds;
    string curr = "seed";
    category cat;
    Function f {{}};
    while (curr != "location") {
        for (auto &it : mappings) {
            cat = it.first; f = it.second;
            if (cat.first == curr) {
                break;
            }
        }
        for (int64_t & location : locations) {
            location = (f)(location);
        }
        curr = cat.second;
    }
    return minimum(locations);
}

int main() {
    initialisation();
    printf("Part 1: %llu\n", get_min_location());
    int64_t m = 0;
    int64_t LB = 0;
    int64_t UB = 1;
    while (!inside_seeds2(inv(UB))) {
        UB *= 2;
    }
    while (LB != UB) {
        m = LB + (UB - LB) / 2;
        if (inside_seeds2(inv(m))) {
            UB = m;
        }
        else {
            LB = m + 1;
        }
    }
    printf("Part 2: %llu", m);
    return 0;
}
