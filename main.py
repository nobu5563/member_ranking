import argparse
from argparse import RawDescriptionHelpFormatter
import numpy as np

from data_prepare import get_artist


def get_parse():

    help_desc = '''アーティストのランキングを作成
    以下のいずれかを入力してください
    - blackpink
    - fromis_9
    - snsn
    - twice
    - aespa
    '''

    parser = argparse.ArgumentParser(description=help_desc,
                                     formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('group_name', type=str, help='アーティスト名')
    args = parser.parse_args()
    return args



def main(group_name):

    name = get_artist(group_name)

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
    print("★☆★☆★☆ 結果発表 ☆★☆★☆★\n")

    for i in range(0, len(result)):
        print(f"{i+1}位:{result[i][0]}")
    print("\n")
    print('ランキング終了')

if __name__ == "__main__":
    print("グループ名を入れてください")
    args = get_parse()
    main(group_name=args.group_name)
