from grafo import Grafo, Vertice;
from rede_knn import distancia_euclidiana;

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

    vertices_para_visitar = [origem];

    visitados = [origem];
    
    predecessores = {};
    predecessores[origem] = -1;
        
    while vertices_para_visitar:
        vertice_atual = vertices_para_visitar.pop(0);
        conectados = grafo.vertices_conectados(vertice_atual);

        for conectado in conectados:
            
            if conectado not in visitados:
                predecessores[conectado] = vertice_atual;
                visitados.append(conectado);
                vertices_para_visitar.append(conectado);
            
            if conectado == destino:
                caminho = predecessores_para_caminho(predecessores, destino);
                return caminho;
    return None;

def dfs(grafo: Grafo, origem: Vertice, destino: Vertice):
    if origem == destino:
        return [origem];

    vertices_para_visitar = [origem];

    visitados = [origem];
    
    predecessores = {};
    predecessores[origem] = -1;
        
    while vertices_para_visitar:
        vertice_atual = vertices_para_visitar.pop();
        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            
            if conectado not in visitados:
                print(grafo.vertices.index(vertice_atual), grafo.vertices.index(conectado))
                predecessores[conectado] = vertice_atual;
                visitados.append(conectado);
                vertices_para_visitar.append(conectado);
            
            if conectado == destino:
                caminho = predecessores_para_caminho(predecessores, destino);
                return caminho;
    return None;

def dijkstra(grafo: Grafo, origem: Vertice, destino: Vertice):
    distancias = {};
    predecessores = {};
    fila = [];

    for vertice in grafo.vertices:
        distancias[vertice] = float('inf');
        predecessores[vertice] = -1;
        fila.append(vertice);

    distancias[origem] = 0;

    while fila:
        vertice_atual = min(fila, key=lambda v: distancias[v]);

        if (vertice_atual == destino):
            return predecessores_para_caminho(predecessores, destino);

        fila.remove(vertice_atual);

        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            nova_distancia = distancias[vertice_atual] + grafo.peso(vertice_atual, conectado);
            if nova_distancia < distancias[conectado]:
                distancias[conectado] = nova_distancia;
                predecessores[conectado] = vertice_atual;

def heuristica(origem: Vertice, destino: Vertice):
    return distancia_euclidiana(origem.dado, destino.dado);

def a_estrela(grafo: Grafo, origem: Vertice, destino: Vertice):
    distancias_reais = {};
    distancias_estimadas = {};
    predecessores = {};
    fila = [origem];

    for vertice in grafo.vertices:
        distancias_reais[vertice] = float('inf');
        distancias_estimadas[vertice] = float('inf');
        predecessores[vertice] = -1;

    distancias_reais[origem] = 0;
    distancias_estimadas[origem] = heuristica(origem, destino);

    while fila:
        vertice_atual = min(fila, key=lambda v: distancias_estimadas[v]);

        if (vertice_atual == destino):
            return predecessores_para_caminho(predecessores, destino);

        fila.remove(vertice_atual);

        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            nova_distancia = distancias_reais[vertice_atual] + grafo.peso(vertice_atual, conectado);
            if nova_distancia < distancias_reais[conectado]:
                distancias_reais[conectado] = nova_distancia;
                distancias_estimadas[conectado] = nova_distancia + heuristica(conectado, destino);
                predecessores[conectado] = vertice_atual;

                if conectado not in fila:
                    fila.append(conectado);