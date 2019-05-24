import numpy as np
import csv

name = []

with open("BLACKPINK.csv", "r", encoding="utf_8_sig") as f:
    r = csv.reader(f, delimiter="\n")
    for row in r:
        name.extend(row)

score = np.zeros(50)
already = np.zeros((50, 50))

print("---メンバーランキング---")

for i in range(len(name)):
    for j in range(len(name)):
        if (name[i] != name[j]) and already[i][j] == 0:
            like = input("1:{} 2:{} ".format(name[i], name[j]))
            if like == "1":
                score[i] += 1
            elif like == "2":
                score[j] += 1
            already[i][j] = 1
            already[j][i] = 1

dic = dict(zip(name, score))
result = sorted(dic.items(), key=lambda x:x[1], reverse=True)

print("★☆★☆★☆ 結果発表 ☆★☆★☆★")

for i in range(0, len(result)):
    print("{}位:{}".format(i+1, result[i]))
