# Importa o gerenciador do restaurante
from gerenciamento import Restaurante
# Importa as classes filhas para popular o sistema
from modelos import Entrada, PratoPrincipal, Bebida, Sobremesa

def popular_sistema(restaurante: Restaurante):
    """Popula o cardápio automaticamente para testes."""
    c = restaurante.cardapio
    c.adicionar_item("Entradas", Entrada("Pão de Alho", 15.00, 2))
    c.adicionar_item("Pratos", PratoPrincipal("Macarrão à Milanesa", 25.99, 30))
    c.adicionar_item("Pratos", PratoPrincipal("Feijoada", 45.50, 45))
    c.adicionar_item("Bebidas", Bebida("Suco de Laranja", 8.00, 500))
    c.adicionar_item("Sobremesas", Sobremesa("Pudim", 12.00, True))

def main():
    meu_restaurante = Restaurante("Restaurante POO")
    popular_sistema(meu_restaurante)
    
    mesa_atual = 1 # Simulando o cliente na mesa 1

    while True:
        print(f"\n=== 🏠 {meu_restaurante.nome.upper()} ===")
        print("1. Ver Cardápio")
        print("2. Fazer um Pedido")
        print("3. Ver Conta Parcial")
        print("4. Pagar e Sair")
        print("0. Desligar Sistema")
        
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                meu_restaurante.cardapio.exibir_cardapio()

            elif opcao == "2":
                lista_itens = meu_restaurante.cardapio.exibir_cardapio()
                if not lista_itens:
                    print("O cardápio está vazio.")
                    continue
                    
                escolha = int(input("\nDigite o NÚMERO do item desejado: "))
                
                if 1 <= escolha <= len(lista_itens):
                    item_selecionado = lista_itens[escolha - 1]
                    pedido = meu_restaurante.abrir_pedido(mesa_atual)
                    pedido.adicionar_item(item_selecionado)
                else:
                    print("❌ Opção de item inválida.")

            elif opcao == "3":
                pedido = meu_restaurante.obter_pedido(mesa_atual)
                if pedido:
                    pedido.resumo()
                else:
                    print("❌ Você ainda não fez nenhum pedido para esta mesa.")

            elif opcao == "4":
                meu_restaurante.encerrar_pedido(mesa_atual)
                mesa_atual += 1 # Passa para a próxima mesa/cliente
                input("\nPressione ENTER para liberar o sistema para o próximo cliente...")

            elif opcao == "0":
                print("Desligando o sistema... Até logo!")
                break
            
            else:
                print("❌ Opção inválida. Tente novamente.")
                
        except ValueError as ve:
            print(f"❌ Erro de Entrada: Digite apenas números válidos. Detalhes: {ve}")
        except Exception as e:
            print(f"❌ Erro inesperado no sistema: {e}")

if __name__ == "_main_":
    main()