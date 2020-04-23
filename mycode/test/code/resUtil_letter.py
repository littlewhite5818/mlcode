
import numpy as np


# 加载数据
def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip(' ').split('\t')
            data.append(np.float64(d))
    file.close()
    return data



if __name__ == '__main__':

    data = dataLoad(r'C:\Users\zz\Desktop\res\cbof\letter.txt')
    m = [25, 50, 80, 100,120,250,300,500, 800, 950]
    n = 0
    num = 100
    rankPower = 0
    Recall = 0
    Prcesion = 0
    sum = 0
    for i in range(1, len(data)+1):
        if 0 <= data[i-1] < num:
            sum = sum + i
            n = n + 1
        if i in m:
            Recall = n / num
            Prcesion = n / i
            rankPower = (n*(n+1))/(2*sum)
            print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if n == num:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
            # break
        # if i == 80:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 120:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 200:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 280:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 300:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 200:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 250:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n*(n+1))/(2*sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        # if i == 450:
        #     Recall = n / num
        #     Prcesion = n / i
        #     rankPower = (n * (n + 1)) / (2 * sum)
        #     print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2), " RankPower: ", round(rankPower, 2))
        #     break
