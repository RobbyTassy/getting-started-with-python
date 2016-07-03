#This will provide Python instruction to locate and write in a file
# w option writes according to your code - in this case, it writes text into a file (alterations made to file directly will be overwritten by code)
file = open ("/users/rtass001/Documents/projects/wyncode_projects/python-projects/newsamplefile.txt", "w")
file.write ("This file was created as a result of code executing from the reading-and-writing-file.py file.")
file.close ()

# a option appends according to your code - in this case, it appends to existing text in a file (alteration made to file directly will continue to exist when using 'a'
file = open ("/users/rtass001/Documents/projects/wyncode_projects/python-projects/newsamplefile.txt", "a")
file.write (" This sentence was appended by executing the append in Python.")
file.close ()
