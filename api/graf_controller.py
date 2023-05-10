from tkinter import Tk

import matplotlib
from flask import Blueprint
graf_controller=Blueprint('graf_controller',__name__)

import io
from flask import send_file

import matplotlib.pyplot as plt
matplotlib.use('agg')
import numpy as np
root = Tk()
# import io
# from flask import Response, send_file
# from ipykernel.pickleutil import buffer
#
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# from flask import Flask
# import numpy as np
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

@graf_controller.route('number_of_students_in_each_training/')
def number_of_students_in_each_training():
    months = np.arange(1, 8)
    data = np.array([6,12,4,76,44,23,12])
    plt.plot(months, data)
    plt.xlabel('subjects')
    plt.ylabel('number of students')
    plt.title('Plot Title')
    month_names = ["math", "history", "sciences", "programing","english","grammar","hebrew"]
    plt.xticks(months, month_names)
    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Return the plot as a response
    return send_file(buffer, mimetype='image/png')

@graf_controller.route('compare_two_students')
def p():
    # data to plot
    #get the ids from the user and get the students marks by their id
    student1_marks = [90, 55, 40, 65]
    student2_marks = [85, 62, 54, 20]
    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    X = np.arange(4)
    p1 = plt.bar(X, student1_marks, bar_width, color='b',
                 label='John')
    # The bar of second plot starts where the first bar ends
    p2 = plt.bar(X + bar_width, student2_marks, bar_width,
                 color='g',
                 label='Sam')
    plt.xlabel('Subject')
    plt.ylabel('Scores')
    plt.title('Scores in each subject')
    plt.xticks(X + (bar_width / 2), ("English", "Science",
                                     "Sports", "History"))

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')
root = Tk()