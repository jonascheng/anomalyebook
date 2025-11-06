# Anomaly Detection and Time Series Analysis Ebook

本專案彙整多種異常偵測與時間序列分析技術，包含理論、實作範例、合成與真實資料集，適合自學或教學使用。

內容取材自 [Anomaly Detection: Through Machine Learning, Deep Learning and AutoML](https://www.amazon.com/Anomaly-Detection-Through-Machine-Learning-ebook/dp/B0D5B991G5) 及網路教學，透過範例介紹常見且可能應用在 OT 場域的異常偵測算法。

## 教學重點摘要
- **異常偵測方法**：涵蓋統計、機器學習、深度學習（Autoencoder, GAN）等多元技術。
- **合成資料生成**：展示如何產生含異常的多維度時間序列資料，並進行視覺化。
- **模型實作流程**：每個 notebook 皆包含資料準備、模型訓練、異常偵測、成效分析與視覺化。
- **簡化流程**：部分範例直接採用 pyod 套件，快速建構異常偵測模型，降低複雜度。
- **成效評估**：利用 sklearn classification_report 等工具，量化模型偵測能力。

## 目錄與內容簡介

### 01_z-score-identify-outliers.ipynb
- 利用 Z-score、IQR、DBSCAN 等方法辨識異常值。
- 適合初學者理解統計型與密度型異常偵測。

### 02_dbscan-vs-hdbscan.ipynb
- 比較 DBSCAN 與 HDBSCAN 在異常偵測上的差異。
- 展示密度型分群演算法的優缺點。

### 03_stl-decomposition.ipynb
- STL 分解時間序列，提取趨勢、季節性與殘差。
- 殘差部分可用於異常偵測。

### 05_iforest-fraud-detection.ipynb
- Isolation Forest 結合 SHAP 進行詐欺偵測與模型解釋。
- 適合理解 ensemble 與可解釋性方法。

### 06_autoencoder-anomaly-detection.ipynb
- 以 pyod AutoEncoder 建構多維度異常偵測模型。
- 模型訓練、異常分數與標記視覺化、成效分析。
- 教學流程簡潔，無需手動設計神經網路結構。

## 使用方式
1. 安裝 Python 3.11。
2. 執行 `make setup` 安裝所有依賴。
3. 執行 `make jupyter` 開啟 JupyterLab，依序執行 notebook。

## 學習建議
- 建議依 notebook 編號循序學習，逐步理解各種異常偵測技術。
- 每個 notebook 皆可獨立執行，並搭配 markdown 說明理解理論與實作細節。
