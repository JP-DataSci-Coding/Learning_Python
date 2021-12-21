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

11. [Projects](#projects)

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

#### Implementing Data Structures

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

#### How is Memory Divided?

Memory is divided into multiple segments. Two of the most important ones are the:

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

### Projects

#### 1. TextPro_App

A very simple console app that asks the user for a phrase and then concatenates each phrase.

#### 2. 