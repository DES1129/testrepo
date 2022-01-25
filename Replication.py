# 1: --------------------PatternCount Function------------------------------------------------------------------------
def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count

#Text = "GCGCGCGCGCGGGGCG"
#Pattern = "GCG"

#print(PatternCount(Text,Pattern))

#2:-----------------------FrequencyMap Function---------------------------------

# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    # your code here
    freq = {}
    n = len(Text)
    count = 0
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
        for i in range(len(Text) - len(Pattern) + 1):
            if Text[i:i + len(Pattern)] == Pattern:
                count = count + 1
                freq[Pattern] += 1
    return freq

#Text = "CGATATATCCATAG"
#k    = 3

#print(FrequencyMap(Text, k))

#3:---------------------------FrequencyWords Fucntion--------------------------------
def FrequentWords(Text, k):
    # your code here
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key]==m:
            words.append(key)
    return words
# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
#Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
#k = 4

# Finally, print the result of calling FrequentWords on Text and k.
#words = sorted(FrequentWords(Text, k))
#print(words)

#4:--------------------Reverse(Pattern) Function-------------------------------
# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    return Pattern[::-1]
    # your code here

#Pattern ='AAAACCCGGT'
#print(Reverse(Pattern))

#5:---------------------Complement(Pattern) Function-------------------------------
# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    # Return the complementary sequence string
    basecomplement = {'A':'T', 'C':'G', 'G': 'C', 'T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't': 'a', 'n':'n'}
    letters = list(Pattern)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

#print(Complement("AAAACCCGGT"))

#6:-----------------------ReverseComplement Function-------------------------------
# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    # your code here
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

#print(ReverseComplement("AAAACCCGGT"))

#7:----------------------PatternMatching Function----------------------------------
#Pattern Matching Problem:  Find all occurrences of a pattern in a string.
# Input: Strings Pattern and Genome.
# #Output: All starting positions in Genome where Pattern appears as a substring.

# fill in your PatternMatching() function along with any subroutines that you need.
# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
#import sys                              # needed to read the genome
#input = sys.stdin.read().splitlines()   #
#v_cholerae = input[1]                   # store the genome as 'v_cholerae'

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)
    # your code here
    return positions

#print(PatternMatching("ATAT","GATATATGCATATACTT"))
#8:--------------------------SymbolArray Function----------------------------------
#This Function uses a modified PatternCount Function-------------------------------
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    # type your code here
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    print(ExtendedGenome)
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


# Reproduce the PatternCount function here.
def PatternCount(symbol,ExtendedGenome):
    count = 0
    for i in range(len(ExtendedGenome)-len(symbol)+1):
        if ExtendedGenome[i:i+len(symbol)] == symbol:
            count = count+1
    return count

#print(SymbolArray("AAAAGGGG","A"))
#9:-----------------------FasterSymbolArray---------------------------------------
#This Function uses a modified PatternCount Function------------------------------
# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # your code here
    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(symbol, ExtendedGenome):
    count = 0 # output variable
    n = len(ExtendedGenome)
    k = len(symbol)
    # your code here
    for i in range(n-k+1):
        if ExtendedGenome[i:i+k] == symbol:
            count +=1
    return count

#print(FasterSymbolArray("AAAAGGGG","A"))

#10:-------------------------SkewArray-------------------------------------------------
# Input:  A String Genome
# Output: The skew array of Genome as a list.
#This Function SkewArray(Genome) takes a DNA string Genome as input
# and returns the skew array of Genome in the form of a list whose
# i-th element is Skew[i].
def SkewArray(Genome):
    Skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew

#print(SkewArray("GATACACTTCCCGAGTAGGTACTG"))

#11:-------------------------------MinimumSkew Function--------------------------------
#Write a function MinimumSkew taking a DNA string Genome as input and returning
# all integers i minimizing Skew[i] for Genome. Then add this function to
# Replication.py. (Hint: make sure to call Skew(Genome) as a subroutine,
# and keep in mind that Python has a built-in min function in addition to max.)
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    Skew = SkewArray(Genome)
    n =len(Skew)
    m = max(Skew)
    for i in range(n):
        if Skew[i] == m:
            positions.append(i)
    return positions

print(MinimumSkew("GATACACTTCCCGAGTAGGTACTG"))

#12:--------------------------HammingDistance Function-------------------------------
#Hamming Distance Problem:Compute the Hamming distance between two strings.
#Input: Two strings of equal length.
#Output: The Hamming distance between these strings.
# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    Pos = []
    n = len(q)
    for i in range(n):
        if p[i] != q[i]:
            Pos.append(i)
    return len(Pos)

print(HammingDistance("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT","CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"))

#13:-----------------------ApproixmatePatternMatching Function----------------------
#Approximate Pattern Matching Problem:Find all approximate occurrences of a pattern in a string.
#Input: Strings Pattern and Text along with an integer d.
#Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    n = len(Pattern)
    k = len(Text)
    for i in range(k-n+1):
        if HammingDistance(Text[i:i+n], Pattern) <= d:
            positions.append(i)
    return positions

#Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
#Pattern = "ATTCTGGA"
#d = 3
#print(ApproximatePatternMatching(Text,Pattern,d))

#14:-------------------------ApproximatePatternCount Function-------------------------------------
#This function computes the number of occurrences of Pattern in Text with at most d mismatches.
#For example,ApproximatePatternCount(AAAAA, AACAAGCATAAACATTAAAGAG, 1) = 4
#because AAAAA appears four times in this string with at most one mismatch: AACAA,ATAAA,AAACA,and AAAGA.
# This code is a slight modification Hamming Distance ans Pattern Count
# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            count += 1
    return count
# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
    # your code here
    count = 0
    n = len(q)
    for i in range(n):
        if p[i] != q[i]:
            count +=1
    return count

#print(ApproximatePatternCount("GAGG","TTTAGAGCCTTCAGAGG",2))
