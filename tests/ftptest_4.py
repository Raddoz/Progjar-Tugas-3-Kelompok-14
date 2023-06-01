import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    # Soal no 4
    def test_upload_file(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        ftp.ftp.storbinary = Mock(return_value='226 Transfer complete.')
        
        self.assertEqual(ftp.uploadFile('samplefile.txt'), '226 Transfer complete.')