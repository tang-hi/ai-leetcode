import os
from leetcode_api import LeetCodeAPI
from openai import OpenAI
import argparse
import time


COOKIE = os.getenv("LEETCODE_COOKIE")
CSRF_TOKEN = os.getenv("LEETCODE_CSRF_TOKEN")
API_KEY = os.getenv("OPENAI_API")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://aihubmix.com/v1"
)


def generate_solution(problem_statement, llm_model, start_code, test_case):
    prompt = f"""You are an expert competitive programmer with extensive experience in algorithmic problem-solving and optimization.

PROBLEM DESCRIPTION:
{problem_statement}

STARTING CODE:
{start_code}

SAMPLE TEST CASE:
{test_case}

REQUIREMENTS:
1. Use the provided starting code template
2. Your solution must handle all edge cases
3. Optimize for both time and space complexity
4. The solution must pass not only the sample test case but also hidden test cases
5. Include brief comments explaining the time and space complexity

IMPORTANT NOTES:
- Consider edge cases like empty inputs, single elements, or maximum constraints
- The solution should be as efficient as possible
- Avoid using any external libraries not included in the starting code
- Return only the solution code that fits within the given template
- Only include the necessary code to solve the problem, don't include any unnecessary code or extra comments
- Don't explain what the code does or how it works, only write the code itself. The only thing you returned should be the python code(no markdown format only text).

The code you should return is just
{start_code}
        # code here


Please write the most efficient solution possible."""
    solution_code = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=llm_model
    )
    solution_code = solution_code.choices[0].message.content
    # if code wrap in ```python``` remove it
    if solution_code.startswith("```python"):
        solution_code = solution_code[9:-4]
    return solution_code


def main():
    llm_models = ['claude-3-5-sonnet-20241022',
                  'gemini-2.0-flash-exp', 'gpt-4o']
    llm_models_sloved = {model: {} for model in llm_models}
    # read weekly contest problems from argument
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--contest", type=str, required=True)
    args = argparser.parse_args()
    contest_file = args.contest

    leetcode_api = LeetCodeAPI(cookie=COOKIE, csrf_token=CSRF_TOKEN)
    problems = []
    with open(contest_file, 'r') as file:
        contest_problems = file.readlines()
        problems = [problem.strip() for problem in contest_problems]

    n = len(problems)
    print(f"Problems to solve: {problems}")
    for model in llm_models:
        for i in range(n):
            llm_models_sloved[model][problems[i]] = 0

    for problem in problems:
        problem_detail = leetcode_api.fetch_problem(problem)
        problem_statement = problem_detail["desc"]
        start_code = problem_detail["code"]
        test_case = problem_detail["test_case"]
        problem_id = problem_detail["id"]
        print(f"Problem: {problem_id}")

        for model in llm_models:
            solution_code = generate_solution(
                problem_statement, model, start_code, test_case)
            print(f"Solution generated for {problem} using {model}")
            print(f"Solution code: {solution_code}")
            status, response = leetcode_api.submit_solution(
                problem_id, problem, solution_code)
            if status == 200:
                print(f"Solution submitted successfully for {problem}")
                submission_id = response["submission_id"]
                print(f"Submission ID: {submission_id}")
            else:
                print(f"Failed to submit solution for {problem}")
                continue

            # wait 10s for the submission to be processed
            time.sleep(10)
            submission_state = leetcode_api.get_submission_state(submission_id)
            if submission_state["statusCode"] == 10:
                llm_models_sloved[model][problem] = 1
                print(f"Problem {problem} solved using {model}")

    for model in llm_models:
        print(f"Problems solved using {model}:")
        for problem, solved in llm_models_sloved[model].items():
            if solved:
                print(problem)


if __name__ == "__main__":
    main()
