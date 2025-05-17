# CP2-DynamicProgramming

# Organizador de Dados em Lista Ligada 

## Descrição
Este projeto implementa um sistema para organizar números inteiros armazenados em uma estrutura de lista ligada customizada. A principal funcionalidade é ordenar os dados de acordo com critérios específicos: números positivos (incluindo zero) são ordenados usando Merge Sort, e números negativos são ordenados usando uma versão adaptada do Radix Sort.

Todo o processo de ordenação é realizado diretamente sobre a estrutura da lista ligada, sem recorrer à conversão para arrays ou listas nativas do Python. O programa também exibe as complexidades teóricas dos algoritmos de ordenação utilizados e mede o tempo real de execução para cada um deles.

## Funcionalidades
* Implementação própria de uma lista ligada simples.
* Separação dos números inteiros da lista de entrada em duas sub-listas: uma para números positivos (e zero) e outra para números negativos.
* Ordenação da lista de números positivos utilizando o algoritmo Merge Sort.
* Ordenação da lista de números negativos utilizando uma adaptação do algoritmo Radix Sort.
* Concatenação das listas ordenadas (negativos primeiro, seguidos pelos positivos).
* Exibição na saída padrão:
    * A lista de números negativos ordenada.
    * A lista de números positivos (e zero) ordenada.
    * A lista final completa, concatenada e ordenada.
    * A complexidade de tempo teórica do Merge Sort (O(n log n)).
    * A complexidade de tempo teórica do Radix Sort (O(nk)).
    * O tempo de execução real (em segundos) para cada algoritmo de ordenação separadamente.

## Estruturas de Dados Utilizadas
O projeto utiliza uma estrutura de lista ligada implementada manualmente:

* **Classe `No`**: Representa um nó individual da lista ligada. Cada nó armazena:
    * `valor`: O número inteiro contido no nó.
    * `proximo`: Uma referência (ponteiro) para o próximo nó na lista, ou `None` se for o último.

* **Classe `ListaLigada`**: Representa a lista ligada como um todo. Contém:
    * `cabeca`: Uma referência ao primeiro nó da lista.
    * Métodos principais:
        * `inserir(valor)`: Adiciona um novo nó com o `valor` especificado ao final da lista.
        * `iterar()`: Um gerador que permite percorrer os nós da lista.
        * `dividir_em_listas()`: Separa os nós da lista original em duas novas `ListaLigada`, uma para valores negativos e outra para valores positivos (e zero).
        * `imprimir()`: Retorna uma lista Python contendo os valores dos nós, útil para visualização.

## Algoritmos de Ordenação

### Merge Sort (para números positivos e zero)
* Implementado pela função `merge_sort_positivos(lista_cabeca)`, que recebe a cabeça da lista ligada a ser ordenada.
* É um algoritmo recursivo do tipo "dividir para conquistar":
    1.  **Dividir**: A lista é dividida ao meio repetidamente até que sub-listas contenham no máximo um elemento. A função `dividir_lista(cabeca)` utiliza a técnica de ponteiros "lento" e "rápido" para encontrar o meio da lista e dividi-la.
    2.  **Conquistar**: As sub-listas (já ordenadas) são mescladas duas a duas de forma ordenada. A função `mesclar_listas(esquerda, direita)` realiza essa mesclagem.
* Toda a operação é feita manipulando os ponteiros dos nós da lista ligada.

### Radix Sort (adaptado para números negativos)
* Implementado pela função `radix_sort_negativos(lista_obj)`, que recebe um objeto `ListaLigada` contendo os números negativos.
* **Adaptação para Ordenação de Negativos em Ordem Ascendente (ex: -99, -7, -1):**
    1.  **Valores Absolutos**: Inicialmente, uma nova lista ligada (`lista_abs`) é criada contendo os valores absolutos dos números negativos (ex: de `[-7, -1, -99]` para `[7, 1, 99]`).
    2.  **Radix Sort Descendente nos Absolutos**: A `lista_abs` é ordenada usando o Radix Sort (LSD - Least Significant Digit). Para que, após a negação, os números fiquem em ordem ascendente (ex: -99, -7, -1), os valores absolutos precisam ser ordenados em ordem *descendente* (ex: `[99, 7, 1]`). Isso é alcançado durante a etapa de coleta dos `baldes` (buckets): os elementos são coletados dos buckets na ordem inversa (do bucket 9 para o bucket 0).
    3.  **Reversão do Sinal**: Após a `lista_abs` estar ordenada de forma descendente, uma nova lista final de negativos é criada, onde cada valor é o negativo do valor correspondente na `lista_abs` ordenada (ex: de `[99, 7, 1]` para `[-99, -7, -1]`).
* **Detalhes da Implementação do Radix Sort:**
    * A função `obter_maior(lista_abs_obj)` é usada para encontrar o maior valor absoluto, determinando o número de dígitos e, consequentemente, o número de passadas do Radix Sort.
    * Em cada passada (para cada dígito, do menos significativo para o mais significativo):
        * Dez `baldes` (buckets), cada um sendo uma `ListaLigada`, são criados para representar os dígitos de 0 a 9.
        * Os nós da `lista_abs` são distribuídos nos `baldes` de acordo com o dígito correspondente na passada atual.
        * A `lista_abs` é reconstruída coletando os nós dos `baldes`. Como mencionado, para a ordenação descendente dos valores absolutos, a coleta é feita do `balde[9]` para o `balde[0]`.

## Estrutura do Código
O código está organizado da seguinte forma:

* **`No`**: Classe para os nós da lista.
* **`ListaLigada`**: Classe para a lista ligada e suas operações básicas.
* **Funções do Merge Sort**:
    * `merge_sort_positivos(lista_cabeca)`
    * `dividir_lista(cabeca)`
    * `mesclar_listas(esquerda, direita)`
* **Funções do Radix Sort**:
    * `radix_sort_negativos(lista_obj)`
    * `obter_maior(lista_abs_obj)`
* **Função Principal de Organização**:
    * `organizar_lista(lista_original_obj)`: Orquestra todo o fluxo de separação, medição de tempo, chamada dos algoritmos de ordenação, concatenação e impressão dos resultados.
* **Bloco de Execução Principal (`if __name__ == "__main__":`)**:
    * Cria uma lista ligada de exemplo com números inteiros.
    * Chama `organizar_lista` para processar e exibir os resultados.

## Como Executar o Código
1.  Salve o código Python em um arquivo (por exemplo, `organizador_dados.py`).
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde o arquivo foi salvo.
4.  Execute o script com o comando:
    ```bash
    python organizador_dados.py
    ```

## Entrada
A entrada de dados é uma lista de números inteiros, atualmente definida diretamente no código dentro do bloco `if __name__ == "__main__":`:
```python
entrada = [-99, -7, -1, 0, 3, 12, 23, 45]
