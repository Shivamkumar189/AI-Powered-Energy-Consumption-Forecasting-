import sys
import os
import pandas as pd
import numpy as np
import warnings

# ✅ Suppress warnings (optional but clean)
warnings.filterwarnings("ignore")

# ✅ Fix import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_PATH)

from preprocessing import load_data, preprocess_data
from model import train_model, predict
from evaluate import evaluate_model
from utils import plot_results


def main():
    print("⚡ Energy Forecasting System Started")

    # ✅ Load Data
    data = load_data("data/energy.csv")

    # ✅ Preprocess
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # ✅ Train Model
    model = train_model(X_train, y_train)

    # ✅ Predict
    y_pred = predict(model, X_test)

    # ✅ Evaluate
    evaluate_model(y_test, y_pred)

    # ✅ Plot Results
    plot_results(y_test, y_pred)

    # 🔥 ===============================
    # 🔮 FUTURE FORECASTING SECTION
    # 🔥 ===============================

    print("\n🔮 Future Forecast (Next 7 Days):")

    # Convert Date column properly
    data['Date'] = pd.to_datetime(data['Date'])

    # Get last date and last energy
    last_date = data['Date'].max()
    last_energy = data['Energy'].iloc[-1]

    # Generate next 7 days (exclude current day)
    future_dates = pd.date_range(start=last_date, periods=8)[1:]

    for date in future_dates:
        day = date.day
        month = date.month
        year = date.year

        # Use last predicted value
        lag1 = last_energy
        rolling_mean = last_energy

        # ✅ FIX: use NumPy array (removes warning)
        input_data = np.array([[day, month, year, lag1, rolling_mean]])

        pred = model.predict(input_data)

        print(f"{date.date()} → Predicted Energy: {pred[0]:.2f}")

        # Update for next prediction
        last_energy = pred[0]

    print("\n✅ Forecasting Completed Successfully!")


if __name__ == "__main__":
    main()