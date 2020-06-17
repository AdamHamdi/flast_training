# flask libraries
from flask import Flask, render_template, request, session, redirect, url_for, flash

# import models
from models.utilisateur import Utilisateur
from models.recruteur import Recruteur
from models.offre_emploi import OffreEmploi

# to import .env file data
import os
from dotenv import load_dotenv
load_dotenv()


# flask config
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.debug = True


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        # get form data
        email = request.form['email']
        mot_d_passe = request.form['mot_de_passe']

        # authentification
        utilisateur = Utilisateur.authentification(email, mot_d_passe)

        if utilisateur:

            session['logged_in'] = True
            session['user_info'] = utilisateur

            if utilisateur[7] == 'RECRUTEUR':
                return redirect(url_for('recruteur_menu'))

        else:
            error = 'svp, vérifiez votre email et mot de passe'
            return render_template('login.html', error=error)

    return render_template('login.html')


################
'''
Recruteur Menu
'''
################
@app.route('/recruteur', methods=['GET'])
def recruteur_menu():
    return render_template('recruteur/index.html')


################
'''
Offre Emploi Menu
'''
################
# index
@app.route('/offre-emploi', methods=['GET'])
def offre_emploi_index():
    return render_template('/offre-emploi/index.html', offre_emploi=OffreEmploi.afficher_tous())
# new
@app.route('/offre-emploi/new', methods=['GET', 'POST'])
def offre_emploi_new():

    if request.method == 'GET':
        return render_template('/offre-emploi/new.html')

    # get form data
    poste = request.form['poste']
    date_expiration = request.form['date_expiration']
    salaire = request.form['salaire']
    description = request.form['description']
    exigence = request.form['exigence']
    experience = request.form['experience']
    type_contrat = request.form['type_contrat']
    niveau_etude = request.form['niveau_etude']
    avantage = request.form['avantage']

    OffreEmploi.new(poste, type_contrat, date_expiration, salaire,
                    niveau_etude, experience, description, exigence, avantage)

    flash('offre ajouter', 'success')
    return redirect(url_for('offre_emploi_index'))
# edit
@app.route('/offre-emploi/edit/<string:id>', methods=['GET', 'POST'])
def offre_emploi_edit(id):

    if request.method == 'GET':
        return render_template('/offre-emploi/edit.html', offre=OffreEmploi.afficher(id))

    # get form data
    poste = request.form['poste']
    date_expiration = request.form['date_expiration']
    salaire = request.form['salaire']
    description = request.form['description']
    exigence = request.form['exigence']
    experience = request.form['experience']
    type_contrat = request.form['type_contrat']
    niveau_etude = request.form['niveau_etude']
    avantage = request.form['avantage']

    OffreEmploi.edit(poste, type_contrat, date_expiration, salaire,
                     niveau_etude, experience, description, exigence, avantage, id)

    flash('offre modifier', 'success')
    return redirect(url_for('offre_emploi_index'))
# delete
@app.route('/offre-emploi/delete/<string:id>', methods=['POST'])
def offre_emploi_delete(id):

    OffreEmploi.delete(id)

    flash('offre supprimer', 'success')
    return redirect(url_for('offre_emploi_index'))


if __name__ == '__main__':
    app.run()
