import mysql.connector
import os
from datetime import *
import time


my_password= os.environ.get('my_password')

def wintercup_open():
    return mysql.connector.connect(host='127.0.0.1', user='root', password=my_password, port='3306',
                                   database='tournament_wintercup',autocommit=True, buffered=True)

db_connection= wintercup_open()

def select_players():
    query = "SELECT * FROM players"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def select_teams():
    query = "SELECT * FROM teams"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def select_highschool():
    query = "SELECT * FROM highschool"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def select_tournament():
    query = "SELECT * FROM tournament"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

# Inutile si on ne sait pas à quel joueur appartient
def select_statistics():
    query = "SELECT * FROM statistics"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def select_coaches():
    query = "SELECT * FROM coaches"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

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

def add_data_highschool(name, adress, prefecture):
    query = "INSERT INTO highschool (name, adress, prefecture) values (%s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, adress, prefecture))
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def add_data_teams(name, creation_date):
    query = "INSERT INTO teams (name, creation_date) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, creation_date))
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def add_data_players(lastname, firstname, age, tall, position, highschool_id, teams_id):
    query = "INSERT INTO players (lastname, firstname, age, tall, position, highschool_id, teams_id) values (%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (lastname, firstname, age, tall, position, highschool_id, teams_id))
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def add_data_tournament(name, place, ranking, matchs_day, teams_id):
    query = "INSERT INTO tournament (name, place, ranking, matchs_day, teams_id) values (%s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, place, ranking, matchs_day, teams_id))
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def add_data_coachs(lastname, firstname, type, teams_id):
    query = "INSERT INTO coaches (lastname, firstname, type, teams_id) values (%s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (lastname, firstname, type, teams_id))
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def add_data_statistics(statistics_points, statistics_assists, statistics_rebounds, statistics_blocks, statistics_steals):
    query = "INSERT INTO statistics (statistics_points, statistics_assists, statistics_rebounds, statistics_blocks, statistics_steals) values (%s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (statistics_points, statistics_assists, statistics_rebounds, statistics_blocks, statistics_steals))
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def get_team_id_from_name(name):
    query = "SELECT id FROM teams WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(name,))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def get_highschool_id_from_name(name):
    query = "SELECT id FROM highschool WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(name,))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def get_player_id_from_name(lastname,firstname):
    query = "SELECT id FROM players WHERE lastname = %s and firstname = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(lastname,firstname))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def get_coach_id_from_name(lastname,firstname):
    query = "SELECT id FROM coaches WHERE name = %s and firstname = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(lastname,firstname))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def update_teams_from_id(id, new_value): 
    query = f"UPDATE teams SET name = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_highschool_from_id(id, column, new_value):
    columns_highschool = ["name","address","prefecture"]

    if column not in columns_highschool:
        raise ValueError("Aucune colonne identifié")
    
    safe_input = columns_highschool[column]
    
    query = f"UPDATE highschool SET {safe_input} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_players_from_id(id, column, new_value):
    columns_player = ["age","tall","position"]

    if column not in columns_player:
        raise ValueError("Aucune colonne identifié")
    
    safe_input = columns_player[column]

    query = f"UPDATE players SET {safe_input} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_coaches_from_id(id, new_value):
    query = f"UPDATE coaches SET type = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_tournament_from_id(id, column, new_value):
    columns_tournament = ["ranking","matchs_day"]

    if column not in columns_tournament:
        raise ValueError("Aucune colonne identifié")
    
    safe_input = columns_tournament[column]
    
    query = f"UPDATE tournament SET {safe_input} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_statistics_from_id(id, column, new_value):
    columns_statistics = ["statistics_points","statistics_assists","statistics_rebounds","statistics_blocks","statistics_steals"]

    if column not in columns_statistics:
        raise ValueError("Aucune colonne identifié")
    
    safe_input = columns_statistics[column]
    
    query = f"UPDATE statistics SET {safe_input} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def delete_teams_from_id(team_id):
    query = "DELETE FROM teams WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (team_id,))
    cursor.close()
    print(f"\nL'équipe {team_id} supprimée avec succès.")

def delete_highschool_from_id(highschool_id):
    query = "DELETE FROM highschool WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (highschool_id,))
    cursor.close()
    print(f"\nL'école {highschool_id} supprimée avec succès.")

def delete_players_from_id(players_id):
    query = "DELETE FROM players WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (players_id,))
    cursor.close()
    print(f"\nLe joueur {players_id} supprimée avec succès.")

def delete_coaches_from_id(coaches_id):
    query = "DELETE FROM coaches WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (coaches_id,))
    cursor.close()
    print(f"\nLe coach {coaches_id} supprimée avec succès.")

def exec_delete_teams():
    print("Voici les données de la table teams: \n")
    for i in range(1,4):
        print("temps pour affichage:",i,end='\r')
        time.sleep(1)
    select_data_teams()
    while True:
        try:
            id_for_delete = int(input("Rentrez l'id pour delete: "))
            break
        except ValueError as err:
            print(err)    
    try:
        delete_teams_from_id(id_for_delete)
    except ValueError as err:
        print("L'id séléctionnez n'existe pas")

    
# Pas d'idée pour l'instant de comment code cette partie qui a une table intermediaire
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

def insert_datas_coachs():
    while True:
        print("Veuillez rentrer les informations du coach")
        lastname_coach = input("Nom: ")
        firstname_coach = input("Prénom: ")
        while True:    
            type_coach = int(input("Veuillez rentre 0 pour coach principale ou 1 pour coach adjoint: "))
            if type_coach != 0 or type_coach != 1:
                print("Veuillez saisir 0 ou 1 ")
            else:
                break
        
        while True:
            try:    
                team_id = int(input("Rentrer l'id de la team qu'il appartient: "))
                break
            except ValueError:
                print("Veuillez rentrer un chiffre") 
        try:
            add_data_coachs(lastname_coach,firstname_coach, type_coach, team_id)
            break
        except ValueError as err:
            print(err)



def insert_datas_team_with_csv():
    with open("/home/yuri/ProjDBPy_2025_WinterCup/csv/teams.csv", encoding='latin-1') as file:
        next(file)
        for line in file:   
            row=line.strip().split(",")
            if get_team_id_from_name(row[0]):
                print(f"La team: {row[0]} existe déjà")
            else:
                add_data_teams(row[0], row[1])

        print("Les données ont bien été enregistrées")

def insert_datas_highschool_with_csv():
    with open("../csv/highschool.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            if get_highschool_id_from_name(row[0]):
                print(f"La highschool: {row[0]} existe déjà")
            else:
                add_data_highschool(row[0], row[1], row[2])

def insert_datas_player_with_csv():
    with open("../csv/players.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            highschool_id = get_highschool_id_from_name(row[5])
            team_id = get_team_id_from_name(row[6])
            if highschool_id and team_id:
                add_data_players(row[0], row[1], row[2], row[3], row[4], highschool_id, team_id)
            elif not highschool_id:
                print(f"La highschool: {row[5]} n'existe pas pour la ligne: {row}")
            else:
                print(f"La team: {row[6]} n'existe pas pour la ligne: {row}")

def insert_datas_coaches_with_csv():
    with open("../csv/coaches.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            team_id = get_team_id_from_name(row[3])
            if team_id:
                add_data_coachs(row[0], row[1], row[2], team_id)
            else:
                print(f"la team: {row[3]} n'existe pas pour la ligne: {row}")

def insert_datas_tournament_with_csv():
    with open("../csv/tournament.csv") as file:
        next(file)
        for line in file:
            row=line.strip().split(",")
            team_id = get_team_id_from_name(row[3])
            if team_id:
                add_data_tournament(row[0],row[1],row[2],row[3],team_id)
            else:
                print(f"La team: {row[4]}")



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

def update_data_coach():
    columns_coach = ["type"]
    print("Voici les colonnes modifiables: ",', '.join(columns_coach))
    
    select_data_coachs()
    while True:
    
        new_type_coach = int(input("Selectionnez 0 pour coach principale ou 1 pour coach adjoint: "))

        if new_type_coach != 0 or new_type_coach != 1:
            print("Choisissez 0 ou 1 ")
        else:
            break

            
    while True:
        try:
            coach_id = int(input("Selectionnez l'ID: "))
            break
        except ValueError as err:
            print(err)
    update_coaches_from_id(coach_id, new_type_coach)
    print(f"\nNouveau nom: {new_type_coach} à été modifié pour l'ID: {coach_id}")    
    pass

def update_data_tournament():
    columns_tournament = ["ranking","matchs_day"]
    print("Voici les colonnes modifiables: ",', '.join(columns_tournament))
    
    select_data_tournament()

    while True:
        choice_column = input("\nChoisissez la colonne qui sera modifiée: ")
        if choice_column in columns_tournament:
            break
        else:
            print("\nVeuillez choisir une colonne modifiables: ",', '.join(columns_tournament))
    
    if choice_column.lower() == columns_tournament[0]:
        while True:
            try:
                new_ranking = int(input("New rank: "))
                id_tournament = int(input("Id: "))
                break
            except ValueError:
                print("Veuillez saisir une donnée de type int (chiffre).")
        update_tournament_from_id(id_tournament,choice_column,new_ranking)
        print(f"Nouveau rank: {new_ranking} à été modifiée pour l'ID: {id_tournament}")
    elif choice_column.lower() == columns_tournament[1]:
        while True:
            try:
                new_match_day = int(input("New match day: "))
                id_tournament = int(input("Id: "))
                break
            except ValueError:
                print("\nVeuillez saisir une donnée de type int (chiffre)")
        update_tournament_from_id(id_tournament,choice_column,new_match_day)
        print(f"Nouveau jour: {new_match_day} à été modifiée pour l'Id: {id_tournament}")




