import plotly.express as px
import csv
#Corrcoef() is present in numpy library
import numpy as np
#Reading the csv file and plotting the scatter plot
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature", y="Ice-cream Sales")
        fig.show()
#Putting the tempearture data and ice cream data int0 arrays
def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    #opening the csv file
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #Dataset is converted into float value
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales"]))

    return {"x" : ice_cream_sales, "y": cold_drink_sales}
#Using Corroef() and pass data sets to it which is x,y
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :-  \n--->",correlation[0,1])
#To load the csv file into data_path
def setup():
    data_path  = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
