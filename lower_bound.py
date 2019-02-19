import collections
#Since T = 15, split the bit string in to a group of 15 bits each.
# A = "010010010110111 110010010000111 100010000011111 110010101001000 010010010110111 110010010000111 1000100000"
# b = A.split()

A = "0100100101101111100100100001111000100000111111100101010010000100100101101111100100100001111000100000"
# b = A.split()
# print(b)
chunks, chunk_size = len(A), 15#len(A)//6
b = [ A[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
print(b)


dictvalue = {"T1" : b[0], "T2" : b[1], "T3" : b[2], "T4" : b[3], "T5" : b[4], "T6" : b[5]}

value_to_key = collections.defaultdict(list)
for k, v in dictvalue.iteritems():
	value_to_key[v].append(k)
print value_to_key
#A = "{010010010110111}{110010010000111}{100010000011111}{110010101001000}{010010010110111}{110010010000111}{1000100000"

# T1 = b[0]
# T2 = b[1]
# T3 = b[2]
# T4 = b[3]
# T5 = b[4]
# T6 = b[5]

# print(T6)
# T7 = b[7]

# print(T1 == T2)

# print(T1 + T2 == T3 + T4)

# print(T1 + T2 + T3) #==  T4 + T5 + T6)
# #T7 = b[7]

# if T1 == T2: #True:
# 	print(f"The period is ", 15*1)
# elif T1  == T3: 
# 	print(f"The period is ", 15*2)
# elif T1  == T4:
# 	print("The period is ", 15*3)
# elif T1  == T5:
# 	print("The period is ", 15*4)	
# else:
# 	print("Not periodic")


# TN = int(T1+T2+T3)
# TM = int(T4+T3+T6)


# #S = len(TN)
# #V = str(S)

# if TN == TM:
# 	# S = len(TN)
# 	# V = str(S)
# 	print("The lower bound is " + V)

