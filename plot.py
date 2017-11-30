import numpy as np
import matplotlib.pyplot as plt

def plot_brownian(data):
    """
    Paratmeters
    -----------
    data: 2D array, dimensions: (t, 2)
          coordinates
    """
    fig, ax = plt.subplots(figsize=(7,7))

    ax.plot(data[0], data[1])
    ax.plot(data[0,0], data[1,0], 'go')
    ax.plot(data[0,-1], data[1,-1], 'ro')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('2D Brownian motion');

def plot_msd(data, percentage=0.3):
    """
    Paratmeters
    -----------
    data: 1D array
    percentage: percentage of plot data
    """
    fig, ax = plt.subplots(figsize=(7,7))

    data = data[:int(len(data)*percentage)]
    ax.plot(np.arange(len(data)), data)
    ax.set_xlabel('t')
    ax.set_title('MSD');
