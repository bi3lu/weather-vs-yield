# Weather vs Yield – Prognozowanie plonów rolnych na podstawie warunków pogodowych

Projekt z zakresu uczenia maszynowego mający na celu przewidywanie **plonów rolnych (t/ha)** na podstawie danych pogodowo-uprawowych, takich jak opady, temperatura, nawadnianie, rodzaj gleby i uprawy.

---

## Cel projektu

Celem projektu jest opracowanie modelu regresyjnego, który pozwoli na oszacowanie wysokości plonu w zależności od czynników środowiskowych i agrarnych.

Problem ten jest istotny ze względu na:
- wpływ zmian klimatu na rolnictwo,
- potrzebę optymalizacji produkcji rolniczej,
- wsparcie decyzji rolników i planistów.

---

## Dane

- **Źródło:** [Kaggle – Crop Yield Dataset](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield/)
- **Rozmiar:** ~100 000 rekordów, 10+ cech
- **Plik źródłowy:** `data/raw/crop_yield.csv`

### Główne cechy:
- `Rainfall_mm`, `Temperature_Celsius`, `Fertilizer_Used`, `Irrigation_Used`
- `Region`, `Soil_Type`, `Crop`, `Weather_Condition`
- `Days_to_Harvest`
- `Yield_tons_per_hectare`

---

## Struktura projektu
weather-vs-yield/
├── data/
│ ├── raw/ # Dane surowe (CSV)
│ ├── processed/ # Dane po przetwarzaniu (train/test)
├── notebooks/
│ ├── 01_exploration.ipynb # Eksploracja danych
│ ├── 02_preprocessing.ipynb # Przygotowanie danych
│ ├── 03_modeling.ipynb # Trening modelu
│ └── 04_evaluation.ipynb # Ewaluacja i wizualizacje
├── outputs/
│ ├── models/ # Zapisany model (.pkl)
│ └── figures/ # Wygenerowane wykresy
├── README.md
└── requirements.txt

---

## Model i uczenie

- **Algorytm:** `RandomForestRegressor`
- **Parametry:** `n_estimators=30`, `random_state=42`, `n_jobs=-1`
- **Podział danych:** 80% trening / 20% test
- **Biblioteki:** `scikit-learn`, `pandas`, `seaborn`, `matplotlib`

Dane zostały odpowiednio przygotowane: brakujące wartości uzupełniono, zmienne kategoryczne zakodowano, cechy numeryczne zeskalowano, a boolean zamieniono na wartości binarne.

---

## Wyniki ewaluacji

Model osiągnął następujące wyniki na zbiorze testowym:

- **MAE (średni błąd bezwzględny):** 0.42
- **RMSE (pierwiastek z błędu średniokwadratowego):** 0.52
- **R2 (współczynnik determinacji):** 0.91

> Wysoka wartość R² oznacza, że model bardzo dobrze wyjaśnia zmienność plonów w danych testowych.

---

## Wizualizacje wyników

Wszystkie wykresy zostały zapisane w folderze `outputs/figures/`:

- `actual_vs_predicted.png` – rzeczywiste vs przewidywane plony
- `error_distribution.png` – rozkład błędów predykcji
- `feature_importance.png` – najważniejsze cechy wpływające na wynik