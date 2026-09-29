import random

responses = [
    "It is certain",
    "Without a doube",
    "Most likely",
    "Ask again later",
    "Acan not predict",
    "The rain that falls.",
]


def get_eight_ball_response():
    return random.choice(responses)
