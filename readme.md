# Cardápio Digital com Python

## 👥 Integrantes
* João Manoel
* Mateus Rocha
* Vinícius Ludson
* Vitor Leonel

---

## 📌 Problema Real Escolhido
O gerenciamento manual de pedidos e cardápios em bares e restaurantes frequentemente resulta em gargalos operacionais. Entre os principais problemas encontrados no modelo tradicional estão:
* **Erros de comunicação:** Pedidos anotados incorretamente ou perdidos entre a mesa e a cozinha.
* **Demora no atendimento:** Clientes esperando longos períodos apenas para solicitar a conta parcial ou adicionar um novo item.
* **Dificuldade de escala:** Falta de flexibilidade para atualizar preços e pratos do cardápio em tempo real sem a necessidade de reimpressões físicas dispendiosas.
* **Falta de autonomia:** Dependência contínua de garçons para ações simples, como visualizar o preço de uma sobremesa ou calcular o valor total gasto até o momento.

---

## 🎯 Objetivo do Sistema
O objetivo deste sistema é automatizar e otimizar o fluxo de atendimento em mesas por meio de um **Cardápio Digital interativo baseado em Programação Orientada a Objetos (POO)**. O sistema visa conferir total autonomia ao cliente, permitindo-lhe visualizar itens categorizados, realizar múltiplos pedidos simultâneos, monitorar o valor parcial acumulado de sua respectiva mesa e efetuar o encerramento da conta de forma independente e digital, garantindo segurança nas regras de negócio e integridade dos dados operacionais.

---

## 🛠️ Funcionalidades
* **Visualização Dinâmica do Cardápio:** Exibição organizada e segmentada por seções pré-definidas (`Entradas`, `Pratos`, `Bebidas`, `Sobremesas`) com detalhes específicos de cada produto.
* **Autonomia na Realização de Pedidos:** Vinculação imediata de itens selecionados à mesa do cliente através de um menu interativo de escolhas.
* **Consulta de Conta Parcial em Tempo Real:** Listagem transparente e discriminada de todos os produtos consumidos na mesa corrente, acompanhada do somatório total atualizado instantaneamente.
* **Encerramento de Conta e Liberação de Mesa:** Módulo de fechamento financeiro que exibe o extrato final da conta, simula a transação de pagamento e libera logicamente o identificador da mesa para os próximos clientes.
* **Validação Rígida e Robusteza de Dados:** Sistema de proteção estrutural que impede o cadastro de itens sem nome, nomes compostos exclusivamente por espaços em branco ou precificações zeradas/negativas.

---

## 📐 Diagrama de Classes UML
O diagrama de classes que mapeia a arquitetura estrutural do sistema, contendo todas as classes, atributos, métodos e os respectivos relacionamentos (herança, dependência, agregação e composição), encontra-se mapeado na pasta local de recursos do projeto:

![Diagrama de Classes UML](imagens/diagrama.png)

*(Certifique-se de salvar a imagem do seu diagrama com o nome `diagrama.png` dentro de uma pasta chamada `imagens` na raiz do projeto para que ela seja renderizada corretamente no GitHub).*

---

## 💻 Explicação dos Conceitos de POO Utilizados

O projeto foi inteiramente edificado seguindo as melhores práticas da Programação Orientada a Objetos em Python, dividindo as responsabilidades do sistema de forma coesa e reutilizável:

### 1. Abstração e Interfaces
* **Aplicação:** A classe `IItemCardapio` funciona estritamente como uma interface abstrata utilizando o módulo nativo `abc` (Abstract Base Classes). Ela define o contrato arquitetural do sistema por meio do método abstrato `@abstractmethod def exibir_detalhes(self) -> str:`.
* **Benefício:** Garante que qualquer novo tipo de produto adicionado ao restaurante futuramente seja obrigado a implementar seu próprio método de exibição de dados, mantendo a padronização.

### 2. Encapsulamento
* **Aplicação:** A classe `ItemBase` protege seus estados internos utilizando atributos privados por meio de *name mangling* (`__nome` e `__preco`). O acesso e a modificação controlada desses atributos ocorrem exclusivamente por meio de propriedades decoradas com `@property` e seus respectivos validadores `@setter`.
* **Benefício:** Impede estados corrompidos no sistema. Se houver uma tentativa de definir um preço menor ou igual a zero, ou um nome vazio, uma exceção do tipo `ValueError` é disparada imediatamente, blindando o ecossistema.

### 3. Herança e Polimorfismo
* **Aplicação:** As classes concretas `Entrada`, `PratoPrincipal`, `Bebida` e `Sobremesa` herdam todas as características estruturais de `ItemBase` (como nome e preço). O **Polimorfismo** manifesta-se na sobrescrita do método `exibir_detalhes()`.
* **Benefício:** Cada classe filha estende o comportamento base para imprimir formatações totalmente distintas e exclusivas à sua natureza, como o tempo de preparo de um prato principal (`tempo_preparo`), a volumetria de uma bebida (`volume_ml`), a quantidade de pessoas que uma entrada serve (`serve_pessoas`) ou a presença de alérgenos em um doce (`contem_lactose`).

### 4. Relações entre Objetos (Composição, Agregação e Associação)
* **Composição:** A classe `Restaurante` possui uma relação de composição com a classe `Cardapio` (`self.__cardapio = Cardapio()`). O ciclo de vida do cardápio está intrinsecamente ligado ao do restaurante; se o restaurante deixar de existir, o cardápio é destruído junto com ele.
* **Agregação:** A classe `Pedido` possui uma relação de agregação com a lista de objetos do tipo `ItemBase`. Os itens do cardápio existem por si só no banco de dados/acervo do sistema e não dependem da existência de um pedido específico para coexistirem.
* **Associação:** A classe `Restaurante` mantém uma associação estrutural e temporal com a classe `Pedido` através do mapeamento de chaves em um dicionário de pedidos ativos (`self.__pedidos_ativos`). O restaurante gerencia e coordena as mesas associadas aos seus respectivos consumos.

---

## 🚀 Tecnologias Utilizadas
* **Linguagem Principal:** Python 3.x (Ambiente CLI - Command Line Interface).
* **Tipagem Estrutural:** Módulo nativo `typing` (uso de `List` e `Dict` para checagem estática de tipos e clareza de código).
* **Meta-Programação:** Módulo nativo `abc` (Abstract Base Classes) para governança e contratos de herança.

---

## 🏃 Como Executar o Projeto

### Pré-requisitos
Certifique-se de possuir o Python 3.8 ou superior instalado em sua máquina local. Você pode checar a instalação utilizando o comando:

    bash
    #Para Linux ou Mac
    python3 --version

    #Para Windows
    python3 --version

Após verificação correta do Python, faça a clonagem do repositório, da seguinte maneira:

    bash
    #Abra seu terminar e acesse o diretório de sua escolha:
    @user: ~/Documentos

E então clone o repositório:
    bash
    
    @user: ~/Documentos: git clone [link-do-repositorio]
    

Acesse o diretório do projeto:
    bash
    
    @user: ~/Documentos/[link-do-repositorio]: cd [nome-do-repositorio]

    #Execute o arquivo principal:
    python3 main.py (ou o nome do arquivo principal)
    