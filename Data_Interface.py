import matplotlib.pyplot as plt
import time


def plot_data(file_name):
    timestamps = []
    weights = []
    
    with open(file_name, 'r') as f:
        for line in f:
            timestamp, weight = line.strip().split(',')
            timestamps.append(int(timestamp))
            weights.append(float(weight))
    
    # Convert timestamps to seconds relative to the start
    start_time = timestamps[0]
    times_in_seconds = [(t - start_time) / 1000.0 for t in timestamps]
    
    plt.figure(figsize=(10, 5))
    plt.plot(times_in_seconds, weights, label='Force Sensor Data (N)')
    plt.xlabel('Time (s)')
    plt.ylabel('Force (N)')
    plt.title('Force vs Time')
    plt.legend()
    plt.grid(True)
    plt.show()
