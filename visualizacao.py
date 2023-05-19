import pygame;
from grafo import Grafo, Vertice, Aresta;


screen = None;
font = None;
raio_vertice = 15;
velocidade_zoom = 0.5;
max_zoom = 100
min_zoom = 0;
max_raio = 20
min_raio = 15;
escala = 30;
camera_x = 0;
camera_y = 0;


def init(size: tuple[int, int], title: str) -> None:
    pygame.init();
    global screen;
    screen = pygame.display.set_mode(size, pygame.RESIZABLE);
    global font;
    font = pygame.font.SysFont(None, 24);
    pygame.display.set_caption(title);

COR_FUNDO = (26, 34, 41);
COR_VERTICE = (67, 48, 191);
COR_ARESTA = (15, 166, 95);
COR_CAMINHO = (242, 46, 155);

def loop(grafo: Grafo, caminho = None) -> None:
    running = True;
    
    global camera_x, camera_y, escala, raio_vertice;
    dragging = False;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    dragging = True
                elif event.button == 4:
                    escala += velocidade_zoom;
                    raio_vertice += velocidade_zoom;
                    if escala > max_zoom:
                        escala = max_zoom
                    if raio_vertice > max_raio:
                        raio_vertice = max_raio;

                elif event.button == 5:
                    escala -= velocidade_zoom
                    raio_vertice -= velocidade_zoom
                    if escala < min_zoom:
                        escala = min_zoom
                    if raio_vertice < min_raio:
                        raio_vertice = min_raio;

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    dx = event.pos[0] - mouse_x
                    dy = event.pos[1] - mouse_y

                    camera_x += dx
                    camera_y += dy

                    mouse_x, mouse_y = event.pos


        screen.fill(COR_FUNDO)
        desenha_arestas(screen, grafo.arestas);

        if caminho != None:
            desenha_caminho(screen, caminho);
        
        desenha_vertices(screen, grafo.vertices);
        pygame.display.flip();


def quit() -> None:
    pygame.quit();

def desenha_vertices(screen: pygame.surface, vertices: list[Vertice]):
    global escala, camera_y, camera_x, raio_vertice;
    for i, vertice in enumerate(vertices):
        coordenada = (vertice.dado[0] * escala + camera_x, vertice.dado[1] * escala + camera_y);
        pygame.draw.circle(screen, COR_VERTICE, coordenada, raio_vertice);
        
        num_vertice = font.render(f'{i:02d}', True, (255,255,255));
        num_vertice_size = num_vertice.get_size();
        
        screen.blit(num_vertice, (coordenada[0] - num_vertice_size[0]/2, coordenada[1] - num_vertice_size[1]/2))

def desenha_arestas(screen: pygame.surface, arestas: dict[Vertice, list[Aresta]]):
    global escala, camera_y, camera_x;
    for origem, arestas in arestas.items():
        coordenada_a = (origem.dado[0] * escala + camera_x, origem.dado[1] * escala + camera_y);
        for aresta in arestas:
            coordenada_b = (aresta.destino.dado[0] * escala + camera_x, aresta.destino.dado[1] * escala + camera_y);
            pygame.draw.line(screen, COR_ARESTA, coordenada_a, coordenada_b, 2);

def desenha_caminho(screen, caminho):
    global escala, camera_y, camera_x;
    for i in range(0, len(caminho) - 1):
        coordenada_a = (caminho[i].dado[0] * escala + camera_x, caminho[i].dado[1] * escala + camera_y);
        coordenada_b = (caminho[i + 1].dado[0] * escala + camera_x, caminho[i + 1].dado[1] * escala + camera_y);
        pygame.draw.line(screen, COR_CAMINHO, coordenada_a, coordenada_b, 2);

