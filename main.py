import visualizacao;
from rede_knn import grafo_knn;
from busca import bfs, dfs, dijkstra, a_estrela, best_first;
from random import randint, seed;

def main() -> None:
    comparacao(2000, 3);

def comparacao(n, k):
    grafo = grafo_knn(n, k);
    
    origem, destino = gera_origem_destino(grafo, n);

    resultados = executa_buscas(grafo, origem, destino);
    
    for algoritmo, resultado in resultados.items():
        imprimir_resultado(grafo, algoritmo, resultado);

def gera_origem_destino(grafo, n):
    seed(1225);
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

    print("Caminho: ", end='');
    for vertice in resultado[0]:
        print(grafo.vertices.index(vertice), end=' '); 
    print();

    print(f'Distância: {resultado[1]:.2f}');

    print(f'Tempo: {resultado[2]:.5f} segundos');

if __name__ == '__main__':
    main();