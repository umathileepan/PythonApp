import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

#question_data = [
#{
#  "response_code": 0,
#  "results": [
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "Entertainment: Video Games",
#      "question": "The edutainment video game series character, Carmen Sandiego, is partially named after Brazilian actress, Carmen Miranda.",
#      "correct_answer": "True",
#      "incorrect_answers": [
#        "False"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "easy",
#      "category": "Entertainment: Board Games",
#      "question": "The card game &quot;Munchkin&quot; won the 2001 Origins Award for Best Traditional Card Game.",
#      "correct_answer": "True",
#      "incorrect_answers": [
#        "False"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "easy",
#      "category": "Entertainment: Film",
#      "question": "In the original script of &quot;The Matrix&quot;, the machines used humans as additional computing power instead of batteries.",
#      "correct_answer": "True",
#      "incorrect_answers": [
#        "False"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "Science &amp; Nature",
#      "question": "A defibrillator is used to start up a heartbeat once a heart has stopped beating.",
#      "correct_answer": "False",
#      "incorrect_answers": [
#        "True"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "Science: Mathematics",
#      "question": "You can square root a negative number with an imaginary number &quot;i&quot;.",
#      "correct_answer": "True",
#      "incorrect_answers": [
#        "False"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "Science &amp; Nature",
#      "question": "Type 1 diabetes is a result of the liver working improperly.",
#      "correct_answer": "False",
#      "incorrect_answers": [
#        "True"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "Entertainment: Video Games",
#      "question": "The game series &quot;Titanfall&quot; runs on the Unreal Engine.",
#      "correct_answer": "False",
#      "incorrect_answers": [
#        "True"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "General Knowledge",
#      "question": "You are allowed to sell your soul on eBay.",
#      "correct_answer": "False",
#      "incorrect_answers": [
#        "True"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "medium",
#      "category": "Sports",
#      "question": "Formula E is an auto racing series that uses hybrid electric race cars.",
#      "correct_answer": "False",
#      "incorrect_answers": [
#        "True"
#      ]
#    },
#    {
#      "type": "boolean",
#      "difficulty": "easy",
#      "category": "Entertainment: Music",
#      "question": "Muse is a British (English) rock band",
#      "correct_answer": "True",
#      "incorrect_answers": [
#        "False"
#      ]
#    }
#  ]
#}
#]
