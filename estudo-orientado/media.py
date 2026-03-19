import numpy as np

# Tempos de resposta comuns (em ms)
tempos = [45, 50, 52, 48, 47, 49, 51]


media_normal = np.mean(tempos)
print(f"Media normal: {media_normal:.2f} ms")

# 2. Inserindo um Outlier (ex: um deadlock ou lentidão na rede)
tempos_com_erro = [45, 50, 52, 48, 47, 49, 51, 1500] 
media_com_outlier = np.mean(tempos_com_erro)

print(f"Media com Outlier: {media_com_outlier:.2f} ms")