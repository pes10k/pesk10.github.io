---
layout: page
title: Homework 1
topic: Git setup and Java basics
due_date: 2017-06-16
---

Goals
---
The purpose of this assignment is familiarize yourself with how git will be
used in the class, ensuring that you have Java 8 set up in your environment,
and to begin to use some of the features of the language.  As will be obvious,
the programming tasks aren't intended to be difficult or challenging, just
to make sure everyone is comfortable with the basics.

Requirements
---
You should find a `hw1/src/Main.java` file in your repo. You should use this
file, and only this file, when writing your solution to this assignment.

You should double check that your solution works with the included `makefile`
by running `make clean` to clear out any previous builds, `make build` to
compile your solution, and `make run` to run your solution and see the output.
This `makefile` is how your assignment will be graded, so please make sure your
solution works correctly with your assignment before submitting.

Your code should print out your answer for each question on a single line,
and not print out anything else.  Since there 5 questions below, your program
should only output 5 lines of text (in addition to the text printed by the
makefile).

For this assignment, please write a Java program that does the following:

1. Prints out your email address as the first line of output.
2. Your program should create a varaible with the type `int`, with the value
   `3`.  You should then create an `Integer` reference with this same value.
   The, create a third variable, of type `String`, that contains the
   string representation of this same value, converted from the `Integer`
   version.  Print this string out to the console.
3. Creates an array of `String`s.  Each string in this array should contain
   one part of your name (e.g. for me, the array would contain the strings
   "Peter", "Edwin" and "Snyder").  Your program should then iterate over
   this array, printing each part of your name, with underscores connecting
   each part of the name (e.g. "Peter_Edwin_Snyder").
4. Prints out the current calendar date (determined at runtime, not hard
   coded into the program).  The output for this line should match the format
   "YYYY-MM-DD".
5. Prints out the version of java running your program (determined at runtime,
   not hardcoded into your progam).  Your output should look similar to
   "1.8.0_131".

Resources and Suggestions
---
You might find the following resources useful when completing this assignment.
*  The [`java.time`](https://docs.oracle.com/javase/8/docs/api/java/time/LocalDateTime.html)
   package.
*  The [`System.getProperties`](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#getProperties--)
   documentation.
*  The [`Oracle documentation on printing in Java`](https://docs.oracle.com/javase/tutorial/essential/io/formatting.html)
   for information on how to print information to standard out.
*  The [`Integer`](https://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html#toString()) class
   documentation.
*  The [git notes](https://www.cs.uic.edu/~psnyder/cs342-summer2017/git/) from
   the course website.

If you have any questions or if anything is not clear, please ask on Piazza.

Grading
---
This assignment will be worth 5 points, one for each of the problems above.
There will be no partial credit for any problem.  Make sure you match the
formatting requirements (for the assignment in general, and for each
of the 5 problems) to receive full credit.

Due Date
---
This assignment is due by 11:59AM on Friday, June 16, 2017.
