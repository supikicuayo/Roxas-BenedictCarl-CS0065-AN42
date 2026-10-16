# CASE-BASED REASONING (CBR)
# Intelligent Tutoring System

# Step 1: Create the case base
case_base = [
    {
        "student": "Student 1",
        "problem": {
            "error": "wrong_formula",
            "topic": "algebra",
            "difficulty": "medium"
        },
        "solution": "Review the correct algebra formula and solve similar examples."
    },
    {
        "student": "Student 2",
        "problem": {
            "error": "calculation_error",
            "topic": "algebra",
            "difficulty": "easy"
        },
        "solution": "Practice basic calculations and check each step."
    },
    {
        "student": "Student 3",
        "problem": {
            "error": "wrong_formula",
            "topic": "geometry",
            "difficulty": "medium"
        },
        "solution": "Review geometry formulas and practice identifying the correct formula."
    },
    {
        "student": "Student 4",
        "problem": {
            "error": "concept_error",
            "topic": "algebra",
            "difficulty": "hard"
        },
        "solution": "Review the basic algebra concept and work through guided examples."
    }
]


# Step 2: Get a new student problem

print("INTELLIGENT TUTORING SYSTEM")
print("\nEnter the new student's problem:")

error = input("Error type (wrong_formula/calculation_error/concept_error): ").lower()
topic = input("Topic (algebra/geometry): ").lower()
difficulty = input("Difficulty (easy/medium/hard): ").lower()

new_problem = {
    "error": error,
    "topic": topic,
    "difficulty": difficulty
}


# Step 3: Similarity Assessment

def calculate_similarity(new_problem, old_problem):
    score = 0

    if new_problem["error"] == old_problem["error"]:
        score += 2

    if new_problem["topic"] == old_problem["topic"]:
        score += 2

    if new_problem["difficulty"] == old_problem["difficulty"]:
        score += 1

    return score


# Step 4: Retrieve the most similar case

best_case = None
best_score = -1

print("\nSimilarity Scores:")

for case in case_base:
    score = calculate_similarity(new_problem, case["problem"])

    print(case["student"], ":", score, "/ 5")

    if score > best_score:
        best_score = score
        best_case = case

print("\nRetrieved Case:")
print(best_case["student"])
print("Similarity Score:", best_score, "/ 5")
print("Previous Solution:", best_case["solution"])


# Step 5: Reuse and Adapt the Solution

adapted_solution = best_case["solution"]

if error == "wrong_formula":
    adapted_solution = "Review the correct formula for " + topic + " and solve similar practice problems."

elif error == "calculation_error":
    adapted_solution = "Practice " + topic + " calculations and check each step carefully."

elif error == "concept_error":
    adapted_solution = "Review the basic concepts of " + topic + " and complete guided practice problems."


print("\nAdapted Final Solution:")
print(adapted_solution)


# Step 6: Retain the New Case

new_case = {
    "student": "New Student",
    "problem": new_problem,
    "solution": adapted_solution
}

case_base.append(new_case)

print("\nNew case saved successfully!")


# Step 7: Display Updated Case Base

print("\nUpdated Case Base:")

for i, case in enumerate(case_base, 1):
    print(
        i,
        "-",
        case["student"],
        "|",
        case["problem"],
        "|",
        case["solution"]
    )