from typing import List, Dict
# Importa a classe base necessária para os relacionamentos e tipagem
from modelos import ItemBase 

class Cardapio:
    """Classe que gerencia as coleções de itens do cardápio."""
    def __init__(self):
        self.__acervo: Dict[str, List[ItemBase]] = {
            "Entradas": [],
            "Pratos": [],
            "Bebidas": [],
            "Sobremesas": []
        }

    def adicionar_item(self, secao: str, item: ItemBase):
        if secao not in self.__acervo:
            raise KeyError(f"Erro: A seção '{secao}' é inválida no cardápio.")
        self.__acervo[secao].append(item)

    def exibir_cardapio(self) -> List[ItemBase]:
        todos_itens = []
        print("\n--- CARDÁPIO ---")
        idx = 1
        for secao, itens in self.__acervo.items():
            if itens:
                print(f"\n[{secao}]")
                for item in itens:
                    print(f"{idx}. {item.exibir_detalhes()}")
                    todos_itens.append(item)
                    idx += 1
        return todos_itens


class Pedido:
    """Demonstração de Agregação (Um pedido agrega objetos de ItemBase)."""
    def __init__(self, numero_mesa: int):
        self.__numero_mesa = numero_mesa
        self.__itens: List[ItemBase] = []  

    @property
    def numero_mesa(self) -> int:
        return self.__numero_mesa

    def adicionar_item(self, item: ItemBase):
        self.__itens.append(item)
        print(f"'{item.nome}' adicionado ao pedido da Mesa {self.numero_mesa}.")

    def calcular_total(self) -> float:
        return sum(item.preco for item in self.__itens)

    def resumo(self):
        print(f"\n---  CONTA (Mesa {self.numero_mesa}) ---")
        if not self.__itens:
            print("Nenhum item no pedido.")
            return
        for item in self.__itens:
            print(f"- {item.nome} (R$ {item.preco:.2f})")
        print(f"Total a Pagar: R$ {self.calcular_total():.2f}")
        print("------------------------")


class Restaurante:
    """Demonstração de Composição (Cardapio) e Associação (Pedido)."""
    def __init__(self, nome: str):
        self.nome = nome
        # Composição: O Cardápio é criado junto com o Restaurante
        self.__cardapio = Cardapio() 
        # Associação: O Restaurante gerencia Pedidos ativos
        self.__pedidos_ativos: Dict[int, Pedido] = {} 

    @property
    def cardapio(self) -> Cardapio:
        return self.__cardapio

    def abrir_pedido(self, mesa: int) -> Pedido:
        if mesa not in self.__pedidos_ativos:
            self.__pedidos_ativos[mesa] = Pedido(mesa)
        return self.__pedidos_ativos[mesa]
    
    def obter_pedido(self, mesa: int) -> Pedido:
        return self.__pedidos_ativos.get(mesa)

    def encerrar_pedido(self, mesa: int):
        if mesa in self.__pedidos_ativos:
            pedido = self.__pedidos_ativos.pop(mesa)
            pedido.resumo()
            print("Pagamento realizado. Mesa liberada!")
        else:
            raise ValueError(f"Erro: Nenhuma conta aberta para a mesa {mesa}.")
