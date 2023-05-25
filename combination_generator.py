import string
from itertools import permutations
import itertools
#list(permutations(alphabet_upper)) and itertools.permutations() is that the former will create a list of all possible permutations of the alphabet, while the latter will generate a generator object that can be used to iterate over the permutations without having to store them all in memory.
alphabet_upper = list(string.ascii_uppercase)

for permutation in itertools.permutations(alphabet_upper,2):
    print(''.join(permutation))