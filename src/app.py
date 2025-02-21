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
        hv = torchhd.random(1, dimensions)
        torch.save(hv, fileName)
        return hv
    
    def generateHypervectorIDs(amount , dimensions, fileName):
        hvs = torchhd.random(amount, dimensions)
        torch.save(hvs, fileName)
        return hvs
    
    # def bundling(hv1, hv2):
    #     return torch.bitwise_or(hv1, hv2)
    
    # def binding(hv1, hv2):
    #     return torch.bitwise_xor(hv1, hv2)
    

# load the hypervectors
try:
    print("\nLoading hypervectors")
    nucleotide_A = someMethods.loadHypervector("nucleotide_A.pt")
    nucleotide_C = someMethods.loadHypervector("nucleotide_C.pt")
    nucleotide_G = someMethods.loadHypervector("nucleotide_G.pt")
    nucleotide_T = someMethods.loadHypervector("nucleotide_T.pt")
    specialChar = someMethods.loadHypervector("specialChar.pt")
    print("Hypervectors loaded\n")
except Exception as e:
    print("Error loading hypervectors")
    print(e)
    print("Generating and saving hypervectors")
    nucleotide_A = someMethods.generateHypervector(dimensions, "nucleotide_A.pt")
    nucleotide_C = someMethods.generateHypervector(dimensions, "nucleotide_C.pt")
    nucleotide_G = someMethods.generateHypervector(dimensions, "nucleotide_G.pt")
    nucleotide_T = someMethods.generateHypervector(dimensions, "nucleotide_T.pt")
    specialChar = someMethods.generateHypervector(dimensions, "specialChar.pt")
    print("Hypervectors generated and saved\n")


testList = ["ACAGTACAGT", "ACAGTCCAGT", "AAAGTCCAGT"]
# testList = ["ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTCGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT",
#             "ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTTGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT",
#             "ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTG---GTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTTCGGGAAACCTGTCGTGGGCCAGCTGCATAA-CGCGGCGGTTTGTTCCCACCGAT"]


print(len("ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCACCAATAACTGCCTTGCGGGCGTGGCAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATAAACGCGCTGATTTATCGGCTGGCTGGTTTATTGCTGATGGTGCTGCTGCCAGGATGTTGCCATTGCTGTGGAAGCTGCCTGCACTGCCCGCTTTCCAGTCGGGAAACCTGTCGTGCCAGCTGCATAACGCGGCGGTTTGTTCCCACCGAT"))

largestString = 0

for test in testList:
    if len(test) > largestString:
        largestString = len(test)

IDs = someMethods.generateHypervectorIDs(largestString, dimensions, "IDs.pt")

# list of hypervectors for each DNA sequence
testResults = []

# print("IDs: ", IDs)


try: 
    # generating the hypervectors for each DNA sequence
    for DNA_SEQUENCE in testList:
        print("DNA_SEQUENCE: ", DNA_SEQUENCE)

        if DNA_SEQUENCE[0] == "A":
            firstLetter = torchhd.bind(nucleotide_A, IDs[0])
        elif DNA_SEQUENCE[0] == "C":
            firstLetter = torchhd.bind(nucleotide_C, IDs[0])
        elif DNA_SEQUENCE[0] == "G":
            firstLetter = torchhd.bind(nucleotide_G, IDs[0])
        elif DNA_SEQUENCE[0] == "T":
            firstLetter = torchhd.bind(nucleotide_T, IDs[0])
        else:
            firstLetter = torchhd.bind(specialChar, IDs[0])

        if DNA_SEQUENCE[1] == "A":
            nextLetter = torchhd.bind(nucleotide_A, IDs[1])
        elif DNA_SEQUENCE[1] == "C":
            nextLetter = torchhd.bind(nucleotide_C, IDs[1])
        elif DNA_SEQUENCE[1] == "G":
            nextLetter = torchhd.bind(nucleotide_G, IDs[1])
        elif DNA_SEQUENCE[1] == "T":
            nextLetter = torchhd.bind(nucleotide_T, IDs[1])
        else:
            nextLetter = torchhd.bind(specialChar, IDs[1])
        sequenceHyperVector = torchhd.bundle(firstLetter, nextLetter)

        for i in range(2, len(DNA_SEQUENCE)):
            if DNA_SEQUENCE[i] == "A":
                nextLetter = torchhd.bind(nucleotide_A, IDs[i])
            elif DNA_SEQUENCE[i] == "C":
                nextLetter = torchhd.bind(nucleotide_C, IDs[i])
            elif DNA_SEQUENCE[i] == "G":
                nextLetter = torchhd.bind(nucleotide_G, IDs[i])
            elif DNA_SEQUENCE[i] == "T":
                nextLetter = torchhd.bind(nucleotide_T, IDs[i])
            else:
                nextLetter = torchhd.bind(specialChar, IDs[i])
            sequenceHyperVector = torchhd.bundle(sequenceHyperVector, nextLetter)
        
        testResults.append(sequenceHyperVector)

    print("Test results: ", testResults)

    string = ""

    for i in range(len(testResults)):
        if len(testList[i]) <= 15:
            string += f"[{testList[i]}]" + f" ({i}) | "
        else:
            shortSequence = testList[i][:5] + " ... " + testList[i][-5:]
            string += f"[{shortSequence}]" + f" ({i}) | "
        for j in range(len(testResults)):
            string += f"-> ({j}) {(torchhd.hamming_similarity(testResults[i], testResults[j]))[0] / dimensions}" + " | "
        string += "\n"
    print(string)
except Exception as e:
    print("ERROR: ", e)
finally:
    someMethods.deleteHypervector("IDs.pt")
    someMethods.deleteHypervector("nucleotide_A.pt")
    someMethods.deleteHypervector("nucleotide_C.pt")
    someMethods.deleteHypervector("nucleotide_G.pt")
    someMethods.deleteHypervector("nucleotide_T.pt")
    someMethods.deleteHypervector("specialChar.pt")
