import argparse
from argparse import RawDescriptionHelpFormatter
import numpy as np
import csv



def get_parse():

    help_desc = '''アーティストのランキングを作成
    以下のいずれかを小文字で入力してください
    - BLACKPINK
    - fromis_9
    - snsn
    - twice
    '''

    parser = argparse.ArgumentParser(description=help_desc,
                                     formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('group_name', type=str, help='アーティスト名')
    args = parser.parse_args()
    return args



def main(group_name):
    name = []

    with open("data/{}.csv".format(group_name), "r", encoding="utf_8_sig") as f:
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
                else:
                    print('error:"1"か"2"で入力してください')
                    print("終了")
                    exit()
                already[i][j] = 1
                already[j][i] = 1


    dic = dict(zip(name, score))
    result = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    print("\n")
    print("★☆★☆★☆ 結果発表 ☆★☆★☆★")

    for i in range(0, len(result)):
        print("{}位:{}".format(i+1, result[i]))

if __name__ == "__main__":
    print("グループ名を入れてください")
    args = get_parse()
    main(group_name=args.group_name)
