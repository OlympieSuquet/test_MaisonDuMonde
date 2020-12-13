# Project description

This project aims to count how many times each element of the list QUERIES can be find in the list STRINGS.

## Project files

This project contains two python files :

- the file SparseArray.py, containing the class SparseArray.
- the file main.py, containing the main function.

## The class SparseArray

This class is constructed from two arrays : queries and strings.
It contains the function matchingStrings.

## Calling the main function

To call the main function, the environment variable STRINGS must be defined.
The user must give the list QUERIES in argument, for exemple like this : python -m main ab,abc,bc

## Using Docker

To build the container, you may use this command : docker build . -t test_mdm
To run the project, you may use this command : docker run -t test_mdm ab,abc,bc

The passed argument for the command docker run corresponds to the variable QUERIES.
The vatiable STRINGS is defined in the dockerfile.
