q = int(input('Enter prime number: '))
xa = int(input('Enter private key of A: '))
xb = int(input('Enter private key of B: '))

# Calculation of a i.e. is primitive root
for a in range(1, q+1):
    l1=[]
    for x in range(1, q):
        l1.append((a**x)%q)
    if(len(l1) == len(set(l1))):
        break

# ya and yb are public keys of A and B person
ya = (a**xa)%q
yb = (a**xb)%q

print('primitive root of ',q,' =',a)
print("Public key of A = ", ya)
print("Public key of B = ", yb)

if (ya**xb)%q == (yb**xa)%q:
    K=(ya**xb)%q
print('secret key K = ',K)

'''
Sample input and output
Enter prime number: 17
Enter private key of A: 4
Enter private key of B: 6
primitive root of  17  = 3
Public key of A =  13
Public key of B =  15
secret key K =  16

time complexity: O(n^2)
space complexity: O(n)
'''