import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    # Soal no 1
    def test_name_and_version(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        with open(os.path.join(os.path.dirname(__file__), 'welcome_message.txt'), 'r') as f:
            welcome_msg = f.read()
            ftp.ftp.getwelcome = Mock(return_value=welcome_msg)

        # print(welcome_msg.split('\n'))
        self.assertEqual(ftp.getNameAndVersion(), 'FileZilla Server 1.7.0')