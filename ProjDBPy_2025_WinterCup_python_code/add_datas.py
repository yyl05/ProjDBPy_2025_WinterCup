from def_area import *
from datetime import datetime

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
            if get_coache_id_from_name(row[0]):
                print(f"Le coache avec l'id: {row[0]} existe déjà")
            else:
                add_data_coaches(row[0], row[1], row[2], row[3])