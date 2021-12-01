def is_unbalanced(str_):
    c_open = str_.count('{')
    s_open = str_.count('[')
    p_open = str_.count('(')

    c_closed = str_.count('}') * -1
    s_closed = str_.count(']') * -1
    p_closed = str_.count(')') * -1

    c_score = c_closed + c_open
    s_score = s_closed + s_open
    p_score = p_closed + p_open

    if c_score != 0 or s_score != 0 or p_score != 0:
        return True
    return False