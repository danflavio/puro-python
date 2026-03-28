from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho
base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent / "arquivos" / "life_expec_alterado.csv"

# Leitura
df = pd.read_csv(csv_path, sep=';', decimal='.', encoding='utf-8-sig')

# Remover valores nulos para as variaveis do grafico de dispersao
df = df.dropna(subset=['Incidents_HIV', 'Thinness_ten_nineteen_years'])

# Grafico de dispersao simples, com uma unica cor
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(
    data=df,
    x='Incidents_HIV',
    y='Thinness_ten_nineteen_years',
    color='black',
    s=25,
    alpha=0.9,
    ax=ax
)

# Labels
ax.set_title(
    'Incidentes de VIH vs Prevalencia de Magreza em Adolescentes',
    fontsize=14,
    fontweight='bold',
    pad=20
)

ax.set_xlabel('Incidentes de VIH por 1000 habitantes (15 a 49 anos)', fontsize=12, fontweight='bold')
ax.set_ylabel('Prevalencia de magreza (10 a 19 anos, IMC < -2 DP)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()