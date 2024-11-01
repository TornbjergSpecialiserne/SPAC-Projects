#Can be run using mprof run non_generator_ram_test.py to record ram usage
#Then use mprof plot to plot the usage

#Open the file all at once
file = open("data.csv","r")
#Loads all the data at once
data = file.read()
#Ram significantly goes down after closing file
file.close()
