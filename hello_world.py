# anything which comes inside the inverted commas is called string 
# ctrl + s for save 
# ctrl + / for comments  
# numbers is know as integers in python and you dont use commas during print 
# escape sequence : \n (next line)  \t (for space)  \ "text \"
# print('hello \nworld  \t Piaic') 
# print(" \"he said\"  : something")




# print : str 
# print = "piaic"
# print(print)


# print(4)

# # anything you use to store data is called variable

# declaration
your_name : str  
# # initialization 
# your_name = 8

# # dont start var name with number
# # pre define name cant be use as a var
# # you cant use space
# # you cant use special character

# # make clear var names
# if you define datatype of any var you have to store same type of data init




# f" uzair {var} "  syntax


# message : str =  "    ahmed   "
# print(message.strip())

# url: str = input("Write your URL: ")

# if url.startswith('http://'):
#     print(url.removeprefix('http://'))
# elif url.startswith('https://'):
#     print(url.removeprefix('https://'))
# else:
#     print("Invalid URL")


# # num : int; num1 :int; num2 : int  = 87,64,67
# # print(num,num1,num2) 
# # Using type hints for individual variables

# # num: int
# # num1: int
# # num2: int

# # # Assigning values to the variables
# # num, num1, num2 = 87, 64, 67

# # print(num, num1, num2)


# # message : str = "Hello Python Crash Course reader!"
# # print(message)

# # name : str = "uzair"
# # age : int = 20
# # address : str = "Lahore"
# # print(f" My name is  {name.title()} \n and my age is {age} \n and my is address {address} ")

# # name : str = "     uzair"
# # print(name)
# # print(name.strip())

# # nostarch_url : str = 'https://nostarch.com'
# # print(nostarch_url)
# # print(nostarch_url.removeprefix('https://nostarch'))
# # universe_age : int = 140_000_00000
# # print(universe_age)

# num1 : int
# num2 : int
# num3 : int

# num1,num2,num3 = 6 ,5 ,8
# FORMULA_OF_WATER : str = "H20"




import os;
base_path = r'C:\Users\LENOVO\OneDrive\Desktop\a'
for i in range(1,101):
    folder_name = f'Folder_{i}'
    folder_path = os.path.join (base_path,folder_name)
    os.makedirs(folder_path,exist_ok = True)
    
    print(f'Folder_{i} created')










