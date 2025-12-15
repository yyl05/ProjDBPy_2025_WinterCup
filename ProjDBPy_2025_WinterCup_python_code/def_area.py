import mysql.connector
import os

my_password= os.environ.get('my_password')

def wintercup_open():
    return mysql.connector.connect(host='127.0.0.1', user='root', password=my_password, port='3306',
                                   database='tournament_wintercup',autocommit=True, buffered=True)

db_connection= wintercup_open()

def menu() :
    print("Que voulez-vous faire comme opération? \n")
    print("1. SELECT")
    print("2. INSERT")
    print("3. UPDATE")
    print("4. DELETE")
    print("5. INSERT WITH CSV FILE")
    print("6. QUIT")

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
    query = "SELECT * FROM tournaments"
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
    query = "SELECT name FROM teams WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(name))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def get_highschool_id_from_name(name):
    query = "SELECT name FROM highschool WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(name))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def get_player_id_from_name(name):
    query = "SELECT name FROM players WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(name))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    
def get_coach_id_from_name(name):
    query = "SELECT name FROM coaches WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(name))
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
    columns_tournament = ["name","place","ranking","matchs_day"]

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
    print(f"L'équipe {team_id} supprimée avec succès.")

def delete_highschool_from_id(highschool_id):
    query = "DELETE FROM highschool WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (highschool_id,))
    cursor.close()
    print(f"L'école {highschool_id} supprimée avec succès.")

def delete_players_from_id(players_id):
    query = "DELETE FROM players WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (players_id,))
    cursor.close()
    print(f"Le joueur {players_id} supprimée avec succès.")

def delete_coaches_from_id(coaches_id):
    query = "DELETE FROM coaches WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (coaches_id,))
    cursor.close()
    print(f"Le coach {coaches_id} supprimée avec succès.")
