from def_area import *

def main() :
    while True:
        print("\n1. SELECT")
        print("2. INSERT")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. INSERT WITH CSV FILE")
        print("6. QUIT")
        while True:
            try:    
                choice_usr = int(input("\nQue voulez-vous faire? ")) 
                break
            except ValueError as err:
                print(err)
            
        if choice_usr == 1:
            print("\n1. Teams")
            print("2. HighSchool")
            print("3. Players")
            print("4. Coachs")
            print("5. Tournament")
            while True:
                try:
                    table_choice = int(input("\nQuelle table voulez-vous afficher? "))
                    break
                except ValueError:
                    print("\nVeuillez choisir un numéro s'ils vous plaît.")
            
            if table_choice == 1:
                print("")
                select_data_teams()
                print("\nVoici les datas pour la table teams.")
                break
            elif table_choice == 2:
                print("")
                select_data_highschool()
                print("\nVoici les datas pour la table highschool.")
                break
            elif table_choice == 3:
                print("")
                select_data_players()
                print("\nVoici les datas pour la table players.")
                break
            elif table_choice == 4:
                print("")
                select_data_coachs()
                print("\nVoici les datas pour la table coachs.")
                break
            elif table_choice == 5:
                print("")
                select_data_tournament()
                print("\nVoici les datas pour la table tournament.")
                break
            else:
                print("Choisissez un chiffre qui appartient au menu s'ils vous plaît.")
        elif choice_usr == 2:
            print("\n1. Teams")
            print("2. HighSchool")
            print("3. Players")
            print("4. Coachs")

            while True:
                try:
                    table_choice = int(input("\nDans quelle table voulez-vous insérer des données? "))
                    break
                except ValueError:
                    print("\nVeuillez choisir un numéro s'ils vous plaît.")
            if table_choice == 1:
                insert_datas_teams()
                break
            elif table_choice == 2:
                insert_datas_highschool()
                break
            elif table_choice == 3:
                insert_datas_players()
                break
            elif table_choice == 4:
                insert_datas_coachs()
                break
            else:
                print("Choisissez un chiffre qui appartient au menu s'ils vous plaît.")
        elif choice_usr == 3:
            print("\n1. Teams")
            print("2. Players")
            print("3. Coachs")
            print("4. Tournament")

            while True:
                try:
                    table_choice = int(input("\nDans quelle table voulez-vous modifier? "))
                    break
                except ValueError:
                    print("\nVeuillez choisir un numéro s'ils vous plaît.")
            if table_choice == 1:
                update_data_team()
                break
            elif table_choice == 2:
                update_data_players()
                break
            elif table_choice == 3:
                update_data_coach()
                break
            elif table_choice == 4:
                update_data_tournament()
                break
            else:
                print("Choisissez un chiffre qui appartient au menu s'ils vous plaît.")
        elif choice_usr == 4:
            print("\n1. Teams")
            print("2. HighSchool")
            print("3. Players")
            print("4. Coachs")            

            while True:
                try:
                    table_choice = int(input("\nDans quelle table voulez-vous insérer en utilisant un fichier csv? "))
                    break
                except ValueError:
                    print("\nVeuillez choisir un numéro s'ils vous plaît.")
            if table_choice == 1:
                exec_delete_teams()
                break
            elif table_choice == 2:
                exec_delete_highschool()
                break
            elif table_choice == 3:
                exec_delete_players()
                break
            elif table_choice == 4:
                exec_delete_coach()
                break
            else:
                print("Choisissez un chiffre qui appartient au menu s'ils vous plaît.")   
            

        elif choice_usr == 5:
            print("\n1. Teams")
            print("2. HighSchool")
            print("3. Players")
            print("4. Coachs")
            print("5. Tournament")


            while True:
                try:
                    table_choice = int(input("\nDans quelle table voulez-vous insérer en utilisant un fichier csv? "))
                    break
                except ValueError:
                    print("\nVeuillez choisir un numéro s'ils vous plaît.")
            if table_choice == 1:
                insert_datas_team_with_csv()
                break
            elif table_choice == 2:
                insert_datas_highschool_with_csv()
                break
            elif table_choice == 3:
                insert_datas_player_with_csv()
                break
            elif table_choice == 4:
                insert_datas_coaches_with_csv()
                break
            elif table_choice == 5:
                insert_datas_tournament_with_csv()
            else:
                print("Choisissez un chiffre qui appartient au menu s'ils vous plaît.")   
        elif choice_usr == 6:
            for i in range(1,4):
                print("Déconnexion dans: ",i,end='\r')
                time.sleep(1)
            quit()
            pass    
                        

if __name__ == '__main__':
    main()