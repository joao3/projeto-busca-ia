import visualizacao;
from rede_knn import grafo_knn;
from busca import bfs, dfs, dijkstra, a_estrela, best_first;
from random import randint, seed;

def main() -> None:
    print('-' * 100);
    print('n = 100 k = 4');
    comparacao(100, 4);

    print('-' * 100);
    print('n = 2000 k = 3');
    media(2000, 3);

    print('-' * 100);
    print('n = 2000 k = 7');
    media(2000, 7);

    print('-' * 100);
    print('n = 2000 k = 11');
    media(2000, 11);

def media(n, k):
    grafo = grafo_knn(n, k);

    # Medias dos resultados.
    medias = {
        'Busca em profundidade': [0, 0, 0],
        'Busca em largura': [0, 0, 0],
        'Algoritmo Best-First': [0, 0, 0],
        'Algoritmo A*': [0, 0, 0],
        'Algoritmo de Dijkstra': [0, 0, 0]
    };

    # Gera n pares de pontos e realiza as buscas, calculando a média dos parâmetros dos resultados da busca.
    n_pontos = 10;
    seed(1225);
    # Acumula valores dos parâmetros dos resultados para cada busca, para cada par de pontos.
    for _ in range(0, n_pontos):
        origem, destino = gera_origem_destino(grafo, n);
        resultado = executa_buscas(grafo, origem, destino);
        for key in resultado.keys():
            # Quantidade de nós no caminho;
            medias[key][0] += len(resultado[key][0]);
            # Distância.
            medias[key][1] += resultado[key][1];
            # Tempo.
            medias[key][2] += resultado[key][2];

    # Divide pelo número de pontos.
    for algoritmo in medias.values():
        for i in range(0, len(algoritmo)):
            algoritmo[i] /= n_pontos;

    for nome, resultado in medias.items():
        imprimir_media(nome, resultado);

def imprimir_media(algoritmo, resultado):
    print('=' * 100);
    print(algoritmo.center(100))
    print('=' * 100);

    print(f'Média total vértices: {resultado[0]}');

    print(f'Média distância: {resultado[1]:.2f}');

    print(f'Média tempo: {resultado[2]:.6f} segundos');

def comparacao(n, k):
    # Compara os algoritmos em um par de pontos.

    grafo = grafo_knn(n, k);
    seed(1225);
    origem, destino = gera_origem_destino(grafo, n);

    resultados = executa_buscas(grafo, origem, destino);
    
    for algoritmo, resultado in resultados.items():
        imprimir_resultado(grafo, algoritmo, resultado);

def gera_origem_destino(grafo, n):
    indice_origem = randint(0, n);
    indice_destino = randint(0, n);
    while indice_origem == indice_destino:
        indice_destino = randint(0, n);
    origem = grafo.vertices[indice_origem];
    destino = grafo.vertices[indice_destino];

    return origem, destino;

def executa_buscas(grafo, origem, destino):
    resultados = {};
    resultados['Busca em profundidade'] = dfs(grafo, origem, destino);
    resultados['Busca em largura'] = bfs(grafo, origem, destino);
    resultados['Algoritmo Best-First'] = best_first(grafo, origem, destino);
    resultados['Algoritmo A*'] = a_estrela(grafo, origem, destino);
    resultados['Algoritmo de Dijkstra'] = dijkstra(grafo, origem, destino);
    return resultados;

def imprimir_resultado(grafo, algoritmo, resultado):
    print('=' * 100);
    print(algoritmo.center(100))
    print('=' * 100);

    print('Caminho: ', end='');
    for vertice in resultado[0]:
        print(grafo.vertices.index(vertice), end=' '); 
    print();
    print(f'Total vértices: {len(resultado[0])}');

    print(f'Distância: {resultado[1]:.2f}');

    print(f'Tempo: {resultado[2]:.6f} segundos');

if __name__ == '__main__':
    main();