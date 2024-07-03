from twikit import Client

from xbot.confing import config

if __name__ == "__main__":
    client = Client("ja")
    client.login(
        auth_info_1=config["USERNAME"],
        auth_info_2=config["EMAIL"],
        password=config["PASSWORD"],
    )
    users = client.search_user("夜勤")
    for user in users:
        print(vars(user))
