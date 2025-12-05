import matplotlib.pyplot as plt
import time
import argparse
print("Script lancé")


def plot_data(file_name):
    timestamps = []
    weights = []
    
    with open(file_name, 'r') as f:
        for line in f:
            timestamp, weight = line.strip().split(',')
            timestamps.append(int(timestamp))
            weights.append(float(weight))
    
    # Convert timestamps to seconds relative to the start
    times_in_seconds = [t / 1000.0 for t in timestamps]
    
    plt.figure(figsize=(10, 5))
    plt.plot(times_in_seconds, weights, label='Force Sensor Data (N)')
    plt.xlabel('Time (s)')
    plt.ylabel('Force (N)')
    plt.title('Force vs Time')
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot force sensor data from CSV file.')
    parser.add_argument('file_name', type=str, help='Path to the CSV file containing the data.')
    args = parser.parse_args()
    print(f"Plotting data from {args.file_name}...")
    
    plot_data(args.file_name)
