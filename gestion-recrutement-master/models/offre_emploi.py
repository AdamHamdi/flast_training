from config import open_connection, close_connection


class OffreEmploi:

    @staticmethod
    def afficher_tous():

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                SELECT * FROM offre_emploi ORDER BY date_creation DESC
            '''

            cur.execute(sql)

            offre_emploi = cur.fetchall()
            return offre_emploi

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)

    @staticmethod
    def afficher(id):

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                SELECT * FROM offre_emploi WHERE _id = %s ORDER BY date_creation DESC
            '''

            cur.execute(sql, [id])

            offre_emploi = cur.fetchone()
            return offre_emploi

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)

    @staticmethod
    def new(poste, type_contrat, date_fin_offre, salaire,
            niveau_d_etude, experiences, description_poste, exigences, avantages):

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                INSERT INTO offre_emploi(poste, type_contrat, date_fin_offre, salaire, niveau_d_etude, experiences, description_poste, exigences, avantages) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            cur.execute(sql, [poste, type_contrat, date_fin_offre, salaire,
                              niveau_d_etude, experiences, description_poste, exigences, avantages])

            con.commit()

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)

    @staticmethod
    def edit(poste, type_contrat, date_fin_offre, salaire,
             niveau_d_etude, experiences, description_poste, exigences, avantages, id):

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                UPDATE offre_emploi
                SET poste = %s, 
                type_contrat = %s, 
                date_fin_offre = %s, 
                salaire = %s, 
                niveau_d_etude = %s, 
                experiences = %s, 
                description_poste = %s, 
                exigences = %s, 
                avantages = %s
                WHERE _id = %s
            '''

            cur.execute(sql, [poste, type_contrat, date_fin_offre, salaire,
                              niveau_d_etude, experiences, description_poste, exigences, avantages, id])

            con.commit()

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)

    @staticmethod
    def delete(id):

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                DELETE FROM offre_emploi WHERE _id = %s
            '''

            cur.execute(sql, [id])
            con.commit()

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)
