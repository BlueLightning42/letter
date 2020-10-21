from zipfile import ZipFile
import os


def give_reward():
	pass
#		os.startfile(os.path.realpath("C:/Users/jawg4/Music/Set It Off"))

def extract_reward():
    with ZipFile('hidden') as zf:
	    zf.extractall(pwd=b'test')