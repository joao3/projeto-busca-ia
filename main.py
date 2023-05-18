import visualizacao;
from rede_knn import grafo_knn;
from busca import bfs, dfs, dijkstra, a_estrela, best_first;
import time;

def main() -> None:
    grafo = grafo_knn(10, 7);
    caminho, distancia = best_first(grafo, grafo.vertices[0], grafo.vertices[3]);
    visualizacao.init((800, 640), "Reden kNN");
    visualizacao.loop(grafo, caminho);
    visualizacao.quit();


if __name__ == '__main__':
    main();