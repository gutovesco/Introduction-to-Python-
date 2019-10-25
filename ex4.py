lista = [28,9,3,19,2]

for i in range(len(lista)): #varre a lista em busca dos valores

	menor = i #menor recebe o valor achado

	for j in range(i+1,len(lista)): #j busca na lista um valor após o outro
		if lista[j] < lista[menor]: #se o valor que foi encontrado for menor do que o anterior
			menor = j #a variavel menor vai receber esse valor

	if lista[i] != lista[menor]: 
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux #usa o auxiliar aux para trocar os valores
print (lista)