import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    # Soal no 5
    def test_mkdir(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        ftp.ftp.mkd = Mock(return_value='257 "/sampledir" created')

        self.assertEqual(ftp.createDirectory('sampledir'), '257 "/sampledir" created')