import os
#import datetime

#x = datetime.datetime.now()
#print(x.strftime("%Y-%m-%d"))

#try:
#    os.mkdir(f"/home/tom-winterton/Documents/code_projects/2025/pi_allSkyCamera/{x.strftime("%Y-%m-%d")}") #creates directory with today's date YYYY-MM-DD
#except OSError:
#    print("directory already exists")



#max_value = max(int())

#x = os.path.dirname(path)

path = '/home/tom-winterton/Documents/code_projects/2025/pi_allSkyCamera/captures/'

x = os.listdir(path)

dirname = [f for f in os.listdir(path) if os.path.isdir(f)]

print(max(x))