def cakes(recipe, available):
    max_cakes = float('inf')  # Start with infinity as the upper bound

    for i, j in recipe.items():
        if i not in available:
            return 0  # Missing ingredient means zero cakes
        max_possible = available[i] // j
        if max_possible < max_cakes:
            max_cakes = max_possible

    return max_cakes