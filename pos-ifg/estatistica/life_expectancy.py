from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent / "arquivos" / "life_expectancy.csv"

df = pd.read_csv(csv_path, sep=';', decimal=',', encoding='utf-8-sig')

print(df['Hepatitis_B'].describe())

print("Desvio Padrao", round(df['Hepatitis_B'].std(), 2))

amplitude = df['Hepatitis_B'].max() - df['Hepatitis_B'].min()
print("Amplitude", amplitude)

media = df['Hepatitis_B'].mean()
desvio_padrao = df['Hepatitis_B'].std()

cv = (desvio_padrao / media) * 100

print(f"O Coeficiente de Variacao é: {cv:.2f}%")

top_3_frequencias = df['Hepatitis_B'].value_counts().head(3)

print("Top 3 valores mais frequentes:")
print(top_3_frequencias)

moda = df['Hepatitis_B'].mode()
print(f"A Moda e: {moda[0]}")

assimetria = df['Hepatitis_B'].skew()

print(f"A assimetria e: {assimetria:.2f}")

curtose = df['Hepatitis_B'].kurt()
print(f"A curtose e: {curtose:.2f}")


# Configuração de estilo para parecer um dashboard profissional
sns.set_theme(style="whitegrid")

# 1. Criando o Histograma (Foco em Frequência e Distribuição)
plt.figure(figsize=(10, 5))
sns.histplot(df['Hepatitis_B'], kde=True, color='blue', bins=20)
plt.title('Histograma - Distribuição de Hepatitis_B')
plt.xlabel('Taxa de Vacinação (%)')
plt.ylabel('Frequência')
plt.savefig('histograma_hepatite.png')

# 2. Criando o Boxplot (Foco em Quartis e Outliers)
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Hepatitis_B'], color='lightgreen')
plt.title('Boxplot - Identificação de Outliers em Hepatitis_B')
plt.xlabel('Taxa de Vacinação (%)')
plt.savefig('boxplot_hepatite.png')