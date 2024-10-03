import matplotlib.pyplot as plt

def setup_plot():
    plt.ion()
    fig, ax = plt.subplots()
    return fig, ax

def update_plot(ax, data, peaks=None):
    ax.clear()
    ax.plot(data, label='EDA Signal')
    if peaks is not None:
        ax.plot(peaks, data[peaks], "x", label='Peaks')
    ax.legend()
    plt.draw()
    plt.pause(0.01)