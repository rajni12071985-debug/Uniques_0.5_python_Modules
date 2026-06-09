


# dictionary----- data type that stores key-value pairs. Each key is unique and maps to a specific value. Dictionaries are mutable, meaning you can change their contents after they are created. They are defined using curly braces {} and key-value pairs are separated by commas. The keys and values can be of any data type.
#my_store = {"apple": 20, "banana": 10, "orange": 15}  
#print((my_store["apple"]))


# loops ---- repetitive task 

# for loop 


for i in range( 1,10):
    print(i)

    # print * square patten
for i in range(1,6):
    for j in range(1,6):
        print("*", end="")
    print()  # Move to the next line after printing each row




    list = [1,2,3,4,5,6,7,8,9,10]
for num in list:
    print(num)

for list in range (3,6):
    print(list)



my_store = {"apple": 20, "banana": 10, "orange": 15}

for item, price in my_store.items():
    print(f"{item}: {price}")



    # function

def greet(name ,age):
    return f"Hello, {name} ,{age}!"  
print(greet("Alice", 25))  # Output: Hello, Alice, 25!
  
 # deffault parameter value
def greet(name, age=30):
    return f"Hello, {name}, {age}!"

print(greet("Bob"))  # Output: Hello, Bob, 30!


def output(message):
    print(message)

def output_1(message):
    print(message)    
output("hii bhaya")   
output_1("hii there") 

# python installation 
# variable
# if - else statement
# data types    
#loops
# function
#dictionary
