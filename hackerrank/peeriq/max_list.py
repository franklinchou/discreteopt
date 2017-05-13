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
# Using a dictionary is a better solution than a list.
# It allows addition to indices without first having to waste
#   time and resources first creating a list of size `n` initialized
#   with values (which are all going to be zero anyway).
# Inevitably there __may__ be some items in a list data structure
#   that will never be modified at runtime, resulting in wasted
#   memory allocation and possibly compute time if the data set is
#   large.
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
  
