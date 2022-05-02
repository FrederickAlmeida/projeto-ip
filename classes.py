#import pygame

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
        fragmentos_arma.quantidade -= 1
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

    # quando o personagem colidir com o item, ele terá sua vida afetada:
    def colisao(self):
        if self == item_especial:
            protagonista.vida = 4
            item_especial.quantidade = 0
        
        else:
            protagonista.vida += self.modificador_vida
            self.quantidade -= 1    
        # fazer o item desaparecer do mapa
        

class personagens:
    todos_personagens = []

    def __init__(self, nome:str, vida:int, velocidade=10):
        assert vida >= 0, f"O {nome} não pode começar com a vida negativa!"
        
        self.nome = nome
        self.vida = vida
        self.velocidade = velocidade

        personagens.todos_personagens.append(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}:('{self.nome}', {self.vida}, {self.velocidade})"
        
protagonista = personagens("Jhonny", 3)
mini_boss = personagens("Pitou", 5, 15)

pocoes_vida = item_modificador_vida("Poção de vida", 3, 1)
armadilhas = item_modificador_vida("Armadilha", 5, -1)
item_especial = item_modificador_vida("Super Item", 1)

fragmentos_arma = item("Fragmentos", 3)

print(item.todos_itens)
print(personagens.todos_personagens)