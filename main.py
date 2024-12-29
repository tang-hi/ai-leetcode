import os
from leetcode_api import LeetCodeAPI
from llm_model import LLMModel

def read_problem_statement(file_path):
    with open(file_path, 'r') as file:
        problem_statement = file.read()
    return problem_statement

def generate_solution(problem_statement, llm_model):
    prompt = f"Generate a Python solution for the following problem:\n\n{problem_statement}"
    solution_code = llm_model.generate_code(prompt)
    return solution_code

def submit_solution(problem_slug, solution_code, leetcode_api):
    result = leetcode_api.submit_solution(problem_slug, solution_code)
    return result

def main():
    problem_file = "problem.txt"
    problem_slug = "two-sum"  # Example problem slug
    api_key = os.getenv("OPENAI_API_KEY")

    leetcode_api = LeetCodeAPI()
    llm_model = LLMModel(api_key)

    problem_statement = read_problem_statement(problem_file)
    solution_code = generate_solution(problem_statement, llm_model)
    result = submit_solution(problem_slug, solution_code, leetcode_api)

    print("Solution Code:\n", solution_code)
    print("Submission Result:\n", result)

if __name__ == "__main__":
    main()
