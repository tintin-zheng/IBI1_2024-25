# import the necessary libraries
import os
import pandas as pd

# change the working directory to the location of the script
os.chdir("Practical13")

# open the file containing the BLOSUM62 matrix in read mode
blosum62_df = pd.read_csv("BLOSUM62.txt", delim_whitespace = True, comment = "#", index_col=0)

# define a function to open the .fasta file and read the sequences
def read_fasta(file_path):
    """read the fasta file and return a dictionary of sequences"""
    # open the file in read mode
    with open(file_path, "r") as file:
        # read the lines of the file
        lines = file.readlines()
    # initialize an empty string to store the sequences
    sequences = ''
    # integrate the lines into a single string
    for line in lines:
        if not line.startswith(">"):
            sequences += line.strip() # remove the newline character
    return sequences

# read the sequences from the fasta files
human_sequence = read_fasta("P04179.fasta")
mouse_sequence = read_fasta("P09671.fasta")
random_sequence = read_fasta("random_sequence.fasta")

# define a function to compare the sequences
def compare_sequences(seq1, name_1, seq2, name_2):
    """compare two sequences; return the score and the percentage of identity"""
    # initialize the score
    score = 0
    count = 0
    # iterate through the sequences
    for i in range(len(seq1)):
        # get the amino acids at the current position
        aa1 = seq1[i]
        aa2 = seq2[i]
        # check if the amino acids are the same
        if aa1 != aa2:
            # increment the count
            count += 1
            # get the score from the BLOSUM62 matrix
            score += blosum62_df.loc[aa1, aa2]
    # calculate the percentage of identity
    identity = (len(seq1) - count) / len(seq1) * 100
    # print the score and the percentage of identity
    print(f"Comparing {name_1} and {name_2}")
    print(f"Score: {score}")
    print(f"Percentage of identity: {identity:.2f}%")

# compare the sequences
compare_sequences(human_sequence, "human_sequence", mouse_sequence, "mouse_sequence")
compare_sequences(human_sequence, "human_sequence", random_sequence, "random_sequence")
compare_sequences(mouse_sequence, "mouse_sequence", random_sequence, "random_sequence")