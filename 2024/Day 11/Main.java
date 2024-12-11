import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicLong;

public class Main {

    private static final int PART1 = 24, BLINKS = 75;
    private static final AtomicLong total = new AtomicLong(0), total2 = new AtomicLong(0);

    public static void handleStone(long num, int blinks) {
        Map<Long, Long> stones = new HashMap<>();
        stones.put(num, 1L);

        for (int i = 0; i < blinks; i++) {
            Map<Long, Long> newStones = new HashMap<>();

            for (Map.Entry<Long, Long> entry : stones.entrySet()) {
                long stone = entry.getKey();
                long count = entry.getValue();

                if (stone == 0) {
                    newStones.merge(1L, count, Long::sum);
                } else if (String.valueOf(stone).length() % 2 == 0) {
                    String stoneStr = String.valueOf(stone);
                    int mid = stoneStr.length() / 2;
                    long part1 = Long.parseLong(stoneStr.substring(0, mid));
                    long part2 = Long.parseLong(stoneStr.substring(mid));
                    newStones.merge(part1, count, Long::sum);
                    newStones.merge(part2, count, Long::sum);
                } else {
                    newStones.merge(stone * 2024, count, Long::sum);
                }
            }

            stones = newStones;
            if (i == PART1) {
                for (long count : stones.values()) {
                    total.addAndGet(count);
                }
            }
        }

        long totalStones = stones.values().stream().mapToLong(Long::longValue).sum();
        total2.addAndGet(totalStones);
    }

    public static void main(String[] args) {
        List<Long> orgStones = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                for (String num : line.split(" ")) {
                    orgStones.add(Long.parseLong(num));
                }
            }
        } catch (IOException e) {
            System.err.println("Failed to read input.txt: " + e.getMessage());
            return;
        }

        List<Thread> threads = new ArrayList<>();
        for (long num : orgStones) {
            Thread thread = new Thread(() -> handleStone(num, BLINKS));
            threads.add(thread);
            thread.start();
        }

        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted: " + e.getMessage());
            }
        }

        System.out.println("Part 1: " + total.get());
        System.out.println("Part 2: " + total2.get());
    }
}