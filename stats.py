def get_num_words(text):
    words = text.split()
    return len(words)

def number_of_symbols(text:str):
    symbols = {}
    unique_symbols = set()
    for t in text:
        t = t.lower()
        if t not in unique_symbols:
            symbols[t] = 1
            unique_symbols.add(t)
        else:
            symbols[t] += 1
    return symbols

def _sort_splitted_chars(chardict):
    return chardict["num"]

def split_into_char_dict(counts):
    dictlist = []
    for k,v in counts.items():
        dictlist.append({
            "char": k,
            "num": v
        })
    dictlist.sort(reverse=True, key=_sort_splitted_chars)
    return dictlist