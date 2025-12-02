# Advent of Code 2025

This repository contains my solutions to [Advent of Code 2025](https://adventofcode.com/2025)

## Day 1: Secret Entrance
[Day 1](https://adventofcode.com/2025/day/1) involves solving a password based on a list of left/right rotations of a dial. The dial always starts at 50, and the input is a list of rotations in the format of direction (L/R) followed by how many steps the dial is rotated. For part 1 we want to solve how many times the dial is at 0 after a rotation from the input list, and for part 2 we want to solve how many times the dial is at 0 after a single step in a rotation from the input list.

## Day 2: Gift Shop
[Day 2](https://adventofcode.com/2025/day/2) required us to identify invalid IDs from the given ID ranges. For the first part, an ID was considered invalid, if the ID was a number that consisted of same digit sequence repeated twice (e.g. 11, 22, 1010). For the second part, an ID was considered to be invalid if it fully consisted of any digit sequence (including singular digits) being repeated twice or more (e.g. 11, 999, 565656). For both parts the solution was the sum of invalid IDs as per specification of an invalid ID for the part.