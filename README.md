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

    ### How to get LeetCode Cookie and CSRF Token
    Firefox:
    1. Open the LeetCode website.
    2. Press `F12` to open the developer tools.
    3. Go to the `Network` tab.
    4. Log in to LeetCode.
    5. Find the request to `leetcode.com` in the network requests.
    6. Find the `Cookie` headers in the request headers.

    ![Firefox Cookie](./imgs/cookie.png)

    7. Copy the value of the `Cookie` header and set it as the `LEETCODE_COOKIE` environment variable.
    8. Extract the `csrftoken` value from the `Cookie` header and set it as the `LEETCODE_CSRF_TOKEN` environment variable.

    Chrome:
    1. Open the LeetCode website.
    2. Press `F12` to open the developer tools.
    3. Go to the `Application` tab.
    4. Find the `Cookies` section in the left sidebar.
    5. Find the `csrftoken` cookie.

    ![Chrome Cookie](./imgs/chrome-csrf.png)

    6. Copy the value of the `Value` field and set it as the `LEETCODE_CSRF_TOKEN` environment variable.
    7. Go to the `Network` tab.
    8. Find the request to `leetcode.com` in the network requests.
    9. Find the `Cookie` headers in the request headers.

    ![Chrome Cookie](./imgs/chrome-cookie.png)

    10. Copy the value of the `Cookie` header and set it as the `LEETCODE_COOKIE` environment variable.


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
- gemini-exp-1206
- o1-preview


## Test Results

| Contest | Model | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- | --- |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | claude-3-5-sonnet-20241022 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | gemini-2.0-flash-exp | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | gpt-4o | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 430](https://leetcode.com/contest/weekly-contest-430) | o1 | :white_check_mark: | :x:  | :x: | :white_check_mark: |
| [Weekly Contest 431](https://leetcode.com/contest/weekly-contest-431) | claude-3-5-sonnet-20241022 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 431](https://leetcode.com/contest/weekly-contest-431) | gemini-exp-1206 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 431](https://leetcode.com/contest/weekly-contest-431) | o1-preview | :white_check_mark: | :white_check_mark:  | :x: | :white_check_mark: |
| [Weekly Contest 432](https://leetcode.com/contest/weekly-contest-432) | claude-3-5-sonnet-20241022 | :x: | :x:  | :x: | :x: |
| [Weekly Contest 432](https://leetcode.com/contest/weekly-contest-432) | gemini-exp-1206 | :x: | :white_check_mark:  | :x: | :x: |
| [Weekly Contest 432](https://leetcode.com/contest/weekly-contest-432) | o1-preview | :white_check_mark: | :white_check_mark:  | :white_check_mark: | :x: |
| [Weekly Contest 433](https://leetcode.com/contest/weekly-contest-433) | claude-3-5-sonnet-20241022 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 433](https://leetcode.com/contest/weekly-contest-433) | gemini-exp-1206 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 433](https://leetcode.com/contest/weekly-contest-433) | o1-preview | :white_check_mark: | :white_check_mark:  | :x: | :x: |
| [Weekly Contest 434](https://leetcode.com/contest/weekly-contest-433) | claude-3-5-sonnet-20241022 | :white_check_mark: | :x:  | :x: | :x: |
| [Weekly Contest 434](https://leetcode.com/contest/weekly-contest-433) | deepseek-reasoner | :white_check_mark: | :white_check_mark:  | :white_check_mark: | :x: |
| [Weekly Contest 434](https://leetcode.com/contest/weekly-contest-433) | o1-preview | :white_check_mark: | :white_check_mark:  | :x: | :x: |