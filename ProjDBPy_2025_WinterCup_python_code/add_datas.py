from def_area import *
from datetime import datetime

def select_data_teams():
    get_teams = select_teams()
    for team in get_teams:
        print(f"{team[0]} - {team[1]} - {team[2]}")

def select_data_highschool():
    get_highschool = select_highschool()
    for highschool in get_highschool:
        print(f"{highschool[0]} - {highschool[1]} - {highschool[2]} - {highschool[3]}")

def select_data_coachs():
    get_coach = select_coaches()
    for coach in get_coach:
        print(f"{coach[0]} - {coach[1]} - {coach[2]} - {coach[3]} - {coach[4]}")

def select_data_players():
    get_player = select_players()
    for player in get_player:
        print(f"\n{player[0]} - {player[1]} - {player[2]} - {player[3]} - {player[4]} - {player[5]} - {player[6]} - {player[7]}")

def select_data_tournament():
    get_tournament = select_tournament()
    for tournament in get_tournament:
        print(f"{tournament[0]} - {tournament[1]} - {tournament[2]} - {tournament[3]} - {tournament[4]} - {tournament[5]}")

# Pas d'idée pour l'instant de comment code cette partie que a une table intermediaire
def select_player_statistics():
    pass



def insert_datas_highschool():
    while True:
        print("Rentrez les informations de l'école: ")
        name_highschool = input("Nom de l'école: ")
        addres_highschool = input("Adresse de l'école: ")
        prefecture_highschool = input("Nom prefecture highschool: ")
        try:
            add_data_highschool(name_highschool, addres_highschool, prefecture_highschool)
            print("\nLes données ont été bien enregistrer")
            break
        except ValueError as err:
            print(err)

def insert_datas_teams():
    while True:
        print("Rentrez les informations de la team: ")
        name_team = input("Nom de la team: ")
        while True:
            creation_date = input("Entrez la date sous format [yyyy-mm-dd]")
            try:
                creation_date=datetime.strptime(creation_date,'%Y-%m-%d')
                break
            except ValueError:
                print("La date doit être sous format [yyyy-mm-dd]")
        try:
            add_data_teams(name_team,creation_date)
            print("\nLes données ont été bien enregistrer")
            break
        except ValueError as err:
            print(err)

def insert_datas_players():
    while True:
        print("Rentrez les informations du joueur: ")
        lastname_player = input("Nom: ")
        firstname_player = input("Prénom: ")
        while True:
            try:
                age = int(input("Âge: "))
                break
            except ValueError:
                print("L'âge doit être un chiffre")
        while True:
            try:
                tall = int(input("Taille en cm: "))
            except ValueError:
                print("La taille doit être un chiffre")
            if len(tall) != 3:
                print("Veuillez rentrer votre taille en cm s'ils vous plaît")
            else:
                break

        while True:
            position = input("Poste du joueur: ")
            if len(position) != 2:
                print("Veuillez entrer seulement les lettres de votre poste")
            else:
                break

        while True:
            try:
                highschool_id = int(input("Highschool ID: "))
                break
            except ValueError:
                print("Le highschool id doit être un chiffre")
        
        while True:
            try:
                teams_id = int(input("Team id: "))
                break
            except ValueError:
                print("La team id doit être un chiffre")
        
        try:
            add_data_players(lastname_player, firstname_player, age, tall, position, highschool_id, teams_id)
        except ValueError as err:
            print(err)


def insert_datas_team_with_csv():
    with open("/home/yuri/ProjDBPy_2025_WinterCup/csv/teams.csv", encoding='latin-1') as file:
        next(file)
        for line in file:   
            row=line.strip().split(",")
            if get_team_id_from_name(row[0]):
                print(f"La team avset foreign_key_checks=0ec l'id: {row[0]} existe déjà")
            else:
                add_data_teams(row[0], row[1])

        print("Les données ont bien été enregistrées")


def insert_datas_highschool_with_csv():
    with open("../csv/highschool.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            if get_highschool_id_from_name(row[0]):
                print(f"La highschool avec l'id: {row[0]} existe déjà")
            else:
                add_data_highschool(row[0], row[1], row[2])

def insert_datas_player_with_csv():
    with open("../csv/players.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            if get_player_id_from_name(row[0]):
                print(f"Le player avec l'id: {row[0]} existe déjà")
            else:
                add_data_players(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

def insert_datas_coaches_with_csv():
    with open("../csv/coaches.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            if get_coach_id_from_name(row[0]):
                print(f"Le coache avec l'id: {row[0]} existe déjà")
            else:
                add_data_coachs(row[0], row[1], row[2], row[3])

def update_data_team():
    columns_team = ["name"]
    print("Voici les colonnes modifiables: ",', '.join(columns_team))
    
    select_data_teams()

    new_name_team = input("Choisissez le nouveau nom de l'équipe: ")
    while True:
        try:
            id_team = int(input("Selectionnez l'ID: "))
            break
        except ValueError as err:
            print(err)
    update_teams_from_id(id_team, new_name_team)
    print(f"\nNouveau nom: {new_name_team} à été modifié pour l'ID: {id_team}")

def update_data_players():
    columns_player = ["age","tall","position"]
    print("\nVoici les colonnes modifiables: ",', '.join(columns_player))

    select_data_players()

    while True:
        choice_column = input("\nChoisissez la colonne qui sera modifiée: ")
        if choice_column in columns_player:
            break
        else:
            print("\nVeuillez choisir une colonne modifiables: ",', '.join(columns_player))
    if choice_column.lower() == columns_player[0]:
        while True:    
            try:
                new_age = int(input("Nouvelle âge: "))
                id_player = int(input("ID: "))
                break
            except ValueError as err:
                print(err)
        update_players_from_id(id_player,choice_column,new_age)
        print(f"Nouvelle age: {new_age} à été modifiée pour l'ID: {id_player}")
    elif choice_column.lower() == columns_player[1]:

        while True:
            try:
                new_height = int(input("Nouvelle taille: "))
                id_player = int(input("ID: "))
                break
            except ValueError as err:
                print(err)

        update_players_from_id(id_player,choice_column,new_height)
        print(f"Nouvelle taille: {new_height} à été modifiée pour l'ID: {id_player}")
        
    elif choice_column.lower() == columns_player[2]:
    
        while True:
            new_position = int(input("Nouvelle poste: "))
            if len(new_position) != 2:
                print("Veuillez rentrer uniquement les 2 lettres du poste")
            else:
                break

        while True:
            try:
                id_player = int(input("ID: "))
                break
            except ValueError as err:
                print(err)
        update_players_from_id(id_player,choice_column,new_height)
        print(f"Nouvelle taille: {new_height} à été modifiée pour l'ID: {id_player}")
