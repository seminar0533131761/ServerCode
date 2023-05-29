from tkinter import Tk

import matplotlib
from flask import Blueprint, make_response

from dal.data_objects.services.student_crud import StudentCrud
from dal.data_objects.services.students_desires_crud import StudentsDesiresCrud
from dal.data_objects.services.diploma_crud import DiplomaCRUD

graf_controller = Blueprint('graf_controller', __name__)

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

# plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.figsize"] = [7.50, 4]


@graf_controller.route('number_of_students_in_each_training')
def number_of_students_in_each_training():
    d = StudentsDesiresCrud()
    opt_names, opt_amount = d.how_many_on_each_trainig()
    subjects = np.arange(1, 7)
    data = opt_amount
    plt.clf()
    plt.plot(subjects, data)
    plt.xlabel('subjects')
    plt.ylabel('number of students')
    plt.title('Plot Title')
    subjects_names = opt_names
    plt.xticks(subjects, subjects_names)
    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Return the plot as a response
    return send_file(buffer, mimetype='image/png')


# /<int:student1_id>/<int:student2_id>
@graf_controller.route("compare_students_grades/<student1_id>/<student2_id>")
def compare_students_grades(student1_id, student2_id):
    diploma = DiplomaCRUD()
    student1 = StudentCrud().get_async(student1_id)
    student1_name = student1.first_name + " " + student1.last_name
    student2 = StudentCrud().get_async(student2_id)
    student2_name = student2.first_name + " " + student2.last_name
    student1_grades, student2_grades, subjects = diploma.compare_students_grades(student1_id, student2_id)
    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    X = np.arange(6)
    p1 = plt.bar(X, student1_grades, bar_width, color='b',
                 label="name {}, id {}".format(student1_name, student1_id))
    # The bar of second plot starts where the first bar ends
    p2 = plt.bar(X + bar_width, student2_grades, bar_width,
                 color='g',
                 label="name {}, id {}".format(student2_name, student2_id))
    plt.xlabel('Subject')
    plt.ylabel('Scores')
    plt.title('Scores in each subject')
    plt.legend()
    plt.xticks(X + (bar_width / 2), (subjects[0], subjects[1], subjects[2], subjects[3],
                                     subjects[4], subjects[5]))

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    response = make_response(send_file(buffer, mimetype='image/png'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragme'] = 'no-cache'
    response.headers['Expires'] = 'O'
    return response
