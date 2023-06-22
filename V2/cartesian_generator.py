import itertools
import csv
import sys
import string
# Example usage
input_string = list(string.ascii_letters)#for all alphabets
input_string = "abc"#for know strings

#possible outcomes
count = 0
for length in range(1, len(input_string) + 1):
    count += len(input_string) ** length
print("total combinations :" ,count)

def update_status_bar(progress, total, bar_length=70):
    filled_length = int(bar_length * progress / total)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    percent = (progress / total) * 100
    sys.stdout.write(f'\r[{bar}] {percent:.1f}%')
    sys.stdout.flush()

def generate_combinations(string):
    generation_count=1
    writer = csv.writer(csv_writer)
    for length in range(1, len(string) + 1):
        for combination in itertools.product(string, repeat=length):
            generation_count=generation_count+1
            writer.writerow([''.join(combination)])
            yield ''.join(combination)
            update_status_bar(generation_count,count)



combinations = generate_combinations(input_string)
with open('passwords.csv','w') as csv_writer:
    for combination in combinations:
        next(combinations)