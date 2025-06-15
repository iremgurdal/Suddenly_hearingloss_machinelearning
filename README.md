# Suddenly_hearingloss_machinelearning
# SHL-Random: Ani İşitme Kaybı Tedavi Tahmin Modeli

Bu proje, ani işitme kaybı (Sudden Hearing Loss - SHL) vakalarında tedaviye verilen yanıtı tahmin etmek amacıyla oluşturulan bir makine öğrenimi modelini içerir. Model, demografik ve klinik verilere dayanarak rastgele üretilmiş bir veri kümesi üzerinde çalışır.

## 🔍 Proje Amacı

Projenin amacı, yaş, cinsiyet, semptomlar, işitme kaybı seviyesi ve uygulanan tedavi türü gibi özellikleri kullanarak hastaların tedaviye yanıt verip vermeyeceğini tahmin etmektir.

## 📊 Kullanılan Kütüphaneler

- pandas
- numpy
- scikit-learn
- matplotlib

## ⚙️ Çalışma Adımları

1. **Veri Oluşturma:**  
   - 500 bireyden oluşan sahte bir SHL veri seti oluşturulur.
   - Kategorik değişkenler sayısallaştırılır.

2. **Modelleme:**  
   - Veriler eğitim ve test olarak ayrılır.
   - Random Forest sınıflandırıcısı ile model eğitilir.
   - Model doğruluğu ve sınıflandırma raporu yazdırılır.

3. **Özellik Önem Analizi:**  
   - Modelin kararlarında hangi özelliklerin daha önemli olduğunu gösteren grafik oluşturulur.

## 🧪 Koşum (Run) Talimatları

Python 3 ve gerekli kütüphaneler kuruluysa aşağıdaki komutla çalıştırabilirsiniz:

```bash
python SHL-Random.py
Doğruluk Oranı: 0.70
              precision    recall  f1-score   support
           0       0.68       0.67       0.67        44
           1       0.71       0.72       0.71        56
    accuracy                           0.70       100
   macro avg       0.70       0.70       0.70       100
weighted avg       0.70       0.70       0.70       100
📈 Özellik Önem Grafiği
Kod sonunda matplotlib ile modelin hangi değişkenlere ne kadar ağırlık verdiği görselleştirilir.

👩‍🔬 Geliştirici
İrem Gürdal
📧 medium.com/@iremgurdal97
