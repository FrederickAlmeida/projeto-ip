import pygame
from pygame.locals import * 
from sys import exit
from random import randrange

pygame.init()

largura = 640
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprits')

class Boneco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/boneco.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (255/5, 255/5))

        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 100
        self.rect.topleft = self.x, self.y

    def update(self):
        # Movimentação
        keys = pygame.key.get_pressed() 
      
        if keys[pygame.K_a] and self.x>0-7: 
            self.x -= 1
            
        if keys[pygame.K_d] and self.x<largura-43: 
            self.x += 1
            
        if keys[pygame.K_w] and self.y>0-8: 
            self.y -= 1
            
        if keys[pygame.K_s] and self.y<altura-48: 
            self.y += 1
        self.rect.topleft = self.x, self.y
        
class Porcaomorte(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/porcaomorte.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (255/5, 255/5))

        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 250
        self.rect.topleft = self.x, self.y

class Porcaovida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/porcaovida1.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (255/6, 255/6))

        self.rect = self.image.get_rect()
        self.x = 250
        self.y = 250
        self.rect.topleft = self.x, self.y

class Arma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/arma.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (200/1.5, 100/1.5))

        self.rect = self.image.get_rect()
        self.x = 300
        self.y = 250
        self.rect.topleft = self.x, self.y

class Municao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/municao.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.x = randrange(40, 500)
        self.y = randrange(50, 500, 10)
        self.rect.topleft = self.x, self.y

todas_sprites = pygame.sprite.Group()
boneco = Boneco()
todas_sprites.add(boneco)

porcaomorte = Porcaomorte()
todas_sprites.add(porcaomorte)     

porcaovida = Porcaovida()
todas_sprites.add(porcaovida)

arma = Arma()
todas_sprites.add(arma)

for i in range(2):
    municao = Municao()
    todas_sprites.add(municao)

while True:
    tela.fill((0,0,0))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()