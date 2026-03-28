from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent / "arquivos" / "life_expec_alterado.csv"
df = pd.read_csv(csv_path, sep=';', decimal='.', encoding='utf-8-sig')

table1 = df[['Hepatitis_B_alt', 'Economy_status_Developed']]

df['Hepatitis_B_alt'] = df['Hepatitis_B_alt'].str.strip().str.lower()

prop_table = pd.crosstab(df['Economy_status_Developed'], df['Hepatitis_B_alt'], normalize='index')
ordem_hepatite = ['baixa', 'moderada', 'alta', 'elevada']
prop_table = prop_table.reindex(columns=ordem_hepatite, fill_value=0)

ax = prop_table.T.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set2', width=0.6)

ax.set_title('Cobertura de Imunização de Hepatite B por Status Econômico', fontsize=14, fontweight='bold')
ax.set_xlabel('Cobertura de Imunização de Hepatite B', fontsize=12)
ax.set_ylabel('Proporção', fontsize=12)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax.legend(title='Economia Desenvolvida', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout()
plt.show()