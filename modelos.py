from abc import ABC, abstractmethod

# =====================================================================
# INTERFACE E CLASSE ABSTRATA
# =====================================================================

class IItemCardapio(ABC):
    """Interface abstrata (Contrato)."""
    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass


class ItemBase(IItemCardapio):
    """Classe Base com Encapsulamento e Validações."""
    def __init__(self, nome: str, preco: float):
        self.nome = nome    # Passa pelo setter
        self.preco = preco  # Passa pelo setter

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not str(valor).strip():
            raise ValueError("Erro: O nome do item não pode estar vazio.")
        self.__nome = str(valor).strip()

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, valor: float):
        if valor <= 0:
            raise ValueError("Erro: O preço deve ser maior que zero.")
        self.__preco = float(valor)


# =====================================================================
# CLASSES FILHAS (HERANÇA E POLIMORFISMO)
# =====================================================================

class Entrada(ItemBase):
    def __init__(self, nome: str, preco: float, serve_pessoas: int):
        super().__init__(nome, preco)
        self.__serve_pessoas = serve_pessoas

    def exibir_detalhes(self) -> str:
        return f":salad: [Entrada] {self.nome} - R$ {self.preco:.2f} (Serve {self.__serve_pessoas} pessoa(s))"


class PratoPrincipal(ItemBase):
    def __init__(self, nome: str, preco: float, tempo_preparo: int):
        super().__init__(nome, preco)
        self.__tempo_preparo = tempo_preparo

    def exibir_detalhes(self) -> str:
        return f":fork_knife_plate: [Prato] {self.nome} - R$ {self.preco:.2f} (Preparo: {self.__tempo_preparo} min)"


class Bebida(ItemBase):
    def __init__(self, nome: str, preco: float, volume_ml: int):
        super().__init__(nome, preco)
        self.__volume_ml = volume_ml

    def exibir_detalhes(self) -> str:
        return f":cup_with_straw: [Bebida] {self.nome} - R$ {self.preco:.2f} ({self.__volume_ml}ml)"


class Sobremesa(ItemBase):
    def __init__(self, nome: str, preco: float, contem_lactose: bool):
        super().__init__(nome, preco)
        self.__contem_lactose = contem_lactose

    def exibir_detalhes(self) -> str:
        lactose_info = "Contém Lactose" if self.__contem_lactose else "Zero Lactose"
        return f":cake: [Sobremesa] {self.nome} - R$ {self.preco:.2f} ({lactose_info})"