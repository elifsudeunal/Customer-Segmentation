# 🎯 **Advanced RFM Customer Segmentation Analysis**

> 🚀 **A comprehensive customer segmentation analysis using RFM (Recency, Frequency, Monetary) methodology with advanced clustering techniques and customer lifetime value calculations.**

---

## 📊 **Project Overview**

This project performs **advanced customer segmentation analysis** on sales data to identify customer behavior patterns, predict churn risk, and calculate customer lifetime value (CLV). The analysis combines traditional RFM segmentation with modern machine learning clustering techniques.

---

## ✨ **Features**

| 🎯 **Feature** | 📝 **Description** |
|----------------|-------------------|
| 🏷️ **Traditional RFM Segmentation** | Classifies customers into 11 distinct segments |
| 🤖 **Advanced Clustering** | K-Means and DBSCAN clustering algorithms |
| 💰 **Customer Lifetime Value (CLV)** | Predictive CLV calculation with multiple approaches |
| ⚠️ **Churn Risk Analysis** | Multi-factor churn prediction scoring |
| 📈 **Cohort Analysis** | Customer retention tracking over time |
| 📊 **Comprehensive Visualizations** | 2D and 3D plots for data insights |
| 📋 **Multi-format Output** | CSV and Excel reports with detailed breakdowns |

---

## 📁 **Project Structure**
```
CUSTOMER_SEGMENTATION/
├── 📂 code/
│   └── 📓 segmentation.ipynb          # Main analysis notebook
├── 📂 data/
│   └── 📄 sales.csv                   # Input sales data
├── 📂 output/                         # Generated reports and results
│   ├── 📊 rfm_sales.csv
│   └── 📈 advanced_rfm_report.xlsx
├── 📖 README.md                       # Project documentation
└── 📋 requirements.txt                # Python dependencies
```

---

## 🛠️ **Technologies Used**

<table>
<tr>
<td align="center">🐍<br><b>Python 3.x</b></td>
<td align="center">🐼<br><b>Pandas</b><br>Data manipulation</td>
<td align="center">🔢<br><b>NumPy</b><br>Numerical computations</td>
</tr>
<tr>
<td align="center">📊<br><b>Matplotlib</b><br>Data visualization</td>
<td align="center">🎨<br><b>Seaborn</b><br>Statistical plots</td>
<td align="center">🤖<br><b>Scikit-learn</b><br>Machine learning</td>
</tr>
<tr>
<td align="center">📅<br><b>Datetime</b><br>Date/time operations</td>
<td align="center">📊<br><b>Plotly</b><br>Interactive plots</td>
<td align="center">📈<br><b>Scipy</b><br>Statistical analysis</td>
</tr>
</table>

---

## 📊 **Analysis Components**

### 1️⃣ **RFM Segmentation**

> 🔍 **Core Metrics:**
> - 🕒 **Recency**: Days since last purchase
> - 🔄 **Frequency**: Number of purchases in analysis period  
> - 💰 **Monetary**: Total spending amount

#### 👥 **Customer Segments:**

<table>
<tr>
<td>🏆 <b>Champions</b></td>
<td>💎 <b>Loyal Customers</b></td>
<td>🔄 <b>Potential Loyalists</b></td>
</tr>
<tr>
<td>🆕 <b>New Customers</b></td>
<td>🔔 <b>Need Attention</b></td>
<td>⚠️ <b>At Risk</b></td>
</tr>
<tr>
<td>💔 <b>Can't Lose</b></td>
<td>😴 <b>About to Sleep</b></td>
<td>💤 <b>Hibernating</b></td>
</tr>
</table>

---

### 2️⃣ **Advanced Clustering**

| 🔍 **Algorithm** | 📝 **Description** |
|------------------|-------------------|
| 🎯 **K-Means Clustering** | Optimal cluster identification using silhouette analysis |
| 🌐 **DBSCAN** | Density-based clustering with noise detection |

---

### 3️⃣ **Customer Lifetime Value (CLV)**

> 💡 **Multiple CLV Approaches:**
> - 📊 Conservative estimates
> - 📈 Optimistic projections  
> - 📋 CLV quartile segmentation

---

### 4️⃣ **Churn Risk Analysis**

| 🎯 **Component** | 📊 **Details** |
|------------------|----------------|
| 📊 **Multi-factor Risk Scoring** | Comprehensive risk assessment |
| 🚦 **Risk Categories** | Low, Medium, High, Critical |
| 💸 **Revenue Loss Estimation** | Potential financial impact |

---

## 📈 **Key Outputs**

### 📋 **Generated Reports**

| 📄 **File** | 📝 **Description** |
|-------------|-------------------|
| 📊 **rfm_sales.csv** | Complete RFM analysis results |
| 📈 **advanced_rfm_report.xlsx** | Multi-sheet Excel report |

#### 📊 **Excel Report Includes:**
- 📋 RFM Data
- 🎯 Clustering Results  
- 💰 CLV Analysis
- ⚠️ Churn Risk Assessment
- 📊 Segment Summaries
- 🌍 Country Analysis
- 📈 Cohort Analysis

---

### 📊 **Visualizations**

<table>
<tr>
<td align="center">📊<br><b>Customer Distribution</b><br>Scatter plots</td>
<td align="center">🥧<br><b>Segment Distribution</b><br>Pie charts</td>
<td align="center">📊<br><b>CLV Histograms</b><br>Value distribution</td>
</tr>
<tr>
<td align="center">🎲<br><b>3D RFM Clustering</b><br>Interactive visualization</td>
<td align="center">🌍<br><b>Country Performance</b><br>Geographic analysis</td>
<td align="center">⚠️<br><b>Churn Risk Distribution</b><br>Risk assessment</td>
</tr>
</table>

---

## 🎯 **Business Applications**

### 📊 **Marketing Strategy**

| 👥 **Segment** | 🎯 **Strategy** |
|----------------|----------------|
| 🏆 **Champions** | VIP programs, early access to new products |
| ⚠️ **At Risk** | Win-back campaigns, personalized offers |
| 🆕 **New Customers** | Onboarding campaigns, welcome series |
| 💔 **Can't Lose** | Urgent intervention, premium support |

### 📈 **Revenue Optimization**

> 🎯 **Key Benefits:**
> - 🔍 Identify high-value customer segments
> - ⚠️ Predict customer churn before it happens
> - 💰 Calculate accurate customer lifetime values
> - 📊 Optimize marketing spend allocation

---

## 📊 **Sample Insights**

The analysis provides **actionable insights** such as:

- 👥 Customer segment distribution and characteristics
- 💰 Revenue contribution by segment
- ⚠️ Churn risk assessment with potential revenue loss
- 🌍 Country-wise performance metrics
- 📈 Retention rates through cohort analysis

---

## 🔄 **Future Enhancements**

| ✅ **Enhancement** | 📝 **Description** |
|-------------------|-------------------|
| 🚀 **Real-time Segmentation API** | Live customer segmentation |
| ⚡ **Apache Spark Migration** | Big data processing |
| 🔗 **CRM Integration** | Seamless system connectivity |
| 🤖 **Automated Model Retraining** | Self-updating algorithms |
| 🧠 **Advanced Behavioral Features** | Deep customer insights |
| 📊 **Predictive Churn Modeling** | ML-powered predictions |

---

## 📧 **Contact**

> 👤 **Elif Sude Ünal** - elifsudeunal6@gmail.com  
> 🔗 **Project Link**: https://github.com/elifsudeunal/Customer-Segmentation.git

---

## ⭐ **If you found this project helpful, please give it a star!** ⭐