-- Description du projet

Winter Cup est une application Python en ligne de commande permettant de gérer un tournoi de basketball scolaire à l’aide d’une base de données relationnelle MySQL.

Le projet met en place un système complet de gestion des données liées à un tournoi, incluant :

les équipes

les lycées

les joueurs

les coachs

les tournois

L’application repose sur un menu interactif accessible depuis le terminal, permettant à l’utilisateur d’effectuer toutes les opérations classiques de gestion de données (CRUD : Create, Read, Update, Delete).

Les fonctionnalités principales incluent :

l’affichage des données stockées en base,

l’ajout manuel de nouvelles entrées,

la modification de certaines informations existantes,

la suppression sécurisée de données en tenant compte des contraintes de clés étrangères,

l’importation automatique de données à partir de fichiers CSV.

Lors des imports CSV, l’application gère automatiquement les relations entre les tables (par exemple : association des joueurs à leur équipe et à leur lycée à partir des noms).

Le projet est structuré de manière claire afin de séparer :

l’interface utilisateur (menus et interactions),

la logique métier,

et les opérations sur la base de données (requêtes SQL préparées).

Winter Cup a été développé dans un cadre pédagogique afin de démontrer la maîtrise de :

Python,

MySQL,

la gestion de bases de données relationnelles,

la conception d’applications en ligne de commande,

et les bonnes pratiques de développement (sécurité SQL, gestion des erreurs, organisation du code).

-- Installation & environnement
-- Prérequis

Avant de lancer le projet, vous devez disposer de :

Python 3.8+

MySQL Server

pip (gestionnaire de paquets Python)