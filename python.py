 
 #these all are functions of python
 #Print is a function used to print a program.
print(3+1)


 #integer uses 1122 type to calculate.
print(11+22)


 #float is in decimal values 1.2.
print(1.2222+222.222)


 #string is in between characters "".
print ("ste"+"herro")

 #variables is containers of data
 #where area, length, width are all variables
 #where 10, 2, length*width is the assigned values to the variables
length = 10
width = 2
area = length*width
print(area) 

# for adding strings and numbers through explicit conversion to convert between one data type and another we call a function with the name of the type we're converting to.
#in this function we are using str() function for converting a number to string .
base = 6
height = 3
area = (base*height)/2
print ("the area of the triangle is: " + str(area))

#defining functions with def to define a function
#the name of the function is what comes after the keyword. in this example the functions name is greeting after name we have the parameters of the function
#which are written between paraintehes in this we only have one parameter name
def greeting(name, department):
#after this we have the body of the funtion where we state what we want our function to do. the body is indented to the right which is the key charasteristic of python
#always notice the indentation & we can add as many as print body function we want     
    print("welcome, " + name)
    print("you are part of " + department)
greeting("kay", "it support")

#returning fuction return function is used when we want to use our function many times or we dont want to print our function
def area_triangle(base, height):
    return base*height/2
#power of return statement used
#these are two functionns
area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)

#sum of two function
sum = area_a + area_b

#printing the calculated function 
print("the sum of both areas is : " + str(sum))

#exampe 1 of return function
#double slash operator is called floor division operator a floor division divides in number and takes the integar part of the division as the result it means it will not take the decimal value in it
 
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours*3600 - minutes*60 
    return hours, minutes, remaining_seconds

hours, minutes, seconds, = convert_seconds(5000)
print(hours, minutes, seconds)

#remember to make code reusable and clean an example of this is given below
def lucky_number(name):
    number = len(name)*9
    print("hello " + name + ". your lucky number is " + str(number))

lucky_number("kay")
lucky_number("cameron")

#refactoring is used to make used code clean and easy to understand for others
def calculate(d):
    q = 3
    z = q*(d **2)
    print(z)
calculate(5)
#this code is not clean and one cannot understand these code to understand these code we need to refactor these codes
def circle_area(radius):
    pi = 3
    area = pi * (radius**2)
    print(area)

circle_area(5)


#comparing values with booleon booleon one of two possible either true or false
#comparing things between two values

print (10>1)

#using comapring values with equality operator which is == we use this together to see two things equal to each other taking an example of two string 
print("cat"=="dog")

#now using not equal operator != which is the negated form of the equality operator opposite to equality operator
print(1 !=2)

#logical operators these operators allow you to connect multiple statements together and perform more complex comparion which are in python and or not examples

#starting with and operator to evaluate as true the AND operator would need both experssions to be true at the same time 
print("yellow" > "cyan" and "Brown" > "Magenta")

#OR operator the expression will be true if either of the expression will be true and false only when both expressions are false

print(25 > 50 or 1 != 2)

#NOT operator inverts the value of the expression thats in front of it
#if it is true it will print false and if it is false it will become true
print(not 42 =="answer")

#branching the ability of a program to alter its execution sequence it is the key component in making your scripts useful
#starting with if we start with if keyword followed by our comparison. we end the line with a colon the body of the if statement is then indented to the right 
#if the comparison is true the code inside the if body is executed if the comparison evaluates to false then the code block is skipped and willl not be run.

def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be at least 3 char long")
    else:
        print("valid username")

#modulo operatorr is represented by the percentage sign and returns the reminder of the integer division between two numbers
#the integer division is an operation between integers that yields two results which are both integers the quotient and the remainder 
#replacing return without else when a return statement is executed the function exits so that the code that follows doesnot executed

def is_even(number):
    if number % 2 == 0:
        return True
    return False
#left side value is function, middle value is operator, right side value is values
#using elif the difference between elif and if statement is we can only write an elif block as a companion to an if block thats because the condition of the elif statement will only be checked if 
# the condition of the if statement wasn't true

def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be at least 3 characters long")
    elif len(username) > 15:
        print("invalid username must be at most 15 characters long")
    else:
        print("valid username")   

#LOOPs
#while Loops instruct your computer to continuously execute your code based on the value of a condition this works in the similar way to branching if statement
#the difference here is that the body of the block can be executed multiple times insttead of just ones.
        
x = 0
while x < 5:
    print("not there yet, x=" + str(x)) #body of while loop same as function
    x = x + 1 #+1 till the statement get false x=5 satifies
print("x=" + str(x)) #final call

#using while inside our function in this expression we start with defining our function with x =1
def attempts(n):
    x = 1
    while x <= n: #using while loop inside our function which checks to see the x variable is less than the parameter n that the function received if it compares that is true
        print("Attempt " + str(x)) #the code inside the while block to be executed id the while condition is true
        x += 1 #this is the shorthand version of x = x + 1
    print("done") #end tag line
attempts(5)

#the condition used in while loops can also become more complex if we use the logical operator that we encountered when looking into branching AND OR NOT
#one of the most common errors is forgetting to initialize variables with the right values
my_value = 1
while my_value < 10:
    print("hello")
    my_value += 1

# NOTE whenever youre writing loop check that youre initializing all the variables you want to use before you use them
# infinite loops a loop that keeps executing and never stops
# the body of the while loops needs to make sure that the condition being checked will change if it doesnt change the loop may never finish and we get whats called an infinite loops
# FOR LOOP iterates over a sequence of values EX loop is to iterate over a sequence of numbers 

for x in range(5):
    print(x)

#impt things about the range functions first in python and a lot of other programmming languages, a range of numbers will start with the value 0 by default.
#the list of numbers generated will be one less than the given value
#where to use for loops use FOR loop where theres a sequence of elements that you want to iterate
#use WHILE loops when you want to repeat an action until a condition changes


#sometimes we want to start our range not from zero or we want to start from specified number for that we define our range from where to start
product = 1
for n in range(1,10):   #we specified our value not not to start from 0
    product = product * n

print(product)

#NESTED FOR LOOPS are used from one inside another
#in this code we are using the new parameter that we passed to the print function END normally once print has taken the content we passed and written it to the screen then it writes a special character
#that creates a new line called the newline character if we want to print something else instead of the newline character we use the end character

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end="")
    print()

#example for NESTED LOOPS
teams = ['drag', 'wol', 'pand', 'uni']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
         print(home_team + " VS " + away_team)

#list function [] in loops 
for x in [25]:
    print (x) 

#recursion in loop python the repeated application of the same procedure to a smaller problem 
#recursion lets us tackle complex problems by reducing the problem to a simpler one
#in programming recursion ia a way of doinga repetitive task by having a function call itself

def factorial(n): #defing a function
    if n < 2:     #conditional block defining BASE CASE 
        return 1  #return function
    return n * factorial(n-1)      #this is called the recursive case

#example of recursion loop
def factorial(n):
    print("factorial called with" + str(n))
    if n < 2:
        print("returning 1")
        return 1
    result = n * factorial(n -1)
    print("returning " + str(result) + " for factorial of " + str(n))
    return result
factorial(4)
#it have limit of 1000 after that it doesnot work

#DATA STRUCTURES string, list & dictorinies
#first string 
#strings can be written in both single cotts and double cotts

prt ="" #empty string 
prt = "reeeeeeeeeeeeeeeeeeeeeeeeeeee" #really long string
print("name: " + prt +  ", favorite color:" )  #concatenating
len(prt)  #we use len function to get to know how long the string is the len function tells us the number of characters contained in the string

#string indexing this operation lets us accesss the character in a given position or index using square brackets and the number of the position we want
name = "jaylen"
print(name[1])

#negative indexing start from minus - 
name = 'hellloo'
print(name[-1])

#slice of a string the portion of a string that can contain more than one character also sometimes called a substring
#ratio from where we want from the length of a string
fruit = 'pineapple'
print(fruit[:4])
print(fruit[4:])

#string in python are immutable they cant be changed or modified 
#we can change the existing string by defining we string

message = 'i am ironman'
new_message = message[0:2] + 'A' + message[3:]
print(new_message)

#assinging new string with different content even not chagning it at all

message = 'i am ironman'
print(message)

message = 'i am superman'
print(message)


#method a function associated with a specific class and which is used in below class
pets = "cats & Dogs"
print(pets.index('&'))

#checking substring is part of a string or not 
pets = "cats & Dogs"
print('dragons' in pets)    #dragon is a substring 

print('cat' in pets)

#applying it all putting all the knowledge together
#switching old domain email to new domain email ex

def replace_domain(email, old_domain, new_domain):            #first we define the replace_domain function which accepts threee parameter the email address to be checked the old domain and the new domain having all these values as parameters instead of directly in the code makes our function reusable we are just chagning one domain to another we have a gunction which will work with all domains
    if '@' + old_domain in email:         #in the body of the function we check if the concatenation of the sign @ and the old domain are contained in the email address using the keyword in we check this to make sure the email has old domain on the portion that comes after the @ sign if the condition is true the email address needs to be updated
        index = email.index('@' + old_domain) #to do that we first find out the index were the old domain including the @ sign starts we know that this index will be a valid number because weve already checked that the substring was present
        new_email = email[:index] + '@' + new_domain  #using this index we created the new email this is a string that contains the first portion of the old email up until the index we had calculated followed by @ sign and the new domain
        return new_email  #this will return new email
    return email   #if the email didnot contain the new domain then we can just return it which is what we do in the last line

#strip in strings methods
" yes ".strip()
'yes'

#lstrip
" yes ".lstrip()
'yes '

#rstrip
" yes ".rstrip()
' yes'

#format string 
#the format method automatically deals with the integer and number of the string so we dont have to
#the curly brackets arent always empty by using certain expressions inside those brackets we can take advantage of the full power of the format expression
#one of the things we can put inside the curly brackets is the name of the variable we want in that position to make the whole string more readable

name = "manny"
number = len(name) * 3
print("hello {}, your lucky number is {}".format(name, number))

#formatting expression string
#the expression starts with colons to separate it from the field name that we saw before afte the colon we write .2f this means we re going to format a float number and that there should be two digits after the decimal dot
#these expressions are needed when we want to tell python to format our values in a way thats different from the default
#so no matter what the price is our function will always print up to two decimal digits

price = 7.5
with_tax = price * 1.09
print("base price: ${:.2f}. with Tax: ${:.2f}".format(price, with_tax))  #.2f is a float number and : is spearating it from first Value

#function to convert ferinate to celcius
#in this first expression were saying we want the numbers to be aligned to the right for a total of three spaces
#in the second expression were saying we want the number to always have exactly two decimal places and we want to align it to the right at six spacesh

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C" .format(x, to_celsius(x)))  #in this we are using greater than operator to allowing text to the right so that the output is neatly aligned


#LIST
#in python we use [] brackets which indicates where the list starts and ends
#string and lists both are example of sequences

#the difference between strings and list is list are mutable which means they can change this means we can add remove and modify elements in a list 
#simplest change using the append method 
#the append methods adds a new element at the end of the list it dosnt matter how long the list is the element always gets added to the end
fruit = ["pineapple", "banana", "Apple", "Melon"]
fruit.append("kiwi")
print(fruit)

#if you want to insert different element istead of the method you can use the insert method 
#the insert takes the element as the index of the first parameter and an element as the second parameter
#if we use an index higher than the current length the element just gets added to the end you can pass any number to insert 

fruit.insert(0, "orange")
print(fruit)

#using the remove method to remove from the list 
fruit.remove("kiwi")
print(fruit)

#another method of removing the element is the pop method which recieves the index
#the pop method returns the element that was removed at the index that was passed 
fruit.pop(3) 
print(fruit)

#assining something else to that position in a list OR REPLACING
fruit[2] = "strawberry"
print(fruit)

#strings is a sequences of characters and are immutable
#lists are squences of elements of any type and are mutable


#TUPLES
#tuples are sequences of elements of any type that are immutable
#we write tuples in parainthesis instead of square brackets
#the position of the elements inside the tuple have meaning

#unpacking a tuple this means we can turn back the tuple of the three elements into three separate variables

animals = ["lions", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("total character : {}, average length : {}".format(chars, chars/len(animals)))

#emmmunrate function in tuple
#the enumerate function returns a tuple for each element in the list the first value in the tuple is the index of the element in the sequence
#the second value in the tuple is the element of the sequence


winners = ["ashley", "dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


#definingt he peoples names with their mail 
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("alex@example.com", "alex diego"), ("shay@example.com", "shay brandt")]))

#list comprehensions it is used to short the code in one line
#let us create new lists based on sequences or ranges

[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
multiples = [ x*7 for x in range(1,11)]
print(multiples)

#Example
languages = ["python", "perl", "Ruby", "go", "java", "c"]
length = [len(language) for language in languages]
print(length)


#another data type dictionaries take the form of pairs of keys and values
#to get a dictionaries value we use a corresponding value keys
#in python dictornay word willl be the key and the meaning will be the value
#dictionaries use curly brackets in their content

x = {}
print(type(x))

#ex of dictionaries 

file_counts = {"jpg": 10, "txt":14, "csv":2, "py":23}
print(file_counts["txt"])

print("jpg" in file_counts)

#dictionaries are mutable we can add remove or replace
#replaceing

file_counts["cfg"] = 8
print(file_counts)

#the inside the dictinaries are unique if we try to store 2 different keys we just replace one with the other
#we can delete in dictinories with the del key word both the dictonary and the key to the element
del file_counts["cfg"]
print(file_counts)

#if we use a dictionary in a for loop the iteration variable will go through the keys in the dictionary if you want to access the associated values you can either use the keys as 

file_counts = {"jpg": 10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)


#indexes of the dictionary or you can use the items method which returns a tuple foreach element in the dictionary
#the tuple fisrt element is the key and second element is the values

for ext, amount in file_counts.items():
    print("there are {} files with the .{} extension".format(amount, ext))

#sometimes you might just be intreseted in the keys of a dictionary other times we might olny wants the values 
#we can access both with their corrresponding dictionary methods

print(file_counts.keys())

print(file_counts.values())

for value in file_counts.values():
    print(value)

#in this code we are initialising an empty code dictionary then going through each letter in the given string
#for each letter we check if its not already in the dictionary and in that case we initilize an entry in the dicitonary with a value of zero
#finally we increment the count for that letter in the dictionary
#to sum up we created a dictionary where the keys are each of the letters present in the strings and the values are how many times each letter is present
 
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))


#NOTE you want to use dictionaries when you plan on searching for a specific element
#difference between list and dictionaries
#type of values stored in lists and dictionaries in list you can store any data type in dictionaries we can store any data type for the values but the keys are restricted to specific types
#we can use numbers booleans strings tuples as dictionary keys
#data type SET which is bit like a cross between a list anda dictionary
#a set is used when you want to store a bunch of elements and be certain that they only present once


#OPP Object oriented programming
#a way of thinking about and implementing our code
#a flexible powerful paradogm where classes repesent and define concepts while objects are instances of classes
#all numbers list strings dictionaries we seen so far is object and each of them are instances of class repesenting a concepts
#the opp comes down to attributes and methods associated with a type
#the attributes are the characteristics associated to a type
#the methods are the functions associated to a type
#each instance we used in python is upto different in up class they all had the same method but the contents were different 

#the dir functions gets the interpreter to print to the screen a list of all the attributes and methods
#the first bunch here is the special method that begin and end with double underscores these methods arent usually called by those wired names
#the last bunch is the string method which we had come accross
#print(dir(""))

#when we use the help function on any variable or value

#print(help(""))

#the power of object oriented programming is that we can define our own classes with their own attributes and methods


#we are defing our own class in python we use class reserved keyword to tell the computer that we are starting a new class we follow this with a name of a class and a colon
#the python style guideline recommend that class names should start with a capital letter so we will be using that convention
#after the line of class comes the body of the class defination which is indented to the right in this case we havent added anything to the body yet so we use the pass keyword to show that the body is empty
#we can also use the same placeholder in any empty python block

class Apple:
    pass

#defining attributes to python of a apple
class Apple:
    color = ""
    flavor = ""
#here we are creating new instances of a apple class and assigning it to our apple class and assigning to a variable called jonagold
#to creaate a new instance of any class we call the name of the class as if it were a function 
#next set the values of the attributes

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)

#the syntax used to access the attributes is called dot notation because of the dot used in the expression
#dot notation lets you access any of the abilities the object might have (called methods) or information it might store (called attributes) like flavor
#the attributes and methods of some objects can be other objects and can be attributes and methods of their own 
#for example we can use the upper method to turn the string of the color attributes to uppercase 
print(jonagold.color.upper())

#methods functions that operate on the attributes of a specific instance of a class
class piglet:
    def speak(self):  #thats how we define a function as a method of the class this function is reciveing a parameter called self this parameter represents the instance that the method is being executed on 
        print("oink oink")

hamlet = piglet()
hamlet.speak()

#example 2
class piglet:
    name = "piglet"  #this time an attribute called name with a default value of piglet we can change that value later but its a good idea to nake sure our variable is inisilize
    def speak(self):
        print("oink! im {}! oink!".format(self.name))  #we are using self name function to know what name to print this means that its accessing the attribute name from the current instance of piglet

hamlet = piglet()
hamlet.name = "hamlet"
hamlet.speak()

#now we have created 2 instance both of them print their speak name and not the other 
#variables that have different values for different instances of the same class are called instance variables just like name
petunia = piglet()
petunia.name = "petunia"
petunia.speak()

#the constructer of a class is the method thats called when you call the name of the class its always named init 
#the method that starts and ends with two underscores are special methods
#here we have defined a constructor one very important special method this method on top of the self variable that repsents the instance recieves two more parameters colo and flavor
#those values as the values of the current instance
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)

#using the str method we are telling python that we want it to display when the print function is called an instance of our class

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "this apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)

#docstring a brief text that explains what something does remember that the docstring alwaays has to be idented at the same level of the block its documenting
def to_seconds(hours, minutes, seconds):
    """Returns the amount"""
    return hours*3600+minutes*11+seconds

help(to_seconds)


#inheritance the principle of inheritance lets a programmer build relatioship between concepts and group them together 
#in particular this allows us to reduce code duplication by generalizing our code 
#in python we use parentheses in the class declaration to show an inheritance relationship 
#for our new fruit classes we used that syntax to tell our computer that both the apple and the grape classes inherit from the class because of this they automatically have the same
#constructor which sets the color and flavor attributes
#you can think of the fruit class as the parent class and the apple and grape classes as siblings

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

#first we crate an instance of the apple class
#now an instance of the grape class 

grapply_smith = Apple("green", "tart")
carnelain = Grape("purple", "sweet")
print(grapply_smith.color)

#with the inheritance techniques we can use the fruit class to store information that applies to all kind of fruit and keep apple or grape specific attributes in their own classes
#inheritance lets you reuse code written for one class in other classes

#always initialize mutable attributes in the constuctor
#to add package to the dictionary we will use add_package method

class Respository:
    def __init__(self):  #its a method inside the repository class 
        self.packages = {}
    def add_package(self, package):  #thats making use of the values method in the dictionary class 
        self.packages[package.name] = package
    def total_size(self):   #and it accessing the size attribute in the package class that is a power of composition 
        result = 0
        for package in self.package.value():
            result += package.size
        return result

#when we have other objects as attributes we can use all their attributes and methods to get our own code to do what we want 
#remember the keys are the package names and the values are the package objects for our calcuation we only care about the objects so we will retrieve them with the values dictionary method 
#now for each package we want to add the size to the result variable 

#python provides abstraction called modules
#modules used to organize functions classes and other data together in a structured way 
#all these modules are contained in a group called the python import library
#first we will use import module for generating random functions & numbers 

import random
print(random.randint(1, 10))

#this function recieves two parameters and generates a random number between the two parameters that we pass in this case we are generating a random number between 1 and 10 
#the syntax used for calling a function provided by a module is similar to calling a method provided by a class 
#it uses a dot to seprate a module and the function provided by that module 

#next example
#a datetime module provides a datetime class and the atetime class gives us a method called now 
#this now method generates an instance of the datetime clas for the current time 
#we can operate on this instance of datetime in a bunch of ways 
#the print function is calling the str method of the datetime class which formats it in the way that we see here 
#we can also access the instance through its attributes and methods 

import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
 
#the datetime module provides more classes than the datetime class for example we can use the timedelta class to calculate a date in the future or in the past
print(now + datetime.timedelta(days=222))

#in this case we are creating an instance of the time delta class with a value of 28 days then we are adding it to the instance of the datetime class that we already had and printing out the result
###real world concepts are represented by classes###
###instances of classes are usually called objects###
###objects have attributes which are used to store information about them
###we can make objects do work by calling their methods

#sort and sorted in python
#the difference between these two options is that the sort method modifies the list its executed on while the sorted function returns a new list thats been sorted. apart from the they work the same.
numbers = [1 ,2, 5, 4, 5,]
numbers.sort()
print(numbers)

#putting all together 
#their is a secirnio in our real world problems like you want to see how many systems are loged in and how many are loged out we want to see and solve this problem and list all the system that are
#are login and logout and are blank after that we will generate a report of these systems 
# we know that we need to process the events to generate our reports we know how to sort the list of events chronologically we know that we will store the data in a dictionary of sets
# which we will use to keep track of whos logged in where and that we will have a function that generates the dictionary and a separate one that prints the dicitionary 
# first definig a helper function that will sort the list 
# next start coding our processing function which we will call current user the first step to define a function 

def get_event_date(event):
    return event.date  #we will use this simple function as the parameter to the sort function to sort the list 

def current_users(events):   #inside the function we will first sort our events by using the sort method and passing the function we just created as the key 
    events.sort(key= get_event_date)
    machines = {}       #now before we start iterating through our list of results we need to create the dictionary where we will store the names and users of a machine  
    for event in events:  #we need to check if the machine affected by this event is in the dictionary if tis not we will add it with an empty set as the value 
        if event.machine not in machines:
            machines[event.machine] = set()   #now for the login events we want to add the user to the list and for the logout events we want ot remove user from the list for this we will use the add and remove methods 
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
           machines[event.machine].remove(event.user)
    return machines

#for generating
#in our report we want to iterate over the keys and values in the dictionary to do that we will use the method called items that returns both the keys and the values for each pair in the dictionary
def generate_report(machine):
    for machine, users in machine.items():   #now before we print anything we want to ensure that we dont print any machines where nobody is currently logged in this could happned if the user logged in and logged out 
      if len(users) > 0:      #to avoid that we tell the computer only to print when the sets of users has more than zero elements 
        user_list = ", ".join(users)   #we want to print the machine name, followed by the users loged in to the machine separated by commas lets generate the string of logged in users for the machine using the method join      
        print("{}: {}".format(machine, user_list))

#using opp for classing our own function
class Event:
    def __init__(self, event_date, event_type, machine_name, user ):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user