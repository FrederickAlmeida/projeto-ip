import pygame
from pygame.locals import *
from sys import exit

pygame.init()
fonte = pygame.font.SysFont('arial', 40, True, False)
# Classes
class item:
    todos_itens = []
  
    def __init__(self, nome:str, quantidade: int):
        # validar os inputs recebidos
        assert quantidade >= 0, f"A quantidade de {nome} tem que ser maior ou igual a zero!"

        # salvar os atributos do item
        self.nome = nome
        self.quantidade = quantidade

        # salvar todos os itens que foram criados
        item.todos_itens.append(self)

    def coletar_fragmento(self):
        self.quantidade -= 1
        # fazer o fragmento desaparecer do mapa

    # método para representar os itens da classe
    def __repr__(self):
        if self.__class__.__name__ == "item" or self.__class__.__name__ == "fragmentos":
            return f"{self.__class__.__name__}:('{self.nome}', {self.quantidade})"
        
        elif self.__class__.__name__ == "item_modificador_vida":
            return f"{self.__class__.__name__}:('{self.nome}', {self.quantidade}, {self.modificador_vida})"


# classe para os itens que vão afetar a vida do personagem, seja aumentanto, seja diminuindo
class item_modificador_vida(item):
    def __init__(self, nome:str, quantidade: int, modificador_vida=0):
        super().__init__(nome, quantidade)

        self.modificador_vida = modificador_vida
        if self.nome == 'armadilha':
            self.dano = 1
        elif self.nome == 'pocao':
            self.recuperar = 1
        elif self.nome == 'pocao_especial':
            self.nova_vida = 4
        

class personagens:
    todos_personagens = []

    def __init__(self):  
        self.nome = 'jhonny'
        self.vida = 3
        self.velocidade = 0.5

        personagens.todos_personagens.append(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}:('{self.nome}', {self.vida}, {self.velocidade})"
largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura)) 
pygame.display.set_caption('jogo projeto ip')
x = 20
y = 20
def colidiu():
        if protagonista.colliderect(linha_1) or protagonista.colliderect(linha_2) or protagonista.colliderect(linha_3) or protagonista.colliderect(linha_4) or protagonista.colliderect(linha_5) or protagonista.colliderect(linha_6) or protagonista.colliderect(linha_7) or protagonista.colliderect(linha_8) or protagonista.colliderect(linha_9) or protagonista.colliderect(linha_10) or protagonista.colliderect(linha_11) or protagonista.colliderect(linha_12) or protagonista.colliderect(linha_13) or protagonista.colliderect(linha_14) or protagonista.colliderect(linha_15) or protagonista.colliderect(linha_16) or protagonista.colliderect(linha_17) or protagonista.colliderect(linha_18) or protagonista.colliderect(linha_19) or protagonista.colliderect(linha_20) or protagonista.colliderect(linha_21) or protagonista.colliderect(linha_22) or protagonista.colliderect(linha_23) or protagonista.colliderect(linha_24) or protagonista.colliderect(linha_25) or protagonista.colliderect(linha_26) or protagonista.colliderect(linha_27) or protagonista.colliderect(linha_28) or protagonista.colliderect(linha_29) or protagonista.colliderect(linha_30) or protagonista.colliderect(linha_31) or protagonista.colliderect(linha_32) or protagonista.colliderect(linha_33):
            return True
        else:
            return False
# Criando objetos 
desenhar_armadilha_1 = True
desenhar_armadilha_2 = True
desenhar_armadilha_3 = True
desenhar_armadilha_4 = True
desenhar_armadilha_5 = True
desenhar_pocao_1 = True
desenhar_pocao_2 = True
desenhar_pocao_3 = True
desenhar_fragmento_1 = True
desenhar_fragmento_2 = True
desenhar_fragmento_3 = True
desenhar_pocao_especial = True
armadilha = item_modificador_vida('armadilha', 1)
pocao = item_modificador_vida('pocao', 1)
pocaoespecial = item_modificador_vida('pocao_especial', 1)
fragmento = item('fragmento_1', 3)
personagem = personagens()
while True:
    
    tela.fill((0,0,0))
    mensagem = f'LP: {personagem.vida}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    mensagem_fragmentos = f'Frags: {fragmento.quantidade}'
    texto_formatado_fragmento = fonte.render(mensagem_fragmentos, False, (255,255,255))
    for c in pygame.event.get():
        if c.type == QUIT:
            pygame.quit()
            exit()
    if fragmento.quantidade == 0:
        pygame.quit()
        exit()
        
    if personagem.vida == 0:
        pygame.quit()
        exit()
    # Protagonista

    protagonista = pygame.draw.circle(tela, (0, 255,0), (x, y), 5)
    # Desenhando o labirinto
    linha_1 = pygame.draw.line(tela, (255,0,0), (0,0), (600,0), 10) # ONDE VAI DESENHAR/COR/PARTIDA/DESTINO, tamanho
    linha_2 = pygame.draw.line(tela, (255,0,0), (600,0 ), (600, 530), 10)
    linha_3 = pygame.draw.line(tela, (255,0,0), (0, 600), (600, 600), 10)
    linha_4 = pygame.draw.line(tela, (255,0,0), (0, 70), (0, 600), 10)
    linha_5 = pygame.draw.line(tela, (255,0,0), (0, 70), (100, 70), 5)
    linha_6 = pygame.draw.line(tela, (255,0,0), (100, 70), (100, 140), 5)
    linha_7 = pygame.draw.line(tela, (255,0,0), (100, 140), (150, 140), 5)
    linha_8 = pygame.draw.line(tela, (255,0,0), (150, 140), (150, 70), 5)
    linha_9 = pygame.draw.line(tela, (255,0,0), (150, 70), (350, 70), 5)
    linha_10 = pygame.draw.line(tela, (255,0,0), (450, 0), (450, 70), 5)
    linha_11 = pygame.draw.line(tela, (255,0,0), (450, 70), (530, 70), 5)
    linha_12 = pygame.draw.line(tela, (255,0,0), (530, 70), (530, 140), 5)
    linha_13 = pygame.draw.line(tela, (255,0,0), (225, 140), (530, 140), 5)
    linha_14 = pygame.draw.line(tela, (255,0,0), (100, 210), (100, 340), 5)
    linha_15 = pygame.draw.line(tela, (255,0,0), (100, 340), (150, 340), 5)
    linha_16 = pygame.draw.line(tela, (255,0,0), (150, 210), (150, 340), 5)
    linha_17 = pygame.draw.line(tela, (255,0,0), (150, 340), (410, 340), 5)
    linha_18 = pygame.draw.line(tela, (255,0,0), (410, 340), (410, 460), 5)
    linha_19 = pygame.draw.line(tela, (255,0,0), (225, 140), (225, 280), 5)
    linha_20 = pygame.draw.line(tela, (255,0,0), (225, 280), (480, 280), 5)
    linha_21 = pygame.draw.line(tela, (255,0,0), (295, 210), (480, 210), 5)
    linha_22 = pygame.draw.line(tela, (255,0,0), (480, 210), (480, 280), 5)
    linha_23 = pygame.draw.line(tela, (255,0,0), (480, 280), (480, 530), 5)
    linha_24 = pygame.draw.line(tela, (255,0,0), (480, 530), (550, 530), 5)
    linha_25 = pygame.draw.line(tela, (255,0,0), (550, 340), (550, 530), 5)
    linha_26 = pygame.draw.line(tela, (255,0,0), (100, 340), (100, 460), 5)
    linha_27 = pygame.draw.line(tela, (255,0,0), (100, 460), (295, 460), 5)
    linha_28 = pygame.draw.line(tela, (255,0,0), (295, 460), (295, 530), 5)
    linha_29 = pygame.draw.line(tela, (255,0,0), (295, 530), (410, 530), 5)
    linha_30 = pygame.draw.line(tela, (255,0,0), (410, 530), (410, 600), 5)
    linha_31 = pygame.draw.line(tela, (255,0,0), (100, 530), (100, 600), 5)
    linha_32 = pygame.draw.line(tela, (255,0,0), (100, 530), (225, 530), 5)
    linha_33 = pygame.draw.line(tela, (255,0,0), (530, 140), (530, 280), 5)
    # Desenhando itens
    if desenhar_armadilha_1 == True:
        armadilha_1 = pygame.draw.circle(tela, (255, 0,0), (100, 35), 4)
    if desenhar_armadilha_2 == True:
        armadilha_2 = pygame.draw.circle(tela, (255, 0,0), (400, 105), 4)
    if desenhar_armadilha_3 == True:
        armadilha_3 = pygame.draw.circle(tela, (255, 0,0), (185, 310), 4)
    if desenhar_armadilha_4 == True:
        armadilha_4 = pygame.draw.circle(tela, (255, 0,0), (445, 565), 4)
    if desenhar_armadilha_5 == True:
        armadilha_5 = pygame.draw.circle(tela, (255, 0,0), (575, 310), 4)
    if desenhar_pocao_1 == True:
        pocao_1 = pygame.draw.circle(tela, (0, 0, 255), (50, 105), 4)
    if desenhar_pocao_2 == True:
        pocao_2 = pygame.draw.circle(tela, (0, 0, 255), (125, 400), 4)
    if desenhar_pocao_3 == True:
        pocao_3 = pygame.draw.circle(tela, (0, 0, 255), (515, 510), 4)
    if desenhar_pocao_especial == True:
        pocao_especial = pygame.draw.circle(tela, (0, 255, 255), (125, 105), 10)
    if desenhar_fragmento_1 == True:
        fragmento_1 = pygame.draw.rect(tela, (255,255,0), (460, 10, 30,30))
    if desenhar_fragmento_2 == True:
        fragmento_2 = pygame.draw.rect(tela, (255,255,0), (430, 230, 30,30))
    if desenhar_fragmento_3 == True:
        fragmento_3 = pygame.draw.rect(tela, (255,255,0), (120, 550, 30,30))
    
    
    # Movimentação
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_a] and x > 0: 
        
        x -= personagem.velocidade
        teste = colidiu()
        if teste == True:
            x = 20
            y = 20
            
          
    if keys[pygame.K_d] and x<largura: 
        
        x += personagem.velocidade
        teste = colidiu()
        if teste == True:
            x = 20
            y = 20
        
          
    if keys[pygame.K_w] and y>0: 
        
        y -= personagem.velocidade
        teste = colidiu()
        if teste == True:
            x = 20
            y = 20
        
          
    
    if keys[pygame.K_s] and y<altura: 
        y += personagem.velocidade
        teste = colidiu()
        if teste == True:
            x = 20
            y = 20
    
    # colidir com itens
    if desenhar_armadilha_1 == True:
        if protagonista.colliderect(armadilha_1):
            personagem.vida -= armadilha.dano
            desenhar_armadilha_1 = False
    if desenhar_armadilha_2 == True:
        if protagonista.colliderect(armadilha_2):
            personagem.vida -= armadilha.dano
            desenhar_armadilha_2 = False
    if desenhar_armadilha_3 == True:
        if protagonista.colliderect(armadilha_3):
            personagem.vida -= armadilha.dano
            desenhar_armadilha_3 = False
    if desenhar_armadilha_4 == True:
        if protagonista.colliderect(armadilha_4):
            personagem.vida -= armadilha.dano
            desenhar_armadilha_4 = False
    if desenhar_armadilha_5 == True:
        if protagonista.colliderect(armadilha_5):
            personagem.vida -= armadilha.dano
            desenhar_armadilha_5 = False
    if desenhar_pocao_1 == True:
        if protagonista.colliderect(pocao_1):
            if personagem.vida < 3:
                personagem.vida += pocao.recuperar
            desenhar_pocao_1 = False
    if desenhar_pocao_2 == True:
        if protagonista.colliderect(pocao_2):
            if personagem.vida < 3:
                personagem.vida += pocao.recuperar
            desenhar_pocao_2 = False
    if desenhar_pocao_3 == True:
        if protagonista.colliderect(pocao_3):
            if personagem.vida < 3:
                personagem.vida += pocao.recuperar
            desenhar_pocao_3 = False
    if desenhar_pocao_especial == True:
        if protagonista.colliderect(pocao_especial):
            personagem.vida = pocaoespecial.nova_vida
            desenhar_pocao_especial = False
    if desenhar_fragmento_1 == True:
        if protagonista.colliderect(fragmento_1):
            fragmento.coletar_fragmento()
            desenhar_fragmento_1 = False
    if desenhar_fragmento_2 == True:
        if protagonista.colliderect(fragmento_2):
            fragmento.coletar_fragmento()
            desenhar_fragmento_2 = False
    if desenhar_fragmento_3 == True:
        if protagonista.colliderect(fragmento_3):
            fragmento.coletar_fragmento()
            desenhar_fragmento_3 = False
    
      
    protagonista = pygame.draw.circle(tela, (0, 255,0), (x, y), 5)
    tela.blit(texto_formatado, (450,40))
    tela.blit(texto_formatado_fragmento, (50,40))
    pygame.display.update()