import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    # Soal no 2
    def test_emulated_message(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        with open(os.path.join(os.path.dirname(__file__), 'welcome_message.txt'), 'r') as f:
            welcome_msg = f.read()
            ftp.ftp.getwelcome = Mock(return_value=welcome_msg)

        self.assertEqual(ftp.getWelcomeMessage(), welcome_msg)