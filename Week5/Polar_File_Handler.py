from Downloader import Downloader
import os
from pathlib import Path
import threading
from typing import Optional
from queue import Queue
import polars as pl

#Class for handling a file with download links
class FileHandler(object):
   
    #Creates an instance of the filehandler with a dictionary of successfull downloads
    def __init__(self,number_of_threads : Optional[int] = 10) -> None:
        self.finish_dict = {}
        self.number_of_threads = number_of_threads

    #Function that starts a download instance using the downloader class. Used in threads
    def download_thread(self,queue:Queue) -> None:
        while not queue.empty():
            link, destination, name, alt_link = queue.get()
            downloader = Downloader()
            Path(destination).mkdir(exist_ok=True)

            #Dictionaries are not necesarily thread safe but appending to it is so this is fine. If more complicated tasks where needed you would use a mutex lock etc
            self.finish_dict[name] = downloader.download(url=link,destination_path=os.path.join(destination, name+".pdf"), alt_url=alt_link)
            queue.task_done()

    #Starts downlaoding files from urls listed in url_file which will be placed in the destination, and reported in the meta file
    def start_download(self, url_file : str,meta_file : str,destination : str) -> dict:

        file_data = pl.read_excel(source=url_file, columns= ["BRnum", "Pdf_URL", "Report Html Address"])
        for row in file_data.rows():
            print(row)
        #We index after the BRnums for now
#        ID = "BRnum"
#
#        #Slow read of excel file with pandas. Would love to know a better way to read it, since python open cannot hanlde xlsx files
#        file_data = pd.read_excel(url_file,index_col = ID)
#        new_meta_file = False
#
#        #Tries reading the files listed as not downloaded if it fails it will make a new meta file that fullfills the structure
#        try:
#            report_data = pd.read_excel(meta_file, index_col = ID)
#            report_data = report_data[report_data["pdf_downloaded"] == "yes"]
#
#            #Sort out files that are downloaded
#            file_data = file_data[~file_data.index.isin(report_data.index)]
#        except:
#            new_meta_file = True
#            print("New meta data file will be created")
#
#        queue = Queue()
#
#        #Sorts out files with no url or alternative urls
#        #counter to only download 10 files
#        j = 0
#        #We thru each br number and starts a download
#        for index in file_data.index:
#            if j == 20:
#                break
#            alt_link = None
#            link = file_data.at[index, "Pdf_URL"]
#            if not file_data.at[index, "Report Html Address"] != file_data.at[index,"Report Html Address"]:
#                alt_link = file_data.at[index,"Report Html Address"]
#            
#            #Creates a new thread and adds them to the list so that we can make sure all downloads are done before exiting
#            queue.put([link,destination,index,alt_link])
#            j += 1
#        #Makes sure each thread is done
#        for i in range(self.number_of_threads):
#            thread = threading.Thread(target=self.download_thread, args = (queue,))
#            thread.start()
#
#        queue.join()
#        #Creates a dataframe from the dictionary of downloads
#        finished_data_frame = {ID:[],"pdf_downloaded":[]}
#        for key, value in self.finish_dict.items():
#            finished_data_frame[ID].append(key)
#            if value:
#                finished_data_frame["pdf_downloaded"].append("yes")
#            else:
#                finished_data_frame["pdf_downloaded"].append("no")
#
#        #Sets the index to be BRnum
#        finished_data_frame = pd.DataFrame.from_dict(finished_data_frame).set_index(ID)
#
#        #If new meta file should be created do so otherwise append to existing file
#        if new_meta_file:
#            with pd.ExcelWriter(meta_file,mode="w") as writer:
#                finished_data_frame.to_excel(writer)
#        else:
#            with pd.ExcelWriter(meta_file,mode="a",if_sheet_exists="overlay") as writer:
#                finished_data_frame.to_excel(writer)
#
#        #Returns the files downloaded and success status
        return self.finish_dict

if __name__ == "__main__":
    file_handler = FileHandler()
    print(file_handler.start_download(os.path.join("customer_data","GRI_2017_2020.xlsx"),os.path.join("customer_data","Metadata2017_2020.xlsx"),"files"))
