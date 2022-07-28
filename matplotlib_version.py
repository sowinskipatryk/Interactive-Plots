import matplotlib.pyplot as plt
import pandas as pd
import random


def draw_interactive_scatter_plot_mpl(*args, legend=[], size=(12, 6), title='',
                                  xlabel='', ylabel='', alpha=0.2, s=1):
    colors = ['r', 'g', 'b']
    plots = []

    fig, ax = plt.subplots(figsize=size)

    for i, arg in enumerate(args):

        if isinstance(arg[0], pd.DataFrame):
            arg[0] = arg[0].squeeze()
        if isinstance(arg[1], pd.DataFrame):
            arg[1] = arg[1].squeeze()

        plot, = ax.plot(arg[0], arg[1], f'{colors[i]}.', label=legend[i],
                        alpha=alpha, markersize=s)

        plots.append(plot)

    graphs = {}

    leg = plt.legend(loc='upper right')
    labels = leg.get_lines()

    for i, label in enumerate(labels):
        label.set_picker(True)
        label.set_pickradius(10)
        graphs[label] = plots[i]

    def on_pick(event):
        leg = event.artist
        is_visible = leg.get_visible()

        graphs[leg].set_visible(not is_visible)
        leg.set_visible(not is_visible)

        fig.canvas.draw()

    plt.connect('pick_event', on_pick)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
