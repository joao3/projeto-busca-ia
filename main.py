import visualizacao;
from rede_knn import grafo_knn;
from busca import bfs, dfs, dijkstra;

def main() -> None:
    grafo = grafo_knn(100, 3);
    resultado = dijkstra(grafo, grafo.vertices[0], grafo.vertices[36]);
    visualizacao.init((800, 640), "Reden kNN");
    visualizacao.loop(grafo, resultado);
    visualizacao.quit();


if __name__ == '__main__':
    main();