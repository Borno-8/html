import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

df = df.dropna()
print(df.head())
print(df.info())
print(df.describe())
print('Species:', df['species'].unique())
print('Island:', df['island'].unique())

sns.histplot(data=df, x='body_mass_g', bins=20, color='red')
plt.title('Distribution of Peguin Body Mass')
plt.xlabel('Body Mass (grmas)')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('Flipper Length Shape by Species (KDE)')
plt.show()

sns.histplot(data=df, x='flipper_length_mm', kde=True, color='yellow')
plt.title('Flipper Length - Histogram with KDE Curve')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Count')
plt.show()

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Flipper Length vs Body Mass by Species')
plt.ylabel('Body Mass (grams)')
plt.show()

corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Penguin Measurments')
plt.show()