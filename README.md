# CP2-DynamicProgramming

# Projeto: Organização de Lista Ligada com Merge Sort e Radix Sort

Este projeto implementa uma solução para organizar uma lista ligada de números inteiros, utilizando dois algoritmos de ordenação distintos: Radix Sort para os números negativos e Merge Sort para os números positivos (incluindo zero).

## Como Executar

1.  Salve o código Python em um arquivo (por exemplo, `organizador_lista.py`).
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde salvou o arquivo.
4.  Execute o script usando o interpretador Python:
    ```bash
    python organizador_lista.py
    ```
5.  Os resultados da ordenação e os tempos de execução serão exibidos no console. Você pode modificar a lista `entrada` no bloco `if __name__ == "__main__":` para testar com diferentes dados ou tamanhos de lista (usando a linha comentada `random.randint`).

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
