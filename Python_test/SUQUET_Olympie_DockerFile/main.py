import SparseArray
import sys
import os

#setting environment variable STRINGS
#os.environ['STRINGS'] = 'ab,ab,abc'

def main():
    queries = sys.argv[1].split(',')
    strings = os.getenv('STRINGS').split(',')
    x = SparseArray.SparseArray(queries,strings)
    print(x.matchingStrings())

main()