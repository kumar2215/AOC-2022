import java.io.File
import kotlin.math.abs

val centres = File("input.txt").readLines().map { it.split(',').map { it.toInt() } }
val X = centres.map { it[0] }
val Y = centres.map { it[1] }
val Z = centres.map { it[2] }

var empty_spaces = mutableListOf<List<Int>>()
for (x in X.min() ..X.max()) {
    for (y in Y.min() .. Y.max()) {
        for (z in Z.min() ..Z.max()) {
            val space = listOf<Int>(x, y, z)
            if (!centres.contains(space)) {
                empty_spaces.add(space)
            }
        }
    }
}

val outer_empty_spaces = mutableListOf<List<Int>>()
for (s in empty_spaces) {
    if (s[0] in listOf<Int>(X.min(), X.max()) || s[1] in listOf<Int>(Y.min(), Y.max()) || s[2] in listOf<Int>(Z.min(), Z.max())) {
        outer_empty_spaces.add(s)
    }
}

val removable = mutableListOf<List<Int>>()

fun adjust() {
    for (s1 in (outer_empty_spaces + removable.toMutableList())) {
        for (s2 in empty_spaces.toMutableList()) {
            val dist = abs(s2[0] - s1[0]) + abs(s2[1] - s1[1]) + abs(s2[2] - s1[2])
            if (dist == 1) {
                empty_spaces.remove(s2)
                removable.add(s2)
            }
        }
    }
}

var old_length = empty_spaces.size
adjust()
var new_length = empty_spaces.size
while (new_length != old_length) {
    old_length = new_length
    adjust()
    new_length = empty_spaces.size
}

inline fun find_surface_area(spaces: List<List<Int>>) : Int {
    var count = 0
    for (c1 in spaces) {
        for (c2 in spaces) {
            val dist = abs(c2[0] - c1[0]) + abs(c2[1] - c1[1]) + abs(c2[2] - c1[2])
            if (c2 != c1 && dist == 1) {
                count++
            }
        }
    }
    return spaces.size * 6 - count
}

println("Part 1: ${find_surface_area(centres)}")
println("Part 2: ${find_surface_area(centres) - find_surface_area(empty_spaces)}")
