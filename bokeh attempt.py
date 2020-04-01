#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dell
#
# Created:     01-04-2020
# Copyright:   (c) dell 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Import library
from bokeh.plotting import figure, output_file, show

#Specify Domain and Function
x = range(10)
y = [ a**0.5 for a in x]



#Graph will be written in the following file
output_file("bokeh_plot.html")

#Generate graph
plot = figure(title= "Y = X**0.5",
                x_axis_label= 'X-Axis',
                y_axis_label= 'Y-Axis')
plot.line(x, y, legend= 'f(X)', line_width = 2)

show(plot)