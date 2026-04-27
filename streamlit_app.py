import streamlit as st
import pandas as pd
from core.loader import load_products
from core.parser import parse_input
from core.recommender import score_product
from core.simulator import simulate_cost

st.set_page_config(page_title="AI Financial Assistant", layout="wide")

st.title("💡 AI Financial Decision Assistant")
st.markdown("### AI-powered financial recommendations with explainability")

user_input = st.text_area("Describe your financial need",
                          "I earn 800000 ARS and want a credit card with no maintenance fee and travel benefits")

if st.button("Get Recommendation"):
    products = load_products()
    profile = parse_input(user_input)

    scored = [(p, score_product(p, profile)) for p in products]
    scored.sort(key=lambda x: x[1], reverse=True)

    best_product, best_score = scored[0]
    cost = simulate_cost(best_product)

    st.success(f"Best match: {best_product['name']} ({best_product['provider']})")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Why this is recommended")
        reasons = []
        if best_product['maintenance_fee'] == 0:
            reasons.append("No maintenance fee")
        if 'travel' in best_product['benefits']:
            reasons.append("Includes travel benefits")
        if profile['income'] >= best_product['min_income']:
            reasons.append("You meet the income requirement")

        for r in reasons:
            st.write(f"✔ {r}")

        st.subheader("💰 Estimated monthly cost")
        st.metric("Cost", f"{cost} ARS")

    with col2:
        st.subheader("📊 Product details")
        st.write(best_product['description'])
        st.write(f"Benefits: {', '.join(best_product['benefits'])}")

    st.subheader("📈 Alternatives")

    df = pd.DataFrame([
        {
            "Product": p['name'],
            "Provider": p['provider'],
            "Score": s,
            "Fee": p['maintenance_fee']
        }
        for p, s in scored
    ])

    st.dataframe(df)

    st.markdown("---")
    st.markdown("**This prototype shows how AI can act as the decision layer of a financial marketplace.**")
