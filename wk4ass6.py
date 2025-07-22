grades = [55, 70, 65, 40, 90, 85, 50, 77]

apply_bonus = lambda grade: round(grade * 1.05, 2)

passed_with_bonus = [apply_bonus(g) for g in grades if g >= 60]

print("Grades after filtering and applying bonus:", passed_with_bonus)
