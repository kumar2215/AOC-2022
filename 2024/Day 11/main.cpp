#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <thread>
#include <atomic>

#define PART1 24
#define BLINKS 75

std::atomic<uint64_t> total(0);
std::atomic<uint64_t> total2(0);

void handle_stone(uint64_t num, int blinks) {
    std::unordered_map<uint64_t, uint64_t> stones = {{num, 1}}; 

    for (int i = 0; i < blinks; ++i) {
        std::unordered_map<uint64_t, uint64_t> new_stones;

        for (const auto& [stone, count] : stones) {
            if (stone == 0) {
                new_stones[1] += count;
            } else if (std::to_string(stone).length() % 2 == 0) {
                std::string stone_str = std::to_string(stone);
                size_t mid = stone_str.length() / 2;
                uint64_t part1 = std::stoull(stone_str.substr(0, mid));
                uint64_t part2 = std::stoull(stone_str.substr(mid));
                new_stones[part1] += count;
                new_stones[part2] += count;
            } else {
                new_stones[stone * 2024] += count;
            }
        }

        stones = std::move(new_stones);
        if (i == PART1) {
            for (const auto& [stone, count] : stones) {
                total += count;
            }
        }
    }

    uint64_t total_stones = 0;
    for (const auto& [stone, count] : stones) {
        total_stones += count;
    }
    total2 += total_stones;
}

int main() {
    std::ifstream input_file("input.txt");
    if (!input_file) {
        std::cerr << "Failed to open input.txt" << std::endl;
        return 1;
    }

    std::vector<uint64_t> org_stones;
    std::string line;

    while (std::getline(input_file, line, ' ')) {
        org_stones.push_back(std::stoull(line));
    }
    input_file.close();

    std::vector<std::thread> threads;
    for (uint64_t num : org_stones) {
        threads.emplace_back(handle_stone, num, BLINKS);
    }

    for (auto& t : threads) {
        if (t.joinable()) {
            t.join();
        }
    }

    std::cout << "Part 1: " << total.load() << std::endl;
    std::cout << "Part 2: " << total2.load() << std::endl;
    return 0;
}