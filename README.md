# AI Financial Decision Assistant

An AI-first prototype inspired by Compara's mission: helping users make better financial decisions through transparency, automation and intelligent product comparison.

This project simulates a financial marketplace assistant where users describe their needs in natural language and receive personalized, explainable recommendations for financial products.

The goal is not to build a generic chatbot. The goal is to show how AI can become the decision layer of a financial marketplace.

---

## Why this project exists

Financial users often struggle to understand which product is best for them. A credit card, loan or account may look attractive, but the real decision depends on income, preferences, fees, travel habits, risk tolerance and total cost.

This prototype explores how an AI-first fintech could:

- Understand user intent from natural language.
- Convert unstructured needs into a structured financial profile.
- Compare products using deterministic business rules.
- Generate explainable recommendations.
- Simulate financial impact.
- Create a foundation for future agentic workflows.

---

## Product concept

> "Tell me what you need. I will compare the market, explain the trade-offs and help you make a better financial decision."

Example user input:

```text
I want a credit card with no maintenance fees. I earn 800000 ARS per month and travel often.
```

Expected output:

- Detected intent: credit card recommendation.
- Extracted user profile: income, preferences, travel behavior.
- Ranked financial products.
- Explanation of the best match.
- Trade-offs against alternatives.
- Simple affordability and cost simulation.

---

## Current MVP scope

This first version includes:

- A mock dataset of financial products.
- A natural-language parser based on rule extraction.
- A recommendation engine.
- A financial simulator.
- A CLI demo.
- Unit tests for core logic.

The architecture is intentionally simple so it can evolve into an LLM-powered assistant, API or Streamlit demo.

---

## Project structure

```text
ai-financial-assistant/
├── app.py
├── data/
│   └── products.json
├── core/
│   ├── __init__.py
│   ├── loader.py
│   ├── parser.py
│   ├── recommender.py
│   └── simulator.py
├── tests/
│   └── test_recommender.py
├── requirements.txt
└── README.md
```

---

## How it works

### 1. User intent parsing

The assistant receives a natural language request and extracts a structured profile:

- Product type
- Monthly income
- Desired benefits
- Fee sensitivity
- Travel preference
- Loan amount and installments, when applicable

### 2. Product matching

The recommendation engine compares the user's profile against the product dataset.

It scores products based on:

- Product type match
- Maintenance cost
- Income eligibility
- Benefits alignment
- Travel-related benefits
- Interest rate or total cost, when applicable

### 3. Explainable recommendation

Each recommendation includes:

- Product score
- Reasons why it fits
- Potential trade-offs
- Estimated monthly cost

---

## Run locally

```bash
python app.py
```

Run tests:

```bash
python -m pytest
```

---

## Example

```bash
python app.py "I earn 800000 ARS and want a credit card with no maintenance fee and travel benefits"
```

Example output:

```text
Best recommendation: Travel Light Credit Card
Why it matches:
- No monthly maintenance fee
- Includes travel benefits
- User income meets product requirement
Estimated monthly cost: 0 ARS
```

---

## Future improvements

- Add an LLM-based parser for better natural language understanding.
- Add embeddings to match user preferences with product descriptions.
- Build a Streamlit or FastAPI interface.
- Add agentic monitoring: notify the user when a better product appears.
- Add real financial formulas for loans and APR comparison.
- Add explainability metrics and confidence scoring.
- Add a product admin module to simulate marketplace operations.

---

## Positioning

This project is designed as a practical AI product prototype, not just a technical exercise.

It reflects the kind of AI-first thinking needed to build a financial marketplace where users do not simply browse products, but receive personalized and transparent decision support.
