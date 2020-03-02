# sequence

## Description
This is a small coding challenge developed in Python 3 to solve the problem of a sequence calculated adding the last to elements, starting with the values 2 and 2.

The sequence example is: 2, 2, 4, 6, 10, 16, 26, ...

## Execution

There are two python programs

sequence_lineal.py is a lineal approach to solve the problem to calculate the n(th) element of the sequence.

sequence_recursive.py is a recursive approach to solve the problem to calculate the n(th) element of the sequence.

To execute the programs:

```
  joniuz@nas $ python sequence_lineal.py

  joniuz@nas $ python sequence_recursive.py
 ```

Example:

![example](https://user-images.githubusercontent.com/12822475/75650235-70356f80-5ca9-11ea-9606-cd5f4a5c5d81.png)

## Questions

- What is the 15th element of the sequent?

The 15th element is 1220

- What is your solution time and space complexity, regarding for the n(th) element of the sequent?

I created two solutions, the first one is lineal and the complexity is O(3 + 3n) and the execution time for the 15th element is 0.000060796737670898 seconds, the second solution is recursive and its complexity is O(2^n) and the execution time for the 15th element is  0.0003662109375 seconds

Clearly, the linear solution has a better performance than the exponential one.

- What clean code principles you have been used, and why?

Effective naming strategy: variable names are meaningful, making easy to a developer understand the code.
K.I.S.S.: The code is simple, avoiding the use of unnecessary libraries and functions
DRY (Don't Repeat Yourself): Every function as has the same parameter so is easy to interchange the function without modify the user interface.

- Bonus: can you make your code recursive? If yes, what would be your time and space complexity?

The python program sequence_recursive.py is the recursive solution. The execution time for the 15th element is 0.0003662109375 seconds and the complexity is O(2^n)
