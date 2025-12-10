---
layout: page
title: Homework 5
topic: Unit testing and test driven development
due_date: 2017-07-17
---


Overview
---
In this assignment, you'll build on and improve the sentence parsing example
from class.  You'll need to write code that'll parse a text into a series
of sentences.  You'll find that this is surprisingly difficult, for a variety
of reasons:

* In English, you can "nest" sentences, with quotation marks.  For example,
  the sentence 'Pete said, "Parsing sentences is difficult.  Good luck!"
  to the class, with a sinister grimace.' should be treated as one sentence,
  not three.
* English overloads period, both as a sentence terminator, and for denoting
  abbreviations.  For example, "Pete is flattered to be mistakenly called
  professor, even though he doesn't have a Ph.D." is one sentence, not two.
* Sometimes, sentence terminators are not really used as terminators.  For
  example, 'Please read this so called "e-text."' is one sentence, even
  though it doesn't end with a period.

You'll find that there is no easy, obvious, general solution to this problem,
and you'll need to rely on a variety of heuristics and rough approaches.  As
a result, you'll need to make sure that improving your solution in some new
manner does not in turn break some other case you previously handled correctly.

This makes the problem a good target for test-driven-development, or
building the "success conditions" for your code first, and then building code
that successfully meets those conditions.

In this case, you'll be using [jUnit](http://junit.org/junit4/) to build unit
tests, each of which should present some new challenge in parsing a text
into sentences.  Your repo already includes one test case in
`tests/SentenceParserTest.java` in the `SentenceParserTest#toSentencesExample1Test`
method.

You have to tasks in this assignment.  **First**, you should create *at least*
10 more test cases, each posing some different challenging test case in
sentence parsing.  Each test you implement should embody some new
difficulty in parsing a text into sentences (and the accompanying javadoc
docblock should explain the difficulty the test is testing for).

**Second**, you should implement a solution for parsing a text into sentences
in the `edu.uic.cs342.SentenceParser#asList` method.  You should improve your
solution by making it pass as many of your tests as possible.  Your solution
will not be evaluated based on how may of *your* tests your solution passes
(it'll be evaluated based on how many TA-created tests your solution passes).
But by passing your own well created tests, you maximize your chances of passing
the TA-created tests.


Requirements
---
Your code should meet all of the following requirements:

* You must create 10 new test cases, each embodying some difficulty in
  sentence parsing, and each test case documented to explain *what* difficulty
  the test case is meant to demonstrate.
* Your code should correctly handle all errors.  Your code *must not* ever
  exit, or print anything to STDOUT or STDERR. Doing so is inappropriate
  for library code.  All output or exiting must be handled by the code
  calling into your libraries (i.e. `Main.java`).  TL;DR, you must handle
  error cases by throwing exceptions, not printing debug messages or
  exiting.
* Your code must be nicely / readably formatted, following Google's Java
  style (not that Google's format is *best*, but that its well documented
  and at least *good*, certainly way better than no standard).
* Your code must be correctly documented.  All methods, properties, and
  classes must be documented following "javadoc" conventions.


Resources and Suggestions
---
* [Regular Expressions in Java](http://www.vogella.com/tutorials/JavaRegularExpressions/article.html)
* [Project Gutenberg](https://www.gutenberg.org/), as a place to find a large
  number of texts to possibly use as new test cases.
* [jUnit 4](https://github.com/junit-team/junit4/wiki/Getting-started) guide for
  using jUnit for unit testing.
* [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)

Your repo also includes a helper `./sentparse` tool, which you can use
to more conveniently interact with your program.  Using `./sentparse --help`
will provide more information about how to use the program and pass filter /
sorting / output options.

You can run a text through your `SentenceParser#asList` method in two ways,
either by providing a path to using the `./sentparse --path <SOME FILE>`, or
by passing the text to your program through `STDIN`, such as
`cat <SOME FILE> | ./sentparse`.

You can also use the included `makefile` to conveniently perform some common
tasks with your code.
* `make clean` will clear out your previously built `*.class` files
* `make build` will build your java project
* `make cases` will build your project, and then run all the jUnit test cases.
* `make check` will check that your code is meeting the required coding
  standards.


Grading
---
There are a maximum of 36 points possible on this assignment.

* **3 Points**:  Correctly formatting your code (ie passing `make check` with
                 no errors).
* **3 Points**:  Correctly documenting your code (i.e. all classes, methods
                 properties having correct docblocks).
* **20 Points**: Correctly creating 10 unit tests cases, each correctly
                 documented, and each testing a different aspect of sentence
                 parsing.
* **10 Points**: Correctly pass 5 TA-provided test cases, of splitting
                 a text into sentences.


Due Date
---
This assignment is due by 11:59AM on Monday, July 17, 2017.
