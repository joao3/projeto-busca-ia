from grafo import Grafo, Vertice;
from rede_knn import distancia_euclidiana;
from time import time;

def predecessores_para_caminho(grafo, predecessores, destino):
    # Reconstrói o caminho percorrido através do dicionário de predecessores.
    caminho = [destino];
    predecessor = predecessores[destino];

    distancia = grafo.peso(predecessor, destino);

    # Enquanto houver vértice predecessor, adiciona ele na lista de caminho.
    while predecessor != -1:
        caminho.append(predecessor);
        if predecessores[predecessor] != -1:
            distancia += grafo.peso(predecessor, predecessores[predecessor]);
        predecessor = predecessores[predecessor];
    
    # Reverte a lista (começamos a montar de trás pra frente).
    caminho.reverse();
    return caminho, distancia;

def bfs(grafo: Grafo, origem: Vertice, destino: Vertice):
    t0 = time();

    # Se a origem é igual o destino, já achou.
    if origem == destino:
        return [origem], 0, time() - t0;

    # Lista de vértices visitados e fila de vértices para visitar, começam com a origem.
    vertices_para_expandir = [origem];
    visitados = [origem];
    
    # Predecessor da origem não existe (usado como critério de parada na função de construção do caminho).
    predecessores = {};
    predecessores[origem] = -1;
        
    # Enquanto houver vértices para visitar.
    while vertices_para_expandir:
        # Pega o primeiro vértice da fila e os vértices conectados a ele.
        vertice_atual = vertices_para_expandir.pop(0);
        conectados = grafo.vertices_conectados(vertice_atual);

        for conectado in conectados:
            # Se o vértice conectado ainda não foi visitado, 
            #   seta seu predecessor como o vértice atual, marca como visitado e adiciona ele na fila.
            if conectado not in visitados:
                predecessores[conectado] = vertice_atual;
                visitados.append(conectado);
                vertices_para_expandir.append(conectado);
            
            # Se o vértice conectado for igual ao destino, achou o caminho.
            if conectado == destino:
                caminho, distancia = predecessores_para_caminho(grafo, predecessores, destino);
                return caminho, distancia, time() - t0;

    # Não existe caminho.
    return None;

def dfs(grafo: Grafo, origem: Vertice, destino: Vertice):
    t0 = time();

    # Se a origem é igual o destino, já achou.
    if origem == destino:
        return [origem], 0, time() - t0;

    # Lista de vértices visitados e pilha de vértices para visitar, começam com a origem.
    vertices_para_expandir = [origem];
    visitados = [origem];
    
    # Predecessor da origem não existe (usado como critério de parada na função de construção do caminho).
    predecessores = {};
    predecessores[origem] = -1;
        
    # Enquanto houver vértices para visitar.
    while vertices_para_expandir:
        # Pega o primeiro vértice no topo da pilha e os vértices conectados a ele.
        vertice_atual = vertices_para_expandir.pop();
        conectados = grafo.vertices_conectados(vertice_atual);

        for conectado in conectados:
            # Se o vértice conectado ainda não foi visitado, 
            #   seta seu predecessor como o vértice atual, marca como visitado e adiciona ele na fila.
            if conectado not in visitados:
                predecessores[conectado] = vertice_atual;
                visitados.append(conectado);
                vertices_para_expandir.append(conectado);
        
            # Se o vértice conectado for igual ao destino, achou o caminho.
            if conectado == destino:
                caminho, distancia = predecessores_para_caminho(grafo, predecessores, destino);
                return caminho, distancia, time() - t0;

    # Não existe caminho.
    return None;

def dijkstra(grafo: Grafo, origem: Vertice, destino: Vertice):
    t0 = time();

    # distancias[v] = distância da origem até o vértice v. 
    distancias = {};

    predecessores = {};
    vertices_para_expandir = [];

    # Inicia todas as distâncias como infinitas, seta predecessores e adiciona os vértices na lista vertices_para_expandir.
    for vertice in grafo.vertices:
        distancias[vertice] = float('inf');
        predecessores[vertice] = -1;
        vertices_para_expandir.append(vertice);

    # Distancia da origem até ela mesma é zero.
    distancias[origem] = 0;

    # Enquanto houver vértices na lista vertices_para_expandir.
    while vertices_para_expandir:
        # Pega o vértice com menor distância.
        vertice_atual = min(vertices_para_expandir, key=lambda v: distancias[v]);

        # Achou o caminho.
        if (vertice_atual == destino):
            caminho, distancia = predecessores_para_caminho(grafo, predecessores, destino);
            return caminho, distancia, time() - t0;

        # Remove vértice atual da lista vertices_para_expandir.
        vertices_para_expandir.remove(vertice_atual);

        # Para todos os vértices conectados com o vértice atual.
        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            # A nova distânicia é a distância da origem até o nó atual + distância do nó atual até o conectado.
            nova_distancia = distancias[vertice_atual] + grafo.peso(vertice_atual, conectado);
            # Se a nova distância for menor, atualiza os valores.
            if nova_distancia < distancias[conectado]:
                distancias[conectado] = nova_distancia;
                predecessores[conectado] = vertice_atual;

    # Nâo existe caminho.
    return None;

def heuristica(origem: Vertice, destino: Vertice):
    return distancia_euclidiana(origem.dado, destino.dado);

def a_estrela(grafo: Grafo, origem: Vertice, destino: Vertice):
    t0 = time();

    # distancias_reais[v] = distância da origem até o vértice v. 
    distancias_reais = {};
    # distancias_estimadas[v] = distancia da origem até o vértice v + estimativa (heurística) de v até o destino.
    distancias_estimadas = {};

    predecessores = {};
    vertices_para_expandir = [origem];

    # Inicia todas as distâncias como infinitas e seta predecessores.
    for vertice in grafo.vertices:
        distancias_reais[vertice] = float('inf');
        distancias_estimadas[vertice] = float('inf');
        predecessores[vertice] = -1;

    distancias_reais[origem] = 0;
    distancias_estimadas[origem] = heuristica(origem, destino);

    while vertices_para_expandir:
        # Pega o vértice mais promissor (segundo a heurística).
        vertice_atual = min(vertices_para_expandir, key=lambda v: distancias_estimadas[v]);

        # Achou o caminho.
        if (vertice_atual == destino):
            caminho, distancia = predecessores_para_caminho(grafo, predecessores, destino);
            return caminho, distancia, time() - t0;

        vertices_para_expandir.remove(vertice_atual);

        # Para todos os vértices conectados com o vértice atual.
        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            # A nova distânicia é a distância da origem até o nó atual + distância do nó atual até o conectado.
            nova_distancia = distancias_reais[vertice_atual] + grafo.peso(vertice_atual, conectado);
            # Se a nova distância for menor, atualiza os valores.
            if nova_distancia < distancias_reais[conectado]:
                distancias_reais[conectado] = nova_distancia;
                distancias_estimadas[conectado] = nova_distancia + heuristica(conectado, destino);
                predecessores[conectado] = vertice_atual;

                if conectado not in vertices_para_expandir:
                    vertices_para_expandir.append(conectado);
    
    # Não existe caminho.
    return None;

def best_first(grafo: Grafo, origem: Vertice, destino: Vertice):
    t0 = time();

    # estimativas[v] = heurística do vértice v até o destino. 
    estimativas = {};

    predecessores = {};
    vertices_para_expandir = [origem];
    visitados = [origem];

    # Inicia todas as estimativas como infinitas, seta predecessores e adiciona os vértices na vertices_para_expandir.
    for vertice in grafo.vertices:
        estimativas[vertice] = float('inf');
        predecessores[vertice] = -1;

    # Heurística da origem até o destino.
    estimativas[origem] = heuristica(origem, destino);

    # Enquanto houver vértices na vertices_para_expandir.
    while vertices_para_expandir:
        # Pega o vértice com menor estimativa.
        vertice_atual = min(vertices_para_expandir, key=lambda v: estimativas[v]);

        # Achou o caminho.
        if (vertice_atual == destino):
            caminho, distancia = predecessores_para_caminho(grafo, predecessores, destino);
            return caminho, distancia, time() - t0;

        # Remove vértice atual da vertices_para_expandir.
        vertices_para_expandir.remove(vertice_atual);

        # Para todos os vértices conectados com o vértice atual.
        conectados = grafo.vertices_conectados(vertice_atual);
        for conectado in conectados:
            # Se ainda não foi visitado, adiciona na vertices_para_expandir, marca como visitado e calcula sua estimativa.
            if conectado not in visitados:
                vertices_para_expandir.append(conectado);
                estimativas[conectado] = heuristica(conectado, destino);
                predecessores[conectado] = vertice_atual;
                visitados.append(conectado);

    # Nâo caminho.
    return None;