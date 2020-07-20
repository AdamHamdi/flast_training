from config import open_connection, close_connection

from models.utilisateur import Utilisateur
class Candidat:

    # create
    @staticmethod
    def create(nom, prenom, adresse, tel, email, mot_de_passe, role):

        try:

            con = open_connection()
            cur = con.cursor()

            sql = '''
                    INSERT INTO utilisateur(nom, prenom, adresse, tel, email, mot_de_passe, role)
                    VALUES(%s, %s, %s, %s, %s, %s, %s)
                    RETURNING _id
                    '''

            cur.execute(sql, [nom, prenom, adresse, tel, email, mot_de_passe, role])

            con.commit()

            id = cur.fetchone()[0]

            return id

        except Exception as e:
            print(e)
        finally:
            close_connection(con, cur)

    
  