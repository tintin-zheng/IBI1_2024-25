# Practical 13 Summary

## task 1

The human SOD2 protein has a length of 222 amino acids.
According to the UniProt entry, it is located in the mitochondrion.

## task 2

The percentage identity of the reported alignments ranged from 58.1% to 100.0%,
with the 100% match representing a self-alignment to the query (human SOD2).

## task 3

| Sequence Pair                 | BLOSUM62 Score | Identity(%)|
| ----------------------------- | -------------- | ---------- |
| Human SOD2 vs Mouse SOD2      | 1              | 90.09%     |
| Human SOD2 vs Random Sequence | -292           | 4.05%      |
| Mouse SOD2 vs Random Sequence | -305           | 4.05%      |

* the origin output:
    Comparing human_sequence and mouse_sequence
    Score: 1
    Percentage of identity: 90.09%
    Comparing human_sequence and random_sequence
    Score: -292
    Percentage of identity: 4.05%
    Comparing mouse_sequence and random_sequence
    Score: -305
    Percentage of identity: 4.05%

## task 4

The human and mouse SOD2 proteins are closely related, as demonstrated by their high percentage of identical amino acids **90.09%** and a neutral-to-positive BLOSUM62 score **1**.