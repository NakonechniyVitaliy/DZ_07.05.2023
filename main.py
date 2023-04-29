from basketball.player import new_player,delete_player,find_player,edit_player,player_list
from basketball.team import team_list, new_team_def,team_def
from basketball.utils import winner

while True:
    print("1)Додати інформацію \n2)Видалити інформацію \n3)Знайти інформацію "
          "\n4)Змінити інформацію \n5)Вивести список гравців\n6)Додати нову команду"
          "\n7)Вивести список команд")
    b = input("Ваша дія: ")
    if b == "1":
        new_player()

    elif b == "2":
        delete_player()

    elif b == "3":
        find_player()

    elif b == "4":
        edit_player()

    elif b == "5":
        player_list()

    elif b == "6":
        new_team_def()

    elif b == "7":
        team_def()

    elif b == "8":
        winner()

