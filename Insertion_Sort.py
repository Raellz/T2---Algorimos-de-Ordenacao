import time

def insertion_sort(lista):
    start = time.perf_counter()  # início da medição de tempo
    comparacoes = 0
    trocas = 0  # vamos contar movimentos/trocas reais

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        # Enquanto o valor anterior for maior, movemos o elemento
        while j >= 0:
            comparacoes += 1  # comparação da condição
            
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
                trocas += 1  # conta movimentação
            else:
                break
        
        # Inserir a chave na posição correta
        lista[j + 1] = chave

    end = time.perf_counter()  # fim da medição
    tempo_ms = (end - start) * 1000.0
    return comparacoes, trocas, tempo_ms

def converter_entrada(texto):
    return list(map(int, texto.replace(",", " ").split()))

# --- Execução ---
entrada = input("Cole os números (ex: 1,2,3,4...): ")
lista = converter_entrada(entrada)

comparacoes, trocas, tempo_ms = insertion_sort(lista)

print("Lista ordenada:", lista)
print(f"Comparações: {comparacoes}")
print(f"Trocas/Movimentações: {trocas}")
print(f"Tempo (ms): {tempo_ms:.3f}")
