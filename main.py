import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

python_challenges = response.json()

for challenge in python_challenges:
    # Evaluate the expression
    solution = eval(challenge['problem'].replace("?", ""))
    # Add the solution to the dictionary
    challenge['solution'] = solution

# Now, the 'problems' list contains solutions as well
for i in python_challenges:
    print(i)