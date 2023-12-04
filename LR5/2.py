import pandas as pd

# Замените 'your_dataset.csv' на реальное имя вашего файла
df = pd.read_csv('your_dataset.csv')
df_sample = df.sample(n=1000, random_state=42)
missing_values = df_sample.isnull().sum()
import matplotlib.pyplot as plt
import seaborn as sns

# Ящики с усами (логарифмическая шкала)
plt.figure(figsize=(10, 6))
sns.boxplot(x='your_column', y='your_value', data=df_sample)
plt.yscale('log')
plt.show()

# Гистограмма
plt.figure(figsize=(10, 6))
sns.histplot(df_sample['your_column'], bins=30, kde=True)
plt.show()
# Заполнение пропусков (например, средними значениями)
df_sample_filled = df_sample.fillna(df_sample.mean())

# Обработка выбросов (например, с использованием z-оценки)
z_scores = (df_sample_filled['your_column'] - df_sample_filled['your_column'].mean()) / df_sample_filled['your_column'].std()
df_no_outliers = df_sample_filled[(z_scores > -3) & (z_scores < 3)]
room_counts = df_no_outliers['room_count'].value_counts()
pivot_table = pd.pivot_table(df_no_outliers, values='your_value', index='district', columns='room_count', aggfunc='count')
df_no_outliers.to_csv('surname.csv', index=False)
