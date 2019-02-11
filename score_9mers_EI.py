# score_9mers_EI.py
# Author: Dan Hu
# Last updated: May 8, 2018
# Purpose: Program to score a sequence using the Position Weight Matrix.
# Program uses the Python function open() and the Python methods readlines(), write(),
#    close() and split(), and the package math to compute logs in base 2
#    The first part of the program is to extract 9mers from the initial training data and
#    write these sequences into the file: EI_nine.txt.
#    The second part of the program is to generate the position weight matrix and write the 
#    results in the file: EI_nine_pwm.txt.
#    The third of the program scores the individual 9-mers and write the result in the
#    file: EI_nine_output.txt 

import math

# Part 1
# To create a new txt file for writing "EI_nine.txt"
file = open('EI_nine.txt', 'w')   
original_file = open('EI_true.seq', 'r') # Open the EI_true.seq for reading
temp = original_file.readlines()[4:] # Read all the lines except the first 4 lines
    
for line in temp:  # Iterate over all the lines
    head, sequence = line.split(': ') # Split each line into 2 parts: 
                                      # 'head' refers to the part before ': '
                                      # 'sequence' refers to the part after ': ', which is the part I need
    file.write(sequence[67:76] + '\n')  # Extract 9 characters from each line from position 67 to 75
                                            # and write them into the new txt file line by line
# Close the file
file.close() 
original_file.close()

# Part 2
# To create a new txt file for writing "EI_nine_pwm.txt"
# Initialize the PWM with four rows and nine columns [i.e., 4 lists of zeros]
a = [0]*9
c = [0]*9
g = [0]*9
t = [0]*9

input_file = open("EI_nine.txt","r")   
count_lines = 0 # Initialize the total number of sequences to 0
# Read line by line, stripping the end of line character and
# updating the PWM with the frequencies of each base at the 9 positions
for line in input_file.readlines():
    line = line.strip('\n')
    count_lines += 1 # Keep counting the sequences
    for i in range(9):
        if line[i] == 'A':
            a[i] = a[i]+1
        elif line[i] == 'C':
            c[i] = c[i]+1
        elif line[i] == 'G':
            g[i] = g[i]+1
        elif line[i] == 'T':
            t[i] = t[i]+1
# Close the file
input_file.close()

# Compute the probability of occurrence of each character after adding the 
#    LaPlace pseudocount i.e., +0.1 added to each base

# Compute the 36 log-odd scores (log of observed/expected) where expected is 0.25
#  and the log is taken in base 2
for i in range(9):
    a[i] = round(math.log((a[i] + 0.1)/(count_lines + 0.4)/0.25,2),3)
    c[i] = round(math.log((c[i] + 0.1)/(count_lines + 0.4)/0.25,2),3)
    g[i] = round(math.log((g[i] + 0.1)/(count_lines + 0.4)/0.25,2),3)
    t[i] = round(math.log((t[i] + 0.1)/(count_lines + 0.4)/0.25,2),3)

# Write the scores in "EI_nine_pwm.txt"    
output_file = open("EI_nine_pwm.txt","w")
for i in range(9):
    output_file.write(str(a[i]) + '\t')
output_file.write("\n")
for i in range(9):
    output_file.write(str(c[i]) + '\t')
output_file.write("\n")
for i in range(9):
    output_file.write(str(g[i]) + '\t')
output_file.write("\n")
for i in range(9):
    output_file.write(str(t[i]) + '\t')
output_file.write("\n")

# Close the file
output_file.close()

# Part 3
# To create a new txt file for writing "EI_nine_output.txt"    
input_file = open("EI_nine.txt","r")
score_file = open('EI_nine_output.txt', 'w')
for line in input_file.readlines():
    score = 0
    for i in range(9):
        if line[i] == 'A':
            score += a[i]
        elif line[i] == 'C':
            score += c[i]
        elif line[i] == 'G':
            score += g[i]
        elif line[i] == 'T':
            score += t[i]
    # Write each input sequence followed by its score into the file
    # "EI_nine_output.txt"
    score_file.write(line[:-1] + '\t' + str(round(score, 3)) + '\n')

# Close the file
input_file.close()
score_file.close()
    

