from flask import Flask, redirect, url_for, session
from flask_oidc import OpenIDConnect


app = Flask(__name__)

# Configuration de l'OIDC
app.config.update({
    'SECRET_KEY': '4c1UxI9WUUO4RvgGNgtSmzRicA2VOCDP',  # Clé secrète pour signer les sessions
    'OIDC_CLIENT_SECRETS': 'keycloak.json',  # Fichier contenant les détails du client Keycloak
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_OPENID_REALM': 'py-messages',  # Nom du client OIDC dans Keycloak
})

oidc = OpenIDConnect(app)

# Route pour la connexion
@app.route('/login')
@oidc.require_login
def login():
    return redirect(url_for('index'))

# Route pour récupérer le nom d'utilisateur
@app.route('/')
def index():
    if oidc.user_loggedin:
        return f"Utilisateur connecté: {oidc.user_getfield('preferred_username')}"
    else:
        return "Utilisateur non connecté"

if __name__ == '__main__':
    app.run(debug=True)
