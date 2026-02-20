# 🐍 Python ile Nesne Yönelimli Programlama (OOP)

Python'da **Nesne Yönelimli Programlamanın (OOP) temellerini** adım adım öğrenmek için hazırlanmış bir çalışma reposudur. Temel sınıf tanımlarından encapsulation, abstraction, inheritance ve polymorphism gibi ileri düzey prensiplere kadar tüm konuları kapsar.

---

## 📂 Proje Yapısı

```
Object-Oriented-Programming-Python/
│
├── classes/
│   └── classes.py                  # Temel sınıf ve metot tanımları
│
├── constructors/
│   └── constructors.py             # __init__, assert, __repr__, sınıf attribute'ları
│
├── classic vs static methods/
│   ├── classic_vs_static.py        # @classmethod ve @staticmethod kullanımı
│   └── items.csv
│
├── getter and setter/
│   ├── getters_and_setters.py      # @property ve @setter dekoratörleri
│   └── items.csv
│
├── inheritance/
│   ├── inheritance.py              # Kalıtım ve super() kullanımı
│   └── items.csv
│
└── OOP Principles/
    ├── oop.py                      # 4 temel OOP prensibi bir arada
    └── items.csv
```

---

## 📖 İşlenen Konular

### 1. Sınıflar (`classes/`)
- Sınıf tanımlama ve nesne oluşturma
- Instance metotları ve `self` anahtar kelimesi
- Nesnelere dinamik olarak attribute atama

### 2. Constructor'lar (`constructors/`)
- `__init__` constructor metodu
- **Sınıf düzeyinde** ve **nesne düzeyinde** attribute farkları
- `assert` ile girdi doğrulama
- `__repr__` magic metodu ile okunabilir çıktı
- Tüm nesneleri takip etmek için sınıf düzeyinde `all` listesi

### 3. Class ve Static Metotlar (`classic vs static methods/`)
- `@classmethod` — CSV dosyasından nesne oluşturma (`instantiate_from_csv`)
- `@staticmethod` — Sınıfla ilişkili ama nesneye bağlı olmayan yardımcı metot (`is_integer`)
- Python `csv.DictReader` ile yapılandırılmış veri okuma

### 4. Getter ve Setter (`getter and setter/`)
- `@property` dekoratörü ile salt okunur (read-only) attribute tanımlama
- `@<attribute>.setter` ile kontrollü değiştirme
- Çift alt çizgi (`__name`) ile **name mangling** ve kapsülleme

### 5. Kalıtım (`inheritance/`)
- Bir üst sınıfı (`Item`) genişleten alt sınıf (`Phone`) oluşturma
- `super().__init__()` ile üst sınıf constructor'ını çağırma
- Alt sınıfa özel attribute ekleme (`broken_phones`)
- Üst sınıf metotlarını alt sınıf nesnelerinde kullanma

### 6. OOP Prensipleri — Hepsi Bir Arada (`OOP Principles/`)

Nesne Yönelimli Programlamanın dört temel ilkesini tek dosyada birleştiren kapsamlı bir modül:

| Prensip | Açıklama |
|---------|----------|
| **Encapsulation (Kapsülleme)** | `@property` ve name mangling ile attribute'lara doğrudan erişimi kısıtlama |
| **Abstraction (Soyutlama)** | Karmaşık iç mantığı (`__connect`, `__prepare_body`, `__send`) basit bir `send_email()` arayüzünün arkasına gizleme |
| **Inheritance (Kalıtım)** | `Phone` sınıfının `Item` sınıfından miras alması |
| **Polymorphism (Çok Biçimlilik)** | Aynı metotların (`apply_discount`, `increment_price`) farklı nesne türlerinde çalışması |

---

## 🚀 Çalıştırma

### Gereksinimler
- Python 3.6+

### Örnekleri Çalıştırma
Her modül bağımsız olarak çalıştırılabilir:

```bash
# Temel sınıflar
python classes/classes.py

# Constructor'lar
python constructors/constructors.py

# Class ve static metotlar
cd "classic vs static methods"
python classic_vs_static.py

# Getter ve setter
cd "getter and setter"
python getters_and_setters.py

# Kalıtım
cd inheritance
python inheritance.py

# Tüm OOP prensipleri
cd "OOP Principles"
python oop.py
```

---

## 📌 Notlar
- `items.csv` dosyası birden fazla modülde kullanılarak yapılandırılmış veriden nesne oluşturma işlemi gösterilmektedir.
- Her modül bir öncekinin üzerine inşa edildiğinden, yukarıdaki sırayı takip etmeniz önerilir.
