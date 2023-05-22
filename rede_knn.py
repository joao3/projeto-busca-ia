from grafo import Vertice, Aresta, Grafo;
from random import randint, seed;
from time import time;
from math import sqrt;
import heapq

def gera_vertices(n: int) -> list[Vertice]:
    # Semente para o gerador de valores aleatórios.
    seed(1225);

    vertices = [];

    # Gera n vértices, com o dado sendo um ponto, onde x e y são valores aleatórios de 0 até 2000.
    for _ in range(0, n):
        x = randint(0, n);
        y = randint(0, n);
        vertices.append(Vertice((x,y)));

    return vertices;

def distancia_euclidiana(a: tuple[int, int], b: tuple[int, int]) -> float:
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2);

def gera_arestas(vertices: list[Vertice], k: int) -> list[tuple[Vertice, Vertice, float]]:
    arestas = [];
    for i, vertice_a in enumerate(vertices):
        distancias = [];
        for j, vertice_b in enumerate(vertices):
            # Se i != j, calcula a distancia entre o i-esimo e o j-esimo vertice.
            if i != j:
                # Vetor distancia = [vertice-j, distancia entre vertice i e vertice j].
                distancia = distancia_euclidiana(vertice_a.dado, vertice_b.dado);
                distancias.append((vertice_b, distancia));
    
        # Pega os k vértices com as menores distâncias até o vértice-i.
        menores_distancias = heapq.nsmallest(k, distancias, lambda distancia: distancia[1]);
        
        # Adiciona ao vetor de arestas, as triplas (vertice_origem, vertice_destino, distancia).
        for distancia in menores_distancias:
            arestas.append((vertice_a, distancia[0], distancia[1]));
            arestas.append((distancia[0], vertice_a, distancia[1]));

    return arestas;

def gera_rede_knn(n: int, k: int) -> tuple[list[Vertice], list[tuple[Vertice, Vertice, float]]]:
    # Gera os vértices e as arestas para os parâmetros n e k.
    lista_vertices = gera_vertices(n);
    lista_arestas = gera_arestas(lista_vertices, k);
    return lista_vertices, lista_arestas;

def grafo_knn(n: int, k: int) -> Grafo:
    # Pega os vertices e as arestas e adiciona em um grafo.
    vertices, arestas = gera_rede_knn(n, k);

    grafo = Grafo();

    for vertice in vertices:
        grafo.adiciona_vertice(vertice);

    for aresta in arestas:
        grafo.adiciona_aresta(aresta[0], aresta[1], aresta[2]);

    return grafo;