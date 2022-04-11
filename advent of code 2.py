import re

array = ["forward 5",
         "down 5",
         "forward 8",
         "up 3",
         "down 8",
         "forward 2"]

horSt = 0
depthSt = 0
horizont = 0
depth = 0

if(array[0] == "forward"):
    horSt = (re.findall('[0-9]+', array[0]))
    print(horSt)
# for i in range(len(array)):
