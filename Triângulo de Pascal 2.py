n=int(input("Quantas linhas? "))
linha1=[1]
print(linha1)
if n>1:
	linha1=[1, 1]
	print(linha1)
for n in range(0, n-2):
	linha2=linha1[:]
	linha1=[]
	linha1.append(1)
	for k in range(1, len(linha2)):
		linha1.append(linha2[k-1]+linha2[k])
	linha1.append(1)
	print(linha1)