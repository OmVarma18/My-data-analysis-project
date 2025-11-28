# 🛒 Customer Shopping Behavior Analysis – README

## 📌 Executive Summary  
This project analyzes shopping patterns using transactional data from 3,900 purchases to uncover customer preferences, spending behavior, and segmentation insights. Using the STAR method, the analysis combines Python, SQL, and Power BI to identify revenue drivers and optimize marketing strategies. The final dashboard provides a comprehensive, data-driven foundation for strategic business decisions.

---

## 🎯 Business Problem *(Situation & Task)*  
The organization needed a clearer understanding of customer shopping behavior to improve marketing effectiveness, increase revenue, boost subscriptions, and enhance customer loyalty. The dataset included demographic details, purchase data, discount behavior, and more. The challenge was to analyze trends and provide actionable recommendations.

---

## 🔬 Methodology *(Action)*  

### 1️⃣ Data Preparation (Python)  
- Cleaned and standardized 3,900 rows across 18 features.  
- Imputed missing *Review Rating* values using median per product category.  
- Created *age_group* and *purchase_frequency_days* features.  
- Removed redundant *promo_code_used* column.  
✓ Loaded cleaned data into PostgreSQL. :contentReference[oaicite:2]{index=2}

### 2️⃣ SQL Analysis  
Used SQL queries to answer business-critical questions:
- Revenue by gender  
- High-spending discount users  
- Top-rated products  
- Shipping type comparison  
- Subscription impact on revenue and spending  
- Customer segmentation (New, Returning, Loyal)  
- Product popularity by category  
- Repeat buyers and subscription likelihood  
- Revenue contribution by age group  
📊 **Example:** Young Adults generated the highest total revenue ($62,143). :contentReference[oaicite:3]{index=3}

### 3️⃣ Dashboard (Power BI)  
Designed a data visualization dashboard including:
- Total customers (3.9K), Average purchase ($59.76), Avg. review rating (3.75)  
- Subscription distribution: 27% subscribed, 73% not subscribed  
- Revenue & sales by category and age group  
- Customer interaction filters (Gender, Category, Shipping Type, etc.) :contentReference[oaicite:4]{index=4}

---

## 🧠 Skills & Tools  
| Category | Tools/Skills |
|----------|--------------|
| Programming | Python (pandas, feature engineering) |
| Database | PostgreSQL, SQL queries |
| Visualization | Power BI |
| Data Cleaning | Handling missing values, column formatting |
| Analytics | Customer segmentation, revenue analysis |
| Strategy | Business insights, storytelling |

---

## 📈 Results *(Result)*  
✔ **Young Adults** generated the highest revenue overall.  
✔ **Discount users** still spent above average, indicating strong value perception.  
✔ **Subscribers** showed higher average purchase and total revenue.  
✔ **Express shipping** customers spent more than standard users.  
✔ **Top-selling products** were dominated by Clothing & Accessories.  
✔ **Repeat buyers (5+ purchases)** were more likely to be subscribers. :contentReference[oaicite:5]{index=5}

---

## 📢 Business Recommendations  
| Area | Recommendation |
|------|----------------|
| 🔁 Customer Loyalty | Implement rewards for repeat buyers to shift them into the “Loyal” segment. |
| 💳 Subscription Growth | Highlight exclusive benefits to drive subscriptions. |
| 💸 Discount Strategy | Reassess discounting to maintain profit margins while sustaining sales. |
| 📍 Product Strategy | Promote top-rated and best-selling items. |
| 🎯 Targeted Marketing | Focus campaigns on high-revenue segments (e.g., Young Adults, Express shipping users). :contentReference[oaicite:6]{index=6} |

---

## 🚀 Next Steps  
- Develop predictive models for churn and customer lifetime value.
- Introduce personalized promotions based on historical behavior.
- Expand feature engineering to include more behavioral metrics.
- Integrate live dashboard updates using automated pipelines.

---

> 🎉 *This project successfully translated raw customer data into strategic insight, enabling data-backed decision-making and future optimization opportunities.*

