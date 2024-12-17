
languages = [
#       e.g. of how should it be written:
#     {"name": "Python", "difficulty": 15, "speed": 50, "documentation": 20, "use_rate": 0.23, "platforms": 8},
#     {"name": "C++", "difficulty": 1, "speed": 1, "documentation": 19, "use_rate": 0.15, "platforms": 10},
#     {"name": "JavaScript", "difficulty": 5, "speed": 10, "documentation": 16, "use_rate": 0.43, "platforms": 8},
#     {"name": "Java", "difficulty": 12, "speed": 20, "documentation": 16, "use_rate": 0.35, "platforms": 9},
#     {"name": "C#", "difficulty": 9, "speed": 15, "documentation": 18, "use_rate": 0.25, "platforms": 9},
#     {"name": "Go", "difficulty": 11, "speed": 5, "documentation": 15, "use_rate": 0.1, "platforms": 7},
#     {"name": "Rust", "difficulty": 14, "speed": 8, "documentation": 8, "use_rate": 0.02, "platforms": 7},
#     {"name": "Ruby", "difficulty": 9, "speed": 40, "documentation": 15, "use_rate": 0.05, "platforms": 7},
#     {"name": "Swift", "difficulty": 12, "speed": 15, "documentation": 12, "use_rate": 0.1, "platforms": 8},
#     {"name": "ASM", "difficulty": 10, "speed": 0.1, "documentation": 20, "use_rate": 0.013, "platforms": 12},
]

# Calculate the score for each language using the provided formula
for lang in languages:
    lang["score"] = (lang["difficulty"] / lang["speed"]) * lang["documentation"] * lang["use_rate"] * lang["platforms"]

# Sorting the best
languages_sorted = sorted(languages, key=lambda x: x["score"], reverse=True)

for lang in languages_sorted:
    print(f"{lang['name']}: {lang['score']:.2f}")
