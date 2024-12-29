# LeetCode LLM Solver

This project aims to automatically solve LeetCode problems using different LLM (Language Learning Model) models. The project fetches the problem statement from LeetCode, uses an LLM model to generate a solution, and then submits the solution to LeetCode to check if it passes the test cases.

A lot of people said LLM models could replace software engineers and the vendor of the LLM model said it could write code better than a software engineer. This project aims to test that claim.

## Setup and Run

1. Clone the repository:
    ```sh
    git clone git@github.com:tang-hi/ai-leetcode.git
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Set up the environment variables:
    ```sh
    export LEETCODE_COOKIE="your_leetcode_cookie"
    export LEETCODE_CSRF_TOEKN="your_leetcode_csrf_token"
    ```
    Replace `LEETCODE_COOKIE` and `LEETCODE_CSRF_TOKEN` with your LeetCode cookie and CSRF token. You can find these values by inspecting the network requests when you log in to LeetCode.

4. Set up the LLM model:
    ```sh
    export API_KEY="your_openai_api_key"
    ```
    I use [aihubmix](https://aihubmix.com/) so I could use one api key for all models. You can use any other LLM model by changing `generate_solution` function in `main.py`.

5. Run the project:
    ```sh
    python main.py --contest ./contest/weekly-contest-430
    ```

## Tested Models
- claude-3-5-sonnet-20241022
- gemini-2.0-flash-exp
- gpt-4o


## Test Results

| Contest | Model | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- | --- |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | claude-3-5-sonnet-20241022 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | gemini-2.0-flash-exp | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | gpt-4o | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | o1 | :white_check_mark: | :x:  | :x: | :white_check_mark: |