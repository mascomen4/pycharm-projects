import random

def get_forenames_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"),
                                (surnames, "data/surnames.txt")):
        for name in open(filename, encoding = "utf8"):
            names.append(name.rstrip())
    return forenames, surnames
forenames, surnames = get_forenames_surnames()
fh = open("test-names1.txt", "w", encoding = "utf8")
for i in range(100):
    name = "{0} {1}".format(random.choice(forenames),
                              random.choice(surnames))
    result = "{0:.<25}.{1} \n".format(name, random.randint(1900,2100))
    fh.write(result)
