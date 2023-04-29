import random

animals = ["개미", "박쥐", "고양이", "개", "장어"]
adjectives = ["큰", "작은", "귀여운", "냄새나는", "반짝이는"]

choiceAnimal = random.choice(animals)
choiceAdjective = random.choice(adjectives)

print("저에게는", choiceAdjective, choiceAnimal, "가 있습니다.")