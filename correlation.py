import matplotlib.pyplot as plt

s = '101001011100101100010'

#a = '100011110101100'
a = '1110010'
#a = '100010011010111'


def shift(sequence,shift_length):
    # shift sequence by taking bits 0 to tau (the shift)
    # and moving them to the end of the sequence
    shifted_sequence = sequence[shift_length:]+sequence[0:shift_length]
    #print shifted_sequence
    return shifted_sequence

def cross_correlation(seq1,seq2):

    # extend sequence a to same length of sequence s
    padding_bits = len(seq1)-len(seq2)
    while padding_bits > len(seq2):
        seq2 = seq2+seq2
        padding_bits = len(seq1)-len(seq2)
    seq2 = seq2+seq2[0:padding_bits]
    count0=0 # count of number of 0 bits in correlated sequence
    count1=0 # count of number of 1 bits in correlated sequence

    # compute correlation (sum of sequence s and sequence a)
    for x in range(0,len(seq2)): 
        t=(int(seq1[x])+int(seq2[x]))%2 # addition is XOR (modulo 2)
        if t == 0:
            count0 = count0 + 1
        elif t == 1:
            count1 = count1 + 1
    #print 'count0=%d, count1=%d' %(count0,count1)
    c = count0-count1 # correlation is number of 0s minus number of 1s
    return c

#main function
n = len(a)
c = [0]*n # initialize correlation array with n 0s

#iterate through all possible tau (t) and output resulting correlation
for t in range(0,n):
    c[t] = cross_correlation(s,shift(a,t))
    print 'C(s,a)(%d)=%d' %(t,c[t])
    
plt.plot(range(0,n),c)
plt.xlabel('Tau')
plt.ylabel('C(s,a)(Tau)')
plt.show()
