from data import trajets, list_trajet
from planner import planifier_voiture
from display import afficher_planification
# , afficher_occupation_par_temps
from recuperatoin_itineraire import recup_trajet


def main_recup(depart: list, destination: list):
    list_vehicule = [
  [-18.901, 47.522],
  [-18.895, 47.518],
  [-18.908, 47.527],
  [-18.890, 47.516],
  [-18.904, 47.524],
  [-18.897, 47.519],
  [-18.906, 47.521],
  [-18.893, 47.525],
  [-18.902, 47.517],
  [-18.899, 47.529],
  [-18.911, 47.520],
  [-18.889, 47.523],
  [-18.909, 47.515],
  [-18.896, 47.526],
  [-18.903, 47.518],
  [-18.887, 47.524],
  [-18.900, 47.519],
  [-18.912, 47.527],
  [-18.894, 47.516],
  [-18.907, 47.522],
  [-18.888, 47.520],
  [-18.905, 47.528],
  [-18.892, 47.517],
  [-18.910, 47.525],
  [-18.898, 47.521],
  [-18.901, 47.529],
  [-18.886, 47.518],
  [-18.904, 47.523],
  [-18.893, 47.515],
  [-18.909, 47.526],
  [-18.899, 47.520],
  [-18.906, 47.524],
  [-18.887, 47.519],
  [-18.902, 47.527],
  [-18.895, 47.516],
  [-18.911, 47.522],
  [-18.891, 47.525],
  [-18.908, 47.517],
  [-18.897, 47.528],
  [-18.900, 47.521],
  [-18.889, 47.529],
  [-18.905, 47.518],
  [-18.894, 47.523],
  [-18.910, 47.515],
  [-18.896, 47.526],
  [-18.903, 47.520],
  [-18.888, 47.524],
  [-18.907, 47.519],
  [-18.902, 47.527]
]
    trajets[f'V{len(trajets)}'] = recup_trajet([depart[1], depart[0]], [
        destination[1], destination[0]])["geometry"]
    vehicule_user = f"V{len(list_trajet)}"
    for voiture, chemin in trajets.items():
        planifier_voiture(voiture, chemin)

    print("vehicule user", vehicule_user)
    print(len(trajets))
    return {
        "deplacement" : [[depart[1], depart[0]], [
        destination[1], destination[0]]],
        "vehicule": list_vehicule
	}
    # afficher_occupation_par_temps()
