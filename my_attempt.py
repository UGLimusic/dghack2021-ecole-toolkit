import json
from copy import deepcopy
from random import sample, randint


def import_data() -> list[list[int]]:
    with open("dghack2021-ecole-repartition.json", 'r') as rf:
        data = json.load(rf)
    result = [None]
    for k in data:
        result.append(k['friends'])
    return result


def compute_score_for_class(cls: list[int]) -> int:
    result = 0
    for i in cls:
        for j in cls:
            if j in prefs[i]:
                result += 20 - 5 * prefs[i].index(j)
    return result


def compute_score(lst: list[list[int]]) -> int:
    return sum(compute_score_for_class(c) for c in lst)


def iterate(lst: [list[list[int]]]) -> tuple[int, list[list[int]]]:
    tmp_score = 0
    tmp = deepcopy(lst)
    choices = []
    while tmp_score < 2950:
        i1, i2 = sample((0, 1, 2), 2)
        j1, j2 = randint(0, 29), randint(0, 29)
        while (i1, i2, j1, j2) in choices or (i2, i1, j2, j1) in choices:
            i1, i2 = sample((0, 1, 2), 2)
            j1, j2 = randint(0, 29), randint(0, 29)
        choices.append((i1, i2, j1, j2))
        tmp[i1][j1], tmp[i2][j2] = tmp[i2][j2], tmp[i1][j1]
        tmp_score2 = compute_score(tmp)

        if tmp_score2 <= tmp_score:
            tmp[i1][j1], tmp[i2][j2] = tmp[i2][j2], tmp[i1][j1]
        else:
            tmp_score = tmp_score2
            print(tmp_score)
    return tmp_score, tmp


prefs = import_data()

lst = [[i + j * 30 for i in range(1, 31)] for j in range(3)]
print(iterate(lst))
