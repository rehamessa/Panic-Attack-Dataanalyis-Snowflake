import seaborn as sns
import matplotlib.pyplot as plt

# Dataset is automatically provided as "dataset"
corr = dataset.corr()

plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Symptom Correlation Heatmap")
plt.show()