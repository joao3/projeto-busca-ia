class Vertice:
    
    # Construtor do vertice, recebe um dado.
    def __init__(self, dado: any) -> None:
        self.dado = dado;

    # To string, utilizado para imprimir um vértice.
    def __str__(self) -> str:
        return self.dado.__str__();

    # Possibilita utilizar um vértice como chave em um dicionário.
    def __hash__(self) -> int:
        return hash(self.dado);

    # Faz com que comparações entre dois vértices sejam feitas pelos seus valores e não referências.
    def __eq__(self, other) -> bool:
        if isinstance(other, Vertice):
            return self.dado == other.dado;
    
        return False;

class Aresta:

    # Construtor da aresta, recebe um vértice de destino e um peso.
    def __init__(self, destino: Vertice, peso: float) -> None:
        self.destino = destino;
        self.peso = peso;

    # To string, utilizado para imprimir uma aresta.
    def __str__(self) -> str:
        return f'{self.destino} {self.peso}';

    # Faz com que comparações entre duas arestas sejam feitas pelos seus valores e não referências.
    def __eq__(self, other):
        if isinstance(other, Aresta):
            return self.destino == other.destino;

class Grafo:

    # Construtor de um grafo, cria ele vazio.
    def __init__(self) -> None:
        # Lista de vértices.
        self.vertices: list[Vertice] = [];
        # Dicionário de arestas. arestas[v] = lista de arestas que saem do vértice v.
        self.arestas: dict[Vertice, list[Aresta]] = {};

    def adiciona_vertice(self, vertice: Vertice) -> None:
        # Se o vértice não existir no grafo, adiciona ele e uma lista vazia no dicionário de arestas.
        if vertice not in self.vertices:
            self.vertices.append(vertice);
            self.arestas[vertice] = [];

    def adiciona_aresta(self, origem: Vertice, destino: Vertice, peso: float) -> None:
        # Cria a aresta a partir do destino e do peso.
        aresta = Aresta(destino, peso);
        # Se a aresta não for repetida, adiciona ela no dicionário.
        if aresta not in self.arestas[origem]:
            self.arestas[origem].append(aresta);

    def vertices_conectados(self, origem: Vertice) -> list[Vertice]:
        # Pega a lista dos vértices que estão conectados ao vértice origem (através da lista arestas[origem]).
        arestas = self.arestas.get(origem, []);
        vertices = [];
        for aresta in arestas:
            vertices.append(aresta.destino);
        return vertices;

    def peso(self, origem: Vertice, destino: Vertice) -> float:
        # Retorna o peso da aresta entre os vértices origem e destino.
        for aresta in self.arestas[origem]:
            if aresta.destino == destino:
                return aresta.peso;
        return None;

    # To string, utilizado para imprimir as informações do grafo.
    def __str__(self) -> str:
        string = '';
        string += '=' * 50 + '\n';
        string += 'Vértices'.center(50) + '\n';
        string += '=' * 50 + '\n';
        for vertice in self.vertices:
            string += self.vertices.index(vertice).__str__() + ': ' + vertice.__str__() + '\n';
        
        string += '=' * 50 + '\n';
        string += 'Arestas'.center(50) + '\n';
        string += '=' * 50 + '\n';
        for origem, arestas in self.arestas.items():
            for aresta in arestas:
                string += self.vertices.index(origem).__str__()  + ': ' + origem.__str__() + ' -> ';
                string += self.vertices.index(aresta.destino).__str__() + ': ' + aresta.destino.__str__() + ' Peso: ' + f'{aresta.peso:.2f}' + '\n';

        return string;
