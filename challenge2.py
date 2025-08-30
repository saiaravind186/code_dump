def check(score):
    if score<50:
        print("fail")
    else:
        print("pass")

score = (int)(input("Enter Score : "))
while (score >= 0):
            check(score)
            score = (int)(input("Enter score : "))
