s = '101001011100101100010'
a = '100011110101100'
b = '1110010'
c = '100010011010111'

def shift(sequence,shift_length):
    shifted_sequence = sequence[shift_length:]+sequence[0:shift_length]
    return shifted_sequence

len_a = len(a)
len_c = len(c)

bb = b+b+b # extend to same length as s

for i in range(0,len(a)): # iterate through all shifts of LFSR 0 output
    aa = shift(a,i)
    aa = aa + aa[0:6] # extend to same length as s
    for j in range(0,len(c)): # iterate through all shifts of LFSR 2 output
        cc = shift(c,j)
        cc = cc + cc[0:6] # extend to same length as s
        outp=''
        for t in range(0,len(aa)): # compute result of function
            z = (int(aa[t])*int(bb[t])+int(bb[t])*(1-int(cc[t])))%2
            outp = outp+str(z)
            if outp == '101001011100101100010': # check if result matches observed sequence
                print 'found it!!!'
                print 'a=%s, d=%s, c=%s' %(aa[0:len(a)],bb[0:len(b)],cc[0:len(c)])
                break
