import time
import os
import requests
import datetime


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


# {"username":"dienesviktor","name":"Dienes Viktor","honor":684,"clan":"Codecool","leaderboardPosition":37155,"skills":["python","javascript"],"ranks":{"overall":{"rank":-5,"name":"5 kyu","color":"yellow","score":494},"languages":{"python":{"rank":-5,"name":"5 kyu","color":"yellow","score":494},"javascript":{"rank":-7,"name":"7 kyu","color":"white","score":20}}},"codeChallenges":{"totalAuthored":2,"totalCompleted":136}}


def get_datas(usernames):
    datas = []
    for user in usernames:
        response = requests.get(f"https://www.codewars.com/api/v1/users/{user}")
        user_data = response.json()
        username = user_data["username"]
        honor = user_data["honor"]
        rank = user_data["ranks"]["overall"]["name"]
        score = user_data["ranks"]["overall"]["score"]
        datas.append([username, rank, honor, score])
    datas = sorted(datas, key=lambda x: x[3], reverse=True)
    return datas


def print_datas(datas):
    print_actual_time()
    print("\n" + "Real-time Codewars leaderboard:" + "\n")
    for i in range(len(datas)):
        username = datas[i][0]
        rank = datas[i][1]
        honor = datas[i][2]
        score = datas[i][3]
        name = change_names(username)
        print(f"{i+1}. {name} - rank: {rank} - honor: {honor} - score: {score}")


def change_names(username):
    if username == "dienesviktor":
        username = "Dienes Viktor"
    elif username == "viktoriasoos":
        username = "Soós Viktória"
    elif username == "DevonCarswell":
        username = "Kasza Zsolt"
    elif username == "keczanilles":
        username = "Keczán Illés"
    elif username == "dalmacsernok":
        username = "Csernok Dalma"
    elif username == "karcagiakos":
        username = "Karcagi Ákos Csaba"
    elif username == "bfiics":
        username = "Ficsór Bence"
    elif username == "Rausz":
        username = "Rausz Ádám"
    elif username == "inf-vendel":
        username = "Bódi Vendel Róbert"
    return username


def print_actual_time():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def main():
    usernames = ["karcagiakos", "viktoriasoos", "dienesviktor", "dalmacsernok", "keczanilles", "DevonCarswell", "bfiics", "Rausz", "inf-vendel"]
    datas = get_datas(usernames)
    clear(0)
    print_datas(datas)


if __name__ == "__main__":
    main()
