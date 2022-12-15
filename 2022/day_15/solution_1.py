import re
from pathlib import Path

import numpy as np

Position = tuple[int, int]

Y_OF_INTEREST = 2_000_000


def parse_input() -> list[tuple[Position, Position]]:
    input_data = Path('input.txt').read_text().splitlines()

    results = []

    for line in input_data:
        digits = re.findall(r'-?\d+', line)
        results.append(
            (
                (int(digits[0]), int(digits[1])),
                (int(digits[2]), int(digits[3])),
            )
        )

    return results


def get_taxicab_distance(a: Position, b: Position) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    input_data = parse_input()

    input_data_with_taxicab_distances = [
        (sensor, beacon, get_taxicab_distance(sensor, beacon))
        for sensor, beacon in input_data
    ]

    max_taxicab_distance = max(
        taxicab_distance
        for _, _, taxicab_distance in input_data_with_taxicab_distances
    )

    min_x_sensor = min(
        sensor[0]
        for sensor, _, _ in input_data_with_taxicab_distances
    )
    max_x_sensor = max(
        sensor[0]
        for sensor, _, _ in input_data_with_taxicab_distances
    )

    min_x = min_x_sensor - max_taxicab_distance
    max_x = max_x_sensor + max_taxicab_distance

    y = Y_OF_INTEREST

    x_vals = np.arange(min_x, max_x + 1)
    x_track = np.array([False] * (max_x - min_x + 1))
    print(x_vals.shape)

    sensors_at_y = {
        sensor
        for sensor, _, _ in input_data_with_taxicab_distances
        if sensor[1] == y
    }
    beacons_at_y = {
        beacon
        for _, beacon, _ in input_data_with_taxicab_distances
        if beacon[1] == y
    }

    for sensor, _, taxicab_distance in input_data_with_taxicab_distances:
        x_track = np.logical_or(
            x_track,
            abs(x_vals - sensor[0]) + abs(y - sensor[1]) <= taxicab_distance,
        )

    print(x_track.sum() - len(beacons_at_y) - len(sensors_at_y))


if __name__ == '__main__':
    main()
