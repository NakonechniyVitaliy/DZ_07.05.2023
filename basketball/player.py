
player_dict = [{
    "Имя" : "Виталий",
    "Фамилия": "Наконечный",
    "Отчество": "Романович",
    "Рост": "172"
},{
    "Имя" : "Олег",
    "Фамилия": "Титаренко",
    "Отчество": "Петрович",
    "Рост": "187"
}]
def new_player():
    name_1 = input("Введите имя игрока: ")
    name_2 = input("Введите фамилию игрока: ")
    name_3 = input("Введите отчество игрока: ")
    heigh = input("Введите рост игрока: ")
    player_dict.append({
        "\nИмя": name_1,
        "Фамилия": name_2,
        "Отчество": name_3,
        "Рост": heigh
    })

def delete_player():
    nomer = int(input("Напишите номер игрока которого хотите удалить со списка:"))
    player_dict.pop(nomer)

def find_player():
    poisk = input("Введите фамилию игрока по которому вы хотите найти информацию: ")
    for key, value in enumerate(player_dict):
        if value["Фамилия"] == poisk:
            print(key, value)

def edit_player():
    redak = int(input("Введите номер игрока по которому вы хотите изменить информацию: "))
    new_name = input("Введите имя ")
    new_name2 = input("Введите фамилию ")
    new_name3 = input("Введите отчество ")
    cm = input("Введите рост ")
    a[redak] = {
        "\nИмя": new_name,
        "Фамилия": new_name2,
        "Отчество": new_name3,
        "Рост": cm
    }
def player_list():
    for key, value in enumerate(player_dict):
        print(key+1, "-", value)