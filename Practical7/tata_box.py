# import the necessary librarie
import re
# open the file in read mode
with open("D:\学习\大一下学习\IBI\IBI1_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file:
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
   
    # recognize the gene containing TATA box
    gene_sequences_with_tatabox = {}
    # got gene_name and sequence from the gene sequences dictionary
    for gene_name, sequence in gene_sequences.items():
        # search for the TATA box in the sequence
        tata_box = re.search("TATA[AT]A[AT]", sequence)
        if tata_box:
            # store the gene name and its sequence in the dictionary
            gene_sequences_with_tatabox[gene_name] = sequence


# output the result in a new file
with open("D:\学习\大一下学习\IBI\IBI1_2024-25\IBI1_2024-25\Practical7\\tata_genes.fa", "w") as output_file:
    for gene_name, sequence in gene_sequences_with_tatabox.items():
        output_file.write(f">{gene_name}\n")
        output_file.write(f"{sequence}\n")
