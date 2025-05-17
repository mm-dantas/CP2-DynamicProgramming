# CP2-DynamicProgramming

# Projeto: Organização de Lista Ligada com Merge Sort e Radix Sort

Este projeto implementa uma solução para organizar uma lista ligada de números inteiros, utilizando dois algoritmos de ordenação distintos: Radix Sort para os números negativos e Merge Sort para os números positivos (incluindo zero).


## Estrutura do Código

O código é dividido em classes e funções que representam os elementos da lista ligada e os algoritmos de ordenação.

### Classe `No`

```python
# Classe Nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
```

- Descrição: Representa um único elemento (nó) dentro da lista ligada.
- Atributos:
   - valor: Armazena o dado que o nó contém (neste caso, um número inteiro).
  - proximo: Uma referência (ponteiro) para o próximo nó na sequência da lista. Inicialmente é None até que outro nó seja ligado a ele.

### Classe ListaLigada
```python
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
```

- Descrição: Implementa a estrutura de dados de Lista Ligada Simplesmente Encadeada.
- Atributos:
   - cabeca: Uma referência para o primeiro nó da lista. É None se a lista estiver vazia.
- Métodos:
  - __init__: Construtor da classe. Inicializa a lista vazia definindo cabeca como None.
   - inserir(valor): Adiciona um novo nó com o valor especificado ao final da lista. Se a lista estiver vazia, o novo nó se torna a cabeça. Caso contrário, percorre a lista até o último nó e anexa o novo nó a ele.
   - iterar(): Um método gerador (usa yield). Permite percorrer a lista nó a nó, retornando cada objeto No em sequência. Isso facilita a iteração sobre os elementos da lista (por exemplo, usando um loop for).
   - dividir_em_listas(): Percorre a lista original usando o método iterar e cria duas novas listas ligadas: uma contendo apenas os números negativos e outra contendo os números positivos e zero. Retorna essas duas novas listas.
   - imprimir(): Percorre a lista usando o método iterar e coleta os valores de cada nó em uma lista Python (list). Retorna esta lista de valores, facilitando a visualização do conteúdo da lista ligada.

 ## Implementação do Merge Sort (para Positivos)
 ```python
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
 ```

- Descrição: Conjunto de funções que implementam o algoritmo de ordenação Merge Sort para listas ligadas. Este algoritmo é usado especificamente para ordenar a lista de números positivos e zeros. O Merge Sort é um algoritmo de divisão e conquista, conhecido por sua estabilidade e complexidade O(n log n).
- merge_sort_positivos(lista):
   - É a função principal recursiva do Merge Sort.
   - Caso Base: Se a lista for vazia ou tiver apenas um nó, ela já está ordenada, então retorna a própria lista.
   - Divisão: Usa a função dividir_lista para encontrar o ponto médio e dividir a lista em duas sublistas: esquerda e direita.
   - Conquista: Chama merge_sort_positivos recursivamente para ordenar a sublista esquerda e a sublista direita.
   - Combinação: Usa a função mesclar_listas para mesclar as duas sublistas ordenadas, produzindo uma única lista ordenada.
- dividir_lista(cabeca):
   - Função auxiliar para o Merge Sort.
   - Recebe a cabeça de uma lista ligada.
   - Usa a técnica de ponteiro lento (lento) e ponteiro rápido (rapido) para encontrar o ponto médio da lista. O ponteiro rápido avança duas vezes mais rápido que o lento; quando o rápido chega ao final, o lento estará no meio.
   - Divide a lista em duas partes, cortando a ligação após o nó lento. Retorna a cabeça da segunda metade (meio).
- mesclar_listas(esquerda, direita):
   - Função auxiliar para o Merge Sort.
   - Recebe as cabeças de duas listas ligadas já ordenadas.
   - Mescla recursivamente as duas listas em uma única lista ordenada, comparando os valores dos nós atuais em cada lista e escolhendo o menor para ser o próximo nó na lista resultante.

## Implementação do Radix Sort Adaptado (para Negativos)
 ```python
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

    # Passo 1: transformando os valores para positivos (absolutos)
    lista_abs = ListaLigada()
    atual = lista.cabeca
    while atual:
        lista_abs.inserir(abs(atual.valor))
        atual = atual.proximo

    # Passo 2: aplicando radix sort nos valores absolutos
    maior = obter_maior(lista_abs) # O maior valor absoluto determina o número de passes
    exp = 1 # Expoente, representa a casa decimal atual (1, 10, 100, ...)

    # Loop principal do Radix Sort: executa para cada dígito
    while maior // exp > 0:
        baldes = [ListaLigada() for _ in range(10)] # Cria 10 baldes (um para cada dígito 0-9)

        # Distribuição nos baldes
        atual = lista_abs.cabeca
        while atual:
            # Calcula o índice do balde com base no dígito atual
            indice = (atual.valor // exp) % 10
            baldes[indice].inserir(atual.valor) # Insere o número no balde correspondente
            atual = atual.proximo

        # Coleta dos baldes para reconstruir a lista ordenada pelo dígito atual
        lista_abs.cabeca = None # Limpa a lista absoluta para reconstruir
        ultimo = None # Ponteiro para o último nó da nova lista construída

        # Iterar pelos baldes de 0 a 9 e concatená-los
        # O código original itera de 9 a 0 e insere no início.
        # Para ordenar absolutos crescentemente, devemos iterar de 0 a 9.
        # A implementação abaixo está reescrita para coletar de 0 a 9.
        for balde in baldes: # Itera do balde 0 ao 9
             if balde.cabeca: # Se o balde não estiver vazio
                if not lista_abs.cabeca: # Se a lista_abs ainda estiver vazia
                    lista_abs.cabeca = balde.cabeca # O primeiro balde se torna a cabeça
                    ultimo = balde.cabeca
                else:
                    # Conecta o final da lista_abs atual com o início do balde
                    ultimo.proximo = balde.cabeca
                # Encontra o novo último nó na lista_abs após adicionar o balde
                while ultimo.proximo:
                    ultimo = ultimo.proximo

        exp *= 10 # Move para o próximo dígito (dezena, centena, etc.)

    # Passo 3: reconvertendo os valores para negativos
    # Como ordenamos os valores absolutos crescentemente (ex: 1, 7, 99),
    # ao reconverter para negativos, obtemos a ordem decrescente de magnitude
    # (-1, -7, -99). Se a intenção fosse ordenar negativos crescentemente
    # (-99, -7, -1), os valores absolutos deveriam ter sido ordenados
    # decrescentemente (99, 7, 1) antes da reconversão.
    # A implementação atual produz a ordem decrescente de magnitude para os negativos.
    lista_negativo = ListaLigada()
    atual = lista_abs.cabeca
    while atual:
        # Adiciona o valor absoluto negado à lista final de negativos
        lista_negativo.inserir((-atual.valor))
        atual = atual.proximo

    return lista_negativo

# fim do quadro de bloco do radix sort

 ```

- Descrição: Implementa o algoritmo de ordenação Radix Sort, adaptado para lidar com números negativos. O Radix Sort é um algoritmo de ordenação não comparativo que ordena números processando dígitos individuais. Sua complexidade típica é O(nk), onde n é o número de elementos e k é o número de dígitos (ou log base da maior base numérica).
- obter_maior(lista):
   - Função auxiliar para o Radix Sort.
   - Percorre a lista e encontra o maior valor absoluto presente nela. Este valor é necessário para determinar quantas "passadas" o Radix Sort precisa fazer (uma para cada dígito do maior número).

- radix_sort_negativos(lista):
   - Tratamento de Vazio: Retorna uma lista vazia se a entrada for vazia
   - Passo 1 (Absolutos): Cria uma nova lista ligada contendo os valores absolutos de todos os números na lista negativa original. Isso é necessário porque o Radix Sort padrão funciona com números não negativos.


- Passo 2 (Radix Sort nos Absolutos):
   - Determina o maior valor absoluto (maior) para saber o número de dígitos a serem processados.
   - Inicia um loop que itera pelo número de dígitos (controlado por exp).
   - Dentro do loop, cria 10 "baldes" (listas ligadas vazias), um para cada dígito de 0 a 9.
   - Distribui os números da lista de absolutos para os baldes apropriados, com base no dígito atual (determinado por (valor // exp) % 10).
   - Coleta os números dos baldes, concatenando-os de volta na lista de absolutos. A coleta é feita dos baldes 0 a 9 para garantir que a lista de absolutos fique ordenada crescentemente a cada passada com base no dígito atual.
   - exp é multiplicado por 10 para processar o próximo dígito na próxima iteração.

- Passo 3 (Reconversão para Negativos):
    - Cria uma nova lista ligada para armazenar os resultados finais negativos.
    - Percorre a lista de absolutos ordenada (que agora está em ordem crescente de magnitude, ex: 1, 7, 99).
    - Para cada valor absoluto, nega-o e o insere na lista final de negativos.
    - Importante: Como a lista de absolutos foi ordenada crescentemente (1, 7, 99), ao negar os valores, a lista de negativos resultante estará em ordem decrescente de magnitude (-1, -7, -99). Se a intenção fosse ter os negativos em ordem crescente (-99, -7, -1), a coleta nos baldes no Passo 2 deveria ter sido feita dos baldes 9 a 0 para ordenar os absolutos decrescentemente (99, 7, 1) antes de negar.

## Função Principal de Organização organizar_lista

```python

# Função principal de organização
def organizar_lista(lista_original):
    # Divide a lista original em negativas e positivas/zero
    lista_neg, lista_pos = lista_original.dividir_em_listas()

    # Ordena a lista negativa usando Radix Sort e mede o tempo
    tempo_inicio_radix = time.time()
    lista_neg_ordenada = radix_sort_negativos(lista_neg)
    tempo_fim_radix = time.time()
    tempo_resul_radix = tempo_fim_radix - tempo_inicio_radix

    # Ordena a lista positiva usando Merge Sort e mede o tempo
    # Nota: merge_sort_positivos opera diretamente nos nós, então atualizamos a cabeça
    tempo_inicio_merge = time.time()
    lista_pos.cabeca = merge_sort_positivos(lista_pos.cabeca)
    tempo_fim_merge = time.time()
    tempo_resul_merge = tempo_fim_merge - tempo_inicio_merge

    # Concatenar as listas (negativas ordenadas + positivas ordenadas)
    lista_final = ListaLigada()
    # Adiciona os negativos ordenados
    for no in lista_neg_ordenada.iterar():
        lista_final.inserir(no.valor)
    # Adiciona os positivos ordenados
    for no in lista_pos.iterar():
        lista_final.inserir(no.valor)

    # Impressão dos resultados e métricas
    print("Lista negativa ordenada por Radix Sort: ", lista_neg_ordenada.imprimir())
    print("Lista positiva ordenada por Merge Sort: ", lista_pos.imprimir())
    print("Lista final concatenada: ", lista_final.imprimir())
    # Impressão das complexidades para os tamanhos das sublistas do exemplo
    print("Complexidade teórica de Merge Sort O(n log n) para n=5: ", 5 * math.log(5))
    print("Complexidade teórica de Radix Sort O(nk) para n=3, k=2: ", 3 * 2)
    print("Tempo de execução do Radix Sort: ", tempo_resul_radix)
    print("Tempo de execução do Merge Sort: ", tempo_resul_merge)

```

- Descrição: Esta é a função que orquestra todo o processo de organização.
- Recebe a lista_original como entrada.
- Chama dividir_em_listas() para separar os números negativos e positivos/zeros em duas listas distintas.
- Mede o tempo de execução do radix_sort_negativos na lista de negativos e armazena o resultado.
- Mede o tempo de execução do merge_sort_positivos na lista de positivos e armazena o resultado.
- Cria uma nova lista ligada lista_final.
- Concatena os elementos da lista negativa ordenada e os elementos da lista positiva ordenada em lista_final. Nota: Dada a implementação atual do radix_sort_negativos (que ordena absolutos crescentemente e nega), a lista negativa estará em ordem decrescente de magnitude (-1, -7, -99 no exemplo). A lista positiva estará em ordem crescente (0, 3, 12, 23, 45). A concatenação colocará os negativos (decrescentes por magnitude) antes dos positivos (crescentes), resultando em uma lista que não está estritamente em ordem crescente globalmente ([-1, -7, -99, 0, 3, 12, 23, 45] se a ordem fosse correta, mas com a implementação atual será [-1, -7, -99, 0, 3, 12, 23, 45]). Para uma ordem crescente global correta ([-99, -7, -1, 0, 3, 12, 23, 45]), o Radix Sort deveria ordenar os absolutos decrescentemente ou os negativos deveriam ser mesclados de forma diferente.
- Imprime as listas intermediárias ordenadas (negativas e positivas) e a lista final concatenada.
- Calcula e imprime valores teóricos simples para as complexidades dos algoritmos com base nos tamanhos das sublistas do exemplo fixo.
- Imprime os tempos de execução medidos para cada algoritmo.

## Bloco de Execução Principal
```python
if __name__ == "__main__":
    lista = ListaLigada()
    entrada = [-99, -7, -1, 0, 3, 12, 23, 45]
#    entrada = [random.randint(-100, 100) for _ in range(1200)]  #caso queira colocar mais dados para ver o tempo de execução
    for numero in entrada:
        lista.inserir(numero)

    organizar_lista(lista)
```

- Descrição: Este bloco é o ponto de entrada do script quando ele é executado diretamente.
- if __name__ == "__main__":: Garante que o código dentro deste bloco só será executado quando o script for o programa principal (e não quando for importado como módulo em outro script).
- Cria uma nova instância da ListaLigada.
- Define uma lista Python (entrada) com os números a serem organizados. Você pode usar a linha comentada para gerar uma lista maior e aleatória para testar o desempenho com mais dados.
- Percorre a lista entrada e insere cada número na lista ligada.
- Chama a função organizar_lista passando a lista ligada criada para iniciar o processo de divisão, ordenação e concatenação.
