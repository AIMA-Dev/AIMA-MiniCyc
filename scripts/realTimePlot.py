from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from PyQt5 import QtWidgets


class RealTimePlot:
    def __init__(self, title):
        self.x_data, self.y_data = [], []
        self.figure, self.ax = plt.subplots()
        self.ax.set_title(title)
        self.line, = self.ax.plot_date(
            self.x_data, self.y_data, '-', color='white')  # Set line color to white
        self.animation = None  # Ref animation object
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
        if not self.x_data:
            self.x_data.append(0)
        else:
            self.x_data.append(self.x_data[-1] + 1)
        self.y_data.append(randrange(0, 10))
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        return self.line,

    def start_animation(self, interval=200):
        self.animation = FuncAnimation(
            self.figure, self.update, interval=interval, cache_frame_data=False)

    def add_plot(self, MainWindow, widget_name):
        widget = MainWindow.findChild(QtWidgets.QWidget, widget_name)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.figure.canvas)
        widget.setLayout(layout)
# Développé avec ❤️ par : www.noasecond.com.