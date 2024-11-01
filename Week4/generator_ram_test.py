#Can be run using mprof run generator_ram_test.py to record ram usage
#Then use mprof plot to plot the usage

import matplotlib.pyplot as plt



#Create generator
def read_line(file): 
    for line in file:
        yield line

if __name__ == "__main__":
    #opens the file
    try:
        file = open("data.csv")
    except:
        #prints error
        print("Error when reading file")
    #Creates an instance of the generator
    generator = read_line(file)

