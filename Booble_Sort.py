def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                houve_troca = True
        
        if not houve_troca:  # otimização: para cedo se já estiver ordenado
            break

    return comparacoes, trocas

def converter_entrada(texto):
    return list(map(int, texto.replace(",", " ").split()))

# --- Execução ---
entrada = input("Cole os números (ex: 1,2,3,1,23,4): ")
lista = converter_entrada(entrada)

comparacoes, trocas = bubble_sort(lista)

print("Lista ordenada:", lista)
print(f"Comparações: {comparacoes}")
print(f"Trocas: {trocas}")
