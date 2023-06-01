import os
import sys
import unittest
from unittest.mock import patch, Mock
from ftplib import FTP

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.main import FtpClient

class TestFTP(unittest.TestCase):
    def test_credential(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)

        self.assertEqual(ftp.host, "localhost")
        self.assertEqual(ftp.user, "progjar")
        self.assertEqual(ftp.password, "Progjar123")
        self.assertEqual(ftp.port, 21)
    
    def test_connect(self):
        ftp = FtpClient("localhost", "progjar", "Progjar123", 21)
        self.assertIsInstance(ftp.ftp, FTP)
