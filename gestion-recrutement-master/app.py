# flask libraries
from flask import Flask, render_template, request, session, redirect, url_for, flash
from werkzeug.utils import secure_filename
from config import open_connection, close_connection

# import models
from models.utilisateur import Utilisateur
from models.recruteur import Recruteur
from models.admin import Admin
from models.candidat import Candidat
from models.offre_emploi import OffreEmploi
from models.demande_emploi import Demandeemploi

# to import .env file data
import os
from dotenv import load_dotenv
load_dotenv()


# flask config
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.debug = True

#login
@app.route('/', methods=['GET', 'POST'])
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
            elif utilisateur[7] == 'ADMIN':
                return redirect(url_for('admin_menu')) 
            elif utilisateur[7] == 'CANDIDAT':
                return redirect(url_for('candidat_menu'))  

        else:
            error = 'svp, vérifiez votre email et mot de passe'
            return render_template('login.html', error=error)

    return render_template('login.html')

#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    
       if request.method == 'GET':
           return render_template('/register.html')
       
       else:
    # get form data
            nom = request.form['nom']
            prenom = request.form['prenom']
            adresse = request.form['adresse']
            tel = request.form['tel']
            email = request.form['email']
            mot_de_passe = request.form['mot_de_passe']#.encode('UTF-8')
            
            role = request.form['role']
            
            #Candidat.create(nom = nom, prenom = prenom, email = email,adresse = adresse, tel = tel, mot_de_passe = mot_de_passe,role=role )
            
            cur.mysql.connection.cursor()
            cur.execute("INSERT INTO utilisateur(nom, prenom, adresse, tel, email, mot_de_passe, role) VALUES(%s, %s, %s, %s, %s, %s, %s)",(nom, prenom, adresse, tel, email, mot_de_passe, role))
            mysql.connection.commit()
            

            flash('Candidat ajouté', 'success')
            return redirect(url_for('candidat_menu'))
       

################
'''
Recruteur Menu
'''
################
@app.route('/recruteur', methods=['GET'])
def recruteur_menu():
    return render_template('recruteur/index.html')
###########################
#ADMIN
@app.route('/admin', methods=['GET'])
def admin_menu():
    return render_template('admin/index1.html')
###########################
#Candidat
@app.route('/candidat', methods=['GET'])
def candidat_menu():
    return render_template('candidats/candidat.html')



################
'''
Offre Emploi Menu
'''
################
# index
@app.route('/offre-emploi', methods=['GET'])
def offre_emploi_index():
    return render_template('/offre-emploi/index.html', offre_emploi=OffreEmploi.afficher_tous())
   
@app.route('/offre-emploi-candiat', methods=['GET'])
def offre_emploi_can_index():
    
    return render_template('/candidats/index-candidat.html', offre_emploi=OffreEmploi.afficher_tous())    
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
  #create demande d'omploi
@app.route('/demande-emploi/create/<string:id>', methods=['GET', 'POST'])
def demande_emploi_create(id):

    if request.method == 'GET':
        return render_template('demandes/new.html',offre=OffreEmploi.afficher(id))

    # get form data
    _id_offre_emploi = request.form['id']
    date_creation = request.form['date_creation']
    cv=request.form['cv']
    _id_candidat=flask_login.user_unauthorized

    OffreEmploi.edit(poste, type_contrat, date_expiration, salaire,
                     niveau_etude, experience, description, exigence, avantage, id)

    flash('Demande ajoutée avec success', 'success')
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
 #Show_info
@app.route('/offre-emploi/info/<string:id>', methods=['GET', 'POST'])
def offre_emploi_info(id):

    if request.method == 'GET':
        return render_template('/offre-emploi/info.html', offre=OffreEmploi.afficher(id))

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

    
   
    return redirect(url_for('offre_emploi_index'))
   
# delete
@app.route('/offre-emploi/delete/<string:id>', methods=['POST'])
def offre_emploi_delete(id):

    OffreEmploi.delete(id)

    flash('offre supprimer', 'success')
    return redirect(url_for('offre_emploi_index'))
    #log out rucreteur

@app.route('/demande-emploi', methods=['GET'])
def demande_emploi():
    return render_template('demandes/demande-emploi.html', demande_emploi=Demandeemploi.afficher_tous())
    # , offre_emploi=OffreEmploi.afficher_tous()
@app.route('/demande-emploi/info/<string:id>', methods=['GET', 'POST'])
def demande_emploi_info(id):

    if request.method == 'GET':
        return render_template('demandes/info.html', demande=Demandeemploi.afficher(id))

    # # get form data
    _id = request.form['_id']
    nom = request.form['nom']
    prenom= request.form['prenom']
    poste = request.form['poste']
    date_creation= request.form['date_creation']
   

    
   
    return redirect(url_for('demande-emploi'))

#show detail offre pour le candidat    
@app.route('/offre-emploi-candidat/info/<string:id>', methods=['GET', 'POST'])
def offre_emploi_info_cand(id):

    if request.method == 'GET':
        return render_template('/demandes/off-info.html', offre=OffreEmploi.afficher(id))

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

    
   
    return redirect(url_for('offre_emploi_can_index'))

#condidat
@app.route('/candidat/offre-emploi', methods=['GET'])
def offre_emploi_condidat():
    return render_template('/offre-emploi/index.html', offre_emploi=OffreEmploi.afficher_tous())

   
# new
       
@app.route('/logout')
def logout():
    session.clear()
    
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
