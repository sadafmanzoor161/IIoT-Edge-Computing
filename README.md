# IoT Sensor Time-Series Analysis Pipeline

A structured exploratory analysis pipeline for **Industrial IoT sensor data**, focusing on **statistical time-series analysis and frequency-domain signal investigation**.

The project analyzes multiple sensor measurements (temperature, pressure, vibration, network latency, and control signals) to understand system behavior and investigate patterns associated with **predictive failure detection**.

The pipeline implements both **time-domain statistical analysis** and **frequency-domain signal processing techniques** commonly used in **Industrial IoT monitoring and predictive maintenance systems**.

---

# Project Structure

| Path | Contents |
|-----|-----|
| `IIoT edge computing_data analysis.py` | Main analysis pipeline script |
| `Iot dataset.csv` | Raw IoT dataset with timestamped sensor readings |
| `iot_analysis_output/` | Generated plots and statistical analysis results |
| `descriptive_statistics.csv` | Statistical summary of sensor variables |
| `adf_results.csv` | Augmented Dickey-Fuller stationarity test results |
| `*_timeseries.png` | Time-series visualization for each sensor |
| `*_acf_pacf.png` | Autocorrelation and partial autocorrelation plots |
| `*_psd.png` | Power Spectral Density plots (Welch method) |
| `*_fft.png` | FFT frequency spectrum plots |
| `*_stft.png` | STFT spectrogram visualizations |
| `failure_distribution.png` | Failure events across time |
| `target_distribution.png` | Failure vs normal class distribution |

---

# Dataset

The dataset contains **IoT sensor measurements collected over time from an industrial monitoring system**.

| Property | Value |
|------|------|
| Data type | Multivariate time series |
| Features | 6 sensor variables |
| Target variable | Predicted_Failure |
| Time index | Timestamp |
| Domain | Industrial IoT monitoring |

### Sensor Features

| Feature | Description |
|------|------|
| Temperature | System operating temperature |
| Pressure | Pressure level in system |
| Vibration | Mechanical vibration intensity |
| Network_Latency | Network communication delay |
| Edge_Processing_Time | Processing time at edge devices |
| Fuzzy_PID_Output | Output of fuzzy PID control system |
| Predicted_Failure | Binary failure indicator |

The dataset is indexed by **timestamp**, allowing analysis of temporal patterns and system dynamics.

---

# Installation

## 1 Clone repository

```bash
git clone https://github.com/yourusername/iot-timeseries-analysis.git
cd iot-timeseries-analysis
```

## 2 Create virtual environment

```bash
python -m venv venv
```

Activate environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

## 3 Install dependencies

```bash
pip install -r requirements.txt
```

Required libraries:

```
pandas
numpy
matplotlib
statsmodels
scipy
```

---

# Running the Analysis Pipeline

Run the complete analysis using:

```bash
python iot_timeseries_analysis.py
```

The pipeline automatically performs all analyses and saves results in:

```
iot_analysis_output/
```

---

# Analysis Pipeline

The pipeline performs a series of structured analyses to examine the dataset from both **statistical and signal-processing perspectives**.

---

# Step 1 — Dataset Loading and Preprocessing

The dataset is loaded and timestamps are converted into datetime format.

Column names are cleaned to remove whitespace and ensure consistent indexing.

Output:

```
Dataset shape and preview printed to console
```

---

# Step 2 — Descriptive Statistical Analysis

Descriptive statistics are computed for all sensor variables.

Metrics include:

- Mean
- Standard deviation
- Minimum and maximum
- Quartiles

These statistics help understand the distribution and variability of sensor readings.

Output:

```
iot_analysis_output/descriptive_statistics.csv
```

---

# Step 3 — Time-Series Visualization

Time-series plots are generated for each sensor variable to examine temporal trends.

Outputs include:

```
Temperature_timeseries.png
Pressure_timeseries.png
Vibration_timeseries.png
Network_Latency_timeseries.png
Edge_Processing_Time_timeseries.png
Fuzzy_PID_Output_timeseries.png
```

These plots reveal fluctuations, spikes, and potential periodic patterns.

---

# Step 4 — Stationarity Assessment

The **Augmented Dickey-Fuller (ADF) test** is used to evaluate stationarity of each sensor signal.

Interpretation:

| p-value | Result |
|------|------|
| < 0.05 | Stationary |
| ≥ 0.05 | Non-stationary |

Stationarity is important for time-series modeling techniques such as ARIMA.

Output:

```
iot_analysis_output/adf_results.csv
```

---

# Step 5 — Autocorrelation Analysis

Autocorrelation (ACF) and partial autocorrelation (PACF) plots are generated.

These plots help identify:

- time dependencies
- lag relationships
- suitable autoregressive model structures

Output:

```
*_acf_pacf.png
```

---

# Step 6 — Power Spectral Density (PSD)

Power Spectral Density is estimated using **Welch’s method** to analyze how signal power is distributed across frequencies.

This helps detect periodic behaviors and dominant oscillations in sensor signals.

Output:

```
*_psd.png
```

---

# Step 7 — Fourier Frequency Analysis

Fast Fourier Transform (FFT) converts time-domain signals into the frequency domain.

FFT helps identify dominant frequency components and harmonic structures in sensor signals.

Output:

```
*_fft.png
```

---

# Step 8 — Time-Frequency Analysis (STFT)

Short-Time Fourier Transform (STFT) spectrograms reveal how frequency components evolve over time.

This allows detection of transient events or signal changes.

Output:

```
*_stft.png
```

---

# Step 9 — Failure Event Analysis

Failure events are aggregated by month to visualize how failures occur over time.

Output:

```
failure_distribution.png
```

---

# Step 10 — Target Class Distribution

The dataset’s class distribution is analyzed to examine balance between failure and normal operation.

Output:

```
target_distribution.png
```

---

# Dependency Order

```
iot_timeseries_analysis.py
        │
        ├── Descriptive statistics
        ├── Time series visualization
        ├── ADF stationarity tests
        ├── ACF/PACF analysis
        ├── PSD estimation
        ├── FFT spectral analysis
        ├── STFT spectrogram generation
        ├── Failure distribution analysis
        └── Target class distribution
```

---

# Key Insights

| Analysis | Finding |
|------|------|
| Descriptive statistics | Sensor readings show moderate variance and occasional spikes |
| Time-series plots | Signals exhibit temporal fluctuations and possible operational cycles |
| ADF tests | Some sensor signals show non-stationary behavior |
| ACF/PACF | Significant short-lag correlations observed |
| PSD analysis | Dominant low-frequency components detected |
| FFT analysis | Harmonic structures present in vibration signals |
| STFT analysis | Frequency bursts occur during specific time intervals |

These insights can support **predictive maintenance models and anomaly detection systems**.

---

# Conclusion

The IIoT sensor dataset shows clear temporal dependencies and operational patterns across multiple sensors such as temperature, pressure, and vibration.
Time-series and autocorrelation analyses indicate that current system behavior is influenced by past readings, while frequency-domain analysis reveals
dominant low-frequency components with occasional bursts that may indicate abnormal conditions. Overall, the dataset contains meaningful temporal and 
spectral patterns that can support predictive maintenance and failure detection models.

