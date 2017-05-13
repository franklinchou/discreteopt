#####################################################
# Based on the HackerRank challenge.
# Determine the divisibility of integer permutations.
# Currently constrained to 3 digit test cases between
#   100 and 999.
#####################################################

__author__ = 'Franklin Chou'

from random import randint
from itertools import permutations

# GENERATE TEST:
test_cases = 100
test_matrix = []
for i in range(test_cases):
  test_matrix.append(randint(100, 999))

print(test_matrix)

# GET PERMUTATIONS:

results = test_cases * [None]

# Appending results to list caused some conditional logic error
#   during the evaluation. Hard to debug: HackerRank environment.
for i, k in enumerate(test_matrix):
  perms = [''.join(p) for p in permutations(str(k))]
  
  results[i] = 'NO'
  for j in perms:
    if int(j)%8 == 0:
      results[i] = 'YES'
      break

# IS EACH ITEM ACCOUNTED FOR?
assert(len(results) == test_cases)

print(results)
