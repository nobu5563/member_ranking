import csv


def get_artist(group_name):
    name = []

    with open("data/{}.csv".format(group_name), "r", encoding="utf_8_sig") as f:
        r = csv.reader(f, delimiter="\n")
        for row in r:
            name.extend(row)

    return name