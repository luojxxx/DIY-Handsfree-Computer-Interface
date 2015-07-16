pmName = input('Enter file name : folder/___.py ')
pm = __import__(pmName)
print(dir(pm)) # just for fun :)