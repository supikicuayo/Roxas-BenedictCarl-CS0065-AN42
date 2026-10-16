# IMPLEMENTING KNOWLEDGE REPRESENTATION, RBR, AND CBR

# PART 1 - KNOWLEDGE REPRESENTATION

facts = {
    "temperature": 32,
    "is_raining": False,
    "humidity": 85,
    "is_cloudy": True,
    "wind_speed": 20,
    "status": "hot"
}

print("KNOWLEDGE BASE")
for key, value in facts.items():
    print(key, ":", value)


# PART 2 - RULE-BASED REASONING

def rule_hot(facts):
    if facts["temperature"] > 30:
        return "Turn on the aircon"


def rule_humid(facts):
    if facts["humidity"] > 80:
        return "Drink more water"


def rule_cloudy(facts):
    if facts["is_cloudy"]:
        return "Bring an umbrella"


def rule_windy(facts):
    if facts["wind_speed"] > 15:
        return "Be careful of strong winds"


rules = [
    rule_hot,
    rule_humid,
    rule_cloudy,
    rule_windy
]

print("\nRULE-BASED REASONING ACTIONS:")

actions = []

for rule in rules:
    result = rule(facts)

    if result:
        actions.append(result)
        print("-", result)


# PART 3 - CASE-BASED REASONING

case_base = [
    {
        "problem": {
            "temperature": 35,
            "is_raining": False,
            "humidity": 80
        },
        "solution": "Stay indoors and drink plenty of water."
    },
    {
        "problem": {
            "temperature": 28,
            "is_raining": True,
            "humidity": 85
        },
        "solution": "Bring an umbrella and avoid flooded areas."
    },
    {
        "problem": {
            "temperature": 30,
            "is_raining": False,
            "humidity": 70
        },
        "solution": "Stay hydrated and avoid too much outdoor activity."
    }
]


new_case = {
    "temperature": int(input("\nEnter current temperature: ")),
    "is_raining": input("Is it raining? (yes/no): ").lower() == "yes",
    "humidity": int(input("Enter humidity: "))
}


# Task 3B - Similarity Assessment

def calculate_similarity(new_problem, old_problem):
    score = 0

    if new_problem["temperature"] >= 30 and old_problem["temperature"] >= 30:
        score += 1

    if new_problem["is_raining"] == old_problem["is_raining"]:
        score += 1

    if abs(new_problem["humidity"] - old_problem["humidity"]) <= 10:
        score += 1

    return score


best_case = None
best_score = -1

print("\nCBR SIMILARITY SCORES:")

for i, case in enumerate(case_base, 1):
    score = calculate_similarity(new_case, case["problem"])

    print("Case", i, ":", score, "/ 3")

    if score > best_score:
        best_score = score
        best_case = case


# Task 3C - Reuse

print("\nRETRIEVED CASE:")
print(best_case["problem"])
print("Similarity Score:", best_score, "/ 3")

print("\nREUSED SOLUTION:")
print(best_case["solution"])


# Task 3D - Revise

revised_solution = input(
    "\nEnter a revised solution, or press Enter to keep the original: "
)

if revised_solution.strip() == "":
    final_solution = best_case["solution"]
else:
    final_solution = revised_solution


print("\nFINAL SOLUTION:")
print(final_solution)


# Task 3E - Retain

new_case_with_solution = {
    "problem": new_case,
    "solution": final_solution
}

case_base.append(new_case_with_solution)

print("\nNew case saved successfully!")

print("\nUPDATED CASE BASE:")

for i, case in enumerate(case_base, 1):
    print("Case", i)
    print("Problem:", case["problem"])
    print("Solution:", case["solution"])
    print()