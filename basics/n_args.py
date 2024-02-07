# for factorial just eg
# def product_of_all(a,b,c,d) instead we will
def product_of_all(*args):
    product = 1

    for i in args:
        product  = product * i

    return product

total = product_of_all(1,2,3,4,5)
#print(total)

# Fn as dict
def stu_data(**kwargs):
    # print("------------------")
    # print("name -- ",kwargs.get('name'))
    # print("------------------")
    # print("age -- ", kwargs.get('age'))
    # print("------------------")
    # print("email -- ", kwargs.get('email'))
    
    for i in kwargs.keys():
        print("------------------")
        print(i, " - ", kwargs.get(i))

stu_data(email = 'shubh@mail.com', name = 'Shubh', age = 22, location = "Bhopal")
