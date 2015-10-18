Color Char
==========

ColorChar colours individual characters in a command line output.

What's the use case for this?

Here's one.

Imagine you have the following 18x18 terrain map:

       1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
     1 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
     2 1  3  3  3  3  3  1  3  3  3  3  3  1  3  3  3  3  3
     3 1  3  1  1  3  1  1  3  1  1  3  1  1  3  1  1  3  1
     4 1  3  1  1  2  1  1  3  1  1  2  1  1  3  1  1  2  1
     5 1  3  3  3  3  1  1  3  3  3  3  1  1  3  3  3  3  1
     6 1  3  1  1  1  1  1  3  1  1  1  1  1  3  1  1  1  1
     7 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
     8 1  3  3  3  3  3  1  3  3  3  3  3  1  3  3  3  3  3
     9 1  3  1  1  3  1  1  3  1  1  3  1  1  3  1  1  3  1
    10 1  3  1  1  2  1  1  3  1  1  2  1  1  3  1  1  2  1
    11 1  3  3  3  3  1  1  3  3  3  3  1  1  3  3  3  3  1
    12 1  3  1  1  1  1  1  3  1  1  1  1  1  3  1  1  1  1
    13 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
    14 1  3  3  3  3  3  1  3  3  3  3  3  1  3  3  3  3  3
    15 1  3  1  1  3  1  1  3  1  1  3  1  1  3  1  1  3  1
    16 1  3  1  1  2  1  1  3  1  1  2  1  1  3  1  1  2  1
    17 1  3  3  3  3  1  1  3  3  3  3  1  1  3  3  3  3  1
    18 1  3  1  1  1  1  1  3  1  1  1  1  1  3  1  1  1  1

It's difficult to get a good sense of the terrain just by looking at the
numbers. By running ColorChar on this, we can colour all of the `3` values
orange, making it easy to see what's going on.

Credits
=======

Author: Richard Barnes (rbarnes@umn.edu)