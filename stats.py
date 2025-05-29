def wordcount(text):
    print("----------- Word Count ----------")
    words = text.split()
    return len(words)

def analyze(text):
    print("--------- Character Count -------")
    counts = {}
    for c in text:
        if c.isalpha():
            counts[c.lower()] = counts.get(c.lower(),0) + 1
    return counts

def dictsort(dict):
    sortDict = []
    for k,v in dict.items():
        sortDict.append({"char":k, "num":v})
    d = sorted(sortDict, key=lambda dict: dict["num"],reverse=True)
    return d
