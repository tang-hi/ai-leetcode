import requests
from string import Template
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json


class LeetCodeAPI:
    def __init__(self, cookie, csrf_token, base_url="https://leetcode.com"):
        self.base_url = base_url
        self.headers = {
            "Cookie": cookie,
            "x-csrftoken": csrf_token,
            "Content-Type": "application/json",
            "Referer": base_url
        }
        self.graphql = base_url + "/graphql"
        self.transport = RequestsHTTPTransport(
            url=self.graphql, headers=self.headers, use_json=True, retries=3)
        self.client = Client(
            transport=self.transport, fetch_schema_from_transport=False)

    def fetch_problem(self, problem_slug):
        problem_query = gql(
            """
            query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                titleSlug
                content
                sampleTestCase
                codeSnippets {
                    lang
                    langSlug
                    code
                }
            }
            }
            """
        )
        params = {"titleSlug": problem_slug}
        result = self.client.execute(problem_query, variable_values=params)
        problem_description = result["question"]["content"]

        # get code template for python3
        code_snippets = result["question"]["codeSnippets"]
        code_template = None
        for code in code_snippets:
            if code["lang"] == "Python3":
                code_template = code["code"]
                break
        sample_test_case = result["question"]["sampleTestCase"]
        question_id = result["question"]["questionId"]
        return {"desc": problem_description, "code": code_template, "test_case": sample_test_case, "id": question_id}

    def submit_solution(self, problem_id, problem_slug, solution_code):
        url = f"{self.base_url}/problems/{problem_slug}/submit/"
        post_data = {
            "lang": "python3",
            "question_id": problem_id,
            "typed_code": solution_code
        }
        response = requests.post(url, json=post_data, headers=self.headers)
        if response.status_code != 200:
            return response.status_code, response.text
        return response.status_code, response.json()

    def get_submission_state(self, submission_id):
        submission_query = gql(
            """
            query submissionDetails($id: Int!) {
                submissionDetails(submissionId: $id) {
                    timestamp
                    statusCode
                    lastTestcase
                }
                }
            """
        )
        params = {"id": submission_id}
        result = self.client.execute(submission_query, variable_values=params)
        return result["submissionDetails"]
