import visualizacao;
from rede_knn import grafo_knn;
from busca import bfs, dfs, dijkstra, a_estrela, best_first;
import time;

def main() -> None:
    grafo = grafo_knn(2000, 3);
    a = time.time()
    resultado = best_first(grafo, grafo.vertices[0], grafo.vertices[36]);
    print(time.time() - a)
    visualizacao.init((800, 640), "Reden kNN");
    visualizacao.loop(grafo, resultado);
    visualizacao.quit();


if __name__ == '__main__':
    main();