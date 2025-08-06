
# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Set plot styles
sns.set(style="whitegrid")
# Load Titanic dataset
df = 
pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic
.csv")
# 1. Summary Statistics
print("Summary Statistics:")
print(df.describe(include='all'))
# 2. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# 3. Histograms for numeric features
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols].hist(figsize=(12, 10), bins=20)
plt.suptitle("Histograms of Numeric Features")
plt.show()
# 4. Boxplots for numeric features by Survived
for col in numeric_cols:
 plt.figure(figsize=(6, 4))
 sns.boxplot(data=df, x='Survived', y=col)
 plt.title(f'Boxplot of {col} by Survival')
 plt.show()
# 5. Correlation matrix
plt.figure(figsize=(10, 8))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
# 6. Pairplot (only on selected features to keep it readable)
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()
# 7. Pattern: Count of survivors vs non-survivors
sns.countplot(data=df, x='Survived')
plt.title("Survivors (1) vs Non-Survivors (0)")
plt.show()
# 8. Sex vs Survival
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title("Survival Count by Gender")
plt.show()
# 9. Embarked vs Survival
sns.countplot(data=df, x='Embarked', hue='Survived')
plt.title("Survival Count by Embarked Port")
plt.show()
# 10. Interactive plot using Plotly (Fare vs Age)
fig = px.scatter(df, x="Age", y="Fare", color="Survived",
 title="Age vs Fare (Colored by Survival)",
 hover_data=['Sex', 'Pclass'])
fig.show()