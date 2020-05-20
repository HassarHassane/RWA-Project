import networkx as nx
import numpy as np
import random 
import tkinter as Tk
from tkinter import *
from tkinter import simpledialog,Label,Button,Toplevel,messagebox
import matplotlib.pyplot as plt
import time
import pandas as pd


root=Tk()
root.geometry('550x600+0+0')
root.title('RWA')
chemins=[]#pathliste
links=[]#pathlisteglobal

start=time.time()
def principale():
    choix = simpledialog.askstring("input string", "please enter  the methode de generation of paths( shortest paths, all paths,k shortest paths) ")
    nb_color= simpledialog.askinteger("color number", "please enter the number of color")
    iteration= simpledialog.askinteger("Iteration", "please enter the number of Iteration")
    if choix=="k shortest paths":
        k=simpledialog.askinteger("k", "please enter the number of shortest paths:")
    else:
        pass
    input_data = pd.read_csv('matrixA.csv', index_col=0)
    G = np.array(input_data.values)
    A = nx.from_numpy_matrix(G)
    input_dataB = pd.read_csv('matrixB.csv', index_col=0)
    B = np.array(input_dataB.values) 
    def affichage(m):     #fonction d'affichage des chemins
     for l in m:
        length=len(l)
        for i in range(length-1):
         print(l[i]+1,end='->')
        print(l[length-1]+1)
    start=time.time()    
#partie d'affichage de tous les path---------------------------------------------------
    import sys    
    sys.stdout=open('PATH.txt','w')
    
    print(''' This is ''',choix,
          '''of the connexion request''')    
    for i in range(len(G)):   #affichage_chemins
        for j in range(len(G)):
            if B[i][j]==1:
                if choix=="k shortest paths": 
                    x=[]
                    m1=[]
                    print('-------------------------------')
                    m = list(nx.all_simple_paths(A, source=i, target=j))
                    for i in range(len(m)):
                        for i in range(len(m)):
                          if len(m[i]) > len(m[j]):
                            x=m[i]
                            m[i]=m[j]
                            m[j]=x
                    for i in range(k):
                        m1.append(m[i])
                    for c in m1:
                        chemins.append(c)  # stockage des chemins
                    links.append(m1)
                    affichage(m1)
                   
                elif choix=='shortest paths':
                    list1 = []
                    m = list(nx.shortest_path(A, source=i, target=j))  # générations des chemins possibles
                    chemins.append(m)  # stockage des chemins
                    list1.append(m)
                    links.append(list1)
                     
                    
                    
                else:
                    print('-------------------------------') 
                    m=list(nx.all_simple_paths(A,source=i,target=j))# générations des chemins possibles
                    for k in m:
                     chemins.append(k) #stockage des chemins
                    links.append(m)
                    affichage(m)
                   
                    
    if choix=='shortest paths':
        for i in range(len(chemins)):
            print('--------------------') 
            for j in range(len(chemins[i])-1):
               print(chemins[i][j]+1,end='->')
            print(chemins[i][len(chemins[i])-1]+1)
            
                    
    
    #print(chemins)
#partie de morceau commun entre les path--------------------------------------
    D = np.zeros((len(chemins), len(chemins)))
    for i in range(len(chemins)):
        for j in range(len(chemins)):
            for k in range(len(chemins[j])-1):
                a, b = chemins[j][k], chemins[j][k+1]
                if chemins[i].count(a) == 1 and chemins[i].count(b) == 1:
                    if chemins[i].index(b) == chemins[i].index(a) + 1:
                        D[i][j] = 1
    np.savetxt('matrixD.txt',D, fmt='%.1i')
    #print(D)
#partie de temps---------------------------------------------
    nbr_demande_conx = len(links)
    T = np.zeros((nbr_demande_conx, nbr_demande_conx))
    input_dataT=pd.read_csv('matrixT.csv', index_col=0)
    x = np.array(input_dataT.values)
    a=[]
    b=[]
    shape=np.shape(x) 
    for i in range(shape[0]):
        for j in range(shape[1]):
            if x[i][j]==1:
                a.append(j)
        b.append(a.copy())
        a.clear()
    
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if (b[i][0]-b[j][1]) < 0 and (b[j][0]-b[i][1]) < 0:
                T[i][j] = 1
                T[j][i] = 1  # T est une matrice symetrique
    
    C = np.zeros((len(chemins), len(chemins)))
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == 1:
                for k in range(len(links[j])):
                    a = chemins.index(links[j][k])
                    for h in range(len(links[i])):
                        b = chemins.index(links[i][h])
                        C[b][a] = 1
                       
    #print(C)
    np.savetxt('Time_matrix.txt',C, fmt='%.1i')                    
#---------------------------------------------------------------------------------
    def randompath(links):
        randpath = []
        for i in range(len(links)):
            k = random.choice(links[i])
            randpath.append(k)
        return randpath 
    #print(randompath(links))
    
    def index(choix):
        indice=[]
        for i in range(nbr_demande_conx):
           indice.append(chemins.index(choix[i]))
        return indice
    #print(index(randompath(links)))
    
    
    def matrix_color(L):
       colors=np.zeros((len(L), len(L))) 
       k=index(L) 
       for i in range(len(k)):
           for j in range(0,len(k)):
              if D[k[i]][k[j]] == 1 and C[k[i]][k[j]] == 1:
                      if i!=j:
                        colors[i][j]=1
       return colors           
    
    
    def nbr_colors(M):#calcule de nombre de couleur
        colornumber= np.where(M==1)
        n = len(set(colornumber[1]))
        if n == 0:
            n = 1
        return n
    
    
#################################
    final=randompath(links)
    M=matrix_color(final)
    f=nbr_colors(M)
    for i in range(iteration):
            choice=randompath(links)
            #indice(choice)
            N=matrix_color(choice)
            n=nbr_colors(N)
            if n< f:
               final=choice
               f=n
               
               
    #print(final)
    def affichage_de_color(m,f):     #fonction d'affichage coloré des chemins
     for l in m:
        length=len(l)
        for i in range(length-1):
         print(l[i]+1,end='->')
        print(l[length - 1] + 1, ' Color number',end=' ')
        for i in range(f):
            if choix_couleur[m.index(l),i]==1:
                print(i+1)
#------------------------------------------------------------------ # this appends a color to each chosen path
    final2=final.copy()
    choix_couleur=np.zeros((len(final),f))
    if f==1:
        for i in range(f):
            choix_couleur[final.index(final2[0]), i] = 1
            for j in final2:
                #if commun[chemins.index(final2[0]), chemins.index(j)] == 0:
                    choix_couleur[final.index(j), i] = 1
            if choix_couleur.sum() == len(final):
                break
    else:
     for i in range(f):
      choix_couleur[final.index(final2[0]),i]=1
      for j in final2:
        if D[chemins.index(final2[0]),chemins.index(j)]==0 or (D[chemins.index(final2[0]),chemins.index(j)]==1 and C[final.index(final2[0]),final.index(j)]==0):
            choix_couleur[final.index(j), i] = 1
            final2.remove(j)
      final2.pop(0)
      if choix_couleur.sum() == len(final):
         break

#---------------------------------------------------------------- # this to show each chosen path with its color
    import sys
    sys.stdout=open('OPTIMI.txt','w')
    print("The choosen path and their color is is:\n ")
    affichage_de_color(final,f)
    print("\n")
    print("The number of colors used is : ",f,"/",nb_color)
    print("The number of connection request succedeed is :",len(final),"/",nbr_demande_conx)
    s=str('''                Time Taken is :        
        ''')+str(time.time()-start)+str('''
        second''')
    lable3=Label(root, text=s,fg='red',font=('helvetica', 10 , 'bold'))
    lable3.place(x=330,y=500)
#----------------------------------------------------------------------
    def time_graph():
        print(b)
        x1 = [0, 2]
        y1 = [1, 1]
        x2 = [2, 3]
        y2 = [2, 2]
        x3 = [0, 3]
        y3 = [3, 3]
        plt.plot(x1, y1, label="Request 1")
        plt.plot(x2, y2, label="Request 2")
        plt.plot(x3, y3, label="Request3")
        plt.xlabel('TIME(second)')
        plt.ylabel('CONNECTION REQUEST')
        plt.title('Time graph')
        plt.legend()
        plt.show()
          
#-----------------------------------------------------------------------
    def graph():
        nx.draw(A)
        plt.show()
        
    button3 = Button(text="Graph",width=11,command=graph,height=2,font=('helvetica', 15, 'bold')).place(x=340,y=390)
    button4 = Button(text="Time graph",width=14,command=time_graph,height=2,font=('helvetica', 15, 'bold')).place(x=50,y=392)
    button_principale.configure(state=DISABLED)
    messagebox.showinfo("SUCSSES", "Congrate,now you can see your choosen path and the optimisation of color !")
    sys.stdout=open('i.txt','w')
    
    
        




                




lable1=Label(root, text='  Routing Wavelenght Assignment',fg='red',font=('helvetica', 20, 'bold'))
lable1.place(x=25,y=30)
lable2=Label(root, text='   ________________________________________',font=('helvetica', 15, 'bold'))
lable2.place(x=25,y=71)
lable3=Label(root, text='   If you want to start press here :',fg='red',font=('helvetica', 20, 'bold'))
lable3.place(x=25,y=132)
button_principale = Button(root, text="START",width=11,height=2,bg='green', fg='white',font=('helvetica', 12, 'bold'),command=principale)
button_principale.place(x=210,y=200)
def path():    
  top = Toplevel()
  top.title('PATHS')
  r=open("PATH.txt", "r")
  Label(top, text=r.read()).pack()
  r.close()
  button6 = Button(top,text="Close",width=10,bg='brown', fg='white', font=('helvetica', 9, 'bold'),command=top.destroy).pack(side=BOTTOM)
  top.mainloop()
def optimisation():    
  top = Toplevel()
  top.title('OPTIMISATION')
  f=open("OPTIMI.txt", "r")
  Label(top, text=f.read()).pack()
  f.close()
  button7 = Button(top,text="Close",width=10,bg='brown', fg='white', font=('helvetica', 9, 'bold'),command=top.destroy).pack(side=BOTTOM)
  top.mainloop()
  
 
button1 = Button(text="Path",width=11,height=2,font=('helvetica', 15, 'bold'),command=path).place(x=340,y=290)
button2 = Button(text="optimisation",width=14,height=2,font=('helvetica', 15, 'bold'),command=optimisation).place(x=50,y=292)

button3 = Button(text="Graph",width=11,height=2,font=('helvetica', 15, 'bold')).place(x=340,y=390)
button4 = Button(text="Time graph",width=14,height=2,font=('helvetica', 15, 'bold')).place(x=50,y=392)
button5 = Button(text="Close",width=11,height=2,bg='brown', fg='white', font=('helvetica', 12, 'bold'),command=root.destroy).place(x=210,y=500)


  
root.mainloop()





