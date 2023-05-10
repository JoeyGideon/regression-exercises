
import numpy as np
import matplotlib.pyplot as plt

def plot_residuals(y, yhat):
    residuals = y - yhat
    plt.scatter(yhat, residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel('Predicted values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.show()

def regression_errors(y, yhat):
    SSE = np.sum((y - yhat)**2)
    ESS = np.sum((yhat - np.mean(y))**2)
    TSS = np.sum((y - np.mean(y))**2)
    MSE = SSE / len(y)
    RMSE = np.sqrt(MSE)
    return SSE, ESS, TSS, MSE, RMSE

def baseline_mean_errors(y):
    yhat_baseline = np.full_like(y, np.mean(y))
    SSE_baseline = np.sum((y - yhat_baseline)**2)
    MSE_baseline = SSE_baseline / len(y)
    RMSE_baseline = np.sqrt(MSE_baseline)
    return SSE_baseline, MSE_baseline, RMSE_baseline

def better_than_baseline(y, yhat):
    SSE_model = np.sum((y - yhat)**2)
    SSE_baseline = baseline_mean_errors(y)[0]
    return SSE_model < SSE_baseline
