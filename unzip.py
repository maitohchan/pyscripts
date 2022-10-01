import glob
import zipfile

files = glob.glob('*.zip')
for f in files:
    print f
    zip = zipfile.ZipFile(f)
    zip.extractall()
    zip.close()

