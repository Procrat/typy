from random import shuffle

def maakTrekking(familie):
    mensen = [x for gezin in familie for x in gezin]
    res = {k: None for k in mensen}
    shuffle(mensen)

    for k in res.keys():
        res[k] = mensen.pop()
    return res
