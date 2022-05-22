m = 0
while True :
    score = input('enter a score:')
    try:
        score = float(score)
        if score >= 70:
            print('A')
        elif score >= 60:
            print('B')
        elif score >= 50:
            print('C')
        elif score >= 45:
            print('D')
        elif score < 45:
            print('F')
        else:
            print('no score')
    except :
        print('invalid syntax: error (please enter a correct score)')
    continue
quit()

