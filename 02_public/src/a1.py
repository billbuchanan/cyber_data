# Python 2.7
p=11
q=3
N=p*q
PHI=(p-1)*(q-1)
e=3
for d in range(1,100):
        if ((e*d % PHI)==1): break
print (e,N)
print (d,N)
M=4
cipher = M**e % N
print ("Cipher is: ",cipher)
message = cipher**d % N
print (message)

# Python 3  - just uncomment if you are using Python 3
# p=11
#q=3
#N=p*q
#PHI=(p-1)*(q-1)
#e=3
#for d in range(1,100):
#        if ((e*d % PHI)==1): break
#print (e,N)
#print (d,N)
#M=4
#cipher = M**e % N
#print (cipher)
#message = cipher**d % N
#print (message)

