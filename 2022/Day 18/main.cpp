#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

FILE *fptr;
vector<vector<int> > input;
vector<int> Xc;
vector<int> Yc;
vector<int> Zc;

void initialisation() {
    fptr = fopen("input.txt", "r");
    char line[10];
    int i = 0;
    while (fgets(line, 10, fptr)) {
        int x, y, z;
        if (sscanf(line, "%d,%d,%d", &x, &y, &z) != 3) {
            printf("Error: failed to read integers from line: %s\n", line);
        }
        vector<int> row;
        row.push_back(x); row.push_back(y); row.push_back(z);
        input.push_back(row);
        Xc.push_back(x); Yc.push_back(y); Zc.push_back(z);
        i++;
    }
    fclose(fptr);
}

vector<vector<int> > empty_spaces;
vector<vector<int> > outer_empty_spaces;
vector<vector<int> > removable;

void adjust() {
    int combined_length = outer_empty_spaces.size() + removable.size();
    vector<vector<int> > combined;
    for (int i = 0; i < combined_length; i++) {
        if (i < outer_empty_spaces.size()) {combined.push_back(outer_empty_spaces[i]);}
        else {combined.push_back(removable[i - outer_empty_spaces.size()]);}
    }
    for (int i = 0; i < combined_length; i++) {
        vector<int> s1 = combined[i];
        int len = empty_spaces.size();
        for (int j = len - 1; j >= 0; j--) {
            vector<int> s2 = empty_spaces[j];
            if (abs(s2[0] - s1[0]) + abs(s2[1] - s1[1]) + abs(s2[2] - s1[2]) == 1) {
                empty_spaces.erase(empty_spaces.begin() + j);
                removable.push_back(s2);
            }
        }
    }
}

int find_surface_area(vector<vector<int> > spaces) {
    int count = 0;
    int size = spaces.size();
    for (int i = 0; i < size; i++) {
        int x1 = spaces[i][0]; int y1 = spaces[i][1]; int z1 = spaces[i][2];
        for (int j = 0; j < size; j++) {
            int x2 = spaces[j][0]; int y2 = spaces[j][1]; int z2 = spaces[j][2];
            if (i != j) {
                if (abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1) == 1) {
                    count++;
                }
            }
        }
    }
    return size * 6 - count;
}

int main() {
    initialisation();
    int mX = *min_element(Xc.begin(), Xc.end()); int mY = *min_element(Yc.begin(), Yc.end()); int mZ = *min_element(Zc.begin(), Zc.end());
    int MX = *max_element(Xc.begin(), Xc.end()); int MY = *max_element(Yc.begin(), Yc.end()); int MZ = *max_element(Zc.begin(), Zc.end());
    for (int x = mX; x <= MX; x++) {
        for (int y = mY; y <= MY; y++) {
            for (int z = mZ; z <= MZ; z++) {
                bool bol = true;
                for (int i = 0; i < input.size(); i++) {
                    if (input[i][0] == x && input[i][1] == y && input[i][2] == z) {
                        bol = false;
                        break;
                    }
                }
                if (bol) {
                    vector<int> coordinate;
                    coordinate.push_back(x); coordinate.push_back(y); coordinate.push_back(z);
                    empty_spaces.push_back(coordinate);
                }
            }
        }
    }
    for (int i = 0; i < empty_spaces.size(); i++) {
        if (empty_spaces[i][0] == mX || empty_spaces[i][0] == MX || empty_spaces[i][1] == mY || empty_spaces[i][1] == MY ||
        empty_spaces[i][2] == mZ || empty_spaces[i][2] == MZ) {
            vector<int> coordinate;
            coordinate.push_back(empty_spaces[i][0]); coordinate.push_back(empty_spaces[i][1]); coordinate.push_back(empty_spaces[i][2]);
            outer_empty_spaces.push_back(coordinate);
        }
    }
    int old_length = empty_spaces.size();
    adjust();
    int new_length = empty_spaces.size();
    while (new_length != old_length) {
        old_length = new_length;
        adjust();
        new_length = empty_spaces.size();
    }
    printf("Part 1: %d\n", find_surface_area(input));
    printf("Part 2: %d\n", find_surface_area(input) - find_surface_area(empty_spaces));
    return 0;
}
