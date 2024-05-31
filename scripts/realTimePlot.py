from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from PyQt5 import QtWidgets

class RealTimePlot:
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
        self.animation = FuncAnimation(
            self.figure, self.update, interval=interval, blit=True, cache_frame_data=False
        )

    def add_plot(self, MainWindow, widget_name):
        widget = MainWindow.findChild(QtWidgets.QWidget, widget_name)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.figure.canvas)
        widget.setLayout(layout)

# Example usage
# plot1 = RealTimePlot("Plot 1", num_lines=2)
# plot1.start_animation()
# figure = plot1.figure
# listWidget_vacuum = MainWindow.findChild(QtWidgets.QListWidget, "listWidget_vacuum")
# item = QtWidgets.QListWidgetItem()
# item.setSizeHint(QtCore.QSize(0, 500))
# listWidget_vacuum.addItem(item)
# listWidget_vacuum.setItemWidget(item, figure.canvas)
# Developed with ❤️ by : www.noasecond.com.
# Développé avec ❤️ par : www.noasecond.com.