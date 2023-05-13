import visualizacao;
from rede_knn import grafo_knn;
from busca import bfs;

def main() -> None:
    grafo = grafo_knn(100, 7);
    resultado = bfs(grafo, grafo.vertices[0], grafo.vertices[5]);
    visualizacao.init((800, 640), "Reden kNN");
    visualizacao.loop(grafo, resultado);
    visualizacao.quit();


if __name__ == '__main__':
    main();