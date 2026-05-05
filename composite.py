from abc import ABC, abstractmethod

# Classe base
class ItemMenu(ABC):
    @abstractmethod
    def get_preco(self):
        pass

# Folha (Prato)
class Prato(ItemMenu):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco

    def __str__(self):
        return f"Prato: {self.nome} - R$ {self.preco:.2f}"

# Composto (Combo)
class Combo(ItemMenu):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def get_preco(self):
        return sum(item.get_preco() for item in self.itens)

    def mostrar(self, nivel=0):
        print(" " * nivel + f"Combo: {self.nome} - R$ {self.get_preco():.2f}")
        for item in self.itens:
            if isinstance(item, Combo):
                item.mostrar(nivel + 2)
            else:
                print(" " * (nivel + 2) + str(item))

# Uso (exemplo)
if __name__ == "__main__":
    # Pratos
    burger = Prato("Hamburguer", 15.0)
    batata = Prato("Batata Frita", 8.0)
    refri = Prato("Refrigerante", 6.0)
    sorvete = Prato("Sorvete", 7.0)

    # Combos
    combo_simples = Combo("Combo Simples")
    combo_simples.adicionar(burger)
    combo_simples.adicionar(batata)
    combo_simples.adicionar(refri)

    combo_master = Combo("Combo Master")
    combo_master.adicionar(combo_simples)
    combo_master.adicionar(sorvete)

    # Mostrar estrutura e preço
    combo_master.mostrar()