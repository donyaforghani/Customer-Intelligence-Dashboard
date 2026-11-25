📊 Customer Intelligence Dashboard

Customer Segmentation, Exploratory Data Analysis & Interactive Visualization

<!-- Project Preview --><p align="center">
  <img src="assets/dashboard-overview.png" width="100%" alt="Customer Intelligence Dashboard Overview">
</p>📌 Project Overview

This project focuses on analyzing customer behavior, purchasing patterns, and marketing campaign performance using Python.

The main objective is to explore customer data, identify meaningful patterns, segment customers based on their total spending, and develop an interactive dashboard to visualize business insights.

The project covers the complete data analysis workflow, from initial data exploration and cleaning to feature engineering, customer segmentation, data visualization, and interactive dashboard development.

🎯 Project Objectives

- Explore customer demographics and purchasing behavior.
- Clean and prepare raw customer data.
- Perform feature engineering.
- Segment customers based on spending behavior.
- Analyze purchasing channels and product preferences.
- Evaluate marketing campaign responses.
- Identify high-value customer characteristics.
- Build an interactive dashboard.

🛠️ Technologies & Libraries

Technology| Application
Python| Core programming language
Pandas| Data manipulation and cleaning
NumPy| Numerical operations
Matplotlib| Data visualization
Seaborn| Statistical visualization
Streamlit| Interactive dashboard
Jupyter Notebook| Data analysis

📂 Project Structure

Customer-Intelligence-Dashboard/
│
├── assets/
│   ├── dashboard-overview.png
│   ├── eda-analysis.png
│   ├── channels-sales.png
│   ├── campaign-analysis.png
│   ├── customer-personas.png
│   ├── high-value-analysis.png
│   └── custom-plot-builder.png
│
├── analyses_project.ipynb
├── app.py
├── dt_clean.csv
├── requirements.txt
├── README.md
└── .gitignore

🔍 Project Workflow

1. Data Exploration

- Dataset inspection and structural analysis.
- Statistical summaries.
- Missing value investigation.
- Understanding customer attributes.

<!-- Data Exploration Screenshot --><p align="center">
  <img src="assets/data-exploration.png" width="85%" alt="Data Exploration">
</p>2. Data Cleaning

- Converting customer registration dates into datetime format.
- Removing unnecessary columns.
- Handling missing income values.
- Filtering invalid age values.
- Preparing the dataset for analysis.

<!-- Data Cleaning Screenshot --><p align="center">
  <img src="assets/data-cleaning.png" width="85%" alt="Data Cleaning">
</p>3. Feature Engineering

Several new features were created:

Feature| Description
Age| Customer age
Total Spend| Spending across six product categories
Children| Combined number of children and teenagers
Total Purchase| Purchases across web, catalog, and store channels

<!-- Feature Engineering Screenshot --><p align="center">
  <img src="assets/feature-engineering.png" width="85%" alt="Feature Engineering">
</p>4. Customer Segmentation

Customers were divided into three spending categories using "Pandas.qcut()":

- Low: Low-spending customers
- Medium: Medium-spending customers
- High: High-spending customers

<!-- Customer Segmentation Screenshot --><p align="center">
  <img src="assets/customer-segmentation.png" width="85%" alt="Customer Segmentation">
</p>5. Exploratory Data Analysis (EDA)

The analysis explores:

- Income and spending distributions.
- Customer age and household composition.
- Spending behavior across segments.
- Product-category purchasing patterns.
- Purchasing channels.
- Marketing campaign responses.
- Relationships between numerical variables.
- High-value customer characteristics.

<!-- EDA Screenshot --><p align="center">
  <img src="assets/eda-analysis.png" width="90%" alt="Exploratory Data Analysis">
</p>📈 Interactive Dashboard

The dashboard was developed using Streamlit and includes six main sections.

1. Interactive EDA

- Histograms
- Box plots
- Scatter plots
- Feature distribution analysis

<p align="center">
  <img src="assets/eda-analysis.png" width="90%" alt="Interactive EDA">
</p>2. Channels & Sales

- Average purchases by channel.
- Revenue contribution by customer segment.
- Income vs. total spending analysis.

<p align="center">
  <img src="assets/channels-sales.png" width="90%" alt="Channels and Sales">
</p>3. Campaign Analysis

- Campaign acceptance rates.
- Last campaign response rates.
- Segment-based campaign comparisons.

<p align="center">
  <img src="assets/campaign-analysis.png" width="90%" alt="Campaign Analysis">
</p>4. Customer Personas

- Customer segment comparison.
- Demographic and behavioral analysis.
- High-value customer profiling.

<p align="center">
  <img src="assets/customer-personas.png" width="90%" alt="Customer Personas">
</p>5. High-Value Customer Analysis

- Purchasing channel preferences.
- Age distribution.
- Recency vs. spending analysis.
- Correlation matrix.

<p align="center">
  <img src="assets/high-value-analysis.png" width="90%" alt="High Value Customer Analysis">
</p>6. Custom Plot Builder

- Interactive feature selection.
- Multiple visualization types.
- Custom analytical comparisons.

<p align="center">
  <img src="assets/custom-plot-builder.png" width="90%" alt="Custom Plot Builder">
</p>🌐 Multilingual Support

The dashboard supports four languages:

- English
- Persian
- Arabic
- Chinese

<!-- Multilingual Dashboard Screenshot --><p align="center">
  <img src="assets/multilingual-dashboard.png" width="90%" alt="Multilingual Dashboard">
</p>📊 Dataset Information

The cleaned dataset contains:

- 2,205 customer records
- 31 features
- 3 spending segments

The dataset includes demographic information, household characteristics, product spending, purchasing channels, and marketing campaign responses.

The final dataset is stored in "dt_clean.csv".

🚀 Installation & Usage

1. Clone the repository

git clone https://github.com/donyaforghani/Customer-Intelligence-Dashboard.git

2. Navigate to the project directory

cd Customer-Intelligence-Dashboard

3. Install dependencies

pip install -r requirements.txt

4. Run the dashboard

streamlit run app.py

🔮 Future Improvements

- Advanced customer segmentation using clustering algorithms.
- RFM (Recency, Frequency, Monetary) analysis.
- Predictive customer behavior modeling.
- Marketing campaign effectiveness optimization.
- Dynamic business insight generation.
- Dashboard deployment and cloud hosting.

👨‍💻 Author

Donya Forghani

Biomedical Engineering | Python | Data Analysis | Machine Learning | Computer Vision

- GitHub: "@donyaforghani" (https://github.com/donyaforghani)
- LinkedIn: "Donya Forghani" (https://www.linkedin.com/in/donyaforghani/)

---

This project was developed as a practical learning project to strengthen Python programming, data analysis, data visualization, and analytical problem-solving skills.
