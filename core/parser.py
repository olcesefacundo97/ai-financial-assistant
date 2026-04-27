def parse_input(text):
    text = text.lower()

    profile = {
        "type": None,
        "income": 0,
        "wants_no_fee": "no maintenance" in text or "no fee" in text,
        "travel": "travel" in text
    }

    if "card" in text:
        profile["type"] = "credit_card"
    elif "loan" in text:
        profile["type"] = "loan"

    for word in text.split():
        if word.isdigit():
            profile["income"] = int(word)

    return profile
