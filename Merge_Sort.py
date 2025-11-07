import time

def merge_sort(lista):
    start = time.perf_counter()  # início da medição de tempo
    comparacoes = [0]
    movimentos = [0]

    def merge(esquerda, direita):
        resultado = []
        i = j = 0

        # compara e junta as sublistas ordenadas
        while i < len(esquerda) and j < len(direita):
            comparacoes[0] += 1
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
            movimentos[0] += 1

        # adiciona o restante dos elementos
        while i < len(esquerda):
            resultado.append(esquerda[i])
            i += 1
            movimentos[0] += 1

        while j < len(direita):
            resultado.append(direita[j])
            j += 1
            movimentos[0] += 1

        return resultado

    def merge_sort_recursivo(sublista):
        if len(sublista) <= 1:
            return sublista
        meio = len(sublista) // 2
        esquerda = merge_sort_recursivo(sublista[:meio])
        direita = merge_sort_recursivo(sublista[meio:])
        return merge(esquerda, direita)

    lista_ordenada = merge_sort_recursivo(lista)
    lista[:] = lista_ordenada  # copia de volta para a lista original

    end = time.perf_counter()  # fim da medição
    tempo_ms = (end - start) * 1000.0
    return comparacoes[0], movimentos[0], tempo_ms


def converter_entrada(texto):
    return list(map(int, texto.replace(",", " ").split()))


# --- Execução ---
entrada = input("Cole os números (ex: 1,2,3,4...): ")
lista = converter_entrada(entrada)

comparacoes, movimentos, tempo_ms = merge_sort(lista)

print("Lista ordenada:", lista)
print(f"Comparações: {comparacoes}")
print(f"Movimentações: {movimentos}")
print(f"Tempo (ms): {tempo_ms:.3f}")