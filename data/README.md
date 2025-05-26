# Szczegółowy opis zbioru danych Agriculture Crop Yield

## Opis

Zbiór danych zawiera informacje dotyczące plonów rolnych w zależności od różnych czynników środowiskowych i rolniczych. Może być używany do analizy wpływu warunków pogodowych, rodzaju gleby i technik rolniczych na wydajność upraw.

## Struktura Danych

| Kolumna                  | Typ danych    | Opis                                                                   |
|--------------------------|----------------|-----------------------------------------------------------------------|
| `Region`                 | Kategoryczny   | Region geograficzny (np. North, South, West)                          |
| `Soil_Type`              | Kategoryczny   | Typ gleby (np. Sandy, Clay, Loam, Silt)                               |
| `Crop`                   | Kategoryczny   | Rodzaj uprawy (np. Rice, Wheat, Soybean, etc.)                        |
| `Rainfall_mm`            | Liczbowy       | Ilość opadów (w milimetrach)                                          |
| `Temperature_Celsius`    | Liczbowy       | Średnia temperatura (w stopniach Celsjusza)                           |
| `Fertilizer_Used`        | Boolean        | Czy zastosowano nawóz (True/False)                                    |
| `Irrigation_Used`        | Boolean        | Czy zastosowano nawadnianie (True/False)                              |
| `Weather_Condition`      | Kategoryczny   | Warunki pogodowe (np. Rainy, Cloudy, Sunny)                           |
| `Days_to_Harvest`        | Liczbowy       | Liczba dni do zbiorów                                                 |
| `Yield_tons_per_hectare` | Liczbowy       | Plon w tonach na hektar   