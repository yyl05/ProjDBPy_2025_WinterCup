from main import *
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
        except ValueError:
            print("\nerror")

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
