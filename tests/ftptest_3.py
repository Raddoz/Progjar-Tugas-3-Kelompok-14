import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    # Soal no 3
    def test_list_of_files(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        ftp.ftp.nlst = Mock(return_value=['file1.txt', 'file2.txt', 'file3.txt'])

        self.assertEqual(ftp.getListOfFiles(), ['file1.txt', 'file2.txt', 'file3.txt'])