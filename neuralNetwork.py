import numpy as np
from random import randint


def sigmusoide(X):#fonction d'activation
    return 1/(1+np.exp(-X))




def direcaupoidsmax(sigm_sortie):#on associe au neurone de sortie dont la fonction d'activation est max la direction qui lui est associée, càd la plus stratégique
    n_lign=len(sigm_sortie)
    n_col=len(sigm_sortie[0])
    if (n_col)!=1:
        return ('ce programme ne fonctionne que pour les matrices colones')
    else :
        nb=0
        m=sigm_sortie[0][0]
        for j in range (1,n_lign):
            if sigm_sortie[j][0]>m:
                m=sigm_sortie[j][0]
                nb=j
        if nb==0:
            return 0
        elif nb==1:
            return -1
        elif nb==2:
            return 1
        return('matrice avec plus de 3 couches de sortie')


def prod(A,B):# on effectue un produit matriciel
    la=len(A)
    ca=len(A[0])
    lb=len(B)
    cb=len(B[0])
    if ca!=lb: return False
    else:
        M=[[0]*cb for i in range(la)]
        for i in range(la):
            for j in range(cb):
                for k in range(ca):
                    M[i][j]=(A[i][k])*(B[k][j])
    return M



def reseau_de_neurones(n_ent,n_cach1,n_cach2,n_sort):

#initialisation des poids et biais

    n_X=6 #nombre de parametres
    WXent=np.random.rand(n_ent,n_X) #W correspond au poids
    #print('WXent=')
    #print(WXent)

    Wentcach1=np.random.rand(n_cach1,n_ent) 
    #print('Wentcach1')
    #print(Wentcach1)

    Wcach1cach2=np.random.rand(n_cach2,n_cach1) #matrice avec des floattants aléatoires

    Wcach2sort=np.random.rand(n_sort,n_cach2)
    b_ent=np.random.rand(n_ent,1) #b correspond au biai
    #print('b_ent=')
    #print (b_ent)

    b_cach1=np.random.rand(n_cach1,1)
    b_cach2=np.random.rand(n_cach2,1)
    b_sort=np.random.rand(n_sort,1) 

    parametres={'WXent': WXent,'Wentcach1': Wentcach1,'Wcach1cach2': Wcach1cach2,'Wcach2sort': Wcach2sort,'b_ent': b_ent,'b_cach1': b_cach1,'b_cach2': b_cach2,'b_sort': b_sort}
    return parametres

def creation_de_reseaux(n):
#créé une premiere generation de n IA
    prem_gene=[]
    for i in range(n):
        prem_gene.append(reseau_de_neurones(6,8,8,3))
    return(prem_gene)



def jeu_du_reseau(X,reseau):
#prend en parametre un reseau et les parametres lies a la position du serpent pour le faire jouer
    WXent_deja_init=reseau['WXent']
    Wentcach1_deja_init=reseau['Wentcach1']
    Wcach1cach2_deja_init=reseau['Wcach1cach2']
    Wcach2sort_deja_init=reseau['Wcach2sort']
    b_ent_deja_init=reseau['b_ent']
    b_cach1_deja_init=reseau['b_cach1']
    b_cach2_deja_init=reseau['b_cach2']
    b_sort_deja_init=reseau['b_sort']

    #somme_ent_deja_init = prod(WXent_deja_init, X) + b_ent_deja_init # on somme le produit de chaque poids Wk[i][j] avec la fonction d'activation du neurone j et on ajoute le biais du neurone i
    #sigm_ent_deja_init = sigmusoide(somme_ent_deja_init)#on applique la fonction d'activation

    somme_cach1_deja_init = prod(Wentcach1_deja_init,X) + b_cach1_deja_init
    #print('somme_cach1_deja_int=')
    #print(somme_cach1_deja_init)
    sigm_cach1_deja_init = sigmusoide(somme_cach1_deja_init)
    #print('sigm_cach1_deja_init=')
    #print(sigm_cach1_deja_init)

    somme_cach2_deja_init = prod(Wcach1cach2_deja_init,sigm_cach1_deja_init) + b_cach2_deja_init
    sigm_cach2_deja_init  =sigmusoide(somme_cach2_deja_init)

    somme_sort_deja_init = prod(Wcach2sort_deja_init,sigm_cach2_deja_init) + b_sort_deja_init
    sigm_sort_deja_init = sigmusoide(somme_sort_deja_init)
    print(sigm_sort_deja_init)
    #print('somme_sort_deja_init=')
    #print(somme_sort_deja_init)
    return direcaupoidsmax(sigm_sort_deja_init)

#tests
#X0=np.array([[[6,8]],[[2,4]],[[0,4]],[[8,7]],[[2,9]]])
#X1=np.array([[2,3,7,9,6]])
#print('X1=')
#print(X1)
#print('prod(XO,X1)=')
#print(prod(X0,X1))
#print('simusoide(X1)=')
#print(sigmusoide(X1))
#print('reseaudeneuronecréé')
#reseau_test=reseau_de_neurones(5,8,8,3)
#print(reseau_test)

#print('jeu du reseau créé :')
#print(jeu_du_reseau(X1,reseau_test))



#print('creation dun reseau a 100 IA')
#print(creation_de_reseaux(100))



































