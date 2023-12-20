#if __name__ == '__main__':
    #d_dict = []
    #for _ in range(int(input())):
        #name = input()
        #score = float(input())
        #d_dict.extend(list(name,score))
        #new_list = list(d_dict)
        #print(d_dict)
        #print(list([new_list]))

students = {}
scores = set()

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.update({name: score})
        scores.add(score)

    sortscores = sorted(list(scores))
    runnerup = sortscores[1]

    for names, scores in sorted(students.items()):
        if scores == runnerup:
            print(names)