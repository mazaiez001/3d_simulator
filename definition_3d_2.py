from math import *
import turtle
from object_3d_2 import *
from turtle import *
from time import *

    #mohamed()

def donne_vecteur (point1, point2):          # donne le vecteur resultant de deux points


    x1 = point1.x
    y1 = point1.y
    z1 = point1.z

    x2 = point2.x
    y2 = point2.y
    z2 = point2.z

    v = vecteur ((x2 - x1), (y2 - y1), (z2 - z1))

    return v



def donne_produit_scalaire (vecteur_1, vecteur_2):          # donne le produit scalaire de deux vecteurs


    x_v1 = vecteur_1.x
    y_v1 = vecteur_1.y
    z_v1 = vecteur_1.z

    x_v2 = vecteur_2.x
    y_v2 = vecteur_2.y
    z_v2 = vecteur_2.z

    resultat = (x_v1 * x_v2) + (y_v1 * y_v2) + (z_v1 * z_v2)

    return resultat



def donne_produit_vectoriel (vecteur_1, vecteur_2):           #donne le produit vectoriel de deux vecteur


    x_v1 = vecteur_1.x
    y_v1 = vecteur_1.y
    z_v1 = vecteur_1.z

    x_v2 = vecteur_2.x
    y_v2 = vecteur_2.y
    z_v2 = vecteur_2.z

    x_v_p = (y_v1 * z_v2) - (z_v1 * y_v2)
    y_v_p = -( (x_v1 * z_v2) - (z_v1 * x_v2) )
    z_v_p = (x_v1 * y_v2) - (y_v1 * x_v2)

    vp = vecteur(x_v_p, y_v_p, z_v_p)

    return vp



def donne_distance_entre_points (point_1, point_2):         # donnner la distance entre deux points

    x_1 = point_1.x
    y_1 = point_1.y
    z_1 = point_1.z

    x_2 = point_2.x
    y_2 = point_2.y
    z_2 = point_2.z

    distance_au_carre = ( (x_2 - x_1)**2 ) + ( (y_2 - y_1)**2 ) + ( (z_2 - z_1)**2 )
    
    distance = sqrt(distance_au_carre)

    return distance



def donne_ver_point_appartient_ligne (point0,ligne1):            # verifie si un point appartient a une ligne


    longeur_ligne1 = donne_distance_entre_points(ligne1.point1,ligne1.point2)
    
    longeur_point0_point1 = donne_distance_entre_points(point0,ligne1.point1)
    longeur_point0_point2 = donne_distance_entre_points(point0,ligne1.point2)

    total = longeur_point0_point1 + longeur_point0_point2
    
    if round(total,5) == round(longeur_ligne1,5) : 

        return True             # le point appartient a la ligne
    
    else :
        
        return False            # le point n'appartient pas a la ligne



def donne_ver_inter_ligne_plan (ligne, plan):           # verifier si il existe une intersection entre une droite et un plan


    produit_scaliare = donne_produit_scalaire(ligne.vecteur_directeur,plan.vecteur_normal)
 

    if produit_scaliare == 0 : 
        
        valeur = False
    
    else : 
        
        valeur = True
    

    return valeur



def donne_inter_ligne_plan (ligne, plan):           # donne le point d'intersection entre une droite et un plan
    

    if donne_ver_inter_ligne_plan(ligne,plan) == False :
        
        return False

    point_x = ligne.point1.x        # cordonner x de un point de la ligne
    point_y = ligne.point1.y        # cordonner y de un point de la ligne
    point_z = ligne.point1.z        # cordonner z de un point de la ligne
    
    vd_ligne_x = ligne.vecteur_directeur.x        # cordonner x du vecteur directeur de la ligne
    vd_ligne_y = ligne.vecteur_directeur.y        # cordonner y du vecteur directeur de la ligne
    vd_ligne_z = ligne.vecteur_directeur.z        # cordonner z du vecteur directeur de la ligne
    
    vn_plan_x = plan.vecteur_normal.x        # cordonner x du vecteur normal du plan          
    vn_plan_y = plan.vecteur_normal.y        # cordonner y du vecteur normal du plan
    vn_plan_z = plan.vecteur_normal.z        # cordonner z du vecteur normal du plan
    
    d_plan = plan.d                   # nombre d de l'eq du plan


    n_alpha = (vn_plan_x * vd_ligne_x) + (vn_plan_y * vd_ligne_y) + (vn_plan_z * vd_ligne_z)        # nombre de alpha dans l'eq du plan
    
    nombre_eq_plan = (vn_plan_x * point_x) + (vn_plan_y * point_y) + (vn_plan_z * point_z) + d_plan      # nombre normal dans l'eq du plan

    alpha = - nombre_eq_plan / n_alpha


    x_intersection = point_x + (alpha * vd_ligne_x)         # cordonner x du point de intersection
    y_intersection = point_y + (alpha * vd_ligne_y)         # cordonner y du point de intersection        
    z_intersection = point_z + (alpha * vd_ligne_z)         # cordonner z du point de intersection

    p = point(x_intersection, y_intersection, z_intersection) # point de intersection
    
    return p



def donne_ver_point_dans_plan (point, plan):          # verifier si un point appartient a un plan


    test = ( plan.vecteur_normal.x * point.x ) + ( plan.vecteur_normal.y * point.y ) + ( plan.vecteur_normal.z * point.z ) + plan.d
    
    
    
    if round(test) == 0 :
        
        
        return True
    
    else :
        
        return False



def donne_ver_point_dans_triangle (point_c, point1, point2, point3):            # donne si un point qui appartien aux meme plan que un triangle est dans le traingle ou a l'exterieur

    v1 = donne_vecteur(point1,point2)
    v2 = donne_vecteur(point2,point3)

    v_normal_tri = donne_produit_vectoriel(v1,v2)           # le vecteur normal du plan qui contien le triangle

    plan_tri = plan(v_normal_tri,point1)
    
    if donne_ver_point_dans_plan(point_c,plan_tri) == False :           #verifie si le point et le triangle sont dans le meme plan
       
        return False

    #PROJECTION SUR LE PLAN X,Y OU Y,Z OU X,Z    
    
    if ( abs(donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1))) >= abs(donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0))) ) and ( abs(donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1))) >= abs(donne_produit_scalaire(v_normal_tri,vecteur(0, 1, 0))) ) :
       
        max = donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1))
    
    elif ( abs(donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0))) >= abs(donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1))) ) and ( abs(donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0))) >= abs(donne_produit_scalaire(v_normal_tri,vecteur(0, 1, 0))) ) :

        max = donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0))
    
    else:

        max = donne_produit_scalaire(v_normal_tri,vecteur(0, 1, 0))
    # ###print("point1 = ",point1.x,point1.y,point1.z)
    # ###print("point2 = ",point2.x,point2.y,point2.z)
    # ###print("point3 = ",point3.x,point3.y,point3.z)
    # ###print("v1 = ",v1.x,v1.y,v1.z)
    # ###print("v2 = ",v2.x,v2.y,v2.z)
   

    # ##print(v_normal_tri.x,v_normal_tri.y,v_normal_tri.z)
    # ##print(donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1)))
    # ##print(donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0)))
    # ##print(donne_produit_scalaire(v_normal_tri,vecteur(0, 1, 0)))
    if donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1)) == max :         # verifie si le plan du triangle est perpendiculaire au plan x,y
        
        ###print("plan1",(donne_produit_scalaire(v_normal_tri,vecteur(0, 0, 1))))
        x_point = point_c.x
        y_point = point_c.y
        
        x_point1 = point1.x
        y_point1 = point1.y
        
        x_point2 = point2.x
        y_point2 = point2.y
        
        x_point3 = point3.x
        y_point3 = point3.y
   
    elif donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0)) == max :        # verifie si le plan du triangle est perpendiculaire au plan y,z
        
        ###print("plan2",(donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0))))
        x_point = point_c.z
        y_point = point_c.y

        x_point1 = point1.z
        y_point1 = point1.y

        x_point2 = point2.z
        y_point2 = point2.y

        x_point3 = point3.z
        y_point3 = point3.y

    elif donne_produit_scalaire(v_normal_tri,vecteur(0, 1, 0)) == max:         # verifie si le plan du triangle est perpendiculaire au plan x,z
        ###print("plan3",(donne_produit_scalaire(v_normal_tri,vecteur(1, 0, 0))))
        x_point = point_c.x
        y_point = point_c.z

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
    
    #print("volume du triangle avec round = ",round(volume_triangle))
    #print("total avec round = ",round(total))
    #print("volume du triangle",volume_triangle)
    #print("total",total)
    
    if round(volume_triangle,5) == round(total,5) :         # si l'ensemble des air des parties des triangle cree par le point a verifier est egale aux volume du triangle alors le point appartient
        
        reponse = True
    
    else : 
        
        reponse = False

    return reponse



def donne_liste_point_intersection_vision (ligne1, carre, point_centre):          # donne une liste des intersection des triangle du carre


    les_points = []
    
    ligne_p1_p2 = ligne(carre.point1, carre.point2)
    ligne_pc_p1 = ligne(point_centre, carre.point1)
    vn_p1 = donne_produit_vectoriel(ligne_pc_p1.vecteur_directeur, ligne_p1_p2.vecteur_directeur)

    p1 = plan(vn_p1,point_centre)


    ligne_p2_p3 = ligne(carre.point2, carre.point3)
    ligne_pc_p2 = ligne(point_centre, carre.point2)
    vn_p2 = donne_produit_vectoriel(ligne_pc_p2.vecteur_directeur, ligne_p2_p3.vecteur_directeur)

    p2 = plan(vn_p2,point_centre)
   
    
    ligne_p3_p4 = ligne(carre.point3, carre.point4)
    ligne_pc_p3 = ligne(point_centre, carre.point3)
    vn_p3 = donne_produit_vectoriel(ligne_pc_p3.vecteur_directeur, ligne_p3_p4.vecteur_directeur)

    p3 = plan(vn_p3,point_centre)


    ligne_p4_p1 = ligne(carre.point4, carre.point1)
    ligne_pc_p4 = ligne(point_centre, carre.point4)
    vn_p4 = donne_produit_vectoriel(ligne_pc_p4.vecteur_directeur, ligne_p4_p1.vecteur_directeur)

    p4 = plan(vn_p4,point_centre)


    vn_p0 = vecteur(0,0,0)

    if vn_p1 == vn_p0 or vn_p2 == vn_p0 or vn_p3 == vn_p0 or vn_p4 == vn_p0 :           # eviter le produit vectoriel de deux vecteur colinaire et parsuite il est non visible
        #print("plan non visible")
        les_points.append("plan non visible")
        return les_points
        
    if donne_ver_point_dans_plan(carre.point4, p1) == True :            # si le plan est non visible
        #print("plan non visible")
        les_points.append("plan non visible")
        return les_points

    p_list = [p1, p2, p3, p4]
    point1_list = [carre.point1, carre.point2, carre.point3, carre.point4]
    point2_list = [carre.point2, carre.point3, carre.point4, carre.point1]
    
    for p, point1, point2 in zip (p_list,point1_list,point2_list) :
        
        if donne_ver_inter_ligne_plan(ligne1,p) :
            #print("intersection")
            point_intersection = donne_inter_ligne_plan(ligne1,p)            # point intersection de la ligne et le plan du triangle
            
            distance = 1000
    
        
            d_pt1 = donne_distance_entre_points(point_centre,point1)
            d_pt2 = donne_distance_entre_points(point_centre,point2)

            rapport1 = distance / d_pt1
            rapport2 = distance / d_pt2

            pt1 = point(point1.x * rapport1, point1.y * rapport1, point1.z * rapport1)
            pt2 = point(point2.x * rapport2, point2.y * rapport2, point2.z * rapport2)

            # verification : le point appartient au triangle ?

            if (donne_ver_point_dans_triangle (point_intersection,point_centre,pt1,pt2) == True ) and (donne_ver_point_dans_triangle (point_intersection,point_centre,point1,point2) == False) :

                les_points.append(point_intersection)
            else:
                pass
                #print('deux triangle')   
        else:
            
            pass
            #print("pas intersection")
    
    
    return les_points

    

def donne_ver_point_dans_carre(point1,carre1):          # donne si un point qui appartien aux meme plan que un carre est dans le traingle ou a l'exterieur
    
    if donne_ver_point_dans_triangle(point1, carre1.point1, carre1.point2, carre1.point3) or donne_ver_point_dans_triangle(point1, carre1.point3, carre1.point4, carre1.point1):
      
        return True
    
    else:

        return False



def donne_intersection_ligne_carre(ligne1,carre1):          # donne le point d'intersection entre une ligne et un plan s'il existe

    point_intersection = []

    if donne_ver_inter_ligne_plan(ligne1,carre1.plan) == False:

        return point_intersection
    
    elif donne_ver_inter_ligne_plan(ligne1,carre1.plan) == True:
        
        
        pt = donne_inter_ligne_plan(ligne1,carre1.plan)
        
        if donne_ver_point_dans_carre(pt,carre1) == True:

            
            point_intersection.append(donne_inter_ligne_plan(ligne1,carre1.plan))

            return point_intersection
        
    return point_intersection
        


def donne_ligne_transformer (ligne_choisie,carre,point_centre):         # donne l'affichage d'une ligne par rapport a un carré


    ligne_transformer = []
    #print('les intersection triangle')
    les_intersection = donne_liste_point_intersection_vision(ligne_choisie,carre,point_centre)
    #print('les intersection carre')
    les_intersection_carre = donne_intersection_ligne_carre(ligne_choisie,carre)
    
    
    
    j = len(les_intersection_carre)
    
    #print('j =', j)
    n = len(les_intersection)
    #print('n =', n)
    
    if n >= 2 and n < 5 :           # 2 , 3 ou 4 intersection
        
        
        if (donne_ver_point_appartient_ligne(les_intersection[0],ligne_choisie) == True) and (donne_ver_point_appartient_ligne(les_intersection[1],ligne_choisie) == True):
            
            # l'intersection 1 et l'intersection 2 appartient a la portion de droite choisie

            if donne_distance_entre_points(les_intersection[0],ligne_choisie.point2) < donne_distance_entre_points(les_intersection[1],ligne_choisie.point2) :
            
                ligne1 = ligne(ligne_choisie.point1,les_intersection[1])
                ligne2 = ligne(ligne_choisie.point2,les_intersection[0])

            else:
        
                ligne1 = ligne(ligne_choisie.point1,les_intersection[0])
                ligne2 = ligne(ligne_choisie.point2,les_intersection[1])
           
            
            ligne_transformer = [ligne1,ligne2]
 

        elif (donne_ver_point_appartient_ligne(les_intersection[0],ligne_choisie) == True) and (donne_ver_point_appartient_ligne(les_intersection[1],ligne_choisie) == False) :
            
            # seulement l'intersection 1 appartient a la portion de droite choisie

            if donne_distance_entre_points(les_intersection[1],ligne_choisie.point1) > donne_distance_entre_points(les_intersection[1],ligne_choisie.point2) :
                
                ligne1 = ligne(ligne_choisie.point1,les_intersection[0])

            else : 
                
                ligne1 = ligne(ligne_choisie.point2,les_intersection[0])
            

            ligne_transformer = [ligne1]
        
        elif (donne_ver_point_appartient_ligne(les_intersection[0],ligne_choisie) == False) and (donne_ver_point_appartient_ligne(les_intersection[1],ligne_choisie) == True):
            # #print("test")
            # #print(donne_distance_entre_points(les_intersection[1],ligne_choisie.point1) + donne_distance_entre_points(les_intersection[1],ligne_choisie.point2))
            # #print(donne_distance_entre_points(ligne_choisie.point1,ligne_choisie.point2))
            # seulement l'intersection 2 appartient a la portion de droite choisie            

            if donne_distance_entre_points(les_intersection[0],ligne_choisie.point1) > donne_distance_entre_points(les_intersection[0],ligne_choisie.point2) :
                
                ligne1 = ligne(ligne_choisie.point1,les_intersection[1])

            else : 
                
                ligne1 = ligne(ligne_choisie.point2,les_intersection[1])
            

            ligne_transformer = [ligne1]
        elif (donne_ver_point_appartient_ligne(ligne_choisie.point1,ligne(les_intersection[0],les_intersection[1])) == True) and (donne_ver_point_appartient_ligne(ligne_choisie.point2,ligne(les_intersection[0],les_intersection[1])) == True):
            
            ligne_transformer = []
        
        else:
            
            # aucun intersection appartient a la portion de droite               

            ligne_transformer = [ligne_choisie]
    

    elif n == 1 :         # une seule intersection

        if les_intersection[0] == "plan non visible":
        
            ligne1 = ligne_choisie

            ligne_transformer = [ligne1]

        elif j == 0:
            
            
            if donne_ver_point_appartient_ligne(les_intersection[0], ligne_choisie) == True:

                if donne_distance_entre_points(ligne_choisie.point1,donne_inter_ligne_plan(ligne_choisie,carre.plan)) < donne_distance_entre_points(ligne_choisie.point2,donne_inter_ligne_plan(ligne_choisie,carre.plan)) :

                    ligne1 = ligne(ligne_choisie.point1, les_intersection[0])

                else:

                    ligne1 = ligne(ligne_choisie.point2, les_intersection[0])
            
                ligne_transformer = [ligne1]
            
            elif donne_ver_point_appartient_ligne(les_intersection[0], ligne_choisie) == False:
                # #print(ligne_choisie.point1.x, ligne_choisie.point1.y, ligne_choisie.point1.z)
                # #print(ligne_choisie.point2.x, ligne_choisie.point2.y, ligne_choisie.point2.z)
                v = donne_vecteur(ligne_choisie.point1,ligne_choisie.point2)
                # #print(v.x,v.y,v.z)
                # #print(carre.plan.vecteur_normal.x,carre.plan.vecteur_normal.y,carre.plan.vecteur_normal.z)
                if donne_distance_entre_points(ligne_choisie.point1, les_intersection[0]) < donne_distance_entre_points(ligne_choisie.point1, donne_inter_ligne_plan(ligne_choisie, carre.plan)):

                    ligne_transformer = []

                
                else:

                    ligne_transformer = [ligne_choisie]


        elif j == 1:
            
            # #print(donne_distance_entre_points(ligne_choisie.point1,ligne_choisie.point2))
            # #print(donne_distance_entre_points(les_intersection[0],ligne_choisie.point1) + donne_distance_entre_points(les_intersection[0],ligne_choisie.point2))
        

            # #print(donne_ver_point_appartient_ligne(les_intersection[0],ligne_choisie))
            # #print(donne_ver_point_appartient_ligne(les_intersection_carre[0],ligne_choisie))
            if (donne_ver_point_appartient_ligne(les_intersection[0],ligne_choisie) == True) and (donne_ver_point_appartient_ligne(les_intersection_carre[0],ligne_choisie) == True):
                
                if donne_distance_entre_points(ligne_choisie.point1,les_intersection[0]) > donne_distance_entre_points(ligne_choisie.point1,les_intersection_carre[0]):

                    ligne1 = ligne(ligne_choisie.point1,les_intersection_carre[0])
                    ligne2 = ligne(ligne_choisie.point2,les_intersection[0])

                else:

                    ligne1 = ligne(ligne_choisie.point2,les_intersection_carre[0])
                    ligne2 = ligne(ligne_choisie.point1,les_intersection[0])
                
                ligne_transformer = [ligne1, ligne2]

            elif (donne_ver_point_appartient_ligne(ligne_choisie.point1, ligne(les_intersection[0], les_intersection_carre[0])) == True) and (donne_ver_point_appartient_ligne(ligne_choisie.point2, ligne(les_intersection[0], les_intersection_carre[0])) == True) :
                
                ligne_transformer = []
            
            elif (donne_ver_point_appartient_ligne(ligne_choisie.point1, ligne(les_intersection[0], les_intersection_carre[0])) == False) and (donne_ver_point_appartient_ligne(ligne_choisie.point2, ligne(les_intersection[0], les_intersection_carre[0])) == True) :
                
                if donne_distance_entre_points(ligne_choisie.point1, les_intersection[0]) < donne_distance_entre_points(ligne_choisie.point1, les_intersection_carre[0]) :

                    ligne1 = ligne(ligne_choisie.point1, les_intersection[0])

                else:

                    ligne1 = ligne(ligne_choisie.point1, les_intersection_carre[0])

                ligne_transformer = [ligne1]
            
            elif (donne_ver_point_appartient_ligne(ligne_choisie.point1, ligne(les_intersection[0], les_intersection_carre[0])) == True) and (donne_ver_point_appartient_ligne(ligne_choisie.point2, ligne(les_intersection[0], les_intersection_carre[0])) == False) :
                
                if donne_distance_entre_points(ligne_choisie.point2, les_intersection[0]) < donne_distance_entre_points(ligne_choisie.point2, les_intersection_carre[0]) :
                    
                    ligne1 = ligne(ligne_choisie.point2, les_intersection[0])

                else:

                    ligne1 = ligne(ligne_choisie.point2, les_intersection_carre[0])

                ligne_transformer = [ligne1]
                   
                
            else :
                 
                ligne_transformer = [ligne_choisie]
    
    elif n == 0:

        
        if j == 1:

            
            if donne_ver_point_appartient_ligne(les_intersection_carre[0], ligne_choisie) == True:

                if donne_distance_entre_points(ligne_choisie.point1, point_centre) < donne_distance_entre_points(ligne_choisie.point2, point_centre) :

                    ligne1 = ligne(ligne_choisie.point1, les_intersection_carre[0])
                
                else:

                    ligne1 = ligne(ligne_choisie.point2, les_intersection_carre[0])

                ligne_transformer = [ligne1]
            
            elif donne_ver_point_appartient_ligne(les_intersection_carre[0], ligne_choisie) == False:

                if donne_distance_entre_points(ligne_choisie.point1, point_centre) > donne_distance_entre_points(ligne_choisie.point1, les_intersection_carre[0]):

                    ligne_transformer = []
                
                else:
                    
                    ligne_transformer = [ligne_choisie]

        else :
            
            ligne_transformer = [ligne_choisie]
    
    return ligne_transformer         
    


def donne_liste_ligne_de_liste_carre(liste_carre,point_centre):         # donne une liste de lignes resultant du traitement de une liste de carre (traitement vision)

    les_ligne = []
    
    for i, carre_i in enumerate(liste_carre) :
        #print('carre = ',i+1)
        
        
        liste_carre_a_verifier = liste_carre.copy()
      
        del liste_carre_a_verifier [i]
      
        
    
        for j,ligne_i in enumerate([carre_i.ligne1, carre_i.ligne2, carre_i.ligne3, carre_i.ligne4]) :
            
            ##print("ligne = ", j+1)
            liste_ligne_transformer = donne_ligne_transformer(ligne_i, liste_carre_a_verifier[0], point_centre)

            for carre_ver_i in liste_carre_a_verifier[1:] :
                
                liste_changer = []
                
                for ligne_tro_i in liste_ligne_transformer :
                    
                    liste_changer.extend(donne_ligne_transformer(ligne_tro_i, carre_ver_i, point_centre))
                
                liste_ligne_transformer = liste_changer.copy()
                
                
            les_ligne.extend(liste_ligne_transformer)
            
   
    return les_ligne



def affichage_liste(liste_carre):
    
    p = plan(vecteur(0,0,1),point(0,0,0.1))
    centre = point(0,0,0)

    liste_ligne_affichage = donne_liste_ligne_de_liste_carre(liste_carre,centre)
    
    
    turtle.tracer(0, 0)
    for lignes in liste_ligne_affichage:

        l1 = ligne(centre,lignes.point1)
        l2 = ligne(centre,lignes.point2)
        
        p1 = donne_inter_ligne_plan(l1,p)

        p2 = donne_inter_ligne_plan(l2,p)
        
        penup()
        goto(p1.x*50000,p1.y*50000)
        pendown()
        goto(p2.x*50000,p2.y*50000)
        penup()
   
    turtle.update() 
    turtle.clear() 
    

def donne_rotation(centre, centre_rotation, point_m, alpha,choix):


    x_d = centre_rotation.x - centre.x
    y_d = centre_rotation.z - centre.z

    x_m_t = point_m.x - x_d
    y_m_t = point_m.z - y_d

    longeur_centre_rotation_point_m = sqrt( (x_m_t ** 2) + (y_m_t ** 2) )

    cos_m = x_m_t / longeur_centre_rotation_point_m
    sin_m = y_m_t / longeur_centre_rotation_point_m

    angle_cos_inverse1 = acos(cos_m)
    angle_cos_inverse2 = - angle_cos_inverse1

    angle_sin_inverse1 = asin(sin_m)
    angle_sin_inverse2 = pi - angle_sin_inverse1
    
    if round(angle_cos_inverse1,2) == round(angle_sin_inverse1,2) :

        angle = angle_cos_inverse1
    
    elif round(angle_cos_inverse1,2) == round(angle_sin_inverse2,2) :

        angle = angle_cos_inverse1

    elif round(angle_cos_inverse2,2) == round(angle_sin_inverse1,2) :

        angle = angle_cos_inverse2
    
    elif round(angle_cos_inverse2,2) == round(angle_sin_inverse2,2) :

        angle = angle_cos_inverse2

    x_m = (cos( angle + alpha ) * longeur_centre_rotation_point_m ) + x_d
    y_m = (sin( angle + alpha ) * longeur_centre_rotation_point_m ) + y_d


    if choix == ("x"):
    
        return x_m

    elif choix == ("y"):

        return y_m 
    


    
                       
                        

            

        



                


       
        














