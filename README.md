# 🎯 Advanced RFM Customer Segmentation Analysis

🚀 A comprehensive customer segmentation analysis using RFM (Recency, Frequency, Monetary) methodology with advanced clustering techniques, customer lifetime value calculations, and high-performance data processing.

---

## 📊 Project Overview
This project performs advanced customer segmentation analysis on sales data to identify customer behavior patterns, predict churn risk, and calculate customer lifetime value (CLV). The analysis combines traditional RFM segmentation with modern machine learning clustering techniques and big data processing capabilities.

---

## ✨ Features

| 🎯 Feature | 📝 Description |
|------------|----------------|
| 🏷️ Traditional RFM Segmentation | Classifies customers into 11 distinct segments |
| 🤖 Advanced Clustering | K-Means and DBSCAN clustering algorithms |
| 💰 Customer Lifetime Value (CLV) | Predictive CLV calculation with multiple approaches |
| ⚠️ Churn Risk Analysis | Multi-factor churn prediction scoring |
| 📈 Cohort Analysis | Customer retention tracking over time |
| ⚡ High-Performance Processing | Dask integration for scalable data processing |
| 🌍 Geographic Analysis | Country-based performance insights |
| 📊 Comprehensive Visualizations | 2D and 3D plots for data insights |
| 📋 Multi-format Output | CSV and Excel reports with detailed breakdowns |

---

## 📁 Project Structure

```
CUSTOMER_SEGMENTATION/
├── 📂 code/
│   └── 📓 segmentation.ipynb          # Main analysis notebook (pandas)
│   └── 📓 dask_rfm_analysis.ipynb     # dask-integration-recovery branch analysis notebook (pandas + dask)
├── 📂 data/
│   └── 📄 sales.csv                   # Input sales data
├── 📂 output/                         # Generated reports and results
│   ├── 📊 rfm_sales.csv
│   └── 📈 advanced_rfm_report.xlsx
├── 📖 README.md                       # Project documentation
└── 📋 requirements.txt                # Python dependencies
```

---


---

## 🛠️ Technologies Used

<table>
<tr>
<td align="center">🐍<br><b>Python 3.x</b></td>
<td align="center">🐼<br><b>Pandas</b><br>Data manipulation</td>
<td align="center">🔢<br><b>NumPy</b><br>Numerical computations</td>
</tr>
<tr>
<td align="center">⚡<br><b>Dask</b><br>Parallel computing</td>
<td align="center">📊<br><b>Dask-ML</b><br>Scalable ML algorithms</td>
<td align="center">📊<br><b>Matplotlib</b><br>Data visualization</td>
</tr>
<tr>
<td align="center">🎨<br><b>Seaborn</b><br>Statistical plots</td>
<td align="center">🤖<br><b>Scikit-learn</b><br>Machine learning</td>
<td align="center">📅<br><b>Datetime</b><br>Date/time operations</td>
</tr>
</table>

---

## ⚡ Performance & Scalability

### 🚀 Big Data Processing
The system automatically detects and handles large datasets using:

- 🔥 Dask DataFrames for distributed computing  
- ⚡ Progress tracking with visual progress bars  
- 🧠 Memory optimization with configurable memory limits  
- 📊 Fallback mechanisms to ensure compatibility  

### 🔧 Adaptive Processing
| 📊 Data Size | 🛠️ Processing Method |
|--------------|----------------------|
| Small datasets | Standard Pandas processing |
| Large datasets | Automatic Dask distributed processing |
| Memory constraints | Chunked processing with progress tracking |

---

## 📊 Analysis Components

### 1️⃣ RFM Segmentation
**Core Metrics:**
- 🕒 Recency: Days since last purchase  
- 🔄 Frequency: Number of purchases in analysis period  
- 💰 Monetary: Total spending amount  

**Customer Segments:**

<table>
<tr>
<td>🏆 <b>Champions</b></td>
<td>💎 <b>Loyal Customers</b></td>
<td>🔄 <b>Potential Loyalists</b></td>
<td>🔔 <b>Promising</b></td>
</tr>
<tr>
<td>🆕 <b>New Customers</b></td>
<td>🔔 <b>Need Attention</b></td>
<td>⚠️ <b>At Risk</b></td>
<td>😴 <b>About to Sleep</b></td>
</tr>
<tr>
<td>💔 <b>Can't Lose</b></td>
<td>💤 <b>Hibernating</b></td>
<td>🔍 <b>Other</b></td>
</tr>
</table>

---

### 2️⃣ Advanced Clustering
| 🔍 Algorithm | 📝 Description | ⚡ Performance |
|--------------|----------------|----------------|
| 🎯 K-Means Clustering | Optimal cluster identification using silhouette analysis | Scalable with Dask-ML |
| 🌐 DBSCAN | Density-based clustering with noise detection | Automatic epsilon optimization |

**Clustering Optimization**
- 📊 Silhouette Score Analysis for optimal K selection  
- 📈 Elbow Method visualization  
- 🎯 Manual vs Automatic cluster selection  
- ⚖️ Cluster Balance Assessment  

---

### 3️⃣ Customer Lifetime Value (CLV)
**Advanced CLV Calculation:**
- 📊 Conservative estimates with risk adjustments  
- 📈 Optimistic projections based on purchase patterns  
- 🎯 AOV (Average Order Value) integration  
- 📋 CLV quartile segmentation  
- 🔄 Purchase frequency modeling  

---

### 4️⃣ Enhanced Churn Risk Analysis
| 🎯 Component | 📊 Details |
|--------------|------------|
| 🔍 Method | Multi-factor Risk Scoring |
| 📊 Multi-factor Risk Scoring | Recency, Frequency, Monetary weighted scoring, custom risk algorithms |
| 🚦 Risk Categories | Low, Medium, High, Critical (Quartile-based classification) |
| 💸 Revenue Loss Estimation | Potential financial impact calculation, statistical modeling |

---

### 5️⃣ Geographic & Country Analysis
🌍 New Geographic Features:
- 🗺️ Country mapping with full country names  
- 📊 Country performance metrics  
- 🎯 Revenue distribution by geography  
- 📈 Customer density analysis  

---

## 📈 Key Outputs

### 📋 Generated Reports
| 📄 File | 📝 Description | 🆕 New Features |
|---------|----------------|----------------|
| 📊 rfm_sales.csv | Complete RFM analysis results | Geographic data included |
| 📈 advanced_rfm_report.xlsx | Multi-sheet Excel report | 8 comprehensive sheets |

**Excel Report Sheets:**
- 📋 RFM_Data: Complete customer segmentation data  
- 🎯 Clustering_Results: K-Means and DBSCAN results  
- 💰 CLV_Analysis: Customer lifetime value calculations  
- ⚠️ Churn_Risk: Risk assessment with categories  
- 📊 Segment_Summary: Business insights by segment  
- 🌍 Country_Analysis: Geographic performance metrics  
- 📈 Cohort_Analysis: Customer retention tracking  
- 🔄 CLV_RFM_Comparison: Cross-analysis insights  

---

### 📊 Enhanced Visualizations
<table>
<tr>
<td align="center">📊<br><b>Customer Distribution</b><br>Bubble scatter plots</td>
<td align="center">📈<br><b>Weekly/Monthly Trends</b><br>Time series analysis</td>
<td align="center">💰<br><b>CLV Distribution</b><br>Filtered histograms</td>
</tr>
<tr>
<td align="center">🎲<br><b>3D RFM Clustering</b><br>Interactive 3D visualization</td>
<td align="center">🌍<br><b>Country Revenue</b><br>Geographic performance</td>
<td align="center">⚠️<br><b>Risk Assessment</b><br>Churn probability</td>
</tr>
<tr>
<td align="center">📊<br><b>Segment Revenue</b><br>Log-scale analysis</td>
<td align="center">🎯<br><b>Clustering Comparison</b><br>Algorithm comparison</td>
<td align="center">📈<br><b>Retention Cohorts</b><br>Customer lifecycle</td>
</tr>
</table>

---

## 🎯 Business Applications

### 📊 Advanced Marketing Strategy
| 👥 Segment | 🎯 Strategy | 💰 Revenue Impact |
|------------|-------------|-------------------|
| 🏆 Champions | VIP programs, early access | High retention value |
| ⚠️ At Risk | Win-back campaigns, personalized offers | Prevent revenue loss |
| 🆕 New Customers | Onboarding campaigns, welcome series | Growth potential |
| 💔 Can't Lose | Urgent intervention, premium support | Critical revenue protection |

### 📈 Advanced Business Insights
**Key Metrics Tracked:**
- 📊 Customer segment distribution with percentages  
- 💰 Revenue contribution by segment and country  
- ⚠️ Churn risk assessment with potential revenue loss  
- 🌍 Geographic performance metrics  
- 📈 Cohort retention rates over time  
- 🎯 Customer lifetime value predictions  

---

## 🔄 Performance Metrics

### 📊 Model Performance
- 🎯 K-Means Silhouette Score: Clustering quality measurement  
- 🔍 DBSCAN Noise Detection: Outlier identification rate  
- ⚖️ Cluster Balance Ratio: Distribution quality assessment  

### 📈 Business Metrics
- 💰 Total Revenue: Complete financial overview  
- ⚠️ Revenue at Risk: Potential churn impact  
- 🔄 Recoverable Potential: Win-back opportunities  
- 📊 Customer Distribution: Segment balance analysis  

---

## 🔄 Future Enhancements
| ✅ Enhancement | 📝 Description | 🚀 Priority |
|----------------|----------------|--------------|
| Real-time Segmentation API | Live customer segmentation | High |
| ⚡ Apache Spark Migration | Big data processing | Medium |
| 🔗 CRM Integration | Seamless system connectivity | High |
| 🤖 Automated Model Retraining | Self-updating algorithms | Medium |
| 🧠 Deep Learning Features | Advanced behavioral analysis | Low |
| 📊 Predictive Churn Modeling | ML-powered predictions | High |

---

📧 Contact  

👤 Elif Sude Ünal - elifsudeunal6@gmail.com
🔗 Project Link: https://github.com/elifsudeunal/Customer-Segmentation.git

## ⭐ **If you found this project helpful, please give it a star!** ⭐
