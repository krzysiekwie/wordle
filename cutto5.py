with open("word-list-raw.txt") as f:
    with open("5-letter-words.txt", "w") as f1:
        for line in f:
            if "'" not in line:
                if len(line) == 6:
                    print(line)
                    f1.write(line)
