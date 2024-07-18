from datetime import time
from colorama import Fore,Style



def mergesort(data):
    if len(data) == 1:    #base case
        return data
    time1 = mergesort(data[:len(data)//2])    #splits the left side of the data
    time2 = mergesort(data[len(data)//2:])    #splits the right side of the data
    return merge(time1,time2)

def merge(time1,time2):
  finaltimes = []
  time1_pos,time2_pos,finaltime_pos = 0,0,0
  while time1_pos < len(time1) and time2_pos < len(time2):
      t1 = time1[time1_pos].split(',')[3]
      t2 = time2[time2_pos].split(',')[3]
      time1_object = time(* [int(i) for i in t1.split(":")])    #splits up the data to get departure time and turns it into a time object
      time2_object = time(* [int(i) for i in t2.split(":")])    #splits up the data to get departure time and turns it into a time object
      
      if time1_object> time2_object:
          finaltimes.append(time2[time2_pos])    #adds time2 to the final items lists
          finaltime_pos += 1
          time2_pos += 1
      else:
          finaltimes.append(time1[time1_pos])    #adds time1 to the final items lists
          finaltime_pos += 1
          time1_pos += 1
  while time1_pos < len(time1):    #adds the remaining time1 times to the final items list
      finaltimes.append(time1[time1_pos])
      finaltime_pos += 1
      time1_pos += 1
  while time2_pos < len(time2):    #adds the remaining time2 times to the final items list
      finaltimes.append(time2[time2_pos])
      finaltime_pos += 1
      time2_pos += 1
  return finaltimes

#main code

file = open("Departure.csv","r")                        #opens the "Departure.csv" file
data = [item.strip() for item in file.readlines()][1:]  #removes the first line of the file and stores the data in a list
file.close()

sorted_data = mergesort(data)

UNDERLINE = '\033[4m'
BOLD = '\033[1m'
RESET = Style.RESET_ALL

print(f"{UNDERLINE}{BOLD}{'Flight Number':^20}{'Departure':^20}{'Destination':^20}{'Departure Time':^20}{'Arrival Time':^20}{RESET}")      #statement will print out the formatted headers


colours = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,  Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]      #colous for individual lines



for i in range(len(sorted_data)):
    print(colours[i%len(colours)])    #mod statement to will loop through the different colours for different lines 
    
    for individual_data in sorted_data[i].split(","):
        print(f"{individual_data:^20}",end="")
    print(RESET)

new_file = open("SortedDeparture.csv","w")    #creates and opens a new file called "SortedDeparture.csv"
new_file.write("Flight Number,Departure,Destination,Departure Time,Arrival Time\n")
new_file.write('\n'.join(sorted_data))    #writes the sorted data to the new file

new_file.close()    #closes the new file
