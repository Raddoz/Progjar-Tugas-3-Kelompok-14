import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    # Soal no 6
    def test_current_dir(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        ftp.ftp.pwd = Mock(return_value='/')

        self.assertEqual(ftp.getCurrentDirectory(), '/')