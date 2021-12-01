from letter_combinations.push_front import push_front


def char_map(P, l):
    result = []
    for c in P:
        result.extend(push_front(c, l))
    return result