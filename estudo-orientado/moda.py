import statistics

# Exemplo do Slide (Pág. 11): Idades de funcionários
idades = [16, 22, 23, 28, 29, 29, 30, 30, 31, 35, 37, 40, 43, 55]

try:
    moda = statistics.mode(idades)
    print(f"A moda das idades: {moda}")
except statistics.StatisticsError:
    print("A amostra e amodal ou multimodal.")

# Para encontrar múltiplas modas (Multimodal):
todas_as_modas = statistics.multimode(idades)
print(f"Modas encontradas: {todas_as_modas}")