from io import TextIOWrapper

class Datahandler(object):

    def __init__(self):
        self.file : TextIOWrapper
        self.data : list

    def open_file(self,file_name : str) -> str:
        try:
            self.file = open(file_name,encoding = "utf-8")
            self.read_data()
            return "file loaded"
        except FileNotFoundError:
            return "file not found"


    def read_data(self) -> None:
        data = self.file.read()
        self.data = data.split("\n")
   
    def close_file(self) -> None:
        self.file.close()


    def get_data(self) -> list:
        return self.data
