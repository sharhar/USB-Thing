import os
import zipfile
import urllib.request

f = open('UpdaterFiles/serverData.txt','r')
text = f.read()
adress = text.split('\n')[0]
name = text.split('\n')[1]
urllib.request.urlretrieve(adress, name)

fh = open(name, 'rb')
z = zipfile.ZipFile(fh)
for n in z.namelist():
    outpath = os.getcwd()
    z.extract(n, outpath)
fh.close()

os.remove(name)