import re
from datasets import load_dataset
ds = load_dataset("netsol/resume-score-details")

print(ds['question'][0])


# answer_text = """Technical capabilities: 6 points, explanation: Candidates participated in the development and improvement of software projects, showing certain technical capabilities, but may need to be further improved in solving complex technical problems independently. Project management capabilities: 5 points, explanation: assist in the completion of the technical environment construction of the project, but have limited experience in project planning and resource management. Technical support capabilities: 7 points, explanation: Responsible for technical research and technical support, showing good problem solving and customer service capabilities. Compliance with technical specifications: 8 points, explanation: performance in ensuring compliance with technical specifications in project development, showing good professional qualities. Technology platform construction ability: 6 points, explanation: assist in building technology platform according to needs, but may require more practice and learning in innovation and optimization of existing platforms."""

# # Split into individual capability assessments
# capabilities = answer_text.split(". ")
# scores = []
# explanations = []
# categories = ["Technical capabilities", "Project management capabilities", "Technical support capabilities", "Compliance with technical specifications", "Technology platform construction ability"]

# for i, capability in enumerate(capabilities):
#     if capability.strip():  # Ignore empty strings
#         # Extract score
#         score_match = re.search(r"(\d+) points", capability)
#         if score_match:
#             scores.append(int(score_match.group(1)))
#         # Extract explanation
#         explanation_match = re.search(r"explanation: (.*)", capability)
#         if explanation_match:
#             explanations.append(explanation_match.group(1))

# # Map to categories (assuming order matches)
# new_answers = {cat: {"score": s, "explanation": e} for cat, s, e in zip(categories, scores, explanations)}

# print(new_answers)