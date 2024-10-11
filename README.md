# Exercises for week 2:

### 1
Write the code that will ask the user for their height and weight. The program must calculate their BMI using the formula weight / (height * height). Print out their weight, height and BMI, each on separate lines and include a description of each, like this:
```
Your weight is: 60kg
Your height is: 1.7m
your BMI is: 21
```

### 2
If we want to total some numbers up we can do it as follows:
```
sum = 0
number = int(input(“enter the first number”))
sum += number
number = int(input(“enter the second number”))
sum += number
number = int(input(“enter the third number”))
sum += number
print(“The sum of the numbers is”, sum)
```
How can we achieve this without using the variable number (we would still have 3 input lines)

### 3
Write a program which estimates a user's typical food expenditure. The program asks the user how many times a week they eat out. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week. Based on this information the program calculates the user's typical food expenditure both weekly and daily. The program should function as follows: 
```
How many times a week do you eat out? 4 
what is the price of a typical student lunch? 4.95 
How much money do you spend on groceries in a week? 45.50
Average food expenditure: Daily: 9.33 Weekly: 65.3 
```

### 4
Make use of functions.py (provided to you from Canvas). Create a new function called average(). Pass 3 marks to the function, calculate the average and print the average in the function. Remember to call the function appropriately.

### 5
Write a function that accepts one integer value. The function contains the following word = “thinking”. Return the word duplicated over and over, depending on argument passed in. for example if the number was 7, then the output should be thinkingthinkingthinkingthinkingthinkingthinkingthinking

### 6
Create a function like this:
```
def summing(*args):
    return sum(args)
```
Call the function 3 times, the first time passing 3 nums, the 2nd time passing 6 numbers and the 3rd time passing 10 nums.

### 7
Write a function using *args and **kwargs that prints out the arguments passed to it, using the following function calls:
```
the_function(5, 10, stud_nbr="12345", mod_code="SWW1")
the_function(8, 7, stud_nbr="56784", mod_code="SWW1")
```
Do you know which arguments are positional and which are keyword?

### 8
Given the following 2 functions, write the calling function.
```
def the_function(num1, num2, num3):
    print(num1, num2, num3)

def another(*args):
    the_function(*args)

#function call here
```

### 9
Given the following function, create a function call to display a name, age and location and another one that just shows the name and age.
```
def create_profile(**kwargs): 
    profile = { 
              'name': kwargs.get('name', 'Unknown'), 
              'age': kwargs.get('age', 'Unknown'), 
              'location': kwargs.get('location', 'Unknown') 
    } 
    return profile 

#function calls here 
```

### 10
Given the function call, write the function to find the minimum and maximum numbers, make use of min() and max() functions to accomplish this.
function call:
```
the_min, the_max = find_min_max(2, 5, 7, 9, 10, 1)
print(the_min, the_max)
```
