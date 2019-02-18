l_seq = [1,0,1,0]
nl_seq = [0,0,0,1]

def LFSR(seq):
    feedback = (seq[0]+seq[1])%2 # feedback a4=a0+a1
    output = seq[0] # output a0
    seq = seq[1:]+[feedback] # new sequence is a1a2a3a4
    return output,seq # a0, a1a2a3a4

def NLFSR(seq,lfsr_output):
    feedback = (seq[0]+seq[1]*seq[2]+seq[2]*seq[3]+lfsr_output)%2 # feedback b4=a0+b0+b1b2+b2b3
    output = seq[0] # output b0
    seq = seq[1:]+[feedback] # new sequence is b1b2b3b4
    return output,seq # b0, b1b2b3b4

def grain(l_seq,nl_seq):
    output = (nl_seq[0]+nl_seq[3]+l_seq[0]*l_seq[2])%2 # s0 = b0+b3+a0a2
    return output # s0

count = 0
out = ''
while count < 100:
    out = out + str(grain(l_seq,nl_seq)) # append latest grain output s_i to output string
    (l_out,l_seq) = LFSR(l_seq) # update LFSR
    (nl_out,nl_seq) = NLFSR(nl_seq,l_out) # update NLFSR
    count+=1

print out
