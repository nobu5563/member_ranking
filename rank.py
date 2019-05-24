import numpy as np
import csv

name = []

print("☆ランキングを作りたいグループ名を入力してください☆")

group = input()

with open("{}.csv".format(group), "r", encoding="utf_8_sig") as f:
    r = csv.reader(f, delimiter="\n")
    for row in r:
        name.extend(row)

score = np.zeros(50)
already = np.zeros((50, 50))

print("---メンバーランキング---")

for i in range(len(name)):
    for j in range(len(name)):
        if (name[i] != name[j]) and already[i][j] == 0:
            print("好きなメンバーの番号を入力してください")
            like = input("1:{} 2:{} ".format(name[i], name[j]))
            if like == "1":
                score[i] += 1
            elif like == "2":
                score[j] += 1
            already[i][j] = 1
            already[j][i] = 1

dic = dict(zip(name, score))
result = sorted(dic.items(), key=lambda x:x[1], reverse=True)

print("\n")
print("★☆★☆★☆ 結果発表 ☆★☆★☆★")

for i in range(0, len(result)):
    print("{}位:{}".format(i+1, result[i]))
