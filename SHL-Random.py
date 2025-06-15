import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "yas": np.random.randint(18, 85, n),
    "cinsiyet": np.random.choice(["Kadın", "Erkek"], n),
    "bas_donmesi": np.random.choice([0, 1], n),
    "kulakta_cinlama": np.random.choice([0, 1], n),
    "gec_baslama_gunu": np.random.randint(0, 10, n),
    "is_kaybi_seviyesi": np.random.choice(["Hafif", "Orta", "İleri", "Total"], n),
    "tedavi_turu": np.random.choice(["Kortikosteroid", "Hiperbarik", "İkili", "Hiçbiri"], n, p=[0.4, 0.3, 0.2, 0.1]),
    "tedavi_yaniti": np.random.choice([0, 1], n, p=[0.4, 0.6])
})
# Kategorik değişkenleri sayısallaştır
df["cinsiyet"] = df["cinsiyet"].map({"Kadın": 0, "Erkek": 1})
df["is_kaybi_seviyesi"] = df["is_kaybi_seviyesi"].map({"Hafif": 0, "Orta": 1, "İleri": 2, "Total": 3})
df["tedavi_turu"] = df["tedavi_turu"].map({
    "Kortikosteroid": 0,
    "Hiperbarik": 1,
    "İkili": 2,
    "Hiçbiri": 3
})
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

X = df.drop("tedavi_yaniti", axis=1)
y = df["tedavi_yaniti"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Doğruluk Oranı:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
import matplotlib.pyplot as plt

feature_importances = pd.Series(model.feature_importances_, index=X.columns)
feature_importances.sort_values().plot(kind='barh', figsize=(8, 5), title="Özellik Önem Sıralaması")
plt.tight_layout()
plt.show()