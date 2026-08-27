from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_model(y_test, y_pred):
    print("\n📊 Evaluation:")

    # Calculate MSE first
    mse = mean_squared_error(y_test, y_pred)

    # Convert to RMSE manually
    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, y_pred)

    print("RMSE:", rmse)
    print("R2 Score:", r2)