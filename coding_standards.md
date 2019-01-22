# Defination

In general they are a set of standards and guidelines which should be used when writing the source code for a program.

# What are coding rules and guidelines?

Coding rules and guidelines ensure that software is:

Safe: It can be used without causing harm.

Secure: It can’t be hacked.

Reliable: It functions as it should, every time.

Testable: It can be tested at the code level.

Maintainable: It can be maintained, even as your codebase grows.

Portable: It works the same in every environment.

# Why coding standards are important

Coding standards are important for safety, security, and reliability.

Every development team should use a coding standard. Even the most experienced developer could introduce a coding defect — without realizing it. And that one defect could lead to a minor glitch. Or worse, a serious security breach.

There are four main drivers for using a coding standard:

Compliance with industry standards (e.g., ISO).
Consistent code quality — no matter who writes the code.
Software security from the start.
Reduced development costs and accelerated time to market.

# Examples

1.Indentation

Indentation is discussed in all coding standards at some level. In some languages, indentation is used by the compiler to identify the scope of functions. In freeform languages, such as Java, it has no actual effect on the compilation of code itself, and is just used to make the code more human readable, giving an indication of scope without actually affecting the program directly.

Type 1

if (g < 17 && h < 22 || i < 60) { return true; } else {System.out.println (“incorrect”) ; return false; }

Type 2

if (g < 17 && h < 22 ||  i < 60) 

{

 	return true; 

}

 else 

{

	System.out.println(“incorrect”);
	
	return false; 

} 


2.Commenting code

Comments should clearly demonstrate the function of the code, not only to other developers but also to you. Often when writing larger programs it can be easy to lose track of what certain functions do, and it is easier to read a well written comment that it is to trawl through lines of code trying to remember what the function of the code you have already written. 
Comments should also not be too long. If your code has followed a coding standard, it should not be too difficult for developers to understand your code. Long comments are often unnecessary and make your code look messy.

#It will add one column to the database

def AddData()

3.Variable declarations.

This is another area which is almost always included in coding standards. Variable declarations are often overlooked when programming but in larger programs they can be the difference between understanding code and not. Variable declarations should be long and demonstrate the function of the variable which they store. In the majority of programming languages, variable can have any name, excluding a few keywords that are reserved by the language itself.

Type 1

if(a < h && z < o && t < e)

  {

      return true;

  }

  else

    {

        return false;

    }
    
Type 2

if (anil < harish && zain < oakly && tony < eminem)

 {

      return true;

 }

  else

    {

        return false;

    }
    
4.Use of Braces

In some languages, braces are used to delimit the bodies of conditional statements, control constructs, and blocks of scope. Programmers shall use either of the following bracing styles:

for (int j = 0 ; j < max_iterations ; ++j)

{

 /* Some work is done here. */

}

or the Kernighan and Ritchie style:

for ( int j = 0 ; j < max_iterations ; ++j ) {

 /* Some work is done here. */

} 

5.Structured Programming

In structured programming,we divide the whole program into small modules, so that program become easy to understand. 

6.Classes, Functions and Methods

Keep subroutines, functions, and methods reasonably sized. The names of the classes, subroutines, functions, and methods shall have verbs in them. That is the names shall specify an action, e.g. “get_name”, “compute_temperature”.

7.Source Files

The name of the source file or script shall represent its function.

8 Compiler Warnings

Compilers often issue two types of messages: warnings and errors. Compiler warnings normally do not stop the compilation process. However, compiler errors do stop the compilation process, forcing the developer to fix the problem and recompile. 

