# **C** Programming Language Fundamentals
---
![](images/c-language.png)
---
### ***C*** is a procedural programming language. It was initially developed by Dennis Ritchie between 1969 and 1973. It was mainly developed as a system programming language to write operating system. The main features of ***C*** language include low-level access to memory, simple set of keywords, and clean style, these features make ***C*** language suitable for system programming like operating system or compiler development. Many later languages have borrowed syntax/features directly or indirectly from ***C*** language.

---
## Structure of **C** Program
![](images/c-structure.png)
---
#### 1. **Header Files Inclusion:** The first and foremost component is the inclusion of the Header files in a C program. A header file is a file with extension .h which contains C function declarations and macro definitions to be shared between several source files.

**Syntax to include a header file in C:**

\#include <(header_file_name).h>

***Example:***
* stdio.h  - Defines core input and output functions

#### 2. **Main Method Declaration:** The next part of a C program is to declare the main() function.

**Syntax to Declare main method:**

**int main()**

{}

#### 3. **Variable Declaration:** The next part of any C program is the variable declaration. It refers to the variables that are to be used in the function. Please note that in C program, no variable can be used without being declared. Also in a C program, the variables are to be declared before any operation in the function.

***Example:***
* int main()

  {

    **int a;**

  .

  .

#### 4. **Body:** Body of a function in C program, refers to the operations that are performed in the functions. It can be anything like manipulations, searching, sorting, printing, etc.

***Example:***
* int main()

  {

    int a;

    **printf("%d", a);**

  .

  .

#### 5. **Return Statement:** The last part in any C program is the return statement. The return statement refers to the returning of the values from a function. This return statement and return value depend upon the return-type of the function. For example, if the return type is void, then there will be no return statement. In any other case, there will be a return statement and the return value will be of the type of the specified return-type.

***Example:***
* int main()

  {

    int a;

    printf("%d", a);

    **return 0;**

  }
