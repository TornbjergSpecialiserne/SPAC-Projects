from Polar_File_Handler import *
import unittest

class test_File_Handler(unittest.TestCase):
    def test_download_thread_running(self):       
        file_handler = FileHandler()
     
        data_holder = {"BRnum": [], "pdf_downloaded": []}

        test_queue = Queue()
        test_queue.put([
            "http://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf",
            "files",
            "BR50042",
            "",
            data_holder
            ])

        try:
            thread = threading.Thread(target=file_handler.download_thread, args = (test_queue,))
            thread.start()     
            test_queue.join()       
        except Exception as e:
            # If an exception is raised, the test will fail
            self.fail(f"An unexpected exception was raised: {e}")

        for pdf_file in data_holder["pdf_downloaded"]:
            self.assertEqual(pdf_file, "yes")      

    def test_empty_input(self):
        file_handler = FileHandler()
     
        data_holder = {"BRnum": [], "pdf_downloaded": []}

        test_queue = Queue()
        test_queue.put([
            "",
            "",
            "",
            "",
            data_holder
            ])

        try:
            thread = threading.Thread(target=file_handler.download_thread, args = (test_queue,))
            thread.start()     
            test_queue.join()       
        except Exception as e:
            # If an exception is raised, the test will fail
            self.fail(f"An unexpected exception was raised: {e}")

        for pdf_file in data_holder["pdf_downloaded"]:
            self.assertEqual(pdf_file, "no")