from math import *
class vecteur (object):

    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z



class point (object):
    
    def __init__(self,x,y,z):
        
        self.x = x
        self.y = y
        self.z = z



class ligne (object):

    def __init__(self,point1,point2):

        self.point1 = point1
        self.point2 = point2
        
        self.vecteur_directeur = self.donne_vecteur (self.point1,self.point2)
    
    def donne_vecteur (self,point1,point2):

        x1 = point1.x
        y1 = point1.y
        z1 = point1.z

        x2 = point2.x
        y2 = point2.y
        z2 = point2.z

        v = vecteur((x2 - x1), (y2 - y1), (z2 - z1))

        return v



class plan (object):

    def __init__(self,vecteur,point):

        self.vecteur_normal = vecteur
        self.point = point
        self.d = - ( (self.point.x * self.vecteur_normal.x) + (self.point.y * self.vecteur_normal.y) + (self.point.z * self.vecteur_normal.z) ) 



class carre (object): 
    
    def __init__(self,point1,point2,point3,point4):
        
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.ligne1 = ligne (self.point1,self.point2)
        self.ligne2 = ligne (self.point2,self.point3)
        self.ligne3 = ligne (self.point3,self.point4)
        self.ligne4 = ligne (self.point4,self.point1)
        self.vecteur_normal = self.donne_produit_vectoriel (self.ligne1.vecteur_directeur, self.ligne2.vecteur_directeur)
        self.plan = plan(self.vecteur_normal,self.point1)

    def donne_addition_cordonner_x(self,n):

        self.point1.x += n
        self.point2.x += n
        self.point3.x += n
        self.point4.x += n

        self.ligne1 = ligne (self.point1,self.point2)
        self.ligne2 = ligne (self.point2,self.point3)
        self.ligne3 = ligne (self.point3,self.point4)
        self.ligne4 = ligne (self.point4,self.point1)
        
        self.vecteur_normal = self.donne_produit_vectoriel (self.ligne1.vecteur_directeur, self.ligne2.vecteur_directeur)
        
        self.plan = plan(self.vecteur_normal,self.point1)
    
    def donne_addition_cordonner_y(self,n):

        self.point1.y += n
        self.point2.y += n
        self.point3.y += n
        self.point4.y += n

        self.ligne1 = ligne (self.point1,self.point2)
        self.ligne2 = ligne (self.point2,self.point3)
        self.ligne3 = ligne (self.point3,self.point4)
        self.ligne4 = ligne (self.point4,self.point1)
        
        self.vecteur_normal = self.donne_produit_vectoriel (self.ligne1.vecteur_directeur, self.ligne2.vecteur_directeur)
        
        self.plan = plan(self.vecteur_normal,self.point1)
    
    def donne_addition_cordonner_z(self,n):

        self.point1.z += n
        self.point2.z += n
        self.point3.z += n
        self.point4.z += n

        self.ligne1 = ligne (self.point1,self.point2)
        self.ligne2 = ligne (self.point2,self.point3)
        self.ligne3 = ligne (self.point3,self.point4)
        self.ligne4 = ligne (self.point4,self.point1)
        
        self.vecteur_normal = self.donne_produit_vectoriel (self.ligne1.vecteur_directeur, self.ligne2.vecteur_directeur)
        
        self.plan = plan(self.vecteur_normal,self.point1)

    
    def donne_produit_vectoriel(self,vecteur1,vecteur2):

        x_v1 = vecteur1.x
        y_v1 = vecteur1.y
        z_v1 = vecteur1.z

        x_v2 = vecteur2.x
        y_v2 = vecteur2.y
        z_v2 = vecteur2.z

        x_v_p = (y_v1 * z_v2) - (z_v1 * y_v2)
        y_v_p = -( (x_v1 * z_v2) - (z_v1 * x_v2) )
        z_v_p = (x_v1 * y_v2) - (y_v1 * x_v2)

        vp = vecteur( x_v_p, y_v_p, z_v_p )

        return vp
    
    def donne_rotation(self,centre, centre_rotation, point_m, alpha):

        
        ##print(x_d)
        x_d = centre_rotation.x - centre.x
        y_d = centre_rotation.z - centre.z

        x_m_t = point_m.x - x_d
        y_m_t = point_m.z - y_d

        longeur_centre_rotation_point_m = sqrt( (x_m_t ** 2) + (y_m_t ** 2) )

        cos_m = x_m_t / longeur_centre_rotation_point_m
        sin_m = y_m_t / longeur_centre_rotation_point_m

        angle_cos_inverse1 = acos(cos_m)
        angle_cos_inverse2 = 0 - angle_cos_inverse1

        angle_sin_inverse1 = asin(sin_m)
        angle_sin_inverse2 = pi - angle_sin_inverse1
        
        tab = [abs(angle_cos_inverse1 - angle_sin_inverse1) %(2*pi), abs(angle_cos_inverse1 - angle_sin_inverse2)%(2*pi), abs(angle_cos_inverse2 - angle_sin_inverse1)%(2*pi), abs(angle_cos_inverse2 - angle_sin_inverse2)%(2*pi),]

        min = tab[0]
        
        for i in range(1,4):

            if tab[i] < min :
                
                min = tab[i] 
        ##print("minnnnnnnnnnnnnnnnnnnnnnnnnnn",min)
        if tab[0] == min :
            
            angle = angle_cos_inverse1
        
        elif tab[1] == min :
            
            angle = angle_cos_inverse1
        
        elif tab[2] == min :
            
            angle = angle_cos_inverse2
        
        elif tab[3] == min :
            
            angle = angle_cos_inverse2

        x_m = (cos( angle + alpha ) * longeur_centre_rotation_point_m ) + x_d
        y_m = (sin( angle + alpha ) * longeur_centre_rotation_point_m ) + y_d
        
        ##print((cos( angle + alpha ) * longeur_centre_rotation_point_m ),"+++++",x_d)
        ##print((sin( angle + alpha ) * longeur_centre_rotation_point_m ),"+++++",y_d)
        # ##print('x_m = ',x_m)
        # ##print('y_m = ',y_m)
        

        return x_m, y_m 

    def donne_rotation_carre(self, centre_de_rotation, alpha):

        tab1 = [self.point1, self.point2, self.point3, self.point4]

        for pointi in tab1 :
            xt,yt = self.donne_rotation(point(0,0,0),centre_de_rotation,pointi,alpha)
            pointi.x = xt
            pointi.z = yt
        
        self.ligne1 = ligne (self.point1,self.point2)
        self.ligne2 = ligne (self.point2,self.point3)
        self.ligne3 = ligne (self.point3,self.point4)
        self.ligne4 = ligne (self.point4,self.point1)
        
        self.vecteur_normal = self.donne_produit_vectoriel (self.ligne1.vecteur_directeur, self.ligne2.vecteur_directeur)
        
        self.plan = plan(self.vecteur_normal,self.point1)



