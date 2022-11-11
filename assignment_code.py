# -*- coding: utf-8 -*-
"""
Created on Fri Nov 7 07:52:21 2022

@author: Charan sai prakash T
"""

#Importing required libraries
import pandas as pnds
import matplotlib.pyplot as mtpltlb
from matplotlib.figure import Figure
import numpy as np

#loading 2 excel files contatining data of different years
data_ = pnds.read_csv("table-11-2020-21.xls" )
_data = pnds.read_csv("table-11-2019-20.xls")


#dropping unnecessary rows
N = 13
data_.drop(index=data_.index[:N], axis=0, inplace=True)
_data.drop(index=_data.index[:N], axis=0, inplace=True)


#cleaning 1st dataframe and making the 1st row as the new header
header1 = data_.iloc[0]
final_data1 = pnds.DataFrame(data_.values[1:], columns = header1)
#dropping Null values if any
final_data1.dropna()
#changing the data type of column "Number"
final_data1 = final_data1.astype({"Number": int})
final_data1["Number"]


#cleaning 2nd dataframe and making the 1st row as the new header
header2 = _data.iloc[0]
final_data2 = pnds.DataFrame(_data.values[1:], columns = header2)
#dropping Null values if any
final_data2.dropna()
#changing the data type of column "Number"
final_data2["Number"] = final_data2["Number"].astype(int)
#extracting this column so that it can be merged with the previous dataframe
extracted_column = final_data2["Number"]
extracted_column.dropna()


#merging the extracted column with the previous dataframe using pd.join()
final_data = final_data1.join(extracted_column, lsuffix=" 2020-21", rsuffix=" 2019-20")
final_data


#grouping the data by 2 columns which are "Level of study" and "Mode of study" and calculating their means
line_data = final_data.groupby(["Level of study", "Mode of study"]).mean()
line_data


def line_plot(dataframe_):
    
    """Defining the line_plot function = This function will plot multiple lines on a single plot wherein only dataframe needs to be fed.
    The rotation has been set to 90 so that they are fit for any length of labels. """
    
    dataframe_.plot()
    mtpltlb.xticks(rotation=90)
    mtpltlb.ylabel("Average Students")
    mtpltlb.xlabel("Study Level, Study Mode")
    mtpltlb.title("Average students on the basis of Level of Study and Mode of Study")
    mtpltlb.legend(["2020-21", "2019-20"], title="Average")
#calling the function
line_plot(line_data)



def pie_plot(data_frame, column_):
    
    """Defining the pie_plot function = This function will plot a pie chart wherein the dataframe and the column required to be plotted need to be fed.
    The criteria here has been fixed to be the column named as 'Level of study'. The column which needs to be fed here can be either 'Number 2019-20' or 'Number 2020-21'.
    This depends upon the user as to which year's data he/she requires. Please note column needs to be fed in string format.
    """
    
    #making a pie chart 
    #making a list of labels for the [pie chart]
    study_level = ['All', 'All postgraduate', 'All undergraduate', 'First degree', 'Other undergraduate', 'Postgraduate (research)', 'Postgraduate (taught)']
    #criteria for explosion
    explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05,0.05)
    ax, fig = mtpltlb.subplots(figsize =(7,7))
    #plotting the pie chart
    mtpltlb.pie(data_frame.groupby(['Level of study'])[column_].mean(), labels = study_level, explode=explode, startangle = 90)
    #defining the legend and its location
    ax.legend(study_level, loc ="lower left")
    #setting the title of the pie chart
    fig.set_title("Average Students based on Study Level ({})".format(column_[7:]), fontsize = 15)
    mtpltlb.show()

#calling the function by passing new parameters
pie_plot(final_data, 'Number 2020-21')

# calling pie-plot function by passing new parameters
pie_plot(final_data, 'Number 2019-20')



def horizontal_bar(_dataframe, column, color_):
    
    """Defining the horizontal_bar function = This function will plot a horizontal bar chart wherein the dataframe and the column on the basis of which the data needs to be visualized need to be fed.
    Please note the column to be fed must contain numeric values. hence, it can take only two columns according to this dataset which are "Number 2019-20" and "Number 2020-21".
    Please note column needs to be fed in string format.
    The other criteria for horizontal bar has been fixed to be the column named '4 Way domicile'. This cannot be changed.
    Apart from the column, the last argument takes in the color of the graph. The user can choose any color of his/her liking and can feed this to the fucntion.
    Please note color needs to be fed in string format."""
    
    #making horizontal bargraph 
    domiciles = ['All', 'European Union','Non-European Union','Not Known', 'UK' ]
    mtpltlb.barh(domiciles, _dataframe.groupby(['4 way domicile'])[column].mean(), color = color_)
    #defining xlabel and ylabel
    mtpltlb.xlabel("Average Students ({})".format(column[7:]), size=14)
    mtpltlb.ylabel("4 Way Domicile", size=14)
    #defining legend and taking the legend outside the plot area
    mtpltlb.legend([domiciles],  bbox_to_anchor=(1.05, 1.0))
    mtpltlb.show()
#calling this function on 2019-20 column with color orange
horizontal_bar(final_data, "Number 2019-20", 'orange')


#calling this function on 2020-21 column with color blue
horizontal_bar(final_data, "Number 2020-21", 'blue')