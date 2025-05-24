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
    data/
        processed/
        raw/
            crop_yield.csv

        README.md

    final__report/
        report.pdf

    model__testing/
        LightGBM/
            lightgbm_evaluation.ipynb
            lightgbm_modeling.ipynb

        XGBoost/
            xgboost_evaluation.ipynb
            xgboost_modeling.ipynb

    notebooks/
        01_exploration.ipynb
        02_preprocessing.ipynb
        03_modeling.ipynb
        04_evaluation.ipynb

    outputs/
        figures/
            LightGBM/
                lightgbm_actual_vs_predicted.png
                lightgbm_error_distribution.png
                lightgbm_feature_importance.png

            XGBoost/
                xgboost_actual_vs_predicted.png
                xgboost_error_distribution.png
                xgboost_feature_importance.png

            actual_vs_predicted.png
            correlation_heatmap.png
            error_distribution.png
            feature_importance.png
            yield_distribution.png
        
        models/

    src/
        main.py

    README.md
    requirements.txt
    
---

## Model i uczenie

- **Główny algorytm:** `RandomForestRegressor`
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

> Wysoka wartość R2 oznacza, że model bardzo dobrze wyjaśnia zmienność plonów w danych testowych.

---

## Wizualizacje wyników

Wszystkie wykresy zostały zapisane w folderze `outputs/figures/`:

- `actual_vs_predicted.png` – rzeczywiste vs przewidywane plony
- `error_distribution.png` – rozkład błędów predykcji
- `feature_importance.png` – najważniejsze cechy wpływające na wynik

---

## Porównanie

Model oparty na RandomForestRegresor porównano z modelami opartymi o Light GBM oraz XGBoost. Wyniki przedstawiono w raporcie końcowym.