from grafo import Grafo, Vertice;
from queue import SimpleQueue;

def predecessores_para_caminho(predecessores, destino):
    caminho = [destino];
    predecessor = predecessores[destino];
    while predecessor != -1:
        caminho.append(predecessor);
        predecessor = predecessores[predecessor];
    caminho.reverse();
    return caminho;

def bfs(grafo: Grafo, origem: Vertice, destino: Vertice):
    if origem == destino:
        return [origem];

    vertices_para_visitar = SimpleQueue();
    vertices_para_visitar.put_nowait(origem);
    visitados = [origem];
    predecessores = {};
    predecessores[origem] = -1;
        
    while not vertices_para_visitar.empty():
        vertice_atual = vertices_para_visitar.get_nowait();
        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            
            if conectado not in visitados:
                predecessores[conectado] = vertice_atual;
                vertices_para_visitar.put_nowait(conectado);
                visitados.append(conectado);
            
            if conectado == destino:
                caminho = predecessores_para_caminho(predecessores, destino);
                return caminho;
    
    for visitado in visitados:
        print(grafo.vertices.index(visitado), end=' ');
    return None;
