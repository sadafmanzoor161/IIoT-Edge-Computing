# ==========================================================
# IoT Sensor Time Series Analysis
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy import signal
from scipy.fft import fft

# ==========================================================
# CONFIGURATION
# ==========================================================

CSV_PATH = r"C:\Users\sadaf manzoor\Documents\Data Analysis\Iot dataset.csv"

DATE_COL = "Timestamp"

SENSOR_COLS = [
    "Temperature",
    "Pressure",
    "Vibration",
    "Network_Latency",
    "Edge_Processing_Time",
    "Fuzzy_PID_Output"
]

TARGET_COL = "Predicted_Failure"

OUTPUT_DIR = "iot_analysis_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================================
# LOAD DATASET
# ==========================================================

print("Loading dataset...")

df = pd.read_csv(CSV_PATH)

# remove spaces in column names
df.columns = df.columns.str.strip()

# convert timestamp
df[DATE_COL] = pd.to_datetime(df[DATE_COL])

print("Dataset shape:", df.shape)
print(df.head())

# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

print("\nGenerating descriptive statistics...")

desc = df[SENSOR_COLS].describe()

print(desc)

desc.to_csv(os.path.join(OUTPUT_DIR, "descriptive_statistics.csv"))

# ==========================================================
# TIME SERIES PREPARATION
# ==========================================================

df_ts = df.set_index(DATE_COL)[SENSOR_COLS].copy()

# ==========================================================
# TIME SERIES VISUALIZATION
# ==========================================================

print("Generating time series plots...")

for col in SENSOR_COLS:

    plt.figure(figsize=(10,4))

    plt.plot(df_ts.index, df_ts[col])

    plt.title(f"{col} Over Time")

    plt.xlabel("Time")
    plt.ylabel(col)

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, f"{col}_timeseries.png"))

    plt.close()

# ==========================================================
# ADF STATIONARITY TEST
# ==========================================================

print("\nADF Stationarity Tests")

adf_results = {}

for col in SENSOR_COLS:

    series = df_ts[col].dropna()

    result = adfuller(series)

    adf_results[col] = {
        "ADF Statistic": result[0],
        "p-value": result[1]
    }

    print(col, result[0], result[1])

pd.DataFrame(adf_results).T.to_csv(
    os.path.join(OUTPUT_DIR, "adf_results.csv")
)

# ==========================================================
# AUTOCORRELATION ANALYSIS
# ==========================================================

print("Generating ACF and PACF plots...")

for col in SENSOR_COLS:

    series = df_ts[col].dropna()

    max_lags = min(40, len(series)//2)

    fig, ax = plt.subplots(1,2, figsize=(12,4))

    plot_acf(series, ax=ax[0], lags=max_lags)
    plot_pacf(series, ax=ax[1], lags=max_lags)

    ax[0].set_title(f"ACF - {col}")
    ax[1].set_title(f"PACF - {col}")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, f"{col}_acf_pacf.png"))

    plt.close()

# ==========================================================
# POWER SPECTRAL DENSITY (PSD)
# ==========================================================

print("Generating PSD plots...")

for col in SENSOR_COLS:

    series = df_ts[col].dropna()

    data = series.to_numpy()

    freqs, psd = signal.welch(data)

    plt.figure(figsize=(8,4))

    plt.semilogy(freqs, psd)

    plt.title(f"PSD - {col}")

    plt.xlabel("Frequency")

    plt.ylabel("Power")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, f"{col}_psd.png"))

    plt.close()

# ==========================================================
# FFT FREQUENCY ANALYSIS
# ==========================================================

print("Generating FFT spectrum...")

for col in SENSOR_COLS:

    series = df_ts[col].dropna()

    data = series.to_numpy()

    fft_vals = fft(data)

    plt.figure(figsize=(8,4))

    plt.plot(np.abs(fft_vals))

    plt.title(f"FFT Spectrum - {col}")

    plt.xlabel("Frequency Index")

    plt.ylabel("Magnitude")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, f"{col}_fft.png"))

    plt.close()

# ==========================================================
# STFT SPECTROGRAM
# ==========================================================

print("Generating STFT spectrograms...")

for col in SENSOR_COLS:

    series = df_ts[col].dropna()

    data = series.to_numpy()

    f, t, Zxx = signal.stft(data)

    plt.figure(figsize=(8,4))

    plt.pcolormesh(t, f, np.abs(Zxx))

    plt.title(f"STFT Spectrogram - {col}")

    plt.ylabel("Frequency")

    plt.xlabel("Time")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, f"{col}_stft.png"))

    plt.close()

# ==========================================================
# FAILURE ANALYSIS
# ==========================================================

print("Generating failure analysis...")

df["YearMonth"] = df[DATE_COL].dt.to_period("M")

failure_counts = df.groupby(["YearMonth", TARGET_COL]).size().unstack(fill_value=0)

failure_counts.index = failure_counts.index.to_timestamp()

plt.figure(figsize=(10,5))

failure_counts.plot(kind="bar", stacked=True)

plt.title("Failure Events Over Time")

plt.xlabel("Month")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "failure_distribution.png"))

plt.close()

# ==========================================================
# TARGET CLASS DISTRIBUTION
# ==========================================================

plt.figure(figsize=(6,4))

df[TARGET_COL].value_counts().plot(kind="bar")

plt.title("Failure vs Normal Distribution")

plt.xlabel("Class")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "target_distribution.png"))

plt.close()

# ==========================================================
# FINISHED
# ==========================================================

print("\nAnalysis Complete.")
print("All outputs saved in:", OUTPUT_DIR)