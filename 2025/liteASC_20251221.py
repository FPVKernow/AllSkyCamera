import datetime
import os


today = datetime.datetime.now()
print(today.strftime("%Y-%m-%d"))

path = '/home/tom-winterton/Documents/code_projects/2025/pi_allSkyCamera/captures/'

def mkdir():
    try:
        os.mkdir(f'{path, today.strftime("%Y-%m-%d")}')
    except:
        print("directory already exists")


mkdir()

def newstDate():
    x = os.listdir(path)
    return x

print(newstDate())