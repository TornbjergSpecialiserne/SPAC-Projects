from data_handler import Datahandler
from io import TextIOWrapper
import csv
from typing import Optional

class CSVDatahandler(Datahandler):
    def __init__(self):
        self.file : TextIOWrapper
        self.data : list
        self.dict : dict

    def read_data(self) -> None:
        self.data = csv.reader(self.file)

    def write_file(self,file_name : str, dialect : Optional[str] = "unix") -> None:
        try:
            with open(file_name, 'a') as file:
                writer = csv.writer(file, dialect = dialect)
                for line in self.data:
                    writer.writerow(line)
        except IOError:
            print("File might be write protected")

    def get_data(self):
        return self.data

    def create_dict(self) -> None:
        self.dict = csv.DictReader(self.file)

    def remove_lines_from_file(self,line : str) -> None:
        self.data = [row for row in self.data if row != line]

    def create_json(self, header : Optional[list] = None) -> None:
        if not header:
            header = next(self.data)
        self.dict = csv.DictWriter(self.data,fieldnames = header)
        print(self.dict)

if __name__ == "__main__":
    loader = CSVDatahandler()
    test = loader.open_file("source_data.csv")
    loader.read_data()
    loader.remove_lines_from_file(["","","",""])
    loader.write_file("test.csv")
