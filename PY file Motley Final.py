#!/usr/bin/env python
# coding: utf-8

# # Motley Final Project
# **This final project contains three separate and unrelated functions.**

# ### Function 1: Extracting Optimized Coordinates (EOC)
# **Data concerning the optimized coordinates of various molecules is extracted from GAMESS output files provided by the instructor.**
# ***This function works for a very restricted set of files.***

# In[11]:


#Extracting the {MoleculeName} data

import os
print(os.getcwd())

def coordinateextraction(MoleculeName):

    #here, we open a log file and put the contents into a variable and then close the file
    seffile = open(f'{MoleculeName}.log','r')
    sefdata = seffile.readlines()
    seffile.close()
    
    #here we define variables as flags
    equilfoundsef = False
    coordsfoundsef = False
    
    #this is our counter that we start after our conditions are met
    countersef = 0 
    
    #this is where we stored the desires lines of data
    outputsef = []

    #this for loop looks for two landmarks in the file to find the data we want
    for lines in sefdata:
        if "EQUILIBRIUM GEOMETRY LOCATED" in lines:
            print(f"this line is present in {MoleculeName} data")
            equilfoundsef = True
        if "COORDINATES OF ALL ATOMS" in lines and equilfoundsef:
            print(f"found right coordinates in {MoleculeName} data")
            coordsfoundsef = True
        if coordsfoundsef and equilfoundsef and countersef <16: #here we constrain the lines to the region where both flags were found
            outputsef.append(lines) #we put the desired lines into an array
            countersef += 1

    #these lines create the file and store the desired lines of data in the file
    seftxt = open(f"{MoleculeName}.txt","w") #writing the new file
    seftxt.writelines(outputsef[3:]) #putting desired lines into the file
    seftxt.close()

#This will test one Molecule log file
coordinateextraction('SeBr')


# ### Function 2: mRNA to Amino Acids (mAA)
# **This function takes an mRNA sequence and returns the corresponding sequence of amino acids.**

# In[1]:


import os

def mRNAtoAA(mRNAstrand):
    #these lines define the corresponding amino acid to a codon
    mRNAdata = []
    mRNAfile = open('mRNA_codon.txt','r')
    mRNAdata = mRNAfile.readlines()
    mRNAfile.close()
#     print(mRNAdata)
    DICTmRNAtoAA = {}
    for lines in mRNAdata:
        codon = lines.split()
#         print(codon)
        DICTmRNAtoAA[codon[0]] = codon[1]
    
    #this splits the mRNA strand's bases into groups of three to make the codons    
    codon_list = [mRNAstrand[i:i+3] for i in range(0,len(mRNAstrand),3)]
    
    #these lines translate the given codon to the corresponding amino acid
    AminoAcid = []
    for item in codon_list:
        AminoAcid.append(DICTmRNAtoAA[item])
        
    #this displays the amino acid sequence
    print(AminoAcid)
    
#Here are two example mRNA strands
mRNAtoAA(mRNAstrand='AAAUGUCCCUUGCGA')
mRNAtoAA(mRNAstrand='AAAUGUCCCUUGCGAAGGGGUGUGCUCGACAAACCCGGG')


# ### Function 3: Complementary DNA Sequence (CDNAS)
# **This function takes a DNA sequence and returns the complementary DNA sequence as well as a text file containing the complementary sequence.**
# 
# ***This function is best suited for short DNA segments. The title of the file returned will be the DNA sequence input by the user.***

# In[14]:


#This function returns the complementary sequence to a given DNA strand of bases
#It also provides the complementary strand in a new text file
#The title of the new text file is the given/input DNA sequence

def complementDNA(DNAstrand):
    
    #these lines define the complementary base that pairs with a given base
    DNAdata = []
    DNAfile = open('DNAbp.txt','r')
    DNAdata = DNAfile.readlines()
    DNAfile.close()
    DICTcpmDNA = {}
    for lines in DNAdata:
        bp = lines.split()
        DICTcpmDNA[bp[0]] = bp[1]
        
    #these lines translate the given bases to the complementary bases
    cmpDNA = []
    for item in DNAstrand:
        cmpDNA.append(DICTcpmDNA[item])
        
    #this line prints out the complementary strand
    print(cmpDNA)
    
    #these lines write the complementary strand to a text file
    cmpDNAtxt = open(f"{DNAstrand}.txt",'w')
    cmpDNAtxt.writelines(cmpDNA)
    cmpDNAtxt.close()

complementDNA('CTCGATGCTGACT')

