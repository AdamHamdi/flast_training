from config import open_connection, close_connection


class Utilisateur:

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

            id_utilisateur = cur.fetchone()[0]

            return id_utilisateur

        except Exception as e:
            print(e)
        finally:
            close_connection(con, cur)

    # authentification
    @staticmethod
    def authentification(email, mot_d_passe):

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                SELECT * FROM utilisateur WHERE email = %s AND mot_de_passe = %s
            '''

            cur.execute(sql, [email, mot_d_passe])

            if cur.rowcount > 0:
                utilisateur = cur.fetchone()
                return utilisateur

            return None

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)
