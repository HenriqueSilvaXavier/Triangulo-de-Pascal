n=int(input("Quantas linhas? "))
linha1=[1]
print(linha1[0])
if n>1:
	linha1=[1, 1]
	c=0
	while c<1:
		print(linha1[c], end=" ")
		c=c+1
	if c==1:
		print(linha1[c])
for n in range(0, n-2):
	c=0
	linha2=linha1[:]
	linha1=[]
	linha1.append(1)
	for k in range(1, len(linha2)):
		linha1.append(linha2[k-1]+linha2[k])
	linha1.append(1)
	while c<len(linha1)-1:
		print(linha1[c], end=" ")
		c=c+1
	if c==len(linha1)-1:
		print(linha1[c])