from config import open_connection, close_connection
from models.utilisateur import Utilisateur

class Admin:

    # create
    @staticmethod
    def create(nom, prenom, adresse, tel, email, mot_de_passe, role):

        try:

            con = open_connection()
            cur = con.cursor()

            id_utilisateur = Utilisateur.create(nom, prenom, adresse, tel, email, mot_de_passe, role)
            
            sql = '''
                    INSERT INTO recruteur(_id_utilisateur)
                    VALUES(%s)
                    '''

            cur.execute(sql, [id_utilisateur])

            con.commit()

        except Exception as e:
            print(e)
        finally:
            close_connection(con, cur)
