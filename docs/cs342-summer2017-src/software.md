---
layout: page
title: Software
permalink: /software/
---

We'll be using a variety of tools in this course to learn and practice
software design skills.  This is an overview of the main ones we'll
be using, both required and suggested.

Required Tools
---

### Java
All of the programming assignments, lectures and tools we'll be discussing
will be in Java.  While the principals and patterns will be (mostly) general
and applicable to any language, we'll be doing things in Java.  You
will need to have a Java 8 runtime installed and working on your machine
to work on the assignments.

You can test the version of Java you have installed by running `java -version`
from the command line.  Any output that doesn't look something like
`java version "1.8.XXX"` means you probably have the wrong version installed.

### Unix-y Operating System
Examples will be given in a unix-y environment (linux and OSX), and assignments
will be tested on linux. With a properly configured environment Windows will
work fine too, but you will be responsible for making sure your project
builds and runs correctly on linux.  If your primary machine is not a linux
machine, please see below for suggestions.

### GnuMake
Most of the programming assignments will be run and tested using a simple
provided make script.  This is for several reasons, including: to allow students
to use any IDEs / development platform they like when writing code, to make it
easier to test students' submissions, and to better demonstrate what complex
IDEs are doing under the hood.

Students will need to make sure that their homework and project submissions work
correctly using the provided make file.

### Git
All homework will be provided using git, and all completed homework assignments
must be submitted through git.  A basic run through of git functionality will
be provided on the first day of class, but students needing a further tutorial /
refresher / catch up may want to consult the
[official git documentation](https://git-scm.com/documentation).

### SSH
Access to your git respository will be controlled by using SSH keys.  You'll
need to generate, secure, and maintain a SSH key private key to fetch and
submit homework assignments.  You'll also need to send me the corresponding
public SSH key.

If you are not familiar with generating and using SSH keys, you might find
resources like the first three step's of
[GitHub's guide to SSH keys](https://help.github.com/articles/connecting-to-github-with-ssh/) useful.


Suggested Tools
---

### CheckStyle
[CheckStyle](http://checkstyle.sourceforge.net/) is a opensource Java
development tool that checks the formatting of your code to, so that it follows
patterns and practices.  This helps ensure that your code is equally as readable
to humans as it is to compilers.  It has configurable rule sets.  A common
ruleset is the [Goole Java Style](https://google.github.io/styleguide/javaguide.html)
guide, which you can instruct checkstyle to use by downloading the XML
[configuration file for the rule set](https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml)
and running `checkstyle -c google_checks.xml <path to java files>`.

### VirtualBox
All homework assignments will be graded on a linux machine, using Java 8
on the command line (unless otherwise stated). If you are on a platform where
installing Java 8 is difficult, or where running programs from the command
line can be tricky, you might consider using
[VirtualBox](https://www.virtualbox.org/) to run linux in a virtual machine.