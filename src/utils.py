import matplotlib.pyplot as plt

def plot_results(y_test, y_pred):
    plt.figure()

    plt.plot(y_test.values, label="Actual")
    plt.plot(y_pred, label="Predicted")

    plt.legend()
    plt.title("Energy Forecasting (Improved Model)")
    plt.xlabel("Samples")
    plt.ylabel("Energy")

    plt.show()