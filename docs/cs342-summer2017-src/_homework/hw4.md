---
layout: page
title: Homework 4
topic: Working with lambda and data formats
due_date: 2017-07-05
---

Overview
---
In this project you will build a tool for processing, filtering, sorting and
formatting external data. The data you'll be using for this project is
slightly reformatted data taken from the Chicago government's open data web
site, describing moving violations recorded at "red light" cameras around
the city.

This homework is also structured to nudge you towards writing good library
code.  This means proper formatting and documentation, and raising errors
to calling code (instead of printing out error messages, or exiting yourself).

Your application will need to do the following (some of which are stubbed out
in the provided code):

1.  Read the source data from a provided JSON file, and process it into
    `uic.redlightcams.DataPoint` instances.
2.  (Possibly) filter the data set by user provided parameters.  These filters
    include options like "only include records from camera ###" (i.e.
    `./camerafilter --fcol CAMERA_ID -fval 2123`), "only include records
    that were recorded at a given intersection" (i.e. `./camerafilter --fcol
    INTERSECTION --fval "CLARK AND FULLERTON"`), or "only include records that
    occured within 3 miles of UIC (i.e. `./camerafilter --dist 3`).
3.  (Possibly) sort the data set by user provided parameters.  For example,
    "show me records, most recent first" (i.e. `./camerafilter --scol DATE
    --sdir DESC`) or "show me the records, sorted by camera ID" (i.e.
    `./camerafilter --scol CAMERA_ID --sdir ASC`).
4.  (Possibly) aggregate the dataset across dates (see below for more details).
5.  Print the resulting data set out, either as a JSON encoded text string,
    or a CSV file, depending on the user provided parameters (i.e.
    `./camerafilter --output JSON` or `./camerafilter --output CSV`).


### Input Data Format
The data you'll be working with, located in your repo at
`hw4/data/red-light-camera-violations.json`, is a JSON encoded string.  This
data contains a large number of arrays of data, each containing the following
pieces of data (in this order):

1.  Intersection of recording
2.  ID of the camera doing the recording
3.  The address of the camera
4.  The date of the recording
5.  Number of redlight violations that the camera recorded, on this date
6.  The latitude where the camera is located
7.  The longitude where the camera is located

Each row / record in this dataset represents the number of red light violations
recorded on a specific camera, on a given date.


### Aggregation Requirements
Your code must support an "aggregation" mode, where data records are combined
across all dates, to provide a summary of what happened for each camera
across the entire data set. For example, consider the below three data records
(some columns are excluded for concision, this example only includes
the "address", "date" and "num violations" columns).

    "800 W 79TH STREET", "2017-03-17T00:00:00", "3"
    "800 W 79TH STREET", "2017-03-18T00:00:00", "5"
    "7432 W TOUHY AVENUE", "2017-03-17T00:00:00", "3"

When "aggregating" these results across time, the correct output should be:

    "800 W 79TH STREET", "8"
    "7432 W TOUHY AVENUE", "3"


### Outputting Data
Your code will need to output in both JSON and CSV formats.  Refer to the
"docblock" for the `Filter#generateReport` method for specific instructions
on in what order to include data in the rows / JSON arrays in your output
reports.


### Data Types
You'll need to make sure you're parsing the JSON file correctly into Java
data types, so that you can sort, filter, etc on them correctly.  For example,
the JSON data includes the "camera id" column as a string.  You should make
sure you represent this in your code as an `Integer` and not a `String`, since
sorting strings can result in unexpected results (e.x. if you're not careful,
"2222" can end up as sorted before "3", when doing string comparisons).


Requirements
---
Your code should meet all of the following requirements:

* You cannot write any loops in this code.  No exceptions.  You will need
  to use lambda, collection methods, and / or recursion.  Any `for`, `do`
  or `while` statements in your code will be a 50% reduction in the homework's
  grade.
* You should only make changes to the `DataPoint.java` and `Filter.java`
  files.  You can create other classes / files if you'd like, but you should
  not make any changes to any of the other provided files.
* Your code should correctly handle all errors.  Your code *must not* ever
  exit, or print anything to STDOUT or STDERR. Doing so is inappropriate
  for library code.  All output or exiting must be handled by the code
  calling into your libraries (i.e. `Main.java`).  TL;DR, you must handle
  error cases by throwing exceptions, not printing debug messages or
  exiting.

  Handling errors incorrectly in your code will be treated as getting a
  test case wrong, regardless of whatever else your code does.
* Your code must be nicely / readably formatted, following Google's Java
  style (not that Google's format is *best*, but that its well documented
  and at least *good*, certainly way better than no standard).
* Your code must be correctly documented.  All methods, properties, and
  classes should be documented following "javadoc" conventions.


Resources and Suggestions
---
* [JSON Specification](http://json.org/)
* [JSON Library Documentation](http://www.json.org.cn/resource/javadoc/org/json/package-summary.html)
* [CSV Information](https://en.wikipedia.org/wiki/Comma-separated_values)
* [Javadoc Information](http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html)
* [Chicago Red Light Camera Data](https://data.cityofchicago.org/Transportation/Red-Light-Camera-Violations/spqx-js37)
* [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
* [Helpful post on finding distance between coordinates](https://gis.stackexchange.com/questions/142326/calculating-longitude-length-in-miles)

Your repo also includes a helper `./camerafilter` too, which you can use
to more conveniently interact with your program.  Using `./camerafilter --help`
will provide more information about how to use the program and pass filter /
sorting / output options.



Grading
---
There are a maximum of 25 points possible on this assignment.

* **3 Points**:  Correctly formatting your code (ie passing `make check` with
                 no errors).
* **2 Points**:  Correctly documenting your code (i.e. all classes, methods
                 properties having correct docblocks).
* **20 Points**: Correctly handling 5 test cases (4 points for each test case,
                 including possibly invalid input).


Due Date
---
This assignment is due by 11:59AM on Wednesday, July 5, 2017.
