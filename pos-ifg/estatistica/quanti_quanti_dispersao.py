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
df = df.dropna(subset=['Schooling', 'Life_expectancy'])

# Grafico de dispersao usando a paleta Set2
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(
    data=df,
    x='Schooling',
    y='Life_expectancy',
    color=sns.color_palette('Set2')[0],
    s=25,
    alpha=0.9,
    ax=ax
)

# Linha de regressao linear para evidenciar a tendencia de correlacao
sns.regplot(
    data=df,
    x='Schooling',
    y='Life_expectancy',
    scatter=False,
    ci=None,
    line_kws={'color': sns.color_palette('Set2')[1], 'linewidth': 2},
    ax=ax
)

# Labels
ax.set_title(
    'Relação entre Escolaridade e Expectativa de Vida\n'
    'X: Média de anos de educação formal (25+ anos) | '
    'Y: Expectativa média de vida (ambos os sexos)',
    fontsize=14,
    fontweight='bold',
    pad=20
)

ax.set_xlabel('Média de anos de educação formal (25+ anos)', fontsize=12, fontweight='bold')
ax.set_ylabel('Expectativa média de vida (ambos os sexos)', fontsize=12, fontweight='bold')

# Pearson
r = df['Schooling'].corr(df['Life_expectancy'], method='pearson')
print(f'Correlação de Pearson: {r:.4f}')

plt.tight_layout()
plt.show()