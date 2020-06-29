from config import open_connection, close_connection


class Demandeemploi:

    @staticmethod
    def afficher_tous():

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
            SELECT demande._id, utilisateur.nom,utilisateur.prenom ,offre_emploi.poste,demande.date_creation FROM `demande`,`candidat`,`offre_emploi`,`utilisateur` WHERE candidat._id = demande._id_candidat AND demande._id_offre_emploi=offre_emploi._id AND utilisateur._id=candidat._id_utilisateur    '''

            cur.execute(sql)

            demande_emploi = cur.fetchall()
            return demande_emploi

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
         SELECT demande._id, candidat.name ,offre_emploi.poste,demande.date_creation FROM `demande`,`candidat`,`offre_emploi` WHERE candidat._id = demande._id_candidat AND demande._id_offre_emploi=offre_emploi._id AND candidat._id = %s
            ORDER BY date_creation DESC
            '''

            cur.execute(sql, [id])

            demande_emploi = cur.fetchone()
            return demande_emploi

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)

    # @staticmethod
    # def new(poste, type_contrat, date_fin_offre, salaire,
    #         niveau_d_etude, experiences, description_poste, exigences, avantages):

    #     try:

    #         con = open_connection()
    #         cur = con.cursor(buffered=True)

    #         sql = '''
    #             INSERT INTO demande(poste, type_contrat, date_fin_offre, salaire, niveau_d_etude, experiences, description_poste, exigences, avantages) 
    #             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    #         '''

    #         cur.execute(sql, [poste, type_contrat, date_fin_offre, salaire,
    #                           niveau_d_etude, experiences, description_poste, exigences, avantages])

    #         con.commit()

    #     except Exception as e:
    #         print('Error: ', e)
    #     finally:
    #         close_connection(con, cur)

    # @staticmethod
    # def edit(poste, type_contrat, date_fin_offre, salaire,
    #          niveau_d_etude, experiences, description_poste, exigences, avantages, id):

    #     try:

    #         con = open_connection()
    #         cur = con.cursor(buffered=True)

    #         sql = '''
    #             UPDATE demande
    #             SET poste = %s, 
    #             type_contrat = %s, 
    #             date_fin_offre = %s, 
    #             salaire = %s, 
    #             niveau_d_etude = %s, 
    #             experiences = %s, 
    #             description_poste = %s, 
    #             exigences = %s, 
    #             avantages = %s
    #             WHERE _id = %s
    #         '''

    #         cur.execute(sql, [poste, type_contrat, date_fin_offre, salaire,
    #                           niveau_d_etude, experiences, description_poste, exigences, avantages, id])

    #         con.commit()

    #     except Exception as e:
    #         print('Error: ', e)
    #     finally:
    #         close_connection(con, cur)

    @staticmethod
    def delete(id):

        try:

            con = open_connection()
            cur = con.cursor(buffered=True)

            sql = '''
                DELETE FROM demande WHERE _id = %s
            '''

            cur.execute(sql, [id])
            con.commit()

        except Exception as e:
            print('Error: ', e)
        finally:
            close_connection(con, cur)
