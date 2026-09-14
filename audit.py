import csv
from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()



def age_est_valide(age):
    try:
        age = int(age)
    except ValueError :
        return False
    if age > 0 and age <= 120:
        return True
    else:
        return False

def email_est_valide(email):
    if "@" in email:
        return True
    else:
        return False

def telephone_est_valide(telephone):
    if len(telephone) == 10 and telephone[0] == "0":
        return True
    else:
        return False

nb_client_invalide = 0
clients_invalide = []
nb_anomalies_age = 0
nb_anomalies_telephone = 0
nb_anomalies_email = 0

with open("clients.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for client in lecteur:
        anomalies = []
        if not age_est_valide(client["age"]):
            anomalies.append("age")
            nb_anomalies_age = nb_anomalies_age + 1
        if not email_est_valide(client["email"]):
            anomalies.append("email")
            nb_anomalies_email = nb_anomalies_email + 1
        if not telephone_est_valide(client["telephone"]):
            anomalies.append("telephone")
            nb_anomalies_telephone = nb_anomalies_telephone + 1
        if len(anomalies)>0:
            nb_client_invalide = nb_client_invalide + 1
            print(client["nom"], "-> anomalies :", ", ".join(anomalies))
            clients_invalide.append({"nom" : client["nom"], "anomalies" : ", ".join(anomalies)})
    print(clients_invalide)

if nb_client_invalide == 0:
    print("aucune anomalie détectée")
if nb_client_invalide == 1:
    print("il y a un seul client ayant au moins une anomalie, voir fichier rapport.md pour plus de détails")
if nb_client_invalide > 1:
    print("un total de", nb_client_invalide, "clients ayant au moins une anomalie, voir fichier rapport.md pour plus de détails")

# écriture du rapport dans un fichier rapport.md dans le même dossier où est exécuté ce code.
with open("rapport.md", "w", encoding="utf-8") as fichier:
    fichier.write("# Rapport d'audit CRM\n")
    fichier.write("\n")
    fichier.write("nombre de clients invalides : ")
    fichier.write(str(nb_client_invalide) + "\n")
    fichier.write("dont : \n")
    fichier.write("le nombre de champs \"age\" incorrects : ")
    fichier.write(str(nb_anomalies_age) + "\n")
    fichier.write("le nombre de champs \"email\" incorrects : ")
    fichier.write(str(nb_anomalies_email) + "\n")
    fichier.write("le nombre de champs \"telephone\" incorrects : ")
    fichier.write(str(nb_anomalies_telephone) + "\n")
    fichier.write("Détails des clients concernés \n")
    for client in clients_invalide:
        fichier.write("- " + client["nom"] + " : " + client["anomalies"] + "\n")


with open("rapport.md", "r", encoding="utf-8") as fichier:
    contenu_rapport = fichier.read()

consigne = "Voici un rapport d'audit qualité CRM brut. Rédige-en une synthèse en 3-4 phrases pour un responsable non technique. base tes chiffres sur les données du fichier afin de respecter les règles GDPR, ne communique jamais directement le noms des clients, utilise leurs identifiant à la places s'il y en a sinon n'inquique rien.\n\n"
question = consigne + contenu_rapport

client = Anthropic()


reponse = client.messages.create(
model="claude-sonnet-4-6",
max_tokens=2000,
messages=[
{"role": "user", "content": question}
]
)
print(reponse.content[0].text)