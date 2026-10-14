from math import *


def donne_vecteur (point1,point2):          # donne le vecteur resultant de deux points


    x1 = point1.x
    y1 = point1.y
    z1 = point1.z

    x2 = point2.x
    y2 = point2.y
    z2 = point2.z

    
    return (x2 - x1), (y2 - y1), (z2 - z1)



def donne_produit_scalaire(vecteur_1,vecteur_2):          # donne le produit scalaire de deux vecteurs


    x_v1 = vecteur_1.x
    y_v1 = vecteur_1.y
    z_v1 = vecteur_1.z

    x_v2 = vecteur_2.x
    y_v2 = vecteur_2.y
    z_v2 = vecteur_2.z

    resultat = (x_v1 * x_v2) + (y_v1 * y_v2) + (z_v1 * z_v2)

    return resultat


    

def donne_produit_vectoriel(vecteur_1,vecteur_2):           #donne le produit vectoriel de deux vecteur


    x_v1 = vecteur_1.x
    y_v1 = vecteur_1.y
    z_v1 = vecteur_1.z

    x_v2 = vecteur_2.x
    y_v2 = vecteur_2.y
    z_v2 = vecteur_2.z

    x_v_p = (y_v1 * z_v2) - (z_v1 * y_v2)
    y_v_p = -( (x_v1 * z_v2) - (z_v1 * x_v2) )
    z_v_p = (x_v1 * y_v2) - (y_v1 * x_v2)


    return x_v_p,y_v_p,z_v_p




def donne_distance_entre_points(point_1,point_2):         # donnner la distance entre deux points

    x_1 = point_1.x
    y_1 = point_1.y
    z_1 = point_1.z

    x_2 = point_2.x
    y_2 = point_2.y
    z_2 = point_2.z

    distance_au_carre = ( (x_2 - x_1)**2 ) + ( (y_2 - y_1)**2 ) + ( (z_2 - z_1)**2 )
    
    distance = sqrt(distance_au_carre)

    return distance




def donne_ver_inter_ligne_plan(ligne,plan):           # verifier si il existe une intersection entre une droite et un plan


    produit_scaliare = donne_produit_scalaire(ligne.vecteur,plan.vecteur)
 

    if produit_scaliare == 0 : 
        
        valeur = False
    
    else : 
        
        valeur = True
    

    return valeur




def donne_inter_ligne_plan(ligne,plan):           # donne le point d'intersection entre une droite et un plan
    

    point_x = ligne.point1.x        # cordonner x de un point de la ligne
    point_y = ligne.point1.y        # cordonner y de un point de la ligne
    point_z = ligne.point1.z        # cordonner z de un point de la ligne
    
    vd_ligne_x = ligne.vecteur.x        # cordonner x du vecteur directeur de la ligne
    vd_ligne_y = ligne.vecteur.y        # cordonner y du vecteur directeur de la ligne
    vd_ligne_z = ligne.vecteur.z        # cordonner z du vecteur directeur de la ligne
    
    vn_plan_x = plan.vecteur.x        # cordonner x du vecteur normal du plan          
    vn_plan_y = plan.vecteur.y        # cordonner y du vecteur normal du plan
    vn_plan_z = plan.vecteur.z        # cordonner z du vecteur normal du plan
    
    d_plan = plan.d                   # nombre d de l'eq du plan


    n_alpha = (vn_plan_x * vd_ligne_x) + (vn_plan_y * vd_ligne_y) + (vn_plan_z * vd_ligne_z)        #nombre de alpha dans l'eq du plan
    
    nombre_eq_plan = (vn_plan_x * point_x) + (vn_plan_y * point_y) + (vn_plan_z * point_z) + d_plan      #nombre normal dans l'eq du plan

    alpha = - nombre_eq_plan / n_alpha


    x_intersection = point_x + (alpha * vd_ligne_x)         #cordonner x du point de intersection
    y_intersection = point_y + (alpha * vd_ligne_y)         #cordonner y du point de intersection        
    z_intersection = point_z + (alpha * vd_ligne_z)         #cordonner z du point de intersection


    return x_intersection, y_intersection, z_intersection




def donne_proj_ortho_point_plan(point,plan):          # donne le projeté orthogonal de un point sur un plan
    
    
    point_x = point.x        # cordonner x de un point de la ligne
    point_y = point.y        # cordonner y de un point de la ligne
    point_z = point.z        # cordonner z de un point de la ligne
    
    vd_ligne_x = plan.vecteur.x        # cordonner x du vecteur directeur de la ligne
    vd_ligne_y = plan.vecteur.y        # cordonner y du vecteur directeur de la ligne
    vd_ligne_z = plan.vecteur.z        # cordonner z du vecteur directeur de la ligne
    
    vn_plan_x = plan.vecteur.x        # cordonner x du vecteur normal du plan          
    vn_plan_y = plan.vecteur.y        # cordonner y du vecteur normal du plan
    vn_plan_z = plan.vecteur.z        # cordonner z du vecteur normal du plan
    
    d_plan = plan.d                   # nombre d de l'eq du plan

    n_alpha = (vn_plan_x * vd_ligne_x) + (vn_plan_y * vd_ligne_y) + (vn_plan_z * vd_ligne_z)        #nombre de alpha dans l'eq du plan
    
    nombre_eq_plan = (vn_plan_x * point_x) + (vn_plan_y * point_y) + (vn_plan_z * point_z) + d_plan      #nombre normal dans l'eq du plan

    alpha = nombre_eq_plan / n_alpha

    x_intersection = point_x + (alpha * vd_ligne_x)         #cordonner x du point de intersection
    y_intersection = point_y + (alpha * vd_ligne_y)         #cordonner y du point de intersection        
    z_intersection = point_z + (alpha * vd_ligne_z)         #cordonner z du point de intersection


    return x_intersection, y_intersection, z_intersection




def donne_distance_point_plan(point,plan):            # donne la distance entre un point et un plan


    projeter_orthogonal = donne_proj_ortho_point_plan(point,plan)

    return donne_distance_entre_points(point,projeter_orthogonal)
#mohamed bhim signé karim



def ver_point_dans_triangle(point,point1,point2,point3):            # donne si un point qui appartien aux meme plan que un triangle est dans le traingle ou a l'exterieur

    x1,y1,z1 = donne_vecteur(point1,point2)
    x2,y2,z2 = donne_vecteur(point2,point3)

    x_p = (y1 * z2) - (z1 * y2)
    y_p = -( (x1 * z2) - (z1 * x2) )
    z_p = (x1 * y2) - (y1 * x2)

    #   PROJECTION SUR LE PLAN X,Y OU Y,Z OU X,Z    

    if ( (x_p * 0) + (y_p * 0) + (z_p * 1) ) != 0 :         # verifie si le plan du triangle est perpendiculaire au plan x,y
        
        x_point = point.x
        y_point = point.y
        
        x_point1 = point1.x
        y_point1 = point1.y
        
        x_point2 = point2.x
        y_point2 = point2.y
        
        x_point3 = point3.x
        y_point3 = point3.y
   
    elif ( (x_p * 1) + (y_p * 0) + (z_p * 0) ) != 0 :        # verifie si le plan du triangle est perpendiculaire au plan y,z

        x_point = point.z
        y_point = point.y

        x_point1 = point1.z
        y_point1 = point1.y

        x_point2 = point2.z
        y_point2 = point2.y

        x_point3 = point3.z
        y_point3 = point3.y

    else:                                                     # verifie si le plan du triangle est perpendiculaire au plan x,z

        x_point = point.x
        y_point = point.z

        x_point1 = point1.x
        y_point1 = point1.z

        x_point2 = point2.x
        y_point2 = point2.z

        x_point3 = point3.x
        y_point3 = point3.z
    
    volume_triangle = abs(( x_point1 * (y_point2 - y_point3) + x_point2 * (y_point3 - y_point1) + x_point3 * (y_point1 - y_point2)) / 2)
    
    a1 = abs(( x_point1 * (y_point2 - y_point) + x_point2 * (y_point - y_point1) + x_point * (y_point1 - y_point2)) / 2) # air de la premier partie
    a2 = abs(( x_point * (y_point2 - y_point3) + x_point2 * (y_point3 - y_point) + x_point3 * (y_point - y_point2)) / 2) # air de la deuxieme partie
    a3 = abs(( x_point1 * (y_point - y_point3) + x_point * (y_point3 - y_point1) + x_point3 * (y_point1 - y_point)) / 2) # air de la troisieme partie

    total  = a1 + a2 + a3 

    if ((abs(volume_triangle - total)) < 2000 and volume_triangle > 10000 ) or ((volume_triangle == total) and (volume_triangle < 500 )):           # si l'ensemble des air des parties des triangle cree par le point a verifier est egale aux volume du triangle alors le point appartient
        print(total)
        print(volume_triangle)
        reponse = True

    else : 
        print(total)
        print(volume_triangle)

        reponse = False

    return reponse












        


   











