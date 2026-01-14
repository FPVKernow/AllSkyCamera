#AllSkyCamera by T. Winterton 2026
#from picamera2 import Picamera2  # type: ignore
import datetime
import os

filePath = '/home/tom-winterton/Documents/code_projects/2025/pi_allSkyCamera/captures'#Desired file path

today = datetime.datetime.now() #Gives today value of current time
print(today.strftime("%Y-%m-%d")) #Prints current date to console in YYYY-MM-DD format
print("AllSkyCamera CLI")

#Write Functions Here#
def runtimeInput(): #Creates function
    maximumTime = 60*24 #60mins x 24hrs = 1440
    timeInput = float(input(f"How many minutes to run? (maximum {maximumTime}) ").replace(" ","")) #Declares timeInput as input and removes string whitespace. Allows decimals.

    if not(int(timeInput) < int(maximumTime) and int(timeInput) > 0):  #Out of time bounds error handelling
        print("Error! Time was out of bounds! Please enter a time between 0 and 1440 minutes.")
        exit
        return False
    else:
        print(":)")   
        print(f"Requested: {timeInput} minutes")
        return timeInput #returns user input for later use


def makeDir():
    todaysDirectory = f"{filePath}/{today.strftime("%Y-%m-%d")}" #String with same YYYY-MM-DD format
    try:
        os.mkdir(todaysDirectory) #Makes directory called todaysDirectory
        print(f"Created directory: {todaysDirectory}")
    except FileExistsError:
        print(f"Directory {todaysDirectory} already exists.")
    except Exception as e:
        print(f"An error occured: {e}")
    return todaysDirectory
    
#Call Functions Here#
if runtimeInput() == False: 
    exit
else:
    print(f"Saving images to: {makeDir()}")#Calls and prints function makeDir
