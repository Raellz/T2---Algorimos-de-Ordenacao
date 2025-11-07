import time

def quick_sort(lista):
    start = time.perf_counter()  # início da medição de tempo
    comparacoes = [0]
    trocas = [0]

    def particiona(inicio, fim):
        pivo = lista[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            comparacoes[0] += 1
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                trocas[0] += 1
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        trocas[0] += 1
        return i + 1

    def quicksort(inicio, fim):
        if inicio < fim:
            pivo_index = particiona(inicio, fim)
            quicksort(inicio, pivo_index - 1)
            quicksort(pivo_index + 1, fim)

    quicksort(0, len(lista) - 1)
    end = time.perf_counter()  # fim da medição
    tempo_ms = (end - start) * 1000.0
    return comparacoes[0], trocas[0], tempo_ms

def converter_entrada(texto):
    return list(map(int, texto.replace(",", " ").split()))

# --- Execução ---
entrada = input("Cole os números (ex: 1,2,3,4...): ")
lista = converter_entrada(entrada)

comparacoes, trocas, tempo_ms = quick_sort(lista)

print("Lista ordenada:", lista)
print(f"Comparações: {comparacoes}")
print(f"Trocas: {trocas}")
print(f"Tempo (ms): {tempo_ms:.3f}")
