import numpy as np

# Dados com o erro (outlier de 1500ms)
tempos_com_erro = [45, 47, 48, 49, 50, 51, 52, 1500] 

# Calculando Mediana
mediana = np.median(tempos_com_erro)

print(f"Média: {np.mean(tempos_com_erro):.2f} ms")
print(f"Mediana: {mediana:.2f} ms")