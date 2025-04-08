
"""
pseudocode:
    def a function to receive two parameters sequence, enzyme_seq
    check if sequence and enzyme_seq are both correct
    find all the position
"""
def restriction_enzyme_cut_sites(sequence, enzyme_seq):
    """
    Input: sequence (str): DNA sequence to be analyzed 
           enzyme (str): restriction enzyme sequence to be searched for
    Returns: the position of the first cut site of the enzyme in the sequence
    """
    # Check if the sequence is correct (only contains A, T, C, G)
    for i in sequence:
        if i == "A" or i == "T" or i == "C" or i == "G":
            # Check if enzyme_seq is correct
            for x in enzyme_seq:
                if x == "A" or x == "T" or x == "C" or x == "G":
                    site = []
                    # find the position of the enzyme_seq
                    for j in range(len(sequence) - len(enzyme_seq) + 1):
                        if sequence[j:j + len(enzyme_seq)] == enzyme_seq:

                            site = site.append(j)
                        # print the enzyme position
                        if site != []:
                            return f"The enzyme sequence {enzyme_seq} cuts the sequence at position {site}"
                        else:
                            return "The enzyme does not cut the sequence"

                else:
                    return "Please enter the correct enzyme sequence (only A, T, C, G)"
        else:
            return "Please enter the correct sequence (only A, T, C, G)"

