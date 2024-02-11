import csv
try:
    print(1/0)
except Exception as e:
    print("This will nor work")
    print(e)
finally: # it will work even if nothing works
    print("Ho gya kya ???")

# try:
#     fl_new = open("new_file_2.csv", 'r')
# try:
#     fl_new = open("new_file_2.csv",'r+') #csv need lib for execution.
#     print(fl_new.read())
#     fl_new.write("\nNilesg,nilesh@rediffmail.com,56")
#     fl_new.close()
# except Exception as e:
#     print("No such File exist !")
#     print(e)
# finally:
#     fl_new.close()
#     print("The code has ended.")
# except:
#     print("File does not Exist !!")

