import math
import random
import copy


def dist(pos1, pos2):
    return abs(math.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2))


def eval_all_edges_length(data):
    all_edges = []
    for i, first in enumerate(data):
        all_edges.append([])
        for j, second in enumerate(data):
            all_edges[i].append(dist(first, second))
    return all_edges


def total_length(sequence, all_edges):
    total = 0
    for i, num in enumerate(sequence):
        total += all_edges[num][sequence[i - 1]]
    return total


def find_neighbour(sequence, all_edges):
    [item1, item2] = random.sample(sequence, k=2)
    index1 = sequence.index(item1)
    index2 = sequence.index(item2)
    new_sequence = copy.deepcopy(sequence)
    new_sequence[index1], new_sequence[index2] = new_sequence[index2], new_sequence[index1]
    new_total_distance = total_length(new_sequence, all_edges)
    return new_sequence, new_total_distance


def plot_graph(data, sequence, plt, camera):
    data_x = [_.x for _ in data]
    data_y = [_.y for _ in data]
    plt.scatter(data_x, data_y, c='#ff0000')
    for i, num in enumerate(sequence):
        if i is 0:
            plt.plot([data[sequence[0]].x, data[sequence[-1]].x], [data[sequence[0]].y, data[sequence[-1]].y])
        else:
            plt.plot([data[num].x, data[sequence[i - 1]].x], [data[num].y, data[sequence[i - 1]].y])
    camera.snap()


def acceptance(new, curr, t):
    if t is 0:
        return 0
    else:
        return math.exp((curr - new) / t)