# Anomaly Detection and Time Series Analysis Ebook Repository

## Repository Overview

This repository contains code examples, notebooks, and datasets demonstrating various anomaly detection and time series analysis techniques. It serves as a resource for learning about different methods for identifying outliers and analyzing time series data.

**Repository Size:** Small-medium
**Project Type:** Educational/Data Science
**Languages:** Python
**Frameworks:** pandas, scikit-learn, statsmodels, matplotlib, TensorFlow
**Target Runtime:** Python 3.11

## Technical Stack

- **Python Version:** 3.11
- **Key Libraries:**
  - Jupyter/JupyterLab (for notebook development)
  - numpy, pandas (data manipulation)
  - scikit-learn (machine learning algorithms)
  - statsmodels (time series analysis)
  - matplotlib (visualization)
  - TensorFlow (for deep learning approaches)

## Anomaly Detection Techniques Covered

The repository covers multiple approaches to anomaly detection:

1. **Statistical Methods:**
   - Z-score method (for normally distributed data)
   - IQR (Interquartile Range) method (for skewed data)

2. **Machine Learning Methods:**
   - DBSCAN clustering (density-based detection)
   - Isolation Forest (ensemble-based detection)
   - SHAP values (for explainable anomaly detection)

3. **Deep Learning Methods:**
   - Autoencoders
   - GANs (Generative Adversarial Networks)

4. **Time Series Analysis:**
   - STL Decomposition (Seasonal-Trend-Loess)
   - ARIMA Decomposition

## Project Layout

- **Jupyter Notebooks:** Interactive examples with explanations
  - `stl-decomposition.ipynb`: Time series decomposition examples
  - `z-score-identify-outliers.ipynb`: Outlier detection using Z-score, IQR, and DBSCAN

- **Python Examples:** Standalone Python scripts demonstrating techniques
  - `py-examples/arima-decomposition.py`: ARIMA-based time series decomposition
  - `py-examples/stl-decomposition.py`: STL decomposition for time series
  - `py-examples/z-score-identify-outliers.py`: Various outlier detection methods

- **Text Files:** Code examples in text format
  - `auto encoders code.txt`: Autoencoder implementation for anomaly detection
  - `GAN code.txt`: GAN-based anomaly detection
  - `isolation forest and SHAP code.txt`: Isolation Forest with SHAP explainability
  - `techniques to detect outliers code - includes dataset.txt`: Various detection techniques
  - `time series hybrid model code - includes dataset.txt`: Hybrid time series models

- **Data Files:**
  - `Anomaly Time Series Data - Used in PowerBI.csv`
  - `InsFraudDataset6 - used in isoforest, shap, GAN.csv`

## Development Setup

### Environment Setup

1. Clone the repository
2. Ensure Python 3.11 is installed
3. Always run the setup command to install dependencies:

```bash
make setup
```

This will:
- Check for required dependencies
- Install Python packages from requirements.txt

### Starting Jupyter

To work with the notebooks, use the following command:

```bash
make jupyter
```

This will:
- Install dependencies (if not already installed)
- Build and launch JupyterLab

## Coding Guidelines

- Keep notebook cells modular and focused on specific tasks
- Add markdown cells with explanations for complex algorithms
- Use pandas for data manipulation whenever possible
- Follow scikit-learn's API patterns for machine learning implementations
- Include visualizations to demonstrate results
- Add appropriate mathematical formulas using LaTeX in markdown cells

## Working with This Repository

- All notebooks should be executable from top to bottom
- Example code in `.txt` files can be copied into notebooks or Python scripts
- Use the included datasets or similar structured data for testing
- The repository is structured for educational purposes, demonstrating each technique clearly
- Always cite sources and provide explanations for complex algorithms

## Useful References

The repository structure suggests consulting the following documentation when implementing features:

- [pandas Documentation](https://pandas.pydata.org/docs/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [statsmodels Documentation](https://www.statsmodels.org/stable/index.html)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)