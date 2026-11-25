import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ====== Page Config & Styling ======
st.set_page_config(page_title="Customer Intelligence Dashboard", layout="wide", page_icon="📊")

st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    h1 { color: #2E4053; }
    h2 { color: #2874A6; }
    h3 { color: #1F618D; }
    .stButton>button { background-color: #2874A6; color: white; border-radius: 8px; }
    .stButton>button:hover { background-color: #1F618D; color: white; }
    .stAlert { background-color: #e8f4f8; border-left: 5px solid #2874A6; }
    </style>
    """, unsafe_allow_html=True)

# ====== Multilingual Dictionary ======
LANG = {
    "en": {
        "title": "📊 Customer Intelligence Dashboard",
        "filters": "🔍 Filters",
        "select_segment": "Select Customer Segment",
        "tabs": ["📈 Interactive EDA", "🛒 Channels & Sales", "🎯 Campaign Analysis", "👤 Customer Personas", "💎 High-Value Analysis", "🛠️ Plot Builder"],
        "eda_header": "Interactive Exploratory Data Analysis",
        "eda_select": "Select a feature to analyze:",
        "dist": "Distribution (Histogram)",
        "box": "Box Plot by Segment",
        "scatter": "Scatter vs Total Spend",
        "channel_header": "Channels & Sales Analysis",
        "avg_channel": "Average Purchases by Channel",
        "rev_share": "Revenue Share by Segment",
        "full_plot": "Trend: Income vs Total Spend (Colored by Children)",
        "camp_header": "Campaign Performance Analysis",
        "camp_acceptance": "Campaign Acceptance Rate by Segment",
        "camp_response": "Response Rate (Last Campaign)",
        "persona_header": "Customer Personas (3 Segments)",
        "persona_table": "Key Feature Comparison",
        "persona_chart": "High-Value Profile vs Overall Average",
        "high_header": "💎 Deep Dive: High-Value Customers",
        "high_channel": "Channel Preference (High-Value)",
        "high_age": "Age Distribution (Box Plot)",
        "high_trend": "Trend: Recency vs Total Spend (with Regression)",
        "high_corr": "Correlation Matrix (High-Value Only)",
        "builder_header": "🛠️ Custom Plot Builder",
        "builder_desc": "Choose features and chart type to visualize relationships instantly.",
        "x_axis": "X-Axis:",
        "y_axis": "Y-Axis:",
        "chart_type": "Chart Type:",
        "generate_btn": "Generate Plot",
        "no_data": "No data available.",
        "insight_title": "💡 Insight & Recommendation",
        "insight_text": "Based on the current data view:"
    },
    "fa": {
        "title": "📊 داشبورد هوشمند تحلیل مشتریان",
        "filters": "🔍 فیلترها",
        "select_segment": "انتخاب گروه مشتری",
        "tabs": ["📈 تحلیل اکتشافی تعاملی", "🛒 کانال‌ها و فروش", "🎯 تحلیل کمپین‌ها", "👤 پرسونای مشتریان", "💎 تحلیل مشتریان باارزش", "🛠️ سازنده نمودار"],
        "eda_header": "تحلیل اکتشافی تعاملی داده‌ها",
        "eda_select": "یک ویژگی را برای تحلیل انتخاب کنید:",
        "dist": "توزیع (هیستوگرام)",
        "box": "نمودار جعبه‌ای بر اساس گروه",
        "scatter": "پراکندگی در برابر کل هزینه",
        "channel_header": "تحلیل کانال‌ها و فروش",
        "avg_channel": "میانگین خرید از هر کانال",
        "rev_share": "سهم درآمد هر گروه",
        "full_plot": "روند: درآمد در برابر کل هزینه (رنگ بر اساس تعداد فرزند)",
        "camp_header": "تحلیل عملکرد کمپین‌ها",
        "camp_acceptance": "نرخ پذیرش کمپین‌ها به تفکیک گروه",
        "camp_response": "نرخ پاسخ به آخرین کمپین",
        "persona_header": "پرسونای مشتریان (سه گروه)",
        "persona_table": "مقایسه ویژگی‌های کلیدی",
        "persona_chart": "مقایسه گروه پرارزش با میانگین کل",
        "high_header": "💎 تحلیل عمیق مشتریان باارزش",
        "high_channel": "ترجیح کانال خرید (مشتریان باارزش)",
        "high_age": "توزیع سن (نمودار جعبه‌ای)",
        "high_trend": "روند: تازگی خرید در برابر کل هزینه (با خط روند)",
        "high_corr": "ماتریس همبستگی (فقط مشتریان باارزش)",
        "builder_header": "🛠️ سازنده نمودار سفارشی",
        "builder_desc": "ویژگی‌ها و نوع نمودار را انتخاب کنید تا روابط را در لحظه ببینید.",
        "x_axis": "محور X:",
        "y_axis": "محور Y:",
        "chart_type": "نوع نمودار:",
        "generate_btn": "تولید نمودار",
        "no_data": "داده‌ای وجود ندارد.",
        "insight_title": "💡 بینش و پیشنهاد",
        "insight_text": "بر اساس نمای فعلی داده‌ها:"
    },
    "ar": {
        "title": "📊 لوحة تحكم ذكاء العملاء",
        "filters": "🔍 الفلاتر",
        "select_segment": "اختر شريحة العملاء",
        "tabs": ["📈 التحليل الاستكشافي", "🛒 القنوات والمبيعات", "🎯 تحليل الحملات", "👤 شخصيات العملاء", "💎 تحليل العملاء ذوي القيمة العالية", "🛠️ منشئ الرسوم البيانية"],
        "eda_header": "تحليل استكشافي تفاعلي للبيانات",
        "eda_select": "اختر ميزة للتحليل:",
        "dist": "التوزيع (المدرج التكراري)",
        "box": "مخطط الصندوق حسب الشريحة",
        "scatter": "مخطط التشتت مقابل إجمالي الإنفاق",
        "channel_header": "تحليل القنوات والمبيعات",
        "avg_channel": "متوسط المشتريات حسب القناة",
        "rev_share": "حصة الإيرادات حسب الشريحة",
        "full_plot": "الاتجاه: الدخل مقابل إجمالي الإنفاق (ملون حسب عدد الأطفال)",
        "camp_header": "تحليل أداء الحملات",
        "camp_acceptance": "معدل قبول الحملة حسب الشريحة",
        "camp_response": "معدل الاستجابة (الحملة الأخيرة)",
        "persona_header": "شخصيات العملاء (3 شرائح)",
        "persona_table": "مقارنة الميزات الرئيسية",
        "persona_chart": "ملف ذوي القيمة العالية مقابل المتوسط العام",
        "high_header": "💎 تحليل عميق: العملاء ذوو القيمة العالية",
        "high_channel": "تفضيل القناة (ذوو القيمة العالية)",
        "high_age": "توزيع العمر (مخطط الصندوق)",
        "high_trend": "الاتجاه: الحداثة مقابل إجمالي الإنفاق (مع خط الانحدار)",
        "high_corr": "مصفوفة الارتباط (لذوي القيمة العالية فقط)",
        "builder_header": "🛠️ منشئ الرسوم البيانية المخصص",
        "builder_desc": "اختر الميزات ونوع المخطط لتصور العلاقات على الفور.",
        "x_axis": "المحور السيني:",
        "y_axis": "المحور الصادي:",
        "chart_type": "نوع المخطط:",
        "generate_btn": "إنشاء المخطط",
        "no_data": "لا توجد بيانات.",
        "insight_title": "💡 الرؤية والتوصية",
        "insight_text": "بناءً على عرض البيانات الحالي:"
    },
    "zh": {
        "title": "📊 客户智能仪表板",
        "filters": "🔍 过滤器",
        "select_segment": "选择客户细分",
        "tabs": ["📈 交互式EDA", "🛒 渠道与销售", "🎯 营销活动分析", "👤 客户画像", "💎 高价值分析", "🛠️ 图表生成器"],
        "eda_header": "交互式探索性数据分析",
        "eda_select": "选择要分析的要素：",
        "dist": "分布（直方图）",
        "box": "按细分划分的箱线图",
        "scatter": "与总消费的散点图",
        "channel_header": "渠道与销售分析",
        "avg_channel": "各渠道平均购买量",
        "rev_share": "按细分划分的收入份额",
        "full_plot": "趋势：收入与总消费（按孩子数量着色）",
        "camp_header": "营销活动绩效分析",
        "camp_acceptance": "按细分划分的活动接受率",
        "camp_response": "响应率（上次活动）",
        "persona_header": "客户画像（3个细分）",
        "persona_table": "关键特征比较",
        "persona_chart": "高价值画像与总体平均值的比较",
        "high_header": "💎 深入探讨：高价值客户",
        "high_channel": "渠道偏好（高价值）",
        "high_age": "年龄分布（箱线图）",
        "high_trend": "趋势：最近购买时间与总消费（带回归线）",
        "high_corr": "相关矩阵（仅限高价值）",
        "builder_header": "🛠️ 自定义图表生成器",
        "builder_desc": "选择要素和图表类型以立即可视化关系。",
        "x_axis": "X轴：",
        "y_axis": "Y轴：",
        "chart_type": "图表类型：",
        "generate_btn": "生成图表",
        "no_data": "没有可用数据。",
        "insight_title": "💡 见解与建议",
        "insight_text": "根据当前数据视图："
    }
}

# ====== Load Data ======
@st.cache_data
def load_data():
    df = pd.read_csv('dt_clean.csv')
    df.columns = [c.lower() for c in df.columns]
    # Ensure all necessary columns exist after your cleaning
    if 'children' not in df.columns:
        df['children'] = df['kidhome'] + df['teenhome']
    if 'total_spend' not in df.columns:
        df['total_spend'] = df[['mntwines', 'mntfruits', 'mntmeatproducts', 'mntfishproducts', 'mntsweetproducts', 'mntgoldprods']].sum(axis=1)
    return df

df = load_data()

# ====== Sidebar: Language & Filters ======
st.sidebar.header("🌐 Language")
lang_option = st.sidebar.selectbox("", ["English", "فارسی", "العربية", "中文"])
lang_map = {"English": "en", "فارسی": "fa", "العربية": "ar", "中文": "zh"}
t = LANG[lang_map[lang_option]]

st.sidebar.header(t["filters"])
selected_segment = st.sidebar.multiselect(
    t["select_segment"],
    options=df['spend_segment'].unique().tolist(),
    default=df['spend_segment'].unique().tolist()
)

filtered_df = df[df['spend_segment'].isin(selected_segment)]

if filtered_df.empty:
    st.warning(t["no_data"])
    st.stop()

# ====== Main Title ======
st.title(t["title"])

# ====== Helper Functions for Insights ======
def show_insight(text):
    st.info(f"**{t['insight_title']}**\n\n{text}")

# ====== Tabs ======
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(t["tabs"])

# ---------------------------------------------------------
# Tab 1: Interactive EDA
# ---------------------------------------------------------
with tab1:
    st.header(t["eda_header"])
    
    # Use exact column names from your dataset
    all_features = ['income', 'age', 'children', 'total_spend', 'total_purchase',
                    'numwebpurchases', 'numcatalogpurchases', 'numstorepurchases', 
                    'numwebvisitsmonth', 'numdealspurchases', 'recency']
    
    feature_to_analyze = st.selectbox(t["eda_select"], all_features)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader(t["dist"])
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(data=filtered_df, x=feature_to_analyze, hue='spend_segment', kde=True, ax=ax, palette='Set2')
        st.pyplot(fig)
        
    with col2:
        st.subheader(t["box"])
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=filtered_df, x='spend_segment', y=feature_to_analyze, palette='Set2', ax=ax)
        st.pyplot(fig)

    with col3:
        st.subheader(t["scatter"])
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=filtered_df, x=feature_to_analyze, y='total_spend', hue='spend_segment', alpha=0.6, ax=ax, palette='Set2')
        st.pyplot(fig)

    show_insight(f"The average **{feature_to_analyze}** is **{filtered_df[feature_to_analyze].mean():.2f}**. The distribution shows how different segments behave. High segments generally have higher values, confirming their higher spending capacity.")

# ---------------------------------------------------------
# Tab 2: Channels & Sales
# ---------------------------------------------------------
with tab2:
    st.header(t["channel_header"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(t["avg_channel"])
        channel_data = filtered_df.groupby('spend_segment')[['numwebpurchases', 'numcatalogpurchases', 'numstorepurchases']].mean()
        fig, ax = plt.subplots(figsize=(6, 4))
        channel_data.plot(kind='bar', ax=ax, color=['#4C72B0', '#55A868', '#C44E52'])
        ax.set_ylabel("Average Purchases")
        plt.xticks(rotation=0)
        st.pyplot(fig)
        show_insight("The **Store** channel is the most utilized across all segments, followed by **Web**. High-value customers use all channels significantly more. Recommendation: Maintain strong in-store experiences while investing in web personalization.")
        
    with col2:
        st.subheader(t["rev_share"])
        revenue = filtered_df.groupby('spend_segment')['total_spend'].sum()
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(revenue, labels=revenue.index, autopct='%1.1f%%', colors=['#66B2FF','#99FF99','#FF9999'])
        st.pyplot(fig)
        top_segment = revenue.idxmax()
        show_insight(f"The **{top_segment}** segment contributes the largest share of total revenue. Focus retention strategies here to protect the core business.")

    st.subheader(t["full_plot"])
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(filtered_df['income'], filtered_df['total_spend'], c=filtered_df['children'], cmap='viridis', alpha=0.6)
    ax.set_xlabel("Income")
    ax.set_ylabel("Total Spend")
    plt.colorbar(scatter, label='Children')
    st.pyplot(fig)
    show_insight("There is a clear positive correlation between Income and Total Spend. Customers with **fewer children** tend to spend more, indicating higher disposable income for personal purchases.")

# ---------------------------------------------------------
# Tab 3: Campaign Analysis (Restored & Enhanced)
# ---------------------------------------------------------
with tab3:
    st.header(t["camp_header"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(t["camp_acceptance"])
        cmp_cols = ['acceptedcmp1', 'acceptedcmp2', 'acceptedcmp3', 'acceptedcmp4', 'acceptedcmp5']
        # Filter columns that exist to avoid KeyErrors
        available_cmp = [c for c in cmp_cols if c in filtered_df.columns]
        
        if available_cmp:
            cmp_means = filtered_df.groupby('spend_segment')[available_cmp].mean()
            fig, ax = plt.subplots(figsize=(8, 5))
            cmp_means.plot(kind='bar', ax=ax, colormap='viridis')
            ax.set_xticklabels(cmp_means.index, rotation=0)
            ax.set_ylabel("Acceptance Rate")
            st.pyplot(fig)
            show_insight("The **High** segment consistently shows higher acceptance rates for past campaigns. This confirms that previous campaign targeting was effective. Recommendation: Continue targeting high-value segments with new campaigns.")
        else:
            st.warning("Campaign columns not found in dataset.")
        
    with col2:
        st.subheader(t["camp_response"])
        response_rate = filtered_df.groupby('spend_segment')['response'].mean()
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(response_rate.index, response_rate.values, color=['#66B2FF','#99FF99','#FF9999'])
        ax.set_ylabel("Response Rate")
        st.pyplot(fig)
        show_insight("The **Response** rate to the last campaign is highest among the High-value segment. This suggests that premium offers resonate well with this group.")

# ---------------------------------------------------------
# Tab 4: Customer Personas
# ---------------------------------------------------------
with tab4:
    st.header(t["persona_header"])
    
    persona_features = ['income', 'age', 'children', 'total_spend', 'numwebpurchases', 'numdealspurchases']
    # Filter features that exist
    available_persona = [c for c in persona_features if c in filtered_df.columns]
    
    if available_persona:
        persona_table = filtered_df.groupby('spend_segment')[available_persona].mean().T
        st.subheader(t["persona_table"])
        st.dataframe(persona_table.style.highlight_max(axis=1, color='lightgreen'), use_container_width=True)
        
        st.subheader(t["persona_chart"])
        high_df = filtered_df[filtered_df['spend_segment'] == 'high']
        if not high_df.empty:
            high_means = high_df[available_persona].mean()
            overall_means = filtered_df[available_persona].mean()
            # Avoid division by zero
            normalized_high = high_means / overall_means.replace(0, 1)
            
            fig, ax = plt.subplots(figsize=(8, 5))
            y_pos = np.arange(len(available_persona))
            ax.barh(y_pos, normalized_high.values, color='#EF476F', alpha=0.8)
            ax.axvline(1.0, color='black', linestyle='--', label='Overall Avg')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(available_persona)
            ax.set_xlabel("Ratio (High vs Overall)")
            ax.legend()
            st.pyplot(fig)
            show_insight("The High-Value persona has significantly higher **Income** and **Total Spend**. Interestingly, their **Deal Purchases** are often lower, meaning they are not primarily driven by discounts. Recommendation: Focus on loyalty and premium products rather than discounts.")
    else:
        st.warning("Persona features not found.")

# ---------------------------------------------------------
# Tab 5: High-Value Analysis
# ---------------------------------------------------------
with tab5:
    st.header(t["high_header"])
    
    high_df = filtered_df[filtered_df['spend_segment'] == 'high']
    
    if high_df.empty:
        st.warning(t["no_data"])
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(t["high_channel"])
            channel_means = high_df[['numwebpurchases', 'numcatalogpurchases', 'numstorepurchases']].mean()
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(channel_means.index, channel_means.values, color=['#FF9999','#66B2FF','#99FF99'])
            ax.set_ylabel("Average Purchases")
            plt.xticks(rotation=0)
            st.pyplot(fig)
            show_insight("High-value customers show a strong preference for the **Store** and **Web** channels. Ensure these touchpoints offer premium experiences to maintain their loyalty.")
            
        with col2:
            st.subheader(t["high_age"])
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.boxplot(y=high_df['age'], color='skyblue', ax=ax)
            ax.set_ylabel("Age")
            st.pyplot(fig)
            show_insight("The age distribution of high-value customers is concentrated between 40 and 70. Marketing campaigns for this segment should be tailored to mature demographics.")
            
        st.subheader(t["high_trend"])
        # Using regplot for a clean trend line with scatter
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.regplot(data=high_df, x='recency', y='total_spend', scatter_kws={'alpha':0.3, 's': 20}, line_kws={'color':'red'}, ax=ax)
        ax.set_xlabel("Recency (Days)")
        ax.set_ylabel("Total Spend")
        st.pyplot(fig)
        show_insight("There is no strong linear relationship between Recency and Total Spend. High-value customers spend consistently regardless of how recently they last purchased. Focus on consistent engagement rather than urgency-based campaigns.")
        
        st.subheader(t["high_corr"])
        numeric_cols = ['income', 'age', 'children', 'total_spend', 'numwebpurchases', 'numstorepurchases']
        available_corr = [c for c in numeric_cols if c in high_df.columns]
        if available_corr:
            corr = high_df[available_corr].corr()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
            st.pyplot(fig)
            show_insight("As seen in the heatmap, **Income** and **Total Spend** have a very high positive correlation. For high-value customers, spending capacity is closely tied to income. **Children** shows a negative correlation with spending. Recommendation: Tailor premium offers to high-income, low-children households.")

# ---------------------------------------------------------
# Tab 6: Plot Builder
# ---------------------------------------------------------
with tab6:
    st.header(t["builder_header"])
    st.write(t["builder_desc"])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        all_numerical = ['income', 'age', 'children', 'total_spend', 'total_purchase',
                         'numwebpurchases', 'numcatalogpurchases', 'numstorepurchases', 
                         'numwebvisitsmonth', 'numdealspurchases', 'recency']
        x_axis = st.selectbox(t["x_axis"], all_numerical)
    with col2:
        y_axis = st.selectbox(t["y_axis"], all_numerical)
    with col3:
        chart_type = st.selectbox(t["chart_type"], [
            "Scatter Plot", "Box Plot", "Bar Chart", "Line Chart", "Violin Plot", "Histogram", "Heatmap", "Pie Chart"
        ])
        
    if st.button(t["generate_btn"]):
        fig, ax = plt.subplots(figsize=(10, 6))
        try:
            if chart_type == "Scatter Plot":
                sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, hue='spend_segment', alpha=0.6, ax=ax)
            elif chart_type == "Box Plot":
                sns.boxplot(data=filtered_df, x='spend_segment', y=y_axis, ax=ax)
            elif chart_type == "Bar Chart":
                sns.barplot(data=filtered_df, x='spend_segment', y=y_axis, ax=ax)
            elif chart_type == "Line Chart":
                line_data = filtered_df.sort_values(x_axis)
                sns.lineplot(data=line_data, x=x_axis, y=y_axis, hue='spend_segment', ax=ax)
            elif chart_type == "Violin Plot":
                sns.violinplot(data=filtered_df, x='spend_segment', y=y_axis, ax=ax)
            elif chart_type == "Histogram":
                sns.histplot(data=filtered_df, x=x_axis, hue='spend_segment', kde=True, ax=ax)
            elif chart_type == "Heatmap":
                if x_axis != y_axis:
                    pivot_table = filtered_df.pivot_table(index='spend_segment', columns=x_axis, values=y_axis, aggfunc='mean')
                    sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt=".1f", ax=ax)
                else:
                    st.warning("Please select different features for X and Y axes.")
                    st.stop()
            elif chart_type == "Pie Chart":
                # Pie charts need categorical data or means
                data = filtered_df.groupby('spend_segment')[y_axis].mean()
                ax.pie(data, labels=data.index, autopct='%1.1f%%', colors=['#66B2FF','#99FF99','#FF9999'])
            
            st.pyplot(fig)
            show_insight(f"This {chart_type} visualizes the relationship between **{x_axis}** and **{y_axis}**. Review the distribution across segments to identify outliers or trends that can inform targeted marketing strategies.")
            
        except Exception as e:
            st.error(f"Error drawing plot: {e}")