from grafo import Vertice, Aresta, Grafo;
from random import randint, seed;
from time import time;
from math import sqrt;
import heapq

def gera_vertices(n: int) -> list[tuple[int, int]]:
    seed(1225);

    vertices = [];

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
            if i != j:
                distancia = distancia_euclidiana(vertice_a.dado, vertice_b.dado);
                distancias.append((vertice_b, distancia));
    
        menores_distancias = heapq.nsmallest(k, distancias, lambda distancia: distancia[1]);
        
        for distancia in menores_distancias:
            arestas.append((vertice_a, distancia[0], distancia[1]));
            arestas.append((distancia[0], vertice_a, distancia[1]));
            

    return arestas;

def gera_rede_knn(n: int, k: int) -> tuple[list[tuple[int, int]], list[Aresta]]:
    lista_vertices = gera_vertices(n);
    lista_arestas = gera_arestas(lista_vertices, k);
    return lista_vertices, lista_arestas;

def grafo_knn(n: int, k: int) -> Grafo:
    vertices, arestas = gera_rede_knn(n, k);
    grafo = Grafo();

    for vertice in vertices:
        grafo.adiciona_vertice(vertice);

    for aresta in arestas:
        grafo.adiciona_aresta(aresta[0], aresta[1], aresta[2]);

    return grafo;