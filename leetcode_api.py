import requests

class LeetCodeAPI:
    def __init__(self, base_url="https://leetcode.com"):
        self.base_url = base_url

    def fetch_problem(self, problem_slug):
        url = f"{self.base_url}/problems/{problem_slug}/description/"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def submit_solution(self, problem_slug, solution_code):
        url = f"{self.base_url}/problems/{problem_slug}/submit/"
        payload = {
            "lang": "python3",
            "typed_code": solution_code
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
