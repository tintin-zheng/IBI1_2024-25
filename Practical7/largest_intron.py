"""
pseoducode:
import the necessary libraries
define the function to find the largest intron in a sequence
(why i define the function? because i want to use it in the future)
    search for the first GT and the last AG in the sequence
    if the first GT and the last AG are found in the sequence
    get the position of the first GT and the last AG
    get the sequence of the intron
    get the length of the intron
    print the intron sequence and its length
    else print 'No intron found in the sequence'
input the sequence provided
call the function to find the largest intron in the sequence
"""
# import the necessary libraries
import re

# define the function to find the largest intron in a sequence
def find_the_largest_intron(seq):
    # find the first GT and the last AG in the sequence
    first_gt = re.search('GT', seq)
    last_ag = re.search('AG(?!.*AG)', seq)
    # question: should i use the last AG or the first AG?

    
    # to see if the first GT and the last AG are found in the sequence
    if first_gt and last_ag:
        # get the position of the first GT and the last AG
        first_gt_position = first_gt.start()
        last_ag_position = last_ag.end() 
        # get the sequence of the intron
        intron_seq = seq[first_gt_position:last_ag_position]
        # get the length of the intron
        intron_length = len(intron_seq)
        # print the intron sequence and its length
        print(f'Intron sequence: {intron_seq}')
        print(f'Intron length: {intron_length}')
    else:
        print('No intron found in the sequence')

# the sequence provided
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
# call the function to find the largest intron in the sequence
print(find_the_largest_intron(seq))
