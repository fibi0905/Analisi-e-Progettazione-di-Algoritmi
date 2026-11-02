INF= float('inf')
NULL = None

def leggi_grafo(nome_file):
    """
    Legge il grafo da un file ASCII.
    Formato:
    - Prima riga: N (numero di nodi)
    - Righe successive: u v costo
    """
    with open(nome_file, 'r') as f:
        linee = f.read().splitlines()
    
    if not linee:
        return 0, {}

    # N: numero di nodi (indicizzati implicitamente da 0 a N-1)
    N = int(linee[0].strip())
    
    # Inizializzazione della struttura dati a liste di adiacenza
    # G[u] conterrà una lista di tuple (vicino, costo)
    G = {i: [] for i in range(N)}
    
    # Lettura della sequenza di archi con costo
    for linea in linee[1:]:
        linea = linea.strip()
        if not linea:
            continue
        parti = linea.split()
        u = int(parti[0])
        v = int(parti[1])
        costo = float(parti[2])
        
        # Sendo il grafo non orientato, l'arco va inserito in entrambe le liste
        G[u].append((v, costo))
        G[v].append((u, costo))
    
    return N, G

def scrivi_output(nome_file, N, parent, G):
    """
    Scrive l'albero di ricoprimento minimo su file nello stesso formato di input.
    """
    with open(nome_file, 'w') as f:
        # Scrive il numero di nodi
        f.write(f"{N}\n")
        
        # Ricostruisce gli archi dell'MST usando il vettore dei parent
        for v in range(N):
            u = parent[v]
            if u is not None:
                # Cerca il costo dell'arco (u, v) nelle liste di adiacenza
                costo = next(c for vicino, c in G[u] if vicino == v)
                f.write(f"{u} {v} {costo}\n")

def algoritmo_prim(N, G, s=0):
    visit= [False]*N
    dist = [INF] * N
    
    parents= [NULL] *N

    parents[s]= NULL
    dist[s]=0
    Q=heapdict()

    for u in G:
        Q[u] = dist[u]


    while Q:
       u, Pu = Q.popitem()
       visit[u] = True
       for v, costo in G[u]:
           if not visit [v] and costo < dist[v]:
               parents[v]=u
               dist[v]=costo
               Q[v] = dist[v]

    return parents

