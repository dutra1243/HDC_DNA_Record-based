"""
secuencias de prueba

original
ACAGTACAGT

variante 1 (un solo cambio)
ACAGTCCAGT

variante 2 (dos cambios respecto al original)
AAAGTCCAGT
"""

"""
secuencias de E.Coli

Original
ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTCGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT

3 cambios en bases
ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTTGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT


3 inserciones y 2 deleciones
ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTG---GTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTTCGGGAAACCTGTCGTGGGCCAGCTGCATAA-CGCGGCGGTTTGTTCCCACCGAT
"""

import torchhd
import torch
from variables import dimensions

# load the hypervectors
try:
    print("Loading hypervectors")
    nucleotide_A = torch.load("nucleotide_A.pt")
    nucleotide_C = torch.load("nucleotide_C.pt")
    nucleotide_G = torch.load("nucleotide_G.pt")
    nucleotide_T = torch.load("nucleotide_T.pt")
    specialChar = torch.load("specialChar.pt")
    print("Hypervectors loaded")
except Exception as e:
    print("Error loading hypervectors")
    print("Generating and saving hypervectors")
    nucleotide_A = torchhd.random_hv(1, dimensions)
    nucleotide_C = torchhd.random_hv(1, dimensions)
    nucleotide_G = torchhd.random_hv(1, dimensions)
    nucleotide_T = torchhd.random_hv(1, dimensions)
    specialChar = torchhd.random_hv(1, dimensions)
    torch.save(nucleotide_A, "nucleotide_A.pt")
    torch.save(nucleotide_C, "nucleotide_C.pt")
    torch.save(nucleotide_G, "nucleotide_G.pt")
    torch.save(nucleotide_T, "nucleotide_T.pt")
    torch.save(specialChar, "specialChar.pt")
    print("Hypervectors generated and saved")


testList = ["ACAGTACAGT", "ACAGTCCAGT", "AAAGTCCAGT"]

largestString = 0

for test in testList:
    if len(test) > largestString:
        largestString = len(test)

print("Largest string: ", largestString)




