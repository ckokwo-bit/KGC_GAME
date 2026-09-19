import json
def creer_compte(nom,psw):
    try:
        with open("data.json","r",encoding="utf-8") as file:
            utilisateur=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        utilisateur={}
    if nom in utilisateur:
        return "ERREUR compte deja present"
    utilisateur[nom]={
        "psw":psw
    }

    with open("data.json","w",encoding="utf-8") as file:
        json.dump(utilisateur,file,indent=4,ensure_ascii=False)

    return f"SUCCESS. compte cree nom:{nom}"

def connexion(nom,psw):
    try:
        with open("data.json","r",encoding="utf-8") as file:
            utilisateur=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        utilisateur={}
    if nom not in utilisateur:
        return "ERREUR utilisateur non reconnu"
    if utilisateur[nom]["psw"] != psw:
        return "ERREUR mot de passe incorrect"
    return "SUCCES CONNEXION REUSSIE"


