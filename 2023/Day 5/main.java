import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

class Range {
    long lower, upper;

    Range(long lower, long upper) {
        this.lower = lower;
        this.upper = upper;
    }

    boolean contains(long x) {
        return x >= this.lower && x <= this.upper;
    }

}

class Function {

    HashMap<Range, Long> ranges = new HashMap<Range, Long>();

    Function() {}

    Function(HashMap<Range, Long> ranges) {
        this.ranges = ranges;
    }

    Function(Function f) {
        this.ranges = f.ranges;
    }
    long call(long x) {
        for (Range R: this.ranges.keySet()) {
            if (R.contains(x)) {
                return x + this.ranges.get(R);
            }
        }
        return x;
    }

    long inv(long y) {
        for (Range R: this.ranges.keySet()) {
            long c = ranges.get(R);
            if (R.contains(y - c)) {
                return y - c;
            }
        }
        return y;
    }

}

public class Main {
    public static ArrayList<Long> seeds = new ArrayList<Long>();
    public static ArrayList<Range> seeds2 = new ArrayList<Range>();
    public static HashMap<ArrayList<String>, Function> mappings = new HashMap<ArrayList<String>, Function>();
    public static HashMap<ArrayList<String>, Function> mappings2 = new HashMap<ArrayList<String>, Function>();

    public static void main(String[] args) {
        initialisation();
        System.out.println("Part 1: " + get_min_location());
        long m = 0;
        while (!inside_seeds2(inv(m))) {
            m++;
        }
        m--;
        System.out.println("Part 2: " + m);
    }
    public static void initialisation() {

        File input = new File("input.txt");
        ArrayList<String> lines = new ArrayList<String>();
        if (input.exists()) {
            try {
                Scanner reader = new Scanner(input);
                while (reader.hasNextLine()) {
                    lines.add(reader.nextLine());
                }
                lines.add("");
                reader.close();
            } catch (FileNotFoundException e) {
                System.out.println("File not found: " + e.getMessage());
            }
        } else {
            System.out.println("File does not exist.");
        }
        String s = lines.get(0);
        s = s.replaceFirst("seeds: ", "");
        for (String num: s.split(" ")) {
            seeds.add(Long.parseLong(num));
        };
        ArrayList<String> curr = new ArrayList<String>();
        Range R;
        HashMap<Range, Long> ranges = new HashMap<Range, Long>();
        for (int i = 2; i < lines.size(); i++) {
            String line = lines.get(i);
            if (line.contains("-")) {
                String[] temp = line.split("-");
                curr.add(temp[0]);
                curr.add(temp[2].replace(" map:", ""));
            } else if (!line.isBlank()) {
                String[] temp = line.split(" ");
                long DR = Long.parseLong(temp[0]);
                long SR = Long.parseLong(temp[1]);
                long RL = Long.parseLong(temp[2]);
                R = new Range(SR, SR + RL);
                ranges.put(R, DR - SR);
            } else {
                Function f = new Function(new HashMap<Range, Long>(ranges));
                mappings.put(new ArrayList<String>(curr), f);
                curr.clear();
                ranges.clear();
            }
        }
        for (ArrayList<String> S: mappings.keySet()) {
            ArrayList<String> temp = new ArrayList<String>();
            temp.add(S.get(1));
            temp.add(S.get(0));
            mappings2.put(temp, mappings.get(S));
        }
        for (int i = 0; i < seeds.size() / 2; i++) {
            long SR = seeds.get(2 * i);
            long RL = seeds.get(2 * i + 1);
            Range r = new Range(SR, SR + RL);
            seeds2.add(r);
        }
    }

    public static long inv(long x) {
        String curr = "location";
        ArrayList<String> cat = new ArrayList<String>();
        Function f = new Function();
        while (!curr.equals("seed")) {
            for (ArrayList<String> S : mappings2.keySet()) {
                if (S.get(0).equals(curr)) {
                    cat = S;
                    f = mappings2.get(S);
                    break;
                }
            }
            x = f.inv(x);
            curr = cat.get(1);
        }
        return x;
    }

    public static boolean inside_seeds2(long x) {
        for (Range R: seeds2) {
            if (R.contains(x)) {
                return true;
            }
        }
        return false;
    }

    public static long get_min_location() {
        ArrayList<Long> locations = new ArrayList<Long>(seeds);
        String curr = "seed";
        ArrayList<String> cat = new ArrayList<String>();
        Function f = new Function();
        while (!curr.equals("location")) {
            for (ArrayList<String> S: mappings.keySet()) {
                if (S.get(0).equals(curr)) {
                    cat = S;
                    f = mappings.get(S);
                    break;
                }
            }
            for (int i = 0; i < locations.size(); i++) {
                locations.set(i, f.call(locations.get(i)));
            }
            curr = cat.get(1);
        }
        long min = Long.MAX_VALUE;
        for (long x: locations) {
            if (x < min) {
                min = x;
            }
        }
        return min;
    }
}
