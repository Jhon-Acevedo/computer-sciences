import matplotlib.pyplot as plt


def generate_plot(name, x, y):

    # plot
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)


