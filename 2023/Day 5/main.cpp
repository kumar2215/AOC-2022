#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
#include <algorithm>
#include <memory>
#include <map>
#include <set>

using namespace std;

class range {
public:
    long long lower, upper;

    range(long long lower, long long upper) : lower(lower), upper(upper - 1) {}

    bool contains(long long x) {
        return x >= this->lower && x <= this->upper;
    }
};

class Function {
public:
    map<shared_ptr<range>, long long> ranges;

    explicit Function (map<shared_ptr<range>, long long> ranges) {
        this->ranges = ranges;
    }

    long long operator()(long long x) {
        for (auto &it : this->ranges) {
            range R = *it.first;
            if (R.contains(x)) {
                return x + it.second;
            }
        }
        return x;
    }

    long long inv(long long y) {
        for (auto &it : this->ranges) {
            range R = *it.first;
            const long long c = it.second;
            if (R.contains(y - c)) {
                return y - c;
            }
        }
        return y;
    }

};

fstream Input;
vector<string> lines;
vector<long long> seeds;
vector<shared_ptr<range>> seeds2;
typedef pair<string, string> category;
map<category, shared_ptr<Function>> mappings, mappings2;

long long minimum(const vector<long long>& nums) {
    return *min_element(nums.begin(), nums.end());
}

vector<string> split(string str, char separator) {
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
    long long DR, SR, RL;
    map<shared_ptr<range>, long long> ranges;
    shared_ptr<range> r;
    for (int i = 2; i < lines.size(); i++) {
        line = lines[i];
        if (line.find('-') != string::npos) {
            temp = split(lines[i], '-');
            s = temp[2];
            curr = {temp[0], s.replace(s.find(" map:"), 5, "")};
        } else if (!line.empty()) {
            temp = split(line, ' ');
            DR = stoll(temp[0]);
            SR = stoll(temp[1]);
            RL = stoll(temp[2]);
            r = make_shared<range>(SR, SR + RL);
            ranges.insert({r, DR - SR});
        } else {
            shared_ptr<Function> f = make_shared<Function>(ranges);
            mappings[curr] = f;
            ranges.clear();
        }
    }
    for (auto &it : mappings) {
        curr = it.first;
        mappings2.insert({{curr.second, curr.first}, it.second});
    }
    for (int i = 0; i < seeds.size() / 2; i++) {
        SR = seeds[2 * i]; RL = seeds[2 * i + 1];
        r = make_shared<range>(SR, SR + RL);
        seeds2.push_back(r);
    }
}

long long inv(long long x) {
    string curr = "location";
    category cat;
    shared_ptr<Function> f;
    while (curr != "seed") {
        for (auto &it: mappings2) {
            cat = it.first; f = it.second;
            if (cat.first == curr) {
                break;
            }
        }
        x = (*f).inv(x);
        curr = cat.second;
    }
    return x;
}

bool inside_seeds2(long long x) {
    for (auto &it : seeds2) {
        if ((*it).contains(x)) {
            return true;
        }
    }
    return false;
}

long long get_min_location(vector<long long> seeds) {
    vector<long long> locations = seeds;
    string curr = "seed";
    category cat;
    shared_ptr<Function> f;
    while (curr != "location") {
        for (auto &it : mappings) {
            cat = it.first; f = it.second;
            if (cat.first == curr) {
                break;
            }
        }
        for (int i = 0; i < locations.size(); i++) {
            locations[i] = (*f)(locations[i]);
        }
        curr = cat.second;
    }
    return minimum(locations);
}

int main() {
    initialisation();
    printf("Part 1: %llu\n", get_min_location(seeds));
    long long m = 0;
    while (!inside_seeds2(inv(m))) {
        m++;
    }
    printf("Part 2: %llu", m);
    return 0;
}
