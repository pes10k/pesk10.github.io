---
layout: page
title: Homework 3
topic: Abstract classes and interfaces
due_date: 2017-06-28
---

Overview
---
This assignment aims to give you more practice thinking of factoring code
into classes, abstract classes, and interfaces.  You'll be implementing code
that represents files on disk, and then using that code to implement a command
line application called `fileinfo`.

This assignment contains three types of code, described below in further detail.

### cs342/filetypes
This is where you'll write your code for this assignment.  You can edit the
files in this directory, and create new files as needed.  The classes in this
directory each represent a different type of file.  You goal is to

1.  correctly taxonomize the file types here, according to their mime types
    (ex the MimedPngFile class represents the `image/png` mime type, and
    so should be put in the type hierarchy in a location like
    `MimedFile > MimedImageFile > MimedPngFile`).  You should create any needed
    additional classes needed to correctly and completely taxonomize these types.
2.  implement and abstract methods where it makes sense.  Types that are
    only in the system for classification reasons should be `abstract`, and
    methods that will only be implemented in child classes should also
    be `abstract`.  In short, make sure your functionality is implemented
    where it makes the most sense.
3.  implement the interfaces for their correct types.  Java's interface
    system allows you to categorize functionality that cuts across the
    type taxonomy.  You should implement each interface discussed in the
    next section, for each type it makes sense.


### cs342/interfaces
The java files in this directory contain interface definitions that you'll
implement in this project.   You should not make any changes to the files in
this directory.  You'll instead implement these interfaces for the filetypes
they make sense for.


### cs342/given
This is code, written for you, that implements some of the glue logic
in the `fileinfo` command line application.  You should not make any changes
to these files, though feel free to look through these files, if you'd like,
to better understand how the command line application works.


Requirements
---
Receiving full credit for this assignment requires that you correctly

1.  categorize / taxonomize all of the file types give in the `cs342/filetypes`
    directory
2.  correctly implement the needed methods on those types
3.  mark the classes and methods as `abstract` where it makes sense, and only
    include method implementation where its useful and clean.
4.  implement all the interfaces on all the types that make sense. If this
    is done correctly, you should implement the interfaces 9 times in the
    8 classes (i.e. one class will implement multiple interfaces).
5.  handle errors reasonably.  This does not need to be extensive or
    comprehensive, but when your code encounters an exceptional case where it
    cannot reasonably continue, you should print a message to
    [STDERR](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_.28stderr.29)
    (not **STDOUT**!) describing the error you've encountered, and end execution.
    These error messages should be informative to the user, and specific to the
    error encountered.  For example "Was not able to read the zip file,
    it's password protected" is a good error to print out,
    "IOException, quitting" is a bad message to print out.

Your repo includes a PDF parsing library.  The `makefile` is configured so
that you can use this library in your solution.

Your solution can use the included PDF library,
[PDFBox](https://pdfbox.apache.org/), and any functionality included in
the Java standard library. You are not allowed to use any other code,
either in the form of third party libraries, or copy-pasted from classmates
or websites.

You are allowed to use any of the documentation provided by Oracle or the
PDFBox library.  You are also encouraged to discuss on Piazza.

Your code should never throw an Exception or dump a stracktrace to the console.
It should handle all errors correctly and internally.  Doing so will loose
you lots of points.  Similarly, changing any files or code blocks that you're
prohibited from changing (either in this document, or in the included code
comments) will either disqualify your solution or result in large point
reductions.


Resources and Suggestions
---
I have stubbed out the class files in the `cs342/filetypes` directory with
all the classes and import statements you'll need to complete the assignment,
along with documentation links for each.  You are welcome to use other code
(within the restrictions mentioned above) if you'd prefer, but the already
imported code is sufficient.

You should use the included `fileinfo` script to test your code.  You can
use it by running `./fileinfo <some file>` and looking to see if the output
matches what is expected.  Two test cases are included in the repo for your
testing, but your code should work successfully on any file with any
of the file extensions mentioned in `cs342/given/Registery.java`.

You may also find the following useful:

* [PDFBox Example](https://svn.apache.org/viewvc/pdfbox/trunk/examples/src/main/java/org/apache/pdfbox/examples/pdmodel/RemoveFirstPage.java?view=markup)
* You can write to STDERR with `System.error`
* The class and package documentation linked to in the class stubs provided in
  `cs342/filetypes`

Grading
---
There are a maximum of 20 points possible on this assignment.

* **2 Points**: Correctly taxonomizing the file types according to their
  mime type.
* **2 Points**:  Correctly handling errors (ie helpful error messages, sent
                 to STDERR, etc.)
* **6 Points**:  Correctly marking classes and methods as abstract
* **10 Points**: Having `fileinfo` return the correct output for each of 5
                 test cases (2 points per test case).

Due Date
---
This assignment is due by 11:59AM on Wednesday, June 28, 2017.
