# 1. Pede ao usuário para digitar a string de números
entrada_usuario = input("Digite os valores (ex: 3, 45 ,323, 324): ")

# 2. Processa a string
# Primeiro, substitui todas as vírgulas por espaços
# Isso transforma "3, 45 ,323" em "3  45  323"
string_com_espacos = entrada_usuario.replace(",", " ")

# 3. Separa os valores e conta
# O método .split() (sem argumentos) é inteligente:
# - Ele divide a string por espaços.
# - Ele trata múltiplos espaços como um só (ignorando os espaços extras).
# - Ele remove espaços no início ou no fim.
lista_de_valores = string_com_espacos.split()

# 4. Conta quantos itens estão na lista resultante
contagem = len(lista_de_valores)

# 5. Exibe o resultado
print(f"A lista de valores digitada foi: {lista_de_valores}")
print(f"Número total de valores: {contagem}")