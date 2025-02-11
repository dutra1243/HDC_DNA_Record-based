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
import os
from variables import dimensions

class someMethods:
    def __init__(self):
        pass

    def deleteHypervector(fileName):
        try:
            os.remove(fileName)
            print(f"{fileName} deleted")
        except Exception as e:
            print("Error deleting file")
            print(e)

    def loadHypervector(fileName):
        return torch.load(fileName)
    
    def saveHypervector(hypervector, fileName):
        torch.save(hypervector, fileName)

    def generateHypervector(dimensions, fileName):
        hv = torchhd.random(1, dimensions, "BSC")
        torch.save(hv, fileName)
        return hv
    
    def generateHypervectorIDs(amount , dimensions, fileName):
        hvs = torchhd.random(amount, dimensions, "BSC")
        torch.save(hvs, fileName)
        return hvs
    
    def bundling(hv1, hv2):
        return torch.bitwise_or(hv1, hv2)
    
    def binding(hv1, hv2):
        return torch.bitwise_xor(hv1, hv2)
    

# load the hypervectors
try:
    print("Loading hypervectors")
    nucleotide_A = someMethods.loadHypervector("nucleotide_A.pt")
    nucleotide_C = someMethods.loadHypervector("nucleotide_C.pt")
    nucleotide_G = someMethods.loadHypervector("nucleotide_G.pt")
    nucleotide_T = someMethods.loadHypervector("nucleotide_T.pt")
    specialChar = someMethods.loadHypervector("specialChar.pt")
    print("Hypervectors loaded")
except Exception as e:
    print("Error loading hypervectors")
    print(e)
    print("Generating and saving hypervectors")
    nucleotide_A = someMethods.generateHypervector(dimensions, "nucleotide_A.pt")
    nucleotide_C = someMethods.generateHypervector(dimensions, "nucleotide_C.pt")
    nucleotide_G = someMethods.generateHypervector(dimensions, "nucleotide_G.pt")
    nucleotide_T = someMethods.generateHypervector(dimensions, "nucleotide_T.pt")
    specialChar = someMethods.generateHypervector(dimensions, "specialChar.pt")
    print("Hypervectors generated and saved")


testList = ["ACAGTACAGT", "ACAGTCCAGT", "AAAGTCCAGT"]
# testList = ["ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTCGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT",
#             "ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTTGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT",
#             "ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTG---GTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTTCGGGAAACCTGTCGTGGGCCAGCTGCATAA-CGCGGCGGTTTGTTCCCACCGAT"]

largestString = 0

for test in testList:
    if len(test) > largestString:
        largestString = len(test)

print("Largest string: ", largestString)

IDs = someMethods.generateHypervectorIDs(largestString, dimensions, "IDs.pt")

print(nucleotide_A)
print(nucleotide_C)
print(nucleotide_G)
print(nucleotide_T)


print("IDs: ", IDs)
print("IDs[0] : ", IDs[0])

# list of hypervectors for each DNA sequence
testResults = []

# generating the hypervectors for each DNA sequence
for DNA_SEQUENCE in testList:
    print("DNA_SEQUENCE: ", DNA_SEQUENCE)

    if DNA_SEQUENCE[0] == "A":
        firstLetter = someMethods.binding(nucleotide_A, IDs[0])
    elif DNA_SEQUENCE[0] == "C":
        firstLetter = someMethods.binding(nucleotide_C, IDs[0])
    elif DNA_SEQUENCE[0] == "G":
        firstLetter = someMethods.binding(nucleotide_G, IDs[0])
    elif DNA_SEQUENCE[0] == "T":
        firstLetter = someMethods.binding(nucleotide_T, IDs[0])
    else:
        firstLetter = someMethods.binding(specialChar, IDs[0])

    if DNA_SEQUENCE[1] == "A":
        nextLetter = someMethods.binding(nucleotide_A, IDs[1])
    elif DNA_SEQUENCE[1] == "C":
        nextLetter = someMethods.binding(nucleotide_C, IDs[1])
    elif DNA_SEQUENCE[1] == "G":
        nextLetter = someMethods.binding(nucleotide_G, IDs[1])
    elif DNA_SEQUENCE[1] == "T":
        nextLetter = someMethods.binding(nucleotide_T, IDs[1])
    else:
        nextLetter = someMethods.binding(specialChar, IDs[1])
    sequenceHyperVector = someMethods.bundling(firstLetter, nextLetter)

    for i in range(2, len(DNA_SEQUENCE)):
        if DNA_SEQUENCE[i] == "A":
            nextLetter = someMethods.binding(nucleotide_A, IDs[i])
        elif DNA_SEQUENCE[i] == "C":
            nextLetter = someMethods.binding(nucleotide_C, IDs[i])
        elif DNA_SEQUENCE[i] == "G":
            nextLetter = someMethods.binding(nucleotide_G, IDs[i])
        elif DNA_SEQUENCE[i] == "T":
            nextLetter = someMethods.binding(nucleotide_T, IDs[i])
        else:
            nextLetter = someMethods.binding(specialChar, IDs[i])
        sequenceHyperVector = someMethods.bundling(sequenceHyperVector, nextLetter)
    
    testResults.append(sequenceHyperVector)

print("Test results: ", testResults)

string = 10*" " + " ACAGTACAGT ACAGTCCAGT AAAGTCCAGT\n"

for i in range(len(testResults)):
    string += testList[i] + " "
    for j in range(len(testResults)):
        string += f"{(torchhd.hamming_similarity(testResults[i], testResults[j]))}" + 10*" "
    string += "\n"
print(string)

someMethods.deleteHypervector("IDs.pt")
