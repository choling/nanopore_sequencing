import tarfile
import zipfile
import sys
import os

fname = sys.argv[-1]

if fname.endswith("tar.gz"):
	tar = tarfile.open(fname, "r:gz")
	tar.extractall()
	tar.close()
elif fname.endswith("tar"):
	tar = tarfile.open(fname, "r:")
	tar.extractall()
	tar.close()
elif fname.endswith("zip"):
	zip = zipfile.ZipFile(fname, "r")
	zip.extractall()
	zip.close()