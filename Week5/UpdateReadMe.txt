Installing
Remove the default vent folder and install you own.

Update note
in requirements.txt added XlsxWriter for automaticly add missing package to enviorment then running pip install -r requirements.txt

Description extensions
A more clear description for how to install exsample:
"
To run the project simply first run in terminal (for vs code)
for window:
./.venv/Scripts/activate
for macos or linux
. .venv/bin/activate

To install requirment
pip install -r requirements.txt

# How to use
This will run the program and download the 10 files from the GRI_2017_2020.xlsx there is not downloadede yet. 
python Controller.py

"

Write a section for there you find the downloadede files.

Usability for not tech users:
- Have a way to show the program is running. 

# Code feedback
Polar_File_Handler:
start_download: maybe could be split to a function for getting the data and one for starting the threads.
	maybe a change destination to fill_destination to explain what kind of destination it is talking about
