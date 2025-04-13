import json
from data import reservation, planification
def afficher_planification(vehicule_user):
    planification_json = {}
    new_dict = {}
    long_max = 0
    print("\n=== PLANIFICATION DU TRAFIC ===\n")
    for voiture, plan in planification.items():
        print(f"{voiture} :")
        new_dict[voiture] = []
        for troncon, t in plan:
            # print(f"  - Passe sur {troncon[0]} ➝ {troncon[1]} à t = {t}")
            new_dict[voiture].append((voiture, troncon[0], troncon[1], t))
        print("")
    
    for el in new_dict:
        # print(len(new_dict[el]), el[0], el[1])
        if len(new_dict[el]) > long_max:
            long_max = len(new_dict[el])
    
    for el in range(long_max):
        planification_json[f"{el}"] = []
    
    for el in new_dict:
        for e in new_dict[el]:
            planification_json[f"{e[3]}"].append(e)
            
    trajet_finale = []
    for el in planification_json:
        for e in planification_json[el]:
            if e[0] == vehicule_user:
                trajet_finale.append(e[1])   
                   
    with open("planification.json", "w") as file:
        json.dump(planification_json, file, indent=4)
    
    #print(trajet_finale)
    return trajet_finale
    
    # print(planification_json)

def afficher_occupation_par_temps():
    print("=== OCCUPATION DES TRONÇONS PAR TEMPS ===\n")
    occup_par_temps = {}
    for troncon, temps_dict in reservation:
        for t, v in enumerate(temps_dict):
            if t not in occup_par_temps:
                occup_par_temps[t] = []
            occup_par_temps[t].append((v, troncon))

    for t in sorted(occup_par_temps.keys()):
        print(f"Temps t = {t}:")
        for v, troncon in occup_par_temps[t]:
            print(f"  {v} circule sur {troncon[0]} ➝ {troncon[1]}")
        print("")
