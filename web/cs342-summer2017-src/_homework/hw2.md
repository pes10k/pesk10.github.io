---
layout: page
title: Homework 2
topic: Class hierarchies and inheritance
due_date: 2017-06-21
---

Overview
---
This assignment aims to give you a little more practice taxonomizing types,
and implementing those taxonomies using Java's class system.

You have two tasks in this assignment.

**First**, you'll need to  create a class hierarchy in Java that depicts a
logical categorization of the following types.

* Animal
* Beluga
* Chameleon
* Dog
* GermanShepard
* Mammal
* Orca
* Reptile
* ShibaInu
* Snake
* Whale

Each of these types is represented as a class, each with its own file in
the `hw2/src/cs342/animals` directory.  These files and classes currently
represent a type hierarchy with `Animal` at the top, and every other
class being a child class of `Animal`.

    Animal
        |- Beluga
        |- Chameleon
        |- Dog
        |- GermanShepard
        |- Mammal
        |- Orca
        |- Reptile
        |- ShibaInu
        |- Snake
        |- Whale

You should first decide what a better organization for these types, and then
implement that organization by updating the `.java` files in
`hw2/src/cs342/animals`. You should have the classes inherit / extend
each other so that they implement your class hierarchy.

**Second**, once you've taxonomized these types, you'll need to describe
them, by overriding the methods in the `Animal` class.  You will need to
override the following methods in your hierarchy:

* public boolean isWarmBlooded()
* public boolean isLivingUnderWater()
* public boolean isNamedAfterEuropeanCountry()
* public boolean canChangeColor()
* public boolean isBlackAndWhite()

The catch is that you can only implement / override each method *once* in your
solution.  In other words, can add a maximum of five new method definitions
*total* to the code in `hw2/src/cs342/animals`.  The goal is to have
the class system express the correct answers (for the questions represented
by these methods) for each type in the system.

The part that will take some thinking through is "which level of the hierarchy
to do the overriding at".  Keep in mind that if you override a method
on a parent class, you're also overriding it for all the children of that class
(unless you re-override it on a child class, which is not possible in this
assignment).

If you've done this correctly, then each of these sets of answers should
give you back exactly one type, describing a logical animal.

Warm Blooded? | Under Water? | Named after EU Country | Changes Color? | Black and White? | Correct type
--------------|--------------|------------------------|----------------|---------------------------------
true          | false        | true                   | false          | false            | GermanShepard
true          | false        | false                  | false          | false            | ?
true          | true         | false                  | false          | true             | ?
true          | true         | false                  | false          | false            | ?
false         | false        | false                  | true           | false            | ?
false         | false        | false                  | false          | false            | ?

A testing program is included in your repo.  See the below "Resources and
Suggestions" section for more information.


Requirements
---

You are only allowed to edit code in `hw2/src/cs342/animals`, with the
exception of the `hw2/src/cs342/animals/Animal.java` file, which you
**cannot** change.  You also may not make any changes to the
`hw2/src/Main.java` file, the included `jar` file, or any other file in
the repo.

You can only override / implement a maximum of five methods in your code.
In other words, if you've written `public boolean` more than five times, your
solution is incorrect :)


Resources and Suggestions
---
There is a test script in your repo, called `run`.  It takes five arguments,
each corresponding to one of the five methods you're allowed to override.
You run it as follows:

`./run --warmblood {true,false} --underwater {true,false} --euroname {true,false} --changecolor {true,false} --blackandwhite {true,false}`

proving the values for each flag (warmblood, underwater, etc.) as desired.
The program will then check your type hierarchy and return a list of
all the types that match the parameters you provided.  A correct solution will
return exactly one type for each of the combination of values described
in the table in the "Overview" section.

For example, to replicate the first row of the table, you'd use
`./run --warmblood true --underwater false --euroname true --changecolor false --blackandwhite false`,
and your program should output "german shepard".

You might also find the following links useful, especially if you're not much
into animals:
* [Orca](https://en.wikipedia.org/wiki/Killer_whale)
* [Beluga](https://en.wikipedia.org/wiki/Beluga_whale)
* [Shiba Inu](https://en.wikipedia.org/wiki/Shiba_Inu)
* [Alaskan Husky](https://en.wikipedia.org/wiki/Alaskan_husky)


Grading
---
This assignment will be worth 10 points.  Four points for implementing
getting the taxonomy / class hierarchy correct, and one point each
for your program generating the correct results for each of the
six sets of terms described in the table above.

No late or partial credit will be given.  Working with other students,
or using resources other than the text book or the above Wikipedia links
is forbidden and will be considered academic dishonesty.


Due Date
---
This assignment is due by 11:59AM on Wednesday, June 21, 2017.
