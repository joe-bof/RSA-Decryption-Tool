from Crypto.Util.number import inverse, long_to_bytes

#hard code values
c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

#use n to determine p and q from online tool.
#hard code in p and q.
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

#decryption
phi = (p -1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
