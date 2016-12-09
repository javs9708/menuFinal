import pygame
import sys
import random

global efecto
global efecto2
global lluviaMenu

ancho=800
alto=600

blanco=[255,255,255]
negro=[0,0,0]
rojo=[255,0,0]
gris=[158,158,158]
azul=[0,0,160]

efecto=True
efecto2=True
lluviaMenu=True

class Opcion:
    ver=False

    def __init__(self,ido,texto,pos,tam):
        self.texto=texto
        self.id=ido
        self.pos=pos
        self.fuente=pygame.font.Font(None,tam)
        self.set_rect()
        self.dibujar()




    def set_rect(self):
        self.enunciado()
        self.rect=self.txt.get_rect()
        self.rect.topleft=self.pos

    def colortxt(self):
        if self.ver:
            return(gris)
        else:
            return(blanco)


    def enunciado(self):
        self.txt=fuente.render(self.texto,True,self.colortxt())

    def dibujar(self):
        self.enunciado()
        pantalla.blit(self.txt,self.rect)

class Opcion2:
    ver=False

    def __init__(self,ido,texto,pos,tam):
        self.texto=texto
        self.id=ido
        self.pos=pos
        self.fuente=pygame.font.Font(None,tam)
        self.set_rect()
        self.dibujar()

    def set_rect(self):
        self.enunciado()
        self.rect=self.txt.get_rect()
        self.rect.topleft=self.pos

    def colortxt(self):
        if self.ver:
            return(gris)
        else:
            return(blanco)

    def enunciado(self):
        self.txt=fuente.render(self.texto,True,self.colortxt())

    def dibujar(self):
        self.enunciado()
        pantalla.blit(self.txt,self.rect)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.display.set_caption("Soul Memory")

    fuente=pygame.font.Font("opciones.ttf",50)
    fuente2=pygame.font.Font(None,40)
    fuenteTitulo=pygame.font.Font("soulMemory.ttf",140)

    ojo=pygame.image.load("ojos.png")



    #-------------MENU---------------------------------------#

    pygame.mixer.music.load("musicaMenu.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.85)




    opciones=[Opcion(1,"Iniciar",(ancho/2+160,alto/20+320),50)]
    opciones2=[Opcion(2,"Salir",(ancho/2+180,alto/20+390),50)]

    titulo=fuenteTitulo.render("Soul Memory",True,blanco)

    ls=[]
    for i in range(30):
        x=random.randrange(0,ancho)
        y=random.randrange(0,alto)
        ls.append([x,y])

    ls2=[]
    for i in range(30):
        x=random.randrange(0,ancho)
        y=random.randrange(0,alto)
        ls2.append([x,y])


    var_y=15
    var_ojos=2

    reloj=pygame.time.Clock()

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for op in opciones:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):
                        pass


                for op in opciones2:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):

                        fin=True


        pantalla.fill(negro)
        pantalla.blit(titulo,(ancho/2-330,alto/2-200))
        if lluviaMenu==True:
            for i in range(len(ls)):
                pygame.draw.circle(pantalla,azul,ls[i],5)

                ls[i][1]+=var_y

                if ls[i][1] > alto:
                    x=random.randrange(0,ancho)
                    ls[i][1]=y
                    y=random.randrange(-50,-10)
                    ls[i][0]=x

        for op in opciones:
            if op.rect.collidepoint(pygame.mouse.get_pos()):
                op.ver=True

                while efecto==True:
                    sonido=pygame.mixer.Sound("mouse.wav")
                    sonido.play()
                    efecto=False
                    lluviaMenu=False

                for i in range(len(ls2)):

                    pantalla.blit(ojo,ls2[i])

                    ls2[i][1]+=var_ojos

                    if ls2[i][1] > alto:
                        x=random.randrange(0,ancho)
                        ls2[i][1]=y
                        y=random.randrange(-50,-10)
                        ls2[i][0]=x

            else:
                op.ver=False
                efecto=True
                lluviaMenu=True

            op.dibujar()

        for op in opciones2:
            if op.rect.collidepoint(pygame.mouse.get_pos()):
                op.ver=True

                while efecto2==True:
                    sonido=pygame.mixer.Sound("mouse.wav")
                    sonido.play()
                    efecto2=False

            else:
                op.ver=False
                efecto2=True

            op.dibujar()


        reloj.tick(60)
        pygame.display.flip()
