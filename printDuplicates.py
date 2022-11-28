# Given an input string, get all the duplicat characters of the string 
# and print the count of duplicate characters

def findDuplicats(string):
    string = string.replace(" ", "")
    countMap = {}

    for i in string:
        countMap[i] = 1 + countMap.get(i, 0)
    
    for char in countMap:
        if countMap[char] > 1:
            print(f"{char}, count = {countMap[char]}")

findDuplicats("my name is binayak")