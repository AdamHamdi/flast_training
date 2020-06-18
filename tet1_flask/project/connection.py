
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="falsk_app"

)

mycursor=mydb.cursor()
#mycursor.execute('CREATE DATABASE falsk_app')
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()
# drop tables
drop_tables = [
    ''' DROP TABLE IF EXISTS demande ''',
    ''' DROP TABLE IF EXISTS stagiaire ''',
    ''' DROP TABLE IF EXISTS offre_emploi ''',
    ''' DROP TABLE IF EXISTS candidat ''',
    ''' DROP TABLE IF EXISTS recruteur ''',
    ''' DROP TABLE IF EXISTS utilisateur ''']

for drop in drop_tables:
    mycursor.execute(drop)
    mydb.commit()

# create tables
create_tables = [
    ''' CREATE TABLE offre_emploi(
        _id SERIAL PRIMARY KEY,
        poste VARCHAR(255),
        type_contrat VARCHAR(255),
        date_creation TIMESTAMP,
        date_fin_offre DATE,
        salaire VARCHAR(50),
        niveau_d_etude VARCHAR(255),
        experiences VARCHAR(255),
        description_poste VARCHAR(255),
        exigences VARCHAR(255),
        avantages VARCHAR(255)
    )''',
    ''' CREATE TABLE utilisateur(
        _id SERIAL PRIMARY KEY,
        nom VARCHAR(60),
        prenom VARCHAR(60),
        adresse VARCHAR(60),
        tel VARCHAR(8),
        email VARCHAR(255),
        mot_de_passe VARCHAR(255),
        role VARCHAR(10)
    )''',
    ''' CREATE TABLE recruteur(
        _id SERIAL PRIMARY KEY,
        _id_utilisateur BIGINT UNSIGNED ,
        FOREIGN KEY (_id_utilisateur) REFERENCES utilisateur(_id) ON UPDATE CASCADE ON DELETE CASCADE
    )''',
    ''' CREATE TABLE candidat(
        _id SERIAL PRIMARY KEY,
        _id_utilisateur BIGINT UNSIGNED ,
        cv_url VARCHAR(255), 
        FOREIGN KEY (_id_utilisateur)
        REFERENCES utilisateur(_id)
        ON UPDATE CASCADE ON DELETE CASCADE
    )''',
    ''' CREATE TABLE stagiaire(
        _id SERIAL PRIMARY KEY,
        _id_candidat BIGINT UNSIGNED ,
        _id_offre_emploi BIGINT UNSIGNED ,
        date_debut date,
        date_fin date,
        FOREIGN KEY (_id_candidat)
        REFERENCES candidat(_id)
        ON UPDATE CASCADE ON DELETE CASCADE
        ,
        FOREIGN KEY (_id_offre_emploi)
        REFERENCES offre_emploi(_id)
        ON UPDATE CASCADE ON DELETE CASCADE
        
    )''',
    ''' CREATE TABLE demande(
        _id SERIAL PRIMARY KEY,
        _id_candidat BIGINT UNSIGNED ,
        _id_offre_emploi BIGINT UNSIGNED ,
        date_creation date,
        FOREIGN KEY (_id_candidat)
        REFERENCES candidat(_id)
        ON UPDATE CASCADE ON DELETE CASCADE
        ,
        FOREIGN KEY (_id_offre_emploi)
        REFERENCES offre_emploi(_id)
        ON UPDATE CASCADE ON DELETE CASCADE
        
    )'''
]

for table in create_tables:
    print(table)
    mycursor.execute(table)
    mydb.commit()

