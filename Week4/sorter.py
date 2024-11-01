from io import TextIOWrapper
from large_file_handler import LargeFileHandler

#Class for sorting files into a smaller data set. Mostly just to slightly speed up tests. Inherites from LargeFileHandler
class Sorter(LargeFileHandler):
    
    #Takes a data file name, a destination file name and a list of values to include 
    def sort_for(self, file_name:str, destination_file:str,sorting_for:list) -> None:
        
        #The sorter is meant for csv, files
        try:
            if not ".csv" in file_name and destination_file:
                raise Exception("Input and output files should be csv, files")
        except Exception as e:
            print(e)

        #Tries to open a file. The most common error here is file not found error
        try:
            file = open(file_name)
        except:
            print("File not found")
            return

        #The destination file should generally only be a new file, thus the file should not be write protected
        try:
            output = open(destination_file,"w")
        except:
            print("Error with output file")

        #Creates the instance of the generator for the file
        generator = self.read_line(file)

        #We generally want to keep the header if it is a csv file
        header = generator.__next__()

        #We make a new list for the lines we want to keep
        sorted_lines = []

        #We go thru each line from the generator
        for line in generator:

            #We check if any of the values we want to keep appears in the line
            for element in sorting_for:
                if element in line:
                    sorted_lines.append(line)

        #We write a new file with the sorted values
        output.write(header)
        for line in sorted_lines:
            output.write(line)
        output.close()


if __name__ == "__main__":
    sorter = Sorter()
    sorter.sort_for("chess_games.csv","sorted_chess_data.csv",["Sicilian Defence","King's Gambit","Ruy Lopez","French Defence","Italian Game","English Opening","Caro-Kann","Indian Game","Queen's Gambit","Queen's Pawn"])
