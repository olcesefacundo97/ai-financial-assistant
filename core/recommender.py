def score_product(product, profile):
    score = 0

    if product.get("type") == profile.get("type"):
        score += 3

    if profile.get("income", 0) >= product.get("min_income", 0):
        score += 2

    if profile.get("wants_no_fee") and product.get("maintenance_fee", 0) == 0:
        score += 2

    if profile.get("travel") and "travel" in product.get("benefits", []):
        score += 2

    return score
