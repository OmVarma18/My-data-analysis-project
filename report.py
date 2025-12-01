import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Configuration
st.set_page_config(page_title="Customer Shopping Behavior Dashboard", layout="wide")

# Title
st.title("🛒 Customer Shopping Behavior Analysis Dashboard")

# Hardcoded file path
FILE_PATH = "D:\Machine Learning Free code camp\DA\Project\end to end\customer_shopping_behavior.csv"  # ← Update this to your actual path!

try:
    df = pd.read_csv(FILE_PATH)
    st.success(f"Dataset loaded")

    # Normalize column names
    df.columns = (
        df.columns.str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
        .str.replace("/", "_")
        .str.strip()
    )

    # st.write("### 🔎 Normalized Column Names")
    # st.write(df.columns.tolist())

    # Rename key columns
    df.rename(
        columns={
            "purchase_amount_usd": "purchase_amount",
            "review_rating": "review_rating",
            "subscription_status": "subscription_status",
            "previous_purchases": "previous_purchases",
        },
        inplace=True,
    )

    # Feature Engineering
    if "age_group" in df.columns and "purchase_amount" in df.columns:
        st.write("### 💰 Revenue by Age Group")
        age_revenue = df.groupby("age_group")["purchase_amount"].sum().reset_index()
        # Example: Revenue by Age Group
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(age_revenue["age_group"], age_revenue["purchase_amount"])
        ax.set_title("Revenue by Age Group")

        col1, col2 = st.columns([1, 3])  # 👈 Chart in column 1, column 2 is empty buffer
        with col1:
            st.pyplot(fig, use_container_width=False)


    # Revenue by Gender
    if "gender" in df.columns:
        st.write("### 👥 Revenue by Gender")
        gender_revenue = df.groupby("gender")["purchase_amount"].sum().reset_index()
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(gender_revenue["gender"], gender_revenue["purchase_amount"])
        ax.set_title("Revenue by Gender")
        st.pyplot(fig)

    # Subscription Impact
    if "subscription_status" in df.columns:
        st.write("### 🎟 Subscription Impact on Revenue")
        subscription_revenue = df.groupby("subscription_status")["purchase_amount"].sum().reset_index()
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(subscription_revenue["subscription_status"], subscription_revenue["purchase_amount"])
        ax.set_title("Revenue by Subscription Status")
        st.pyplot(fig)

    # Category Performance
    if "category" in df.columns:
        st.write("### 📦 Orders by Category")
        category_sales = df["category"].value_counts().reset_index()
        category_sales.columns = ["Category", "Order Count"]
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(category_sales["Category"], category_sales["Order Count"])
        ax.set_title("Top Product Categories")
        st.pyplot(fig)

    # Review Rating by Category
    if "review_rating" in df.columns:
        st.write("### ⭐ Average Rating by Category")
        category_rating = df.groupby("category")["review_rating"].mean().reset_index()
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(category_rating["category"], category_rating["review_rating"])
        ax.set_title("Average Category Rating")
        st.pyplot(fig)

    # Repeat Buyers & Subscription
    if "previous_purchases" in df.columns:
        st.write("### 🔁 Repeat Buyers & Subscription")
        df["repeat_buyer"] = df["previous_purchases"].apply(lambda x: "Yes" if x > 5 else "No")
        repeat_sub = df.groupby(["repeat_buyer", "subscription_status"]).size().reset_index(name="count")
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(repeat_sub["subscription_status"], repeat_sub["count"])
        ax.set_title("Repeat Buyers vs Subscription Status")
        st.pyplot(fig)

    # Business Recommendations
    st.write("### 📢 Business Recommendations")
    st.markdown("""
    - Reward repeat buyers to improve retention.
    - Promote subscription perks to improve sign-ups.
    - Optimize discounts for profitability.
    - Prioritize high-rated and best-selling products.
    - Focus on high-revenue age segments (Young Adults).
    """)

except FileNotFoundError:
    st.error(f"❌ File not found at `{FILE_PATH}`. Please update the hardcoded path.")

# Footer
st.markdown("---")
st.markdown("📊 *Developed as part of the Customer Behavior Analysis Project*")