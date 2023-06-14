import os
import math
import string

#core count
num_cores = os.cpu_count()
print("Number of CPU cores:", num_cores)

#number of password combinations
Upper_case_permutations = math.factorial(len(list(string.ascii_uppercase)))
Lower_case_permutations = math.factorial(len(list(string.ascii_lowercase)))
Number_permutations = math.factorial(len(range(0,10)))
print("Uppercase permutations :",Upper_case_permutations)
print("Lowercase permutations :",Lower_case_permutations)
print("Number permutations :",Number_permutations)
