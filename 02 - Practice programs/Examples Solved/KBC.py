
def correct():
    print("Sahiiii jawaaaaaaaaaaab")
    print("Your current points: ",points)
def Wrong():
    print("Galat jawab :(")


print("Q1. What is Anirudh's age?       P :1")
age = int(input())
points = 0
if age == 20:
    points = points + 1
    correct()
else:
    Wrong()
print("Q1. What is Anirudh's fav color?       P :1")
color = input()
if color  == 'red' or 'RED' or 'Red':
    points = points + 1
    correct()
else:
    Wrong()

