def all_variants(text):
    for start in range(len(text)):
        yield text[start]
    for start in range(len(text)):
        for end in range(start+2, len(text)+1):
            yield text[start:end]


a = all_variants("abcd")
for i in a:
    print(i)