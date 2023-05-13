class Vertice:

    def __init__(self, dado: any) -> None:
        self.dado = dado;

    def __str__(self) -> str:
        return self.dado.__str__();

    def __hash__(self) -> int:
        return hash(self.dado);

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.dado == other.dado;

class Aresta:
    def __init__(self, destino: Vertice, peso: float) -> None:
        self.destino = destino;
        self.peso = peso;

    def __str__(self) -> str:
        return f'{self.destino} {self.peso}';


    def __eq__(self, other):
        if isinstance(other, Aresta):
            return self.destino == other.destino;

class Grafo:

    def __init__(self) -> None:
        self.vertices: list[Vertice] = [];
        self.arestas: dict[Vertice, list[Vertice]] = {};

    def adiciona_vertice(self, vertice: Vertice) -> None:
        if vertice not in self.vertices:
            self.vertices.append(vertice);
            self.arestas[vertice] = [];

    def adiciona_aresta(self, origem: Vertice, destino: Vertice, peso: float) -> None:
        aresta = Aresta(destino, peso);
        if aresta not in self.arestas[origem]:
            self.arestas[origem].append(aresta);

    def vertices_conectados(self, origem: Vertice) -> list[Vertice]:
        arestas = self.arestas.get(origem, []);
        vertices = [];
        for aresta in arestas:
            vertices.append(aresta.destino);
        return vertices;

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
                string += self.vertices.index(aresta.destino).__str__() + ': ' + aresta.destino.__str__() + '\n';

        return string;