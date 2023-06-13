#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

FILE *fptr;
vector<string> lines;
class Blueprint;
class Pack;
vector<Blueprint*> blueprints;
vector<Blueprint*> blueprints2;
int total_quality_level = 0;
int total_quality_level_2 = 1;

int get_max(vector<int> nums) {
    int Max = nums[0];
    for (int x: nums) {
        if (x > Max) {
            Max = x;
        }
    }
    return Max;
}

class Pack {
public:
    int ore = 0;
    int clay = 0;
    int obsidian = 0;
    int geode = 0;
    int ore_robots = 1;
    int clay_robots = 0;
    int obsidian_robots = 0;
    int geode_robots = 0;
    int time = 0;

    Pack() {}

    Pack(int t, vector<int> robots, vector<int> resources) {
        this->time  = t;
        this->ore_robots = robots[0]; this->clay_robots = robots[1]; this->obsidian_robots = robots[2]; this->geode_robots = robots[3];
        this->ore = resources[0]; this->clay = resources[1]; this->obsidian = resources[2]; this->geode = resources[3];
    }

    int perform_round(Blueprint* blueprint);
};

class Blueprint {
public:
    int ID;
    int ore_robot_cost;
    int clay_robot_cost;
    vector<int> obsidian_robot_cost;
    vector<int> geode_robot_cost;
    int limit;
    int max_geodes = 0;
    map<int, map<vector<int>, set<vector<int> > > > collection;

    Blueprint(int lim, int id, int ore, int clay, vector<int> obsidian, vector<int> geode)
            : limit(lim), ID(id), ore_robot_cost(ore), clay_robot_cost(clay), obsidian_robot_cost(obsidian), geode_robot_cost(geode) {
        for (int t = 1; t <= limit; t++) {
            this->collection[t] = map<vector<int>, set<vector<int> > >();
        }
    }

    void action();

    void filter(int time) {
        for (auto it = this->collection[time].begin(); it != this->collection[time].end(); ++it) {
            vector<int> robots = it->first;
            vector<int> ores, clays, obsidians, geodes;
            for (vector<int> r : this->collection[time][robots]) {
                ores.push_back(r[0]);
                clays.push_back(r[1]);
                obsidians.push_back(r[2]);
                geodes.push_back(r[3]);
            }
            int max_geode = get_max(geodes); int max_obsidian = get_max(obsidians); int max_clay = get_max(clays); int max_ore = get_max(ores);
            for (int t = 1; t < time; t++) {
                if (this->collection[t].count(robots)) {
                    vector<int> ore_variations, clay_variations, obsidian_variations, geode_variations;
                    for (vector<int> resources : this->collection[time][robots]) {
                        if (this->collection[t][robots].count(resources)) {
                            this->collection[t][robots].erase(resources);
                        }
                        else if (max_ore && resources[0] < max_ore && resources[1] == max_clay && resources[2] == max_obsidian && resources[3] == max_geode) {
                            ore_variations.push_back(resources[0]);
                            if (resources[0] < get_max(ore_variations)) {this->collection[time][robots].erase(resources);}
                        }
                        else if (max_clay && resources[0] == max_ore && resources[1] < max_clay && resources[2] == max_obsidian && resources[3] == max_geode) {
                            clay_variations.push_back(resources[1]);
                            if (resources[1] < get_max(clay_variations)) {this->collection[time][robots].erase(resources);}
                        }
                        else if (max_obsidian && resources[0] == max_ore && resources[1] == max_clay && resources[2] < max_obsidian && resources[3] == max_geode) {
                            obsidian_variations.push_back(resources[2]);
                            if (resources[2] < get_max(obsidian_variations)) {this->collection[time][robots].erase(resources);}
                        }
                        else if (max_geode && resources[0] == max_ore && resources[1] == max_clay && resources[2] == max_obsidian && resources[3] < max_geode) {
                            geode_variations.push_back(resources[3]);
                            if (resources[3] < get_max(geode_variations)) {this->collection[time][robots].erase(resources);}
                        }
                    }
                }
            }
        }
    }
};

int Pack::perform_round(Blueprint* blueprint) {
    Pack pack = *this;
    int limit = blueprint->limit;
    if (pack.time == limit) {
        blueprint->max_geodes = max(blueprint->max_geodes, pack.geode);
        return 0;
    }
    vector<int> costs = {blueprint->ore_robot_cost, blueprint->clay_robot_cost, blueprint->obsidian_robot_cost[0], blueprint->geode_robot_cost[0]};
    int max_ore_needed = get_max(costs);
    if (pack.ore_robots < blueprint->clay_robot_cost && blueprint->ore_robot_cost <= pack.ore && pack.ore < max_ore_needed * (limit - 1 - pack.time)) {
        vector<int> robots = {pack.ore_robots + 1, pack.clay_robots, pack.obsidian_robots, pack.geode_robots};
        vector<int> resources =
        {pack.ore - blueprint->ore_robot_cost + pack.ore_robots,
         pack.clay + pack.clay_robots,
         pack.obsidian + pack.obsidian_robots,
         pack.geode + pack.geode_robots};
        if (blueprint->collection[pack.time + 1].count(robots)) {
            blueprint->collection[pack.time + 1][robots].insert(resources);
        }
        else {blueprint->collection[pack.time + 1][robots] = {resources};}
    }
    if (pack.clay_robots < blueprint->obsidian_robot_cost[1] && blueprint->clay_robot_cost <= pack.ore && pack.ore < blueprint->clay_robot_cost * (limit - 1 - pack.time)) {
        vector<int> robots = {pack.ore_robots, pack.clay_robots + 1, pack.obsidian_robots, pack.geode_robots};
        vector<int> resources =
        {pack.ore - blueprint->clay_robot_cost + pack.ore_robots,
         pack.clay + pack.clay_robots,
         pack.obsidian + pack.obsidian_robots,
         pack.geode + pack.geode_robots};
        if (blueprint->collection[pack.time + 1].count(robots)) {
            blueprint->collection[pack.time + 1][robots].insert(resources);
        }
        else {blueprint->collection[pack.time + 1][robots] = {resources};}
    }
    if (pack.obsidian_robots < blueprint->geode_robot_cost[1] && blueprint->obsidian_robot_cost[0] <= pack.ore && pack.ore < blueprint->obsidian_robot_cost[0] * (limit - 1 - pack.time)
        && blueprint->obsidian_robot_cost[1] <= pack.clay && pack.clay < blueprint->obsidian_robot_cost[1] * (limit - 1 - pack.time)) {
        vector<int> robots = {pack.ore_robots, pack.clay_robots, pack.obsidian_robots + 1, pack.geode_robots};
        vector<int> resources =
        {pack.ore - blueprint->obsidian_robot_cost[0] + pack.ore_robots,
         pack.clay - blueprint->obsidian_robot_cost[1] + pack.clay_robots,
         pack.obsidian + pack.obsidian_robots,
         pack.geode + pack.geode_robots};
        if (blueprint->collection[pack.time + 1].count(robots)) {
            blueprint->collection[pack.time + 1][robots].insert(resources);
        }
        else {blueprint->collection[pack.time + 1][robots] = {resources};}
    }
    if (blueprint->geode_robot_cost[0] <= pack.ore && blueprint->geode_robot_cost[1] <= pack.obsidian) {
        vector<int> robots = {pack.ore_robots, pack.clay_robots, pack.obsidian_robots, pack.geode_robots + 1};
        vector<int> resources =
        {pack.ore - blueprint->geode_robot_cost[0] + pack.ore_robots,
         pack.clay + pack.clay_robots,
         pack.obsidian - blueprint->geode_robot_cost[1] + pack.obsidian_robots,
         pack.geode + pack.geode_robots};
        if (blueprint->collection[pack.time + 1].count(robots)) {
            blueprint->collection[pack.time + 1][robots].insert(resources);
        }
        else {blueprint->collection[pack.time + 1][robots] = {resources};}
    }
    vector<int> robots = {pack.ore_robots, pack.clay_robots, pack.obsidian_robots, pack.geode_robots};
    vector<int> resources = {pack.ore + pack.ore_robots, pack.clay + pack.clay_robots, pack.obsidian + pack.obsidian_robots, pack.geode + pack.geode_robots};
    if (blueprint->collection[pack.time + 1].count(robots)) {
        blueprint->collection[pack.time + 1][robots].insert(resources);
    }
    else {blueprint->collection[pack.time + 1][robots] = {resources};}
    return 0;
}

void Blueprint::action() {
    int LB = 1; int UB = 24;
    if (this->limit == 24) {
        Pack pack = Pack();
        pack.perform_round(this);
    }
    else if (this->limit == 32) {
        LB = 21; UB = 32;
        printf("Blueprint %d starting... \n", this->ID);
    }
    for (int t = LB; t <= UB; t++) {
        for (auto it = this->collection[t].begin(); it != this->collection[t].end(); ++it) {
            vector<int> robots = it->first;
            for (vector<int> resources : it->second) {
                Pack new_pack = Pack(t, robots, resources);
                new_pack.perform_round(this);
            }
        }
        if (t > 1 && t < this->limit) {this->filter(t+1);}
    }
    printf("%d: %d\n", this->ID, this->max_geodes);
    if (this->limit == 24) {
        total_quality_level += this->ID * this->max_geodes;
        if (this->ID <= 3) {
            blueprints2[this->ID -  1]->collection = this->collection;
        }
    }
    else if (this->limit == 32) {total_quality_level_2 *= this->max_geodes;}
    this->collection.clear();
}

void initialisation() {
    fptr = fopen("input.txt", "r");
    char line[170];
    int i = 1;
    while (fgets(line, 170, fptr)) {
        int ID;
        int ore_robot_cost;
        int clay_robot_cost;
        int obsidian_robot_ore_cost;
        int obsidian_robot_clay_cost;
        int geode_robot_ore_cost;
        int geode_robot_obsidian_cost;
        if (sscanf(line, "Blueprint %d: Each ore robot costs %d ore. Each clay robot costs %d ore. Each obsidian robot costs %d ore and %d clay. Each geode robot costs %d ore and %d obsidian.",
         &ID, &ore_robot_cost, &clay_robot_cost, &obsidian_robot_ore_cost, &obsidian_robot_clay_cost, &geode_robot_ore_cost, &geode_robot_obsidian_cost) != 7) {
            printf("Error: failed to read integers from line %d\n", i);
        }
        i++;
        vector<int> obsidian_robot_cost = {obsidian_robot_ore_cost, obsidian_robot_clay_cost};
        vector<int> geode_robot_cost = {geode_robot_ore_cost, geode_robot_obsidian_cost};
        Blueprint* blueprint = new Blueprint(24, ID, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost);
        blueprints.push_back(blueprint);
        if (ID <= 3) {
            Blueprint* blueprint2 = new Blueprint(32, ID, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost);
            blueprints2.push_back(blueprint2);
        }
    }
}

int main() {
    initialisation();
    for (Blueprint* blueprint: blueprints) {blueprint->action();}
    printf("Part 1: %d\n", total_quality_level);
    for (Blueprint* blueprint: blueprints) {delete blueprint;}
    for (Blueprint* blueprint: blueprints2) {blueprint->action();}
    printf("Part 2: %d\n", total_quality_level_2);
    for (Blueprint* blueprint: blueprints2) {delete blueprint;}
    return 0;
}
