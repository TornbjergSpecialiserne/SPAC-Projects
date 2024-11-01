from io import TextIOWrapper

#Generic class for creating a generator handling large files
class LargeFileHandler(object):

    #creates a generator
    def read_line(self,file:TextIOWrapper):
        for line in file:
            yield line
