from data import reservation, planification, temps_par_troncon

def planifier_voiture(nom, chemin):
    t_depart = 0
    while True:
        conflit = False
        t_courant = t_depart
        traj_planifie = []

        for i in range(len(chemin) - 1):
            depart = chemin[i]
            arrivee = chemin[i + 1]
            troncon = (depart, arrivee)

            if troncon in reservation and t_courant in reservation:
                conflit = True
                break

            traj_planifie.append((troncon, t_courant))
            t_courant += temps_par_troncon

        if not conflit:
            for troncon, t in traj_planifie:
                print(troncon)
                if troncon not in reservation:
                    reservation.append(troncon)
                # reservation[troncon][t] = nom
            planification[nom] = traj_planifie
            break
        else:
            t_depart += 1
