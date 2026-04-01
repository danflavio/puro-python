import heapq

# Estado objetivo padrão do 8-puzzle (1 a 8 na ordem, 0 representa o espaço vazio)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan_distance(state):
    """Calcula a heurística: a soma das distâncias de Manhattan de cada peça até seu lugar correto."""
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        # Posição atual da peça (linha e coluna)
        current_row, current_col = divmod(i, 3)
        # Posição onde a peça deveria estar
        goal_index = GOAL.index(tile)
        goal_row, goal_col = divmod(goal_index, 3)
        # Soma a diferença absoluta das linhas e colunas
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(state):
    """Identifica onde está o espaço vazio e retorna os próximos movimentos válidos."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    # Dicionário de movimentos mapeando o nome para o deslocamento (linha, coluna)
    directions = {
        'Cima': (row - 1, col),
        'Baixo': (row + 1, col),
        'Esquerda': (row, col - 1),
        'Direita': (row, col + 1)
    }

    for move, (new_row, new_col) in directions.items():
        # Verifica se o movimento não sai do tabuleiro 3x3
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            # Cria o novo estado trocando as posições
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append((tuple(new_state), move))
    
    return neighbors

def a_star_solver(start_state):
    """Coração do algoritmo: Fila de prioridade buscando o menor custo total f(x) = g(x) + h(x)."""
    # A fila heap armazena: (custo_f, movimentos_g, estado_atual, historico_de_caminho)
    heap = [(manhattan_distance(start_state), 0, start_state, [])]
    # Set para acesso O(1) e evitar loops de estados já visitados
    visited = set([start_state])

    while heap:
        f_score, g_score, current_state, path = heapq.heappop(heap)

        # Se o estado atual é o objetivo, a busca acabou
        if current_state == GOAL:
            return path

        # Explora os vizinhos do estado atual
        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [(move, neighbor)]
                
                # Custo G: número de movimentos até o vizinho (movimentos atuais + 1)
                new_g_score = g_score + 1
                # Custo F: G (movimentos) + H (estimativa de distância de Manhattan)
                new_f_score = new_g_score + manhattan_distance(neighbor)
                
                heapq.heappush(heap, (new_f_score, new_g_score, neighbor, new_path))
    
    return None

# --- EXECUÇÃO DO PROGRAMA ---

# O estado inicial mostrado na sua imagem (0 é o quadrado lilás/vazio)
initial_state = (0, 8, 7, 6, 5, 4, 3, 2, 1)

print("Processando algoritmo A*...\n")
solution_path = a_star_solver(initial_state)

if solution_path:
    print(f"Solução otimizada encontrada! Total de {len(solution_path)} movimentos exatos.\n")
    print("-" * 30)
    for step_num, (move, state) in enumerate(solution_path, 1):
        # Formatando a tupla em uma matriz 3x3 visualmente limpa
        board = f"[{state[0]:<2} {state[1]:<2} {state[2]:<2}]\n[{state[3]:<2} {state[4]:<2} {state[5]:<2}]\n[{state[6]:<2} {state[7]:<2} {state[8]:<2}]"
        # Substitui o 0 por um espaço em branco para ficar igual ao jogo físico
        board = board.replace(" 0", "  ").replace("[0 ", "[  ")
        
        print(f"Passo {step_num} (Espaco moveu para: {move})")
        print(board)
        print("-" * 30)
else:
    print("Nenhuma solução possível encontrada para este estado inicial.")