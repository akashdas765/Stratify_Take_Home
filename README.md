# Stratify_Take_Home
Structify Take Home Question 

# Chord Intersection Counter

## Overview

This Python program calculates the number of intersections among chords in a circle, using the radian measures of their start and end points, along with unique IDs for each chord. The algorithm is versatile, capable of managing different chord arrangements while accurately detecting intersections, provided that intersections at the exact endpoints of chords are excluded.

## Algorithm Description

The algorithm uses a technique similar to sweep-line, along with sorting events, to effectively identify intersections between multiple chords on a circle, based on their start and end points on the circle's edge.

### Steps Involved

1. **Initialization**: This step involves converting the given radian values and identifiers into a structured format that pairs up the start and end points of each chord.
2. **Event Sorting**: It treats the start and end points of the chords as events and sorts them by their radian values. This mimics a sweep line moving around the circle's circumference.
3. **Intersection Detection**: As it moves, the algorithm keeps track of chords that have started but not finished. It checks for any intersections between these active chords and each new starting chord.



## Time Complexity Analysis of `count_intersections` Function

The `count_intersections` function is designed to calculate the number of intersections between chords on a circle, given arrays of radians and identifiers. This document breaks down the time complexity of the function based on its operations.


The function performs several key operations:

1. Constructs a dictionary to map chords by their identifiers.
2. Sorts events based on the start and end points of chords.
3. Iterates through sorted events to count intersections between chords.

Each of these steps contributes to the overall time complexity of the function.

### Analysis

#### 1. Chords Dictionary Construction

The function iterates once through the input lists, creating a dictionary where each key-value pair corresponds to a chord and its start/end radians:

- **Complexity**: `O(n)` where `n` is the number of chord events.

Dictionary operations such as insertion and lookup are considered `O(1)` on average, making this step linear in complexity.

#### 2. Sorting Events

For each chord, two events (start and end) are created and then all events are sorted based on their radian values:

- **Complexity**: `O(n log n)` for sorting `2n` events (`n` chords result in `2n` events).

This step ensures that events are processed in the correct order, which is essential for accurately counting intersections.

#### 3. Counting Intersections

The function iterates through each event, checking for intersections by comparing active chords:

- **Complexity**: Up to `O(n^2)` in the worst case.

This is because, for each start event, the function might compare the current chord against all other active chords, leading to a nested loop scenario.

### Overall Time Complexity

The dominant factor in determining the function's time complexity is the intersection counting step, with a worst-case scenario of `O(n^2)`. Even though the sorting step has a complexity of `O(n log n)`, the quadratic nature of the intersection check makes it the limiting factor.

Therefore, the overall time complexity of the `count_intersections` function is **`O(n^2)`**.

## Conclusion

While the `count_intersections` function is efficient in organizing and processing chord events, its quadratic time complexity makes it less suitable for very large datasets. The analysis highlights the importance of considering both data organization and the computational cost of nested iterations when assessing algorithm efficiency.
