# manipulating files from py

# make and write to a new file 

fl = open("Created.txt", 'w')
fl.write("Shubham,Gautam,Ravi,Lukman")
fl.close()

# read from a existing file

fl = open("Created.txt",'r')
tmp_st = fl.read()
fl.close()
# print(tmp_st)

# append to the exiting file

fl = open("Created.txt",'a')
tmp_st = fl.write("Learning Python, Going college, on_going")
fl.close()

fl = open("Created.txt",'r')
tmp_st = fl.read()
fl.close()
# print(tmp_st)

# append in new Line
fl = open("Created.txt",'a')
tmp_st = fl.write("\n\n New line hai ye to,ok, le lo aab")
fl.close()

fl = open("Created.txt",'r')
tmp_st = fl.read()
fl.close()
print(tmp_st)

print("\n\n\n")

# reading new file directly 

fl2 = open("new_file.txt",'r')
print(fl2.read())
fl2.close()