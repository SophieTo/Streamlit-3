import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/SophieTo/Streamlit-3/refs/heads/main/comptes.csv")
# Initialiser le dictionnaire des données utilisateurs
lesDonneesDesComptes = {'usernames': {}}

# Parcourir chaque ligne et ajouter au dictionnaire
for _, row in df.iterrows():
    utilisateur = row['name']  # Nom de l'utilisateur
    lesDonneesDesComptes['usernames'][utilisateur] = {
        'name': row['name'],
        'password': row['password'],
        'email': row['email'],
        'failed_login_attemps': 0,  # Valeur par défaut
        'logged_in': False,  # Valeur par défaut
        'role': row['role'],
    }


authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    st.title("Bienvenue sur ma page")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq3hqEgj1fvZNlvaxSlEx0JRKeIqNnXUU-6Q&s") 

def album():
    st.title("Bienvenue dans l'album de mon chat")
    col1, col2, col3 = st.columns(3)

    with col1:
      st.image("https://catissimo.com/wp-content/uploads/2022/03/catissimo_NB230322.jpg")
    with col2:
      st.image("https://t4.ftcdn.net/jpg/01/59/75/29/240_F_159752966_NbiVlB0T9guWGX11jHAolcrHpom6j39w.jpg")

    with col3:
      st.image("https://maviedechat.net/wp-content/uploads/2022/06/iStock-1265566709-1024x683.jpg") 

  

if st.session_state["authentication_status"]:
    with st.sidebar:
        # bouton déconnexion
        authenticator.logout("Déconnexion")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Les photos de mon chat"]
        )

    # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        accueil()
    elif selection == "Les photos de mon chat":
        album()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect(s)")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
