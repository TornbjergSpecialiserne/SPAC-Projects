from large_file_handler import LargeFileHandler
from io import TextIOWrapper
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#The data set is so huge that we need to load the plots in chunks, unless it crashes
mpl.rcParams['agg.path.chunksize']=10000

class DataAnalyser(LargeFileHandler):
    
    #Analyses a data file. Will only work for the brewery data sadly
    def analyse_data(self,data_file : str):
        
        #There can only really happen a file not found error here
        try:
            file = open(data_file)
        except:
            print("File not found error")

        #Creates an instance of the generator
        generator = self.read_line(file)

        #We need the header seperatly to find the indecies we want to analyse
        header = next(generator).replace("\n","").split(",")

        #We find the indecies and store them
        sales_index = header.index("Total_Sales")
        temp_index = header.index("Temperature")
        ph_index = header.index("pH_Level")
        alcohol_index = header.index("Alcohol_Content")
        quality_index = header.index("Quality_Score")
        brewing_loss_index = header.index("Loss_During_Brewing")
        fermantation_loss_index = header.index("Loss_During_Fermentation")

        #We create a list of beer types we want to look for
        names = ["Stout","Ale","Pilsner","Porter","IPA","Lager"]

        #We create a list of values to look at the total sales of each beer types
        sales = [0]*len(names)

        #We create list of other values we want to look at
        stout_temp = []
        stout_ph = []
        stout_brewing_loss = []
        stout_alcohol = []
        stout_quality_score = []
        stout_fermantation_loss = []

        #I only print the header to check if I spelled something wrong, cause I can't open the data in excel cause it is too big
        print(header)
        for lines in generator:
            lines = lines.replace("\n","").split(",")

            #We put the different values we want to look at into their lists
            if names[0] in lines:
                sales[0] = sales[0] + float(lines[sales_index])
                stout_temp.append(float(lines[temp_index]))
                stout_ph.append(float(lines[ph_index]))
                stout_brewing_loss.append(float(lines[brewing_loss_index]))
                stout_alcohol.append(float(lines[alcohol_index]))
                stout_quality_score.append(float(lines[quality_index]))
                stout_fermantation_loss.append(float(lines[fermantation_loss_index]))
            elif names[1] in lines:
                sales[1] = sales[1] + float(lines[sales_index])
            elif names[2] in lines:
                sales[2] = sales[2] + float(lines[sales_index])
            elif names[3] in lines:
                sales[3] = sales[3] + float(lines[sales_index])
            elif names[4] in lines:
                sales[4] = sales[4] + float(lines[sales_index])
            elif names[5] in lines:
                sales[5] = sales[5] + float(lines[sales_index])

        #We get ready to plot
        plt.figure()

        #I sort the values with regards to the x value when plotting in ascending order
        sales , names = (list(t) for t in zip(*sorted(zip(sales,names))))
        stout_temp , stout_brewing_loss = (list(t) for t in zip(*sorted(zip(stout_temp,stout_brewing_loss))))
        stout_ph , stout_fermantation_loss = (list(t) for t in zip(*sorted(zip(stout_ph,stout_fermantation_loss))))
        stout_alcohol, stout_quality_score = (list(t) for t in zip(*sorted(zip(stout_alcohol,stout_quality_score))))

        #Sales are plotted in a bar plot, and we use log scale for y axis cause the difference is too small to see otherwise (It also turns out that the values are completly random hence why they are so similar)
        plt.bar(names,sales,log=True)
        plt.xlabel("Beer style")
        plt.ylabes("Total sales")
        plt.figure()

        #Normally I would plot theese like a function, but there was no correlation at all, so i wanted to check if they where random using a histogram to check if there where more values centered at a line, but they where uniformly spread (Cause the values are randomly generated :<)
        plt.hist2d(stout_temp,stout_brewing_loss,bins=100)
        plt.title("Temp influence of loss")
        plt.xlabel("Temp")
        plt.ylabel("Loss")
        plt.figure()
        plt.hist2d(stout_ph,stout_brewing_loss,bins=100)
        plt.title("pH influence on loss")
        plt.xlabel("pH_level")
        plt.ylabel("Loss")
        plt.show()

if __name__ == "__main__":
    analyser = DataAnalyser()
    analyser.analyse_data("sorted_brewery_data.csv")
        
