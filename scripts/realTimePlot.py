from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from PyQt5 import QtWidgets

# ================================================================================================= #
#                          RealTimePlot are random for dev purposes                                 #
# ================================================================================================= #


class RealTimePlot:
    """
    A class for creating and updating a real-time plot.

    Args:
        title (str): The title of the plot.
        num_lines (int, optional): The number of lines to plot. Defaults to 1.

    Attributes:
        num_lines (int): The number of lines to plot.
        x_data (list): A list of lists to store the x-axis data for each line.
        y_data (list): A list of lists to store the y-axis data for each line.
        figure (Figure): The matplotlib Figure object.
        ax (Axes): The matplotlib Axes object.
        lines (list): A list of Line2D objects representing the lines in the plot.
        animation (FuncAnimation): The matplotlib FuncAnimation object for animating the plot.

    Methods:
        update(frame): Update the plot with new data.
        start_animation(interval): Start the animation of the plot.
        add_plot(MainWindow, widget_name): Add the plot to a specified widget in a PyQt5 MainWindow.
    """

    def __init__(self, title, num_lines=1):
        self.num_lines = num_lines
        self.x_data = [[] for _ in range(num_lines)]
        self.y_data = [[] for _ in range(num_lines)]
        self.figure, self.ax = plt.subplots()
        self.ax.set_title(title)
        self.lines = [
            self.ax.plot_date([], [], '-', color=f'C{i}')[0] for i in range(num_lines)
        ]
        self.animation = None
        # Colors
        self.figure.patch.set_facecolor('#424242')
        self.ax.set_facecolor('#424242')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.title.set_color('white')

    def update(self, frame):
        """
        Update the plot with new data.

        Args:
            frame: The current frame of the animation.

        Returns:
            list: A list of Line2D objects representing the updated lines in the plot.
        """
        for i in range(self.num_lines):
            if not self.x_data[i]:
                self.x_data[i].append(0)
            else:
                self.x_data[i].append(self.x_data[i][-1] + 1)
            self.y_data[i].append(randrange(0, 10))
            self.lines[i].set_data(self.x_data[i], self.y_data[i])
        self.ax.relim()
        self.ax.autoscale_view()
        return self.lines

    def start_animation(self, interval=200):
        """
        Start the animation of the plot.

        Args:
            interval (int, optional): The interval between frames in milliseconds. Defaults to 200.
        """
        self.animation = FuncAnimation(
            self.figure, self.update, interval=interval, blit=True, cache_frame_data=False
        )

    def add_plot(self, MainWindow, widget_name):
        """
        Add the plot to a specified widget in a PyQt5 MainWindow.

        Args:
            MainWindow: The PyQt5 MainWindow object.
            widget_name (str): The name of the widget to add the plot to.
        """
        widget = MainWindow.findChild(QtWidgets.QWidget, widget_name)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.figure.canvas)
        widget.setLayout(layout)
# Développé avec ❤️ par : www.noasecond.com.
