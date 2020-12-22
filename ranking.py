import numpy as np

from images import show_images


def get_rank(group_name, name):
    """
    ランキングを作成

    Args:
        name (str): group name

    Returns:
        tuple: (name, score)
    """
    score = np.zeros(50)
    already = np.zeros((50, 50))

    print("---メンバーランキング---")

    for i in range(len(name)):
        for j in range(len(name)):
            if (name[i] != name[j]) and already[i][j] == 0:
                print("好きなメンバーの番号を入力してください")
                show_images(group_name=group_name, name_1=name[i], name_2=name[j])
                like = input(f"1:{name[i]} 2:{name[j]} ")
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

    return result