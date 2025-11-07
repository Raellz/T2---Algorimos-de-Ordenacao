import time

def selection_sort(lista):
    start = time.perf_counter()  # início da medição
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparacoes += 1

            if lista[j] < lista[min_index]:
                min_index = j

        # Só troca se o menor não for o próprio i
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
            trocas += 1

    end = time.perf_counter()  # fim da medição
    tempo_ms = (end - start) * 1000.0
    return comparacoes, trocas, tempo_ms

def converter_entrada(texto):
    return list(map(int, texto.replace(",", " ").split()))

# --- Execução ---
entrada = input("Cole os números (ex: 1,2,3,4...): ")
lista = converter_entrada(entrada)

comparacoes, trocas, tempo_ms = selection_sort(lista)

print("Lista ordenada:", lista)
print(f"Comparações: {comparacoes}")
print(f"Trocas: {trocas}")
print(f"Tempo (ms): {tempo_ms:.3f}")
