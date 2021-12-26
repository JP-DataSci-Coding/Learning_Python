# Python_100_Days_Of_Code

This repo contains general notes, exercises and projects written in Python.

## Table of Contents

1. [Basics](#basics)

2. [Primitive Types](#primitive-data-types)

3. [Mathematical Operations](#mathematical-operations)

4. [File Processing](#file-processing)

5. [Modules](#modules)

6. [Data Structures](#data-structures)

7. [Big-O](#big-o)

8. [Memory](#memory)

9. [Threading and Concurrency](#threading-and-concurrency)

10. [Solving Problems](#solving-problems)

11. [Software Development Principles](#software-development-principles)

12. [Projects](#projects)

### Basics

Python is a high-level programming language - a programming language with strong abstraction from the details of the computer. For example, C and C++ are now considered low-level languages because they have no automatic memory management. High-level languages may automate (or even hide entirely) significant areas of computing systems (e.g. memory management), making the process of developing a program simpler and more understandable than when using a lower-level language. The amount of abstraction provided defines how "high-level" a programming language is.

Python is also an object-oriented language, i.e., everything is an object (an instance of a class).

#### Strings

Strings are a data type used for data values that are made up of ordered sequences of characters, such as "Hello World!". A string can contain any sequence of characters, visible or invisible, and characters may be repeated. The number of characters in the string is called its length.

##### String Concatenation

String concatenation is the operation of joining character strings end-to-end:

```
print("Hello" + " " + "World!")
```

#### Variables

Variables are an abstract storage location paired with an associated reference name. 

##### Naming Convention

Typically you can either use:

1. Snakecase - words are delimited by an underscore.

variable_one

2. Pascalcase - words are delimited by capital letters.

VariableOne

### Primitive Types

A program updates variables in memory according to its instructions. Variables come in types - a type is a classification of data with a well-defined set of possible values it can take and the operations that can be performed on it. 

Python has a number of built-in types:

- Integer
- Float
- String
- Boolean (true or false)
- Sequences (e.g. list)
- Mappings (e.g. dict)
- Classes
- Instances
- Exceptions

#### Check Type

You can check the type using the following syntax:

```
char = "Hello"

type(char)
```

#### Convert Type

There are various functions available for converting to different types, for example, the below syntax would convert the type to a string:

```
num_char = 9

str(num_char)
```

### Mathematical Operations

The basic mathematical operations are as follows:

```
6 + 3
6 - 3
6 * 3
6 / 3 # Divisions always return a float
2 ** 2 # Power
```

It is important to also remember the order of mathematical operations:

1. ()
2. **
3. * or / depending on the order of which comes first in the code
4. + or - depending on the order of which comes first in the code


#### Number Manipulation

##### Floor Division

Floor division cuts off the part after the decimal in a division and will always take the floor or the lower number. So, for example:

```
10 // 3 # Returns 3 instead of 3.33...
```

##### Modulo

Modulo returns the remainder of an **integer** division:

```
27 % 16 # Returns 11 because 27 can only be divided by 16 once, i.e., 11 is the remainder of 27 - 16
```

The process is basically:

```
27 // 16 = 1

1 * 16 = 16

27 - 16 = 11
```

##### String Interpolation

```
weight = 50

print(f"You weigh {weight}kg.")
```

### File Processing

#### Opening and Reading a File

When the read operation of a file first begins, the file cursor (pointer) starts with the very first character in the file and eventually ends with the very last character. It is important to remember this because if you execute two read operations like so:

```
my_file = open(path_to_file + 'file.txt')

print(my_file.read())
print(my_file.read())
```

A file can also be opened with the following syntax, and is probably a better way of doing it:

```
with open(path_to_file + 'file.txt') as my_file:
    content = my_file.read()
```

You may expect the second read operation to re-print the entire content of the file.txt file, but what will actually happen is nothing will get printed to the console, as the cursor for the file is no longer pointing to the start of the file. This is why it is better to save the content to a variable first like so:

```
my_file = open(path_to_file + 'file.txt')

file_content = my_file.read()
```

#### Closing a File

It is good practice to also close a file once you are finished with it, as this reduces the risk of the file being unwarrantedly modified or read.

```
my_file.close()
```

**Note!** When opening a file using the "with" syntax, the file closes implicitly.

### Modules

A module is a software component or part of a program that contains one or more functions. One or more independently developed modules make up a program. An enterprise-level software application may contain several different modules, and each module serves unique and separate business operations.

In Python, modules are simply files with the “. py” extension containing Python code that can be imported inside another Python program. In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.

We can import modules by:

```
import module_name
```

### Data Structures

#### Python's Built-in Data Structures

Python has four built-in data structures:

- Lists
- Dictionaries
- Tuples
- Sets

##### Lists

Lists are used to store multiple items in a single variable and are created using square brackets:

```
fruits = [apple, orange, grape]
```

List items are ordered, changeable, and allow duplicate values.

You can also create a list of ranges, so for example, if we wanted to create a list of numbers between 0 and 9:

```
list(range(1, 10)) # Outputs [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Notice how the range function does not include the last number.

Lists can also contain other lists, also called a 2D list:

```
two_lists = [[1, 2, 3]]
```

##### Dictionaries

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates:

```
names_age = {
    "James": 20,
    "Alice": 25,
    "Bob": 34
}
```

##### Tuples

Tuple items are ordered, **unchangeable** (immutable, so you cannot even append or remove), and allow duplicate values:

```
tuple = ("apple", "banana", "cherry", "apple", "cherry")
```

##### Sets

A set is a collection which is*unordered, unchangeable, and **unindexed**.

```
set = {'apple', 'banana', 'cherry}
```

#### Implementing Data Structures

A data structure is just an object where we store and organise data, and each type has its own characteristics and purpose.

##### Arrays (Lists)

- Lookup - O(1)
- Push (Append) - O(1)
- Insert - O(n)
- Delete - O(n)

##### Hash Tables (Dictionaries)

Hash tables are great for accessing data quick and efficiently. This is because each piece of data is assigned to a unique key, and we can instantly access the data if we know the key. 

So, say we create a key called 'grapes', this gets sent into a **hash function** (cryptography - take inputs of variable lengths to return outputs of a fixed length, the output is the crypto key or secret that hides the data) and the hash is mapped to a memory address where the data is stored. In other words the hash value generated is the memory location where the record is stored. This adds a layer of protection because it makes it impractical to reverse the hash back into the original key.

- Lookup - O(1)
- Push (Append) - O(1)
- Insert - O(1)
- Delete - O(1)

From the above, it seems like hash tables should be used all the time, but, there is an issue called **collisions** that we need to remember. A hash collision occurs when a hash algorithm produces the same hash value for two different input values.

For instance, say we use a person's name as the key and their phone number as the value. The phone number would get stored in a memory bucket/slot. Now, in a scenario where we have many records of people's phone numbers, eventually we would run into a scenario where the hash funtion will produce the same hash value for two or more people. Due to this collision, these records with the same hash value will essentially get stored in a **linked list** in memory (just one of the solutions), since you cannot store the record in the same memory slot. Therefore, this significantly slows down our ability to access information and the time complexity will become **O(n)**.

Every hash function will eventually result in collision because there are a finite number of possible address values that can be created from a hash value through modulo. The longer the hash value, the less chance of a collision. For example:

*Consider a really stupid hash function: A number modulo 31. In other words, the remainder when you divide the number by 31. 1 modulo 31 is 1. 35 modulo 31 is 4. And so on. It’s pretty obvious that 32 mod 31 is 1, and 63 modulo 31 is 1… and that’s a hash collision. And it happens pretty often for random numbers - 1 try in 31. And it’s trivial to make it happen on demand - knowing that some other number is 5 modulo 31, it’s pretty easy to find another number that’s also 5 modulo 31. This is obviously too weak for cryptography, but if you’re just implementing a hash function for storage it may be good enough to split a single long linked list into 31 shorter lists.

Now, any given hash function *will* have potential collisions. Consider a hash function that outputs a 16-bit binary number. This can have one of 65,536 possible values. So it’s possible that you can hash 65,536 different inputs and (potentially) get back that many outputs. But the 65,537th input *has* to hash to the same thing as one of the first 65,536 inputs.*

Good explanations can be found here: 

https://stackoverflow.com/questions/730620/how-does-a-hash-table-work

https://www.quora.com/Why-do-collisions-occur-in-hashing

###### Static vs Dynamic Arrays

**Static**

Static arrays are fixed in size, so the user would need to specify the number of elements the array will hold before instantiation.

**Dynamic**

Dynamic arrays are the most commonly used as they are flexible. When an array is resized, the following process is executed:

1. An initial array of 4 elements is created.

2. Machine receives instructions to add a fifth element.

3. Machine loops over each element, and copies and moves them to another set of free memory slots. It usually doubles 
the amount of slots, so in this case 8 free slots are assigned for the array object.


### Big-O

#### What Is Good Code?

1. Readable

2. Scalable:

- Time (speed) complexity (Big-O)
- Space (memory) complexity

**Note!** Usually there is a trade-off between speed and memory.

#### Big-O and Scalability

Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. 

In other words, it measures the performance or complexity of your code in relation to the amount of inputs or data it has to process.

#### Time Complexity

Time complexity refers to how the overall runtime of your code is affected with the increase in input size.

##### Rules of Calculating Big-O

When calculating the Big-O of a piece of code, there are several rules that simplifies the process:

- Take the worst time complexity, i.e. the best case scenario does not matter in the grand scheme of things
- Ignore constants - we only care about scalability, i.e. does the increase in inputs matter?
- Different terms for inputs - e.g. a function takes two different input arguments, then we need to account for this. So if a function has one for loop for each input, then instead of just O(n), the Big-O becomes O(a + b) where a and b represents the scalability for each input.
- Drop non-dominant terms - this is related to the first rule. Say that we have a function with the following Big-O:

O(x^2 + 3x + 100 + x/2)

As we are only worried about scale, we just need to keep x^2 and drop the rest as they are non-determinant, thus, the Big-O just becomes:

O(x^2)

##### Big-O Types

- O(1) - constant time, i.e. input does not affect complexity.

- O(log n) - logarithmic time. Usually searching algorithms have log n if they are sorted (binary search).

- O(n) - linear time.

- O(n log(n)) - log linear time. Usually for sorting operations.

- O(n^2) - quadratic time (nested loops). **Note!** For the huge majority of cases, if you have three nested loops, you usually are doing something wrong. So O(n^3) should be an extreme rarity.

- O(2^n) - exponential time. Recursive algorithms that solves a problem of size n.

- O(n!) - factorial time. If your code has this Big-O, then you are almost certainly doing something wrong. What this basically means is that you have a nested loop for every input element have!

#### Space Complexity

When we are talking about space complexity, what we are really looking for is the amount of **additional** space that our code requires. Therefore, we don't really care how large the input is, because it is not a variable that we can really control. So, what are variables we can control that take space?

- Variables
- Data Structures
- Function Calls
- Allocations (requesting access to data)

Like, time complexity, we use big-o to assess how much the amount of memory required increases with the size of the input. The concept is essentially exactly the same, but we are just looking at code from a memory point of view.

### Memory

A machine can simply be broken down into three parts:

- CPU (Central Processing Unit) - runs the actual processes of the machine.

The CPU is connected to the RAM through what is called a **memory controller**, which carries out the actual reading and writing of data in the RAM.

It also has an extremely tiny space of memory where it stores data that has been used very recently. This is what we all the **cache**.

- RAM (Random Access Memory) - you lose the memory when the machine turns off. So why do we need the RAM if we lose our data? Storage is slow, i.e. the CPU can access data from the RAM much faster than storage.

For example, say we have Google Chrome installed on our machine. It obviously consists of thousands of lines of code (which are stored in storage). The CPU will execute the browser when the user commands it to, and any data that is part of the scripts involved in running the various processes of the browser (when in use) will be temporarily stored in the RAM and deleted when the browser is closed.

Now, the RAM consists of shelves, with each shelf having an address - which is bascially a number, kind of like an ID, and each shelf can store 8-bits (0 or 1) or byte of data. The memory controller has connections to each of these shelves through the address, therefore, it can access the required memory instantly without having to go through each one.

- Storage - also called **permanent** or **persistent** because the objects that are stored here must be deleted manually. So software, photos, videos, documents etc are stored in persistent storage.

#### How is Memory Divided?

Memory (RAM) is divided into multiple segments. Two of the most important ones are the:

- Stack
- Heap

The stack is essentially an ordered insertion place while the heap is all random — you allocate memory wherever you can.

#### Stack Memory Overview

A stack is a special area of a machine's memory which stores temporary variables created by a function. In a stack, variables are declared, stored and initialised during **runtime**.

It is a temporary storage memory. When the computing task is complete, the memory of the variable will be automatically erased. The stack section mostly contains methods, local variables, and reference variables (reference to some object instance of a given class).

This memory is also managed by the program and not by the developer.

#### Heap Memory Overview

The heap is often used to allocate big amounts of memory that are supposed to exist as long as the developer wants. It is used by programming languages to store **global variables** (variables that are visible and hence accessible throughout the program, i.e. the global environment). By default, all global variable are stored in heap memory space. It supports Dynamic memory allocation.

The heap is not managed automatically for you and is not as tightly managed by the CPU. It is more like a free-floating region of memory.

When building complex programs, you often need to allocate big chunks of memory, and that’s where you use the heap. We call this **dynamic memory**.

#### Garbage Collection

In Python memory allocation and deallocation method is automatic as the Python developers created a **garbage collector**, so that developers do not have to do manual garbage collection.

Garbage collection is a process in which the interpreter frees up memory slots that are not in use to make it available for other objects.

Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine has a garbage collector that automatically deletes that object from the heap memory.

#### Stack Overflow

A stack overflow is an undesirable condition in which a particular computer program tries to use more memory space than the call stack has available.

The size of a call stack depends on various factors. It is usually defined at the start of a program. Its size can depend on the architecture of the computer on which the program runs, the language in which the program is written, and the total amount of available memory in the system. When a stack overflow occurs as a result of a program's excessive demand for memory space, that program (and sometimes the entire computer) may crash.

### Threading and Concurrency

### Solving Problems

#### General Steps

1. Verify the constraints of the problem

2. Write test cases

### Software Development Principles

#### Object-Oriented Programming (OOP)

##### Creating a Class/Object in Python

###### Constructors

Constructors are the first function that gets called when an object is instantiated. The task of constructors is to **initialise(assign instance attribute values)** to the **instance attributes** of the class when an object of the class is created. A **class attribute** is a variable that is defined within the class and not the constructor, i.e. it is defined before instantiation and is thus shared across all instantiations of the class. There are two important rules to remember when it comes to class attributes:

1. Class attributes can be accessed using the class name as well as well as the object (instantiation) name with dot notation, e.g. classname.class_attribute or object.class_attribute.

2. Changing value by using classname.class_attribute = value will be reflected to all the objects.

In Python the __init__() method is called the constructor and is always called when an object is created:

```
class myClass:

    count = 0 # Class attribute

    def __init__(self, name, age): 
            self.name = name # Instance attribute
            self.age = age # Instance attribute
```

The **self** keyword is used to represent an instance (object) of the given class. It basically is a reference pointer to the current instantiation, so we need to use this keyword everytime we define a function that is unique to the object and not the class:

```
class myClass:

    count = 0 # Class attribute

    def __init__(self, name, age): 
            self.name = name # Instance attribute

    def say_phrase(self, phrase):
        print(self.name + ' says' + phrase)

```  

#### Parent and Child Objects

In OOP, a parent is one class, and a child is another class that inherits all of the attributes and functions assigned to the parent class.

### Projects

#### 1. TextPro App

A very simple console app that asks the user for a phrase and then concatenates each phrase.

#### 2. Population and Volcano Interactive Web Map App

A simple interactive web map that consists of three layers:

- World map
- Population polygons
- US volcano markers

This project has been built using the **Folium** library. Python Folium allows us to combine data and Python programming with **Leaflet.js** (an open source JavaScript library used to build web mapping applications.) to build powerful, interactive web maps. 



