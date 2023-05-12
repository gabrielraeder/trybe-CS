string = "serdevemuitolegalmasehprecisoestudarbastante"


def substring(string):
    seen_before = set()
    subs = []

    new_sub = ""
    for letter in string:
        if letter not in seen_before:
            new_sub += letter
            seen_before.add(letter)
        else:
            subs.append(new_sub)
            seen_before.clear()
            new_sub = letter
            seen_before.add(letter)
    biggest = subs[0]
    for sub in subs:
        if len(sub) > len(biggest):
            biggest = sub
    print(subs)
    return biggest


print(substring(string))
