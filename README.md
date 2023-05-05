#A&C Sportsweaer's stock management
Ce projet represente les taches de gestion de stock du magasin #A&C Sportsweaer's
Les fonctonnalitées sont les suivantes:
-connexion
-creation déun nouveau compte
-Ajout d'un produit 
-Modification d'un produit
-Recherche d'un produit
-Suppression d'un produit

Afin de tester le programme voici la base de données convenable 'projet'
(ps:veuillez la copier dans votre MYSQL WORKBENCH et changer les parametres du compte)
use pfa;


CREATE TABLE Utilisateur (
  idUtilisateur int NOT NULL AUTO_INCREMENT primary key,
  nomUtilisateur varchar(20) NOT NULL ,
  mdpUtilisateur varchar(20) NOT NULL
);


CREATE TABLE Produits (
  numSerie int NOT NULL primary key,
  nomProduit varchar(30) NOT NULL,
  descProduit varchar(300),
  prixU double,
  qntProduit int,
  seuilAlerteProduit int,
  date_entree date,
  date_sortie date,
  imageProduit longblob
);

