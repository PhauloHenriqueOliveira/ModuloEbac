import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')


plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', color='blue', linestyle='-')
plt.title('Preço da gasolina ao longo dos dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)


plt.savefig('gasolina.png')


with open('gasolina.py', 'w') as f:
    f.write('''import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('gasolina.csv')


plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', color='blue', linestyle='-')
plt.title('Preço da gasolina ao longo dos dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)


plt.savefig('gasolina.png')
''')


plt.show()