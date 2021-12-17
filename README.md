# Python_100_Days_Of_Code

## Table of Contents

1. [Basics](#basics)

2. [Primitive Types](#primitive-data-types)

3. [Mathematical Operations](#mathematical-operations)

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

A program updates variables in memory according to its instructions. Variables come in types - a type is a classification of data that spells out the possible values and the operations that can be performed on it. 

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

Floor division cuts off the part after the decimal in a division and will always take the floor or the lower number. So, for example:

```
10 // 3 # Returns 3 instead of 3.33...
```



