#####################################################
# Based on the HackerRank challenge.
# Find the maximum difference in a list.
#####################################################

__author__ = 'Franklin Chou'

import operator
from random import randint

__test_case_size = 5
__test_matrix = []
# GENERATE TEST CASE
for i in range(__test_case_size):
  __test_matrix.append(randint(0, 999))
  
# print(__test_matrix)
  

# If we assume the difference is always the non-absolute difference,
#   i.e., difference >= 0, then the maximum difference will be 0.

# max diff in a list

#SOLUTION
dummy_solution_list = list(__test_matrix)
i, k = max(enumerate(dummy_solution_list), key=operator.itemgetter(1))
m1 = dummy_solution_list.pop(i)
i, k = max(enumerate(dummy_solution_list), key=operator.itemgetter(1))
m2 = dummy_solution_list.pop(i)

max_diff = m1 - m2

print(max_diff)

