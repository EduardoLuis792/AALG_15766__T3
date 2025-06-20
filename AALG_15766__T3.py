import sys
from functools import lru_cache
sys.setrecursionlimit(10_000)
UMBRAL = 23

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [ 3 , 0, 0, 1, 0, 1, 0, 0, 1],
    [ 1 , 1, 0, 1, 1, 1, 1, 0, 1],
    [ 0 , 1, 0, 1, 0, 0, 1, 0, 1],
    [ 1 , 1, 1, 1, 1, 1, 3, 1, 1],
    [ 3 , 0, 1, 0, 0, 0, 1, 0, 1],
    [ 1 , 1, 1, 1, 3, 1, 1, 1, 1],
    [ 1 , 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1],
]

inicio = (8, 0)
meta   = (0, 0)
direcciones = [(-1,0),(0,1),(1,0),(0,-1)]

def valor_celda(x, y):
    v = laberinto[x][y]
    return v if v in (3, 4) else 0

def imprimir_laberinto(m):
    for fila in m:
        print(" ".join(f"{str(v):>2}" for v in fila))
    print()

def imprimir_camino_sobrepuesto(m, camino):
    conjunto = set(camino)
    for i, fila in enumerate(m):
        línea = []
        for j, v in enumerate(fila):
            línea.append(" X" if (i, j) in conjunto else f"{str(v):>2}")
        print(" ".join(línea))
    print()
    
def dfs(x, y, máscara):
    if (x, y) == meta:
        return 0, [(x, y)]

    mejor_pts = -10**9
    mejor_camino = []

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 9 and 0 <= ny < 9 and laberinto[nx][ny] != 0:
            bit = 1 << (nx * 9 + ny)
            if máscara & bit:
                continue

            pts = valor_celda(nx, ny)
            sub_pts, sub_camino = dfs(nx, ny, máscara | bit)
            if sub_camino:
                total = pts + sub_pts
                if total > mejor_pts:
                    mejor_pts = total
                    mejor_camino = [(x, y)] + sub_camino

    return mejor_pts, mejor_camino

def main():
    print("\nLaberinto original:")
    imprimir_laberinto(laberinto)

    máscara_inicial = 1 << (inicio[0] * 9 + inicio[1])
    pts_restantes, camino = dfs(inicio[0], inicio[1], máscara_inicial)
    pts_totales = pts_restantes

    if camino and pts_totales >= UMBRAL:
        print(f"Ruta encontrada. Puntos Totales = {pts_totales}\n")
        print("Laberinto con camino marcado (X):")
        imprimir_camino_sobrepuesto(laberinto, camino)
    else:
        print(f" No hay ruta con ≥ {UMBRAL} puntos (máx encontrado = {pts_totales}).")

if __name__ == "__main__":
    main()












