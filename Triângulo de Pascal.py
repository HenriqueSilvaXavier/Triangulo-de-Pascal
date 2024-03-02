n=int(input("Digite um número de linhas: "))
c2=1
while c2<=n:
	c=1
	while c<c2:
		print(c, end=" ")
		c=c+1
	if c==c2:
		print(c)
	c2=c2+1