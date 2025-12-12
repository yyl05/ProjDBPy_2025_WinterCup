import mysql.connector

def wintercup_open():
    return mysql.connector.connect(host='127.0.0.1', user='root', password='KqGeB/&105-mO', port='3306',
                                   database='tournament_wintercup', autocommit=True, buffered=True)

db_connection = wintercup_open()

def menu() :
    print("Que voulez-vous faire comme opération? \n")
    print("1. SELECT")
    print("1. INSERT")
    print("1. UPDATE")
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

def add_data_coaches(lastname, firstname, type, teams_id):
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
    
def get_coache_id_from_name(name):
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
    
def update_teams_from_id(id, column, new_value):
    columns_team = ["name","creation_date"]

    if column not in columns_team:
        raise TypeError("Aucune colonne identifié")
    
    query = f"UPDATE teams SET {column} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_highschool_from_id(id, column, new_value):
    columns_highschool = ["name","address","prefecture"]

    if column not in columns_highschool:
        raise TypeError("Aucune colonne identifié")
    
    query = f"UPDATE highschool SET {column} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_players_from_id(id, column, new_value):
    columns_player = ["lastname","firstname","age","tall","position",""]

    if column not in columns_player:
        raise TypeError("Aucune colonne identifié")
    
    query = f"UPDATE players SET {column} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_tournament_from_id(id, column, new_value):
    columns_tournament = ["name","place","ranking","matchs_day"]

    if column not in columns_tournament:
        raise TypeError("Aucune colonne identifié")
    
    query = f"UPDATE tournament SET {column} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()

def update_statistics_from_id(id, column, new_value):
    columns_statistics = ["statistics_points","statistics_assists","statistics_rebounds","statistics_blocks","statistics_steals"]

    if column not in columns_statistics:
        raise TypeError("Aucune colonne identifié")
    
    query = f"UPDATE statistics SET {column} = %s WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query,(new_value, id))
    cursor.close()