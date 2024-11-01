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
        opening_index = header.index("Opening")
        white_elo_index = header.index("WhiteElo")
        elo_diff_index = header.index("WhiteRatingDiff")
         
        #List of openings we want to analyse
        openings=["Sicilian Defense","King's Gambit","Ruy Lopez","French Defense","Italian Game","English Opening","King's Pawn","Indian Game","Queen's Gambit","Queen's Pawn"]

        #List of winnings for both black and white
        white_winnings = [0]*len(openings)
        black_winnings = [0]*len(openings)
        draw_high = [0]*len(openings)
        draw_low = [0]*len(openings)

        #in the data set 0-1 means black won and 1-0 means white won
        black_won = "0-1"
        white_won = "1-0"
        draw_text = "1/2-1/2"
        for line in generator:

            #Replace new line char and split into a list
            line = line.replace("\n","").split(",")
            i = 0

            #We go thru each opening and check who won
            for opening in openings:
                if opening in line[opening_index]:
                    if black_won in line:
                        black_winnings[i] += 1
                    elif white_won in line:
                        white_winnings[i] += 1
                    elif draw_text in line:
                        if float(line[white_elo_index]) > 1500:
                            draw_high[i] += 1
                        elif float(line[white_elo_index])<=1500:
                            draw_low[i] += 1
                i +=1
        #Plots for the different winnings in a pie
        plt.figure()
        plt.title("White winnings")
        plt.pie(white_winnings,labels=openings,autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        plt.figure()
        plt.title("Black winnings")
        plt.pie(black_winnings,labels=openings,autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        plt.figure()
        plt.title("Draws high")
        plt.pie(draw_high,labels=openings,autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        plt.figure()
        plt.title("Draws low")
        plt.pie(draw_low,labels=openings,autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        plt.show()

if __name__ == "__main__":
    analyser = DataAnalyser()
    analyser.analyse_data("sorted_chess_data.csv")
        
