"""
pseudocode:
    import the necessary librarie
    receive the input splice donor/acceptor site from the user
    open the file in read mode
        2. store the gene name and sequence in a dictionary
        3. search for the splice site in the sequence, if found, store the gene name and its sequence in a new dictionary
        4. search for the TATA box in the sequence, if found, store the gene name and its sequence in a new dictionary
    
    output the result in a new file

    for more details, please refer to the comments below

"""
# import the necessary librarie
import re
import os
# change the working directory to the location of the script
os.chdir("Practical7")
# receive the input splice donor/acceptor site from the user
while True:
    splice_site = input("Please enter the splice donor/acceptor site: ")
    # check if the splice site is the correct one
    if splice_site == "GTAG" or splice_site == "GCAG" or splice_site == "ATAC" :
        break
    else:
        print("please enter the correct splice donor/acceptor site (GTAG or GCAG or ATAC)")

# open the file in read mode
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file:

    # initialize the variables
    gene_name = None
    sequence = ""
    gene_sequences = {}
    # read the file line by line
    for line in input_file:
        # remove the leading and trailing whitespace from the line
        line = line.strip()
        # check if the line starts with '>'
        # if it does, it means it's a gene name line
        if line.startswith(">"):
            # the line start with '>' means it's a new gene name
            # so we need to store the previous gene and its sequence
            if gene_name and sequence:
                # store the previous gene and its sequence
                gene_sequences[gene_name] = sequence    
            # reset the sequence variable for the new gene        
            sequence = ""
            gene_name = re.search("gene:(\w+)", line).group(1)
        # if the line does not start with '>', it means it's a sequence line
        # so we need to append it to the sequence variable
        else:
            sequence += line
    # def a function to find the gene sequences with splice site
    def find_the_line_with_splice_site(gene_sequences, splice_site):
        global head_half, tail_half
        # initialize a new dictionary
        gene_sequences_with_splice_site = {}
        # split the splice site into two halves
        head_half = splice_site[:2]
        tail_half = splice_site[2:]
        # got gene_name and sequence from the gene sequences dictionary
        for gene_name, sequence in gene_sequences.items():
            # search for the splice site in the sequence
            splice_site_match = re.search(f"{head_half}.*?{tail_half}", sequence)
            if splice_site_match:
                # store the gene name and its sequence in the dictionary
                gene_sequences_with_splice_site[gene_name] = sequence
        return gene_sequences_with_splice_site
    
    gene_sequences_with_splice_site = find_the_line_with_splice_site(gene_sequences, splice_site)
    
    # recognize the gene containing TATA box
    gene_sequences_with_tatabox = {}
    # got gene_name and sequence from the gene sequences dictionary
    for gene_name, sequence in gene_sequences_with_splice_site.items():
        # search for the TATA box in the sequence
        tata_box = re.search("TATA[AT]A[AT]", sequence)
        the_number_of_tata_box = len(re.findall("TATA[AT]A[AT]", sequence))
        # add the number of TATA box to the gene name
        gene_name = gene_name + "   " + f"The number of TATA box is {the_number_of_tata_box}."
        if tata_box:
            # store the gene name and its sequence in the dictionary
            gene_sequences_with_tatabox[gene_name] = sequence


# output the result in a new file
with open(f"D:\学习\大一下学习\IBI\IBI1_2024-25\IBI1_2024-25\Practical7\\{splice_site}_tata_genes.fa", "w") as output_file:
    for gene_name, sequence in gene_sequences_with_tatabox.items():
        output_file.write(f">{gene_name}\n")
        output_file.write(f"{sequence}\n")
