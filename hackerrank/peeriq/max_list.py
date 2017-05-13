#####################################################
# Based on the HackerRank challenge.
# Determine the max number in a list based on the
#   following operation:
# start end add
# Where:
# * start = initial list index 
# * end = terminal list index (INCLUSIVE)
# * add = number to add from start THROUGH end (INCLUSIVE)
#####################################################

__author__ = 'Franklin Chou'

import operator

# Number of total operations expected
__total_operations = 2

# Create dictionary
result = {}

for i in range(__total_operations):
  f = input().split(" ")
  assert(len(f) == 3)

  # SOLUTION

  start = f[0]
  end = f[1]
  add = f[2]

  # Mistake I made during the evaluation:
  #   Thinking the range was inclusive.
  #   Simple debugger would have solved that; thanks HackerRank IDE :(
  #   Replaced with a while statement; circumvent Python range() function;
  #   also gets rid of the zero-indexing mismatch between the problem universe
  #   and Python conventions.
  i = int(end)
  while (i >= int(start)):
    
    if i not in result:
      result[i] = int(add)
    else:
      result[i] = result[i] + int(add)
    
    i = i - 1

# print(result)

print(max(result.items(), key=operator.itemgetter(1))[1])
  
