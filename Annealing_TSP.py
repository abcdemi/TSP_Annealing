import read_data
from util import *
import random
import matplotlib.pyplot as plt
from matplotlib import animation
from celluloid import Camera
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\admin\\Documents\\ffmpeg\\bin\\ffmpeg.exe'

fig = plt.figure()
camera = Camera(fig)
data = read_data.from_file('./data/wi29.txt')  # change file name here
all_edges = eval_all_edges_length(data)
sequence = random.sample(range(0, len(data)), len(data))
current_total_distance = total_length(sequence, all_edges)
list_length = len(sequence)

for t in range(6000, -1, -1):
    for i in range(1000):
        new_sequence, new_total_distance = find_neighbour(sequence, all_edges)
        if new_total_distance < current_total_distance:
            # always accept move when new distance is shorter
            sequence = new_sequence
            current_total_distance = new_total_distance
        elif acceptance(new_total_distance, current_total_distance, t) > random.uniform(0, 1):
            # accept move by chance based on acceptance probability e^(delta E / T) where delta E is non-positive
            sequence = new_sequence
            current_total_distance = new_total_distance
    # print data to console and plot graph by step of 100
    if t % 100 is 0:
        print(f"T: {t}")
        print(f'Best Sequence So Far: {sequence}')
        print(f'Shortest Distance So Far: {current_total_distance}')
        plot_graph(data, sequence, plt, camera)

animation = camera.animate()
animation.save('wi29.mp4') 