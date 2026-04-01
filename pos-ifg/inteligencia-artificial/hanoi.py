# Modelagem do estado: Uma tupla contendo 3 tuplas (representando os pinos A, B e C)
# Exemplo inicial: ((3, 2, 1), (), ()) -> O disco 1 é o menor e está no topo.

def gerar_movimentos_validos(estado_atual):
    """
    Avalia o tabuleiro atual e retorna todos os próximos estados possíveis.
    """
    novos_estados = []
    
    # Avalia cada pino como origem
    for origem in range(3):
        if not estado_atual[origem]: 
            continue # Pino vazio, não há disco para mover
            
        disco_topo = estado_atual[origem][-1]
        
        # Avalia cada pino como destino
        for destino in range(3):
            if origem == destino:
                continue
                
            # Regra de negócio: Destino deve estar vazio OU o disco do topo deve ser maior
            if not estado_atual[destino] or estado_atual[destino][-1] > disco_topo:
                
                # Converte as tuplas para listas para podermos manipular (pop e append)
                estado_temp = [list(pino) for pino in estado_atual]
                
                # Executa o movimento
                disco_movido = estado_temp[origem].pop()
                estado_temp[destino].append(disco_movido)
                
                # Converte de volta para tupla (imutável) para poder salvar no SET de visitados
                novo_estado = tuple(tuple(pino) for pino in estado_temp)
                novos_estados.append(novo_estado)
                
    return novos_estados

def dfs_hanoi(estado_inicial, estado_objetivo):
    """
    Motor da Busca em Profundidade (DFS) usando Pilha (LIFO).
    """
    # A pilha armazena tuplas: (estado_atual, historico_de_caminho)
    pilha = [(estado_inicial, [estado_inicial])]
    visitados = set()
    visitados.add(estado_inicial)
    
    while pilha:
        # DFS puro: tira sempre o último elemento que entrou na pilha
        estado_atual, caminho = pilha.pop()
        
        # Objetivo alcançado?
        if estado_atual == estado_objetivo:
            return caminho
            
        # Gera e empilha os próximos passos possíveis
        for proximo_estado in gerar_movimentos_validos(estado_atual):
            if proximo_estado not in visitados:
                visitados.add(proximo_estado)
                
                # Adiciona o novo estado ao histórico de movimentos
                novo_caminho = caminho + [proximo_estado]
                pilha.append((proximo_estado, novo_caminho))
                
    return None # Retorna None se não achar solução (impossível no Hanói padrão)

# --- EXECUÇÃO E TESTE DE MESA ---

if __name__ == "__main__":
    # 3 Discos no pino 0
    inicio = ((3, 2, 1), (), ())
    # Objetivo: todos os 3 discos no pino 2
    objetivo = ((), (), (3, 2, 1))
    
    print("Iniciando varredura DFS...\n")
    solucao = dfs_hanoi(inicio, objetivo)
    
    if solucao:
        print(f"Solução encontrada em {len(solucao) - 1} movimentos!\n")
        for passo, estado in enumerate(solucao):
            print(f"Passo {passo}: Pino 1: {estado[0]} | Pino 2: {estado[1]} | Pino 3: {estado[2]}")
    else:
        print("Nenhum caminho encontrado.")