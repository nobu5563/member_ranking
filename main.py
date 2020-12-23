import argparse
from argparse import RawDescriptionHelpFormatter

from data_prepare import get_artist
from ranking import get_rank


def get_parse():

    help_desc = '''アーティストのランキングを作成
    以下のいずれかを入力してください
    - blackpink
    - fromis_9
    - snsn
    - twice
    - aespa
    - izone
    '''

    parser = argparse.ArgumentParser(description=help_desc,
                                     formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('group_name', type=str, help='アーティスト名')
    args = parser.parse_args()
    return args



def main(group_name):

    name = get_artist(group_name)

    result = get_rank(group_name=group_name, name_list=name)

    print("\n")
    print("★☆★☆★☆ 結果発表 ☆★☆★☆★\n")

    for i in range(0, len(result)):
        print(f"{i+1}位:{result[i][0]}")
    print("\n")

    print('ランキング終了')



if __name__ == "__main__":
    args = get_parse()
    main(group_name=args.group_name)
