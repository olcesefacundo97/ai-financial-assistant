import streamlit as st
from core.loader import load_products
from core.parser import parse_input
from core.recommender import recommend
from core.simulator import simulate_cost

st.set_page_config(page_title="AI Financial Assistant", layout="centered")

st.title("💡 AI Financial Decision Assistant")
st.write("Describe your financial need and get a recommendation.")

user_input = st.text_area("Your request", "I earn 800000 ARS and want a credit card with no maintenance fee and travel benefits")

if st.button("Get Recommendation"):
    products = load_products()
    profile = parse_input(user_input)
    best_product, score = recommend(products, profile)
    cost = simulate_cost(best_product)

    st.subheader("✅ Best Recommendation")
    st.write(f"**{best_product['name']}**")

    st.subheader("🧠 Why this matches")
    if best_product['maintenance_fee'] == 0:
        st.write("- No maintenance fee")
    if 'travel' in best_product['benefits']:
        st.write("- Includes travel benefits")
    if profile['income'] >= best_product['min_income']:
        st.write("- Meets income requirement")

    st.subheader("💰 Estimated Cost")
    st.write(f"{cost} ARS / month")

    st.subheader("📊 Score")
    st.write(score)
