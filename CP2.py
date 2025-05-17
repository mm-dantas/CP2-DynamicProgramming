import time
import math
import random

# Classe Nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


# Classe Lista Ligada
class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def iterar(self):
        atual = self.cabeca
        while atual:
            yield atual
            atual = atual.proximo

    def dividir_em_listas(self):
        lista_negativa = ListaLigada()
        lista_positiva = ListaLigada()
        for no in self.iterar():
            if no.valor < 0:
                lista_negativa.inserir(no.valor)
            else:
                lista_positiva.inserir(no.valor)
        return lista_negativa, lista_positiva

    def imprimir(self):
        return [no.valor for no in self.iterar()]


def merge_sort_positivos(lista):
    if lista is None or lista.proximo is None:
        return lista

    meio = dividir_lista(lista)
    esquerda = merge_sort_positivos(lista)
    direita = merge_sort_positivos(meio)

    return mesclar_listas(esquerda, direita)


def dividir_lista(cabeca):
    lento = cabeca
    rapido = cabeca.proximo

    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

    meio = lento.proximo
    lento.proximo = None
    return meio


def mesclar_listas(esquerda, direita):
    if esquerda is None:
        return direita
    if direita is None:
        return esquerda

    if esquerda.valor <= direita.valor:
        resultado = esquerda
        resultado.proximo = mesclar_listas(esquerda.proximo, direita)
    else:
        resultado = direita
        resultado.proximo = mesclar_listas(esquerda, direita.proximo)

    return resultado


# Quadro de bloco do radix sort
def obter_maior(lista):
    maior = 0
    atual = lista.cabeca
    while atual:
        if atual.valor > maior:
            maior = atual.valor
        atual = atual.proximo
    return maior


# Radix Sort adaptado para negativos
def radix_sort_negativos(lista):
    if not lista.cabeca:
        return ListaLigada()

    # Passo 1: transformando os valores para positivos
    lista_abs = ListaLigada()
    atual = lista.cabeca
    while atual:
        lista_abs.inserir(abs(atual.valor))
        atual = atual.proximo

    # Passo 2: aplicando radix sort nos valores absolutos
    maior = obter_maior(lista_abs)
    exp = 1

    contador_passos = 0
    while maior // exp > 0:
        contador_passos += 1
        baldes = [ListaLigada() for _ in range(10)]

        atual = lista_abs.cabeca
        contador_interno = 0
        while atual:
            contador_interno += 1
            indice = (atual.valor // exp) % 10
            baldes[indice].inserir(atual.valor)
            atual = atual.proximo

        lista_abs.cabeca = None
        ultimo = None
        for balde in reversed(baldes):
            if balde.cabeca:
                if not lista_abs.cabeca:
                    lista_abs.cabeca = balde.cabeca
                    ultimo = balde.cabeca
                else:
                    ultimo.proximo = balde.cabeca
                while ultimo.proximo:
                    ultimo = ultimo.proximo
        exp *= 10

    # Passo 3: reconvertendo os valores para negativos
    lista_negativo = ListaLigada()
    atual = lista_abs.cabeca
    while atual:
        lista_negativo.inserir((-atual.valor))
        atual = atual.proximo
    return lista_negativo

# fim do quadro de bloco do radix sort


# Função principal de organização
def organizar_lista(lista_original):
    lista_neg, lista_pos = lista_original.dividir_em_listas()


    tempo_inicio_radix = time.time()
    lista_neg_ordenada = radix_sort_negativos(lista_neg)
    tempo_fim_radix = time.time()
    tempo_resul_radix = tempo_fim_radix - tempo_inicio_radix

    tempo_inicio_merge = time.time()
    lista_pos.cabeca = merge_sort_positivos(lista_pos.cabeca)
    tempo_fim_merge = time.time()
    tempo_resul_merge = tempo_fim_merge - tempo_inicio_merge

    # Concatenar as listas
    lista_final = ListaLigada()
    for no in lista_neg_ordenada.iterar():
        lista_final.inserir(no.valor)
    for no in lista_pos.iterar():
        lista_final.inserir(no.valor)

    # Impressão dos resultados
    print("Lista negativa ordenada por Radix Sort: ", lista_neg_ordenada.imprimir())
    print("Lista positiva ordenada por Merge Sort: ", lista_pos.imprimir())
    print("Lista final concatenada: ", lista_final.imprimir())
    print("Complexidade de Merge Sort O(n log n): ", 5 * math.log(5))
    print("Complexidade de Radix Sort O(nk): ", 3 * 2)
    print("Tempo de execução do Radix Sort: ", tempo_resul_radix)
    print("Tempo de execução do Merge Sort: ", tempo_resul_merge)


if __name__ == "__main__":
    lista = ListaLigada()
    entrada = [-99, -7, -1, 0, 3, 12, 23, 45]
#    entrada = [random.randint(-100, 100) for _ in range(1200)]  #caso queira colocar mais dados para ver o tempo de execução
    for numero in entrada:
        lista.inserir(numero)

    organizar_lista(lista)
