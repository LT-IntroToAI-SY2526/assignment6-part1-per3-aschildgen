"""
Assignment 6 – Part 1
Student Score Prediction

This program builds a simple linear regression model to estimate
student test scores based on how many hours they study.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def load_data(file):
    """Load a CSV file and show basic info."""
    df = pd.read_csv(file)
    print(df.head())
    print("Shape:", df.shape)
    print(df.describe())
    return df


def scatter_plot(df):
    """Plot hours vs scores."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Hours"], df["Scores"], color="purple", alpha=0.6)
    plt.xlabel("Study Hours")
    plt.ylabel("Score")
    plt.title("Scores vs Hours Studied")
    plt.grid(alpha=0.3)
    plt.savefig("scatter_plot.png", dpi=300)
    print("Saved: scatter_plot.png")
    plt.show()


def split_sets(df):
    """Split into train/test sets."""
    X = df[["Hours"]]
    y = df["Scores"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))
    return X_train, X_test, y_train, y_test


def train(X_train, y_train):
    """Train linear regression model."""
    reg = LinearRegression()
    reg.fit(X_train, y_train)

    print("Model trained.")
    print("Slope:", round(reg.coef_[0], 2))
    print("Intercept:", round(reg.intercept_, 2))

    return reg


def test_model(model, X_test, y_test):
    """Evaluate model accuracy."""
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)

    print("R²:", round(r2, 4))
    print("MSE:", round(mse, 2))
    print("RMSE:", round(rmse, 2))

    return preds


def show_results(X_train, y_train, X_test, y_test, preds, model):
    """Plot actual vs predicted values."""
    plt.figure(figsize=(12, 6))

    plt.scatter(X_train, y_train, label="Train", alpha=0.5)
    plt.scatter(X_test, y_test, label="Test Actual", alpha=0.7, color="green")
    plt.scatter(X_test, preds, label="Predicted", color="red", marker="x", s=100)

    x_line = np.linspace(X_train.min(), X_train.max(), 100)
    y_line = model.predict(x_line)

    plt.plot(x_line, y_line, color="black", linewidth=2, label="Fit Line")
    plt.xlabel("Study Hours")
    plt.ylabel("Score")
    plt.title("Prediction Results")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.savefig("results_plot.png", dpi=300)
    print("Saved: results_plot.png")
    plt.show()


def single_prediction(model, hours):
    """Predict score for a specific number of study hours."""
    arr = np.array([[hours]])
    outcome = model.predict(arr)[0]

    print(f"For {hours} hours, predicted score = {outcome:.2f}")
    return outcome


if __name__ == "__main__":
    print("=== STUDENT SCORE PREDICTOR ===")

    data = load_data("student_scores.csv")
    scatter_plot(data)

    X_train, X_test, y_train, y_test = split_sets(data)

    model = train(X_train, y_train)

    predictions = test_model(model, X_test, y_test)

    show_results(X_train, y_train, X_test, y_test, predictions, model)

    single_prediction(model, 7)

    print("\nDone! Check saved images.")
