# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:39:00 2022

@author: kka007
"""
# ImportLibraries
from bokeh.io import output_file,show
from bokeh.models import Button, CustomJS, TextInput
from bokeh.layouts import column, row
from bokeh.plotting import figure


output_file("Outputs.html")
button1 = Button(label="HYDRAULIC PRIFILE COMPUTATIONS", button_type="success") # Header
button2 = Button(label="INPUTS", button_type="success")                         # Inputs include channel Geometry, Numerical parameters & Boundary conditions
button3 = TextInput(value="", title="CHANNEL LENGTH L [m]")
button4 = TextInput(value="", title="BOTTOM WIDTH (b) [m]")
button5 = TextInput(value="", title="FLOW (Q) [m3/s]")
button6 = TextInput(value="", title="CHEZY'S COEFFICIENT C")
button7 = TextInput(value="", title="DELTA X [m]")
button8 = TextInput(value="", title="INITIAL DEPTH (h) [m]")
button9 = TextInput(value="", title="DATUM LEVEL (Hg) [m]")
button10 = Button(label="RUN!", button_type="success")                          # For executing the program in the back end
## Graphing the outputs
figure = figure(title="GRAPH FOR THE BACK WATER CURVE", x_axis_label='DISTANCE [m]', y_axis_label='DEPTH h [m]')  # Shows figures and ordinates
show(row(column(button1,button2,button3,button4,button5, button6,button7,button8,button9,button10),column(figure)))













