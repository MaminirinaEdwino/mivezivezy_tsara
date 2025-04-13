import json
from recuperatoin_itineraire import recup_trajet
# trajets = {
#     'V1': ['A', 'B', 'D', 'E'],
#     'V2': ['A', 'C', 'D', 'E'],
#     'V3': ['B', 'D', 'E'],
#     'V4': ['C', 'D'],
#     'V5': ['A', 'C', 'D', 'E'],
#     'V6': ['B', 'D', 'E'],
#     'V7': ['B', 'D', 'E'],
#     'V8': ['A', 'B', 'D', 'E'],
#     'V9': ['A', 'B', 'D', 'E'],
#     'V10': ['A', 'C', 'D', 'E'],
#     'V11': ['B', 'D', 'E'],
#     'V12': ['B', 'D', 'E'],
#     'V13': ['A', 'B', 'D', 'E'],
#     'V14': ['A', 'B', 'D', 'E'],
#     'V15': ['A', 'C', 'D', 'E'],
#     'V16': ['A', 'C', 'D', 'E'],
#     'V17': ['B', 'D', 'E'],
#     'V18': ['C', 'D'],
#     'V19': ['A', 'C', 'D', 'E'],
#     'V20': ['B', 'D', 'E'],
#     'V21': ['B', 'D', 'E'],
#     'V22': ['A', 'B', 'D', 'E'],
#     'V23': ['A', 'B', 'D', 'E'],
#     'V34': ['A', 'C', 'D', 'E'],
#     'V35': ['A', 'B', 'D', 'E'],  # Corrigé pour éviter doublons
#     'V36': ['B', 'D', 'E']
# }

list_trajet = [
  { "depart": [-18.894, 47.517], "destination": [-18.871, 47.544] },
  { "depart": [-18.903, 47.526], "destination": [-18.882, 47.541] },
  { "depart": [-18.886, 47.515], "destination": [-18.853, 47.548] },
  { "depart": [-18.905, 47.525], "destination": [-18.873, 47.558] },
  { "depart": [-18.899, 47.520], "destination": [-18.860, 47.540] },
  { "depart": [-18.907, 47.517], "destination": [-18.854, 47.559] },
  { "depart": [-18.900, 47.528], "destination": [-18.865, 47.549] },
  { "depart": [-18.892, 47.519], "destination": [-18.858, 47.535] },
  { "depart": [-18.893, 47.521], "destination": [-18.867, 47.537] },
  { "depart": [-18.910, 47.529], "destination": [-18.875, 47.543] },
  { "depart": [-18.891, 47.523], "destination": [-18.877, 47.548] },
  { "depart": [-18.897, 47.517], "destination": [-18.878, 47.546] },
  { "depart": [-18.902, 47.516], "destination": [-18.862, 47.536] }
]
#list_trajet.append({"depart": [-18.894, 47.517], "destination": [-18.871, 47.544]})

temps_par_troncon = 1
reservation = []
planification = {}
trajets = {}


for el in list_trajet:
    depart = el["depart"]
    destination = el["destination"]
    # recup_trajet(depart, destination)
    trajets[f'V{len(trajets)}'] = recup_trajet([depart[1], depart[0]], [destination[1], destination[0]])["geometry"]





# for idx, value in enumerate(res):
#     trajets[f'V{idx}'] = value['geometry']