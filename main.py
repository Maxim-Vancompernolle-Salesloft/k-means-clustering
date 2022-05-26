import random as r
import math as m
import turtle as t
from turtle import *

k = 4
n = 100
coordinates = []
centroids = []
clusters = []
stamp_coordinate_ids = []
stamp_centroid_ids = []

screensize(400, 400)
color('black')
penup()
hideturtle()
shape('circle')
speed('fastest')

def create_coordinate():
    x = r.random() * 400 * (-1) ** r.randint(0, 1)
    y = r.random() * 400 * (-1) ** r.randint(0, 1)

    return (x, y)

def create_coordinate_q1():
    x = r.random() * 200 + 100
    y = r.random() * 200 + 100

    return (x, y)

def create_coordinate_q2():
    x = r.random() * -200 - 100
    y = r.random() * -200 - 100

    return (x, y)

def create_coordinate_q3():
    x = r.random() * -200 - 100
    y = r.random() * 200 + 100

    return (x, y)

def create_coordinate_q4():
    x = r.random() * 200 + 100
    y = r.random() * -200 - 100

    return (x, y)

def find_distance(coordinate, centroid):
    x_diff = centroid[0] - coordinate[0]
    y_diff = centroid[1] - coordinate[1]
    distance = m.sqrt(x_diff ** 2 + y_diff ** 2)

    return distance

def find_closest_centroid(coordinate):
    l = []

    for i in range(k):
        l.append(find_distance(coordinate, centroids[i]))

    return l.index(min(l))

def calculate_new_centroids():
    coordinate_x_sum_1 = 0.0
    coordinate_y_sum_1 = 0.0
    coordinate_counter_1 = 0.0
    coordinate_x_sum_2 = 0.0
    coordinate_y_sum_2 = 0.0
    coordinate_counter_2 = 0.0
    coordinate_x_sum_3 = 0.0
    coordinate_y_sum_3 = 0.0
    coordinate_counter_3 = 0.0
    coordinate_x_sum_4 = 0.0
    coordinate_y_sum_4 = 0.0
    coordinate_counter_4 = 0.0

    for i in range(n):
        if clusters[i] == 0:
            coordinate_x_sum_1 += coordinates[i][0]
            coordinate_y_sum_1 += coordinates[i][1]
            coordinate_counter_1 += 1
        if clusters[i] == 1:
            coordinate_x_sum_2 += coordinates[i][0]
            coordinate_y_sum_2 += coordinates[i][1]
            coordinate_counter_2 += 1
        if clusters[i] == 2:
            coordinate_x_sum_3 += coordinates[i][0]
            coordinate_y_sum_3 += coordinates[i][1]
            coordinate_counter_3 += 1
        if clusters[i] == 3:
            coordinate_x_sum_4 += coordinates[i][0]
            coordinate_y_sum_4 += coordinates[i][1]
            coordinate_counter_4 += 1

    centroid_1_x = coordinate_x_sum_1 / coordinate_counter_1
    centroid_1_y = coordinate_y_sum_1 / coordinate_counter_1
    centroids[0] = (centroid_1_x, centroid_1_y)
    centroid_2_x = coordinate_x_sum_2 / coordinate_counter_2
    centroid_2_y = coordinate_y_sum_2 / coordinate_counter_2
    centroids[1] = (centroid_2_x, centroid_2_y)
    centroid_3_x = coordinate_x_sum_3 / coordinate_counter_3
    centroid_3_y = coordinate_y_sum_3 / coordinate_counter_3
    centroids[2] = (centroid_3_x, centroid_3_y)
    centroid_4_x = coordinate_x_sum_4 / coordinate_counter_4
    centroid_4_y = coordinate_y_sum_4 / coordinate_counter_4
    centroids[3] = (centroid_4_x, centroid_4_y)

def clear_centroids():
    for i in range(k):
        clearstamp(stamp_centroid_ids[i])

def clear_coordinates():
    for i in range(n):
        clearstamp(stamp_coordinate_ids[i])

def find_closest_centroid_all():
    for i in range(n):
        clusters.append(find_closest_centroid(coordinates[i]))

def refind_closest_centroid_all():
    for i in range(n):
        clusters[i] = find_closest_centroid(coordinates[i])

def draw_centroids():
    for i in range(k):
        if i == 0:
            color('red')
        if i == 1:
            color('green')
        if i == 2:
            color('blue')
        if i == 3:
            color('gold')

        goto(centroids[i][0], centroids[i][1])
        stamp_centroid_ids.append(stamp())

def draw_coordinates():
    for i in range(n):
        if clusters[i] == 0:
            color('pink')
        if clusters[i] == 1:
            color('lightgreen')
        if clusters[i] == 2:
            color('cyan')
        if clusters[i] == 3:
            color('yellow')

        goto(coordinates[i][0], coordinates[i][1])
        stamp_coordinate_ids.append(stamp())

def redraw_centroids():
    for i in range(k):
        if i == 0:
            color('red')
        if i == 1:
            color('green')
        if i == 2:
            color('blue')
        if i == 3:
            color('gold')

        goto(centroids[i][0], centroids[i][1])
        stamp_centroid_ids[i] = stamp()

def redraw_coordinates():
    for i in range(n):
        if clusters[i] == 0:
            color('pink')
        if clusters[i] == 1:
            color('lightgreen')
        if clusters[i] == 2:
            color('cyan')
        if clusters[i] == 3:
            color('yellow')

        goto(coordinates[i][0], coordinates[i][1])
        stamp_coordinate_ids[i] = stamp()

def setup():
    for i in range(int(n/k)):
        coordinates.append(create_coordinate_q1())
        coordinates.append(create_coordinate_q2())
        coordinates.append(create_coordinate_q3())
        coordinates.append(create_coordinate_q4())

    for i in range(k):
        centroids.append(create_coordinate())

    find_closest_centroid_all()
    draw_centroids()
    draw_coordinates()

    print('Setup Complete')

def iterate():
    clear_centroids()
    calculate_new_centroids()
    redraw_centroids()
    refind_closest_centroid_all()
    clear_coordinates()
    redraw_coordinates()

    print('Iteration Complete')

setup()
for i in range(10):
    iterate()

print('Done')

done()