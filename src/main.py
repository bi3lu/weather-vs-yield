# -*- coding: utf-8 -*-
"""
Plik główny do przetwarzania danych i trenowania modelu Random Forest (główny algorytm użyty w projekcie).
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Przygotowanie danych
file_path = '../data/raw/crop_yield.csv'
df = pd.read_csv(file_path)

X = df.drop("Yield_tons_per_hectare", axis=1)
y = df["Yield_tons_per_hectare"]

numerical_features = ["Rainfall_mm", "Temperature_Celsius", "Days_to_Harvest"]
categorical_features = ["Region", "Soil_Type", "Crop", "Weather_Condition"]
boolean_features = ["Fertilizer_Used", "Irrigation_Used"]

numerical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

boolean_transformer = Pipeline(steps=[
    ("to_int", FunctionTransformer(lambda x: x.astype(int))),
    ("imputer", SimpleImputer(strategy="most_frequent"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numerical_transformer, numerical_features),
    ("cat", categorical_transformer, categorical_features),
    ("bool", boolean_transformer, boolean_features)
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

train_df = pd.DataFrame(X_train_processed.toarray() if hasattr(X_train_processed, "toarray") else X_train_processed)
train_df["Yield_tons_per_hectare"] = y_train.values

test_df = pd.DataFrame(X_test_processed.toarray() if hasattr(X_test_processed, "toarray") else X_test_processed)
test_df["Yield_tons_per_hectare"] = y_test.values

train_df.to_csv("../data/processed/train.csv", index=False)
test_df.to_csv("../data/processed/test.csv", index=False)

# Trenowanie modelu
train_df = pd.read_csv("../data/processed/train.csv")
test_df = pd.read_csv("../data/processed/test.csv")

X_train = train_df.drop("Yield_tons_per_hectare", axis=1)
y_train = train_df["Yield_tons_per_hectare"]

X_test = test_df.drop("Yield_tons_per_hectare", axis=1)
y_test = test_df["Yield_tons_per_hectare"]

model = RandomForestRegressor(n_estimators=30, random_state=42)
model.fit(X_train, y_train)

output_path = "../outputs/models"
os.makedirs(output_path, exist_ok=True)
joblib.dump(model, os.path.join(output_path, "random_forest_model_n_30.pkl"))