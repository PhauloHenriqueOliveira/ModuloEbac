import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('gasolina.csv')


plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')


plt.title('Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')


plt.savefig('gasolina.png')


plt.show()