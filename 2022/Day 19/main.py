from scanf import scanf
from copy import deepcopy

total_quality_level = 0
total_quality_level_2 = 1

class Blueprint:

    def __init__(self, ID: int, Costs: dict, limit):  # NOQA
        self.ID = ID
        self.limit = limit
        self.ore_robot_cost = Costs['ore']
        self.clay_robot_cost = Costs['clay']
        self.obsidian_robot_cost = Costs['obsidian']
        self.geode_robot_cost = Costs['geode']
        self.max_geodes = 0
        self.pack = Pack(self)
        self.collection = {t: {} for t in range(1, 32 + 1)}

    def filter(self, time):
        for robots in self.collection[time]:
            max_geode = max(r[3] for r in self.collection[time][robots])
            max_obsidian = max(r[2] for r in self.collection[time][robots])
            max_clay = max(r[1] for r in self.collection[time][robots])
            max_ore = max(r[0] for r in self.collection[time][robots])
            for t in range(1, time):
                if robots in self.collection[t]:
                    template = self.collection[t][robots]
                    ore_variations, clay_variations, obsidian_variations, geode_variations = [], [], [], []
                    for resources in self.collection[time][robots].copy():
                        if resources in template:
                            self.collection[time][robots].remove(resources)
                        elif max_ore and resources[3] == max_geode and resources[2] == max_obsidian and resources[1] == max_clay and resources[0] < max_ore:
                            ore_variations.append(resources[0])
                            if resources[0] < max(ore_variations):
                                self.collection[time][robots].remove(resources)
                        elif max_clay and resources[3] == max_geode and resources[2] == max_obsidian and resources[1] < max_clay and resources[0] == max_ore:
                            clay_variations.append(resources[1])
                            if resources[1] < max(clay_variations):
                                self.collection[time][robots].remove(resources)
                        elif max_obsidian and resources[3] == max_geode and resources[2] < max_obsidian and resources[1] == max_clay and resources[0] == max_ore:
                            obsidian_variations.append(resources[2])
                            if resources[2] < max(obsidian_variations):
                                self.collection[time][robots].remove(resources)
                        elif max_geode and resources[3] < max_geode and resources[2] == max_obsidian and resources[1] == max_clay and resources[0] == max_ore:
                            geode_variations.append(resources[3])
                            if resources[3] < max(geode_variations):
                                self.collection[time][robots].remove(resources)

    def action(self):
        global total_quality_level, total_quality_level_2
        LB, UB = 1, 24
        if self.limit == 24:
            self.pack.perform_round()
        elif self.limit == 32:
            LB, UB = 21, 32
            print(f'Blueprint {self.ID} starting...')
        for t in range(LB, UB + 1):
            for robots in self.collection[t].copy():
                for resources in self.collection[t][robots].copy():
                    pack = Pack(self)
                    pack.time = t
                    pack.ore_robots, pack.clay_robots, pack.obsidian_robots, pack.geode_robots = robots
                    pack.ore, pack.clay, pack.obsidian, pack.geode = resources
                    pack.perform_round()
                    del pack
            if 1 < t < self.limit: self.filter(t+1)
        print(f'{self.ID}: {self.max_geodes}')
        if self.limit == 24:
            total_quality_level += self.ID * self.max_geodes
            if self.ID <= 3:
                blueprints2[self.ID - 1].collection = deepcopy(self.collection)
        elif self.limit == 32:
            total_quality_level_2 *= self.max_geodes
        self.collection.clear()

class Pack:

    def __init__(self, blueprint: Blueprint):
        self.time = 0
        self.blueprint = blueprint
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.max_ore_needed = max(blueprint.ore_robot_cost, blueprint.clay_robot_cost, blueprint.obsidian_robot_cost[0], blueprint.geode_robot_cost[0])

    def perform_round(self):
        limit = self.blueprint.limit
        if self.time == limit:
            self.blueprint.max_geodes = max(self.blueprint.max_geodes, self.geode)
            return
        if self.ore_robots < self.blueprint.clay_robot_cost and self.blueprint.ore_robot_cost <= self.ore < self.max_ore_needed * (limit - 1 - self.time):
            robots = (self.ore_robots + 1, self.clay_robots, self.obsidian_robots, self.geode_robots)
            resources = (self.ore - self.blueprint.ore_robot_cost + self.ore_robots,
                         self.clay + self.clay_robots,
                         self.obsidian + self.obsidian_robots,
                         self.geode + self.geode_robots)
            if robots not in self.blueprint.collection[self.time + 1]:
                self.blueprint.collection[self.time + 1][robots] = {resources}
            else:
                self.blueprint.collection[self.time + 1][robots].add(resources)
        if self.clay_robots < self.blueprint.obsidian_robot_cost[1] and self.blueprint.clay_robot_cost <= self.ore < self.blueprint.clay_robot_cost * (limit - 1 - self.time):
            robots = (self.ore_robots, self.clay_robots + 1, self.obsidian_robots, self.geode_robots)
            resources = (self.ore - self.blueprint.clay_robot_cost + self.ore_robots,
                         self.clay + self.clay_robots,
                         self.obsidian + self.obsidian_robots,
                         self.geode + self.geode_robots)
            if robots not in self.blueprint.collection[self.time + 1]:
                self.blueprint.collection[self.time + 1][robots] = {resources}
            else:
                self.blueprint.collection[self.time + 1][robots].add(resources)
        if self.obsidian_robots < self.blueprint.geode_robot_cost[1] and self.blueprint.obsidian_robot_cost[0] <= self.ore < self.blueprint.obsidian_robot_cost[0] * (limit - 1 - self.time) \
            and self.blueprint.obsidian_robot_cost[1] <= self.clay < self.blueprint.obsidian_robot_cost[1] * (limit - 1 - self.time):
            robots = (self.ore_robots, self.clay_robots, self.obsidian_robots + 1, self.geode_robots)
            resources = (self.ore - self.blueprint.obsidian_robot_cost[0] + self.ore_robots,
                         self.clay - self.blueprint.obsidian_robot_cost[1] + self.clay_robots,
                         self.obsidian + self.obsidian_robots,
                         self.geode + self.geode_robots)
            if robots not in self.blueprint.collection[self.time + 1]:
                self.blueprint.collection[self.time + 1][robots] = {resources}
            else:
                self.blueprint.collection[self.time + 1][robots].add(resources)
        if self.blueprint.geode_robot_cost[0] <= self.ore and self.blueprint.geode_robot_cost[1] <= self.obsidian:
            robots = (self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots + 1)
            resources = (self.ore - self.blueprint.geode_robot_cost[0] + self.ore_robots,
                         self.clay + self.clay_robots,
                         self.obsidian - self.blueprint.geode_robot_cost[1] + self.obsidian_robots,
                         self.geode + self.geode_robots)
            if robots not in self.blueprint.collection[self.time + 1]:
                self.blueprint.collection[self.time + 1][robots] = {resources}
            else:
                self.blueprint.collection[self.time + 1][robots].add(resources)
        robots = (self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots)
        resources = (self.ore + self.ore_robots, self.clay + self.clay_robots, self.obsidian + self.obsidian_robots,
                     self.geode + self.geode_robots)
        if robots not in self.blueprint.collection[self.time + 1]:
            self.blueprint.collection[self.time + 1][robots] = {resources}
        else:
            self.blueprint.collection[self.time + 1][robots].add(resources)

with open("input.txt", "r") as f:
    lines = f.read().split('\n')
    blueprints = []
    blueprints2 = []
    for n, line in enumerate(lines, start=1):
        result = scanf("Blueprint %d: Each ore robot costs %d ore. Each clay robot costs %d ore. Each obsidian robot costs %d ore and %d clay. Each geode robot costs %d ore and %d obsidian.", line)
        if len(result) == 7:
            ID, ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost = result
            costs = {'ore': ore_robot_cost, 'clay': clay_robot_cost,
                     'obsidian': (obsidian_robot_ore_cost, obsidian_robot_clay_cost),
                     'geode': (geode_robot_ore_cost, geode_robot_obsidian_cost)}
            blueprints.append(Blueprint(ID, costs, limit=24))
            if ID <= 3:
                blueprints2.append(Blueprint(ID, costs, limit=32))
        else:
            print(f'Error in parsing line {n}.')

for blueprint in blueprints:
    blueprint.action()
print(f"Part 1: {total_quality_level}")
for blueprint in blueprints2:
    blueprint.action()
print(f"Part 2: {total_quality_level_2}")
