import itertools

def combine(PINS, ADJ):
    result = []
    for P in PINS:
        for n in ADJ:
            aux = P+n
            result.append(aux[::-1]) # string reverse

    return result


def getPins(PIN):
    adyacentes = {}
    adyacentes[0] = ["0","8"]
    adyacentes[1] = ["1","2","4"]
    adyacentes[2] = ["1","2","3","5"]
    adyacentes[3] = ["2","3","6"]
    adyacentes[4] = ["1","4","5","7"]
    adyacentes[5] = ["2","4","5","6","8"]
    adyacentes[6] = ["3","5","6","9"]
    adyacentes[7] = ["4","7","8"]
    adyacentes[8] = ["5","7","8","9","0"]
    adyacentes[9] = ["6","8","9"]


    if len(PIN) == 1:
        return map(lambda x : x+"", adyacentes[int(PIN[0])])
    else:
        actual = PIN[0]
        resto = PIN[1:]

        return map(lambda x: combine(x,adyacentes[int(actual)]), getPins(resto))


if __name__ == "__main__":
    PINS=sorted(list(itertools.chain.from_iterable(getPins("55555555"))))
    print(PINS)


