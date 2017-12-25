import math
import numpy as np

pi = math.pi


def round_nearest(x, a):
    return round(x / a) * a


def get_hex_angle(angle):
    return round_nearest(angle + pi/6, pi/3) - pi/6


def get_max_dist(steps):
    delta = {}
    delta["n"] = np.array([0., 1])
    delta["ne"] = np.array([math.cos(pi/6), math.sin(pi/6)])
    delta["se"] = np.array([math.cos(-pi/6), math.sin(-pi/6)])
    delta["s"] = np.array([0., -1])
    delta["sw"] = np.array([math.cos(-5*pi/6), math.sin(-5*pi/6)])
    delta["nw"] = np.array([math.cos(5*pi/6), math.sin(5*pi/6)])
    point = np.array([0., 0])

    max_dist = 0
    for step in steps:
        point += delta[step]

        # get principle component
        s3 = np.linalg.norm(point)
        angle = math.atan2(point[1], point[0])
        hex_angle = get_hex_angle(angle)
        a1 = abs(hex_angle - angle)
        a3 = 2*pi/3
        a2 = pi - a1 - a3  # inner triangle angles sum to pi
        s1 = s3 / math.sin(a3) * math.sin(a1)  # law of sines
        s2 = s3 / math.sin(a3) * math.sin(a2)  # law of sines
        if s1 + s2 > max_dist:
            max_dist = s1 + s2

    return max_dist


if __name__ == "__main__":
    with open("input.txt") as filename:
        steps = filename.read().strip("\n").split(",")
    dist = get_max_dist(steps)
    print(dist)
