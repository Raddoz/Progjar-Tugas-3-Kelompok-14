from ftplib import FTP
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class FtpClient:
    # TODO: Initialize FTP client object
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.ftp = FTP()

    # TODO: Connect to FTP server & login
    def connect(self):
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.user, self.password)


    # TODO: Disconnect from FTP server
    def disconnect(self):
        self.ftp.quit()

    # Soal no 1
    # Nama dan versi FTP server
    def getNameAndVersion(self):
        read_ftp = self.ftp.getwelcome()
        read_ftp = read_ftp.split('\n')[0][4:]
        return read_ftp
    
    # Soal no 2
    # Sistem yang diemulasikan FTP server
    def getWelcomeMessage(self):
        read_ftp = self.ftp.getwelcome()
        return read_ftp
    
    # Soal no 3
    # Daftar file di FTP server
    def getListOfFiles(self):
         self.ftp.nlst()
         return self.ftp.nlst()
    
    # Soal no 4
    # Mengunggah file ke FTP server
    def uploadFile(self, filename):
        read_ftp = self.ftp.storbinary('STOR ' + filename, open(os.path.join(BASE_DIR, filename), 'rb'))
        return read_ftp

    # Soal no 5
    # Membuat direktori
    def createDirectory(self, dirname):
        read_ftp = self.ftp.mkd(dirname)
        return read_ftp

    # Soal no 6
    # Direktori saat ini di FTP server
    def getCurrentDirectory(self):
        read_ftp = self.ftp.pwd()
        return read_ftp
    
    # Soal no 7
    # Mengganti nama direktori
    def renameDirectory(self, oldname, newname):
        read_ftp = self.ftp.rename(oldname, newname)
        return read_ftp
    
    # Soal no 8
    # Menghapus direktori
    def removeDirectory(self, dirname):
        read_ftp = self.ftp.rmd(dirname)
        return read_ftp
        

if __name__ == '__main__':
    # TODO: Read FTP server configuration from ftp.conf
    with open(os.path.join(BASE_DIR, 'ftp.conf')) as config_file:
        config = dict(line.strip().split('=') for line in config_file)

    HOST = config.get("host")
    USER = config.get("user")
    PASS = config.get("pass")
    PORT = config.get("port")

    ftp = FtpClient(HOST, USER, PASS, PORT)
    ftp.connect()

    print(ftp.getNameAndVersion())
    print(ftp.getWelcomeMessage())
    print(ftp.getListOfFiles())
    print(ftp.uploadFile('samplefile.txt'))
    print(ftp.createDirectory('test'))
    print(ftp.getCurrentDirectory())
    print(ftp.renameDirectory('test', 'test2'))
    print(ftp.removeDirectory('test2'))