# Aplicação Web com Flask e Componentes HTML Dinâmicos

Este projeto é um protótipo de uma aplicação web desenvolvida em **Python** utilizando o microframework **Flask**. A aplicação demonstra conceitos essenciais de desenvolvimento web, como roteamento de URLs, uso de modelos (`templates`) HTML e renderização de dados dinâmicos.

Um dos pontos de destaque do projeto é a criação de um módulo para **gerar componentes HTML de forma programática**, em vez de escrevê-los manualmente nos arquivos `.html`.

-----

### **Funcionalidades**

  * **Rotas e Páginas Estáticas:** A aplicação possui rotas básicas para as páginas `home`, `sobre`, `produtos` e `index` (`/`).
  * **Conteúdo Dinâmico:** A página `index` e `produtos` demonstram como passar variáveis e listas de dados do Python para os modelos HTML, exibindo informações personalizadas para o usuário.
  * **Sistema de Templates:** Utiliza o sistema de `templates` Jinja2, que vem integrado ao Flask, com um arquivo `base.html` que centraliza a estrutura do site (cabeçalho, rodapé) para reutilização.
  * **Geração de Tags HTML em Python:**
      * Um módulo chamado `tags` foi criado para abstrair a criação de elementos HTML.
      * As classes como `Card`, `Table`, e `ComboBox` permitem construir componentes de interface completos diretamente no código Python, tornando a criação de elementos de interface mais modular e menos propensa a erros.

-----

### **Tecnologias e Conhecimentos Utilizados**

  * **Linguagem:** **Python**
  * **Framework Web:** **Flask**
  * **Sistema de Templates:** **Jinja2**
  * **Conceitos de Programação:**
      * **Programação Orientada a Objetos (POO):** As classes `Tag`, `Card`, `Table`, entre outras, são um exemplo claro do uso de POO para modelar e gerar o código HTML de forma organizada.
      * **Modularização:** O projeto é bem estruturado com diretórios (`templates`, `tags`), separando a lógica da aplicação dos arquivos de visualização.

### **Estrutura de Arquivos**

  * `app.py`: O arquivo principal da aplicação, onde as rotas e a lógica de renderização são definidas.
  * `templates/`: Diretório que armazena os arquivos HTML (`.html`) da aplicação.
      * `base.html`: O modelo base que outras páginas herdam.
      * `home.html`, `sobre.html`, `produtos.html`, `index.html`: Modelos específicos de cada página.
  * `tags/`: Diretório que contém os módulos Python para geração de HTML.
      * `tag.py`: A classe base `Tag` que representa um elemento HTML genérico.
      * `cards.py`, `combo_boxes.py`, `tables.py`: Classes que herdam de `Tag` para criar componentes HTML mais complexos.

### **Como Executar**

1.  **Instalar Flask:** Certifique-se de ter o Flask instalado. Caso não tenha, use o `pip`:
    ```bash
    pip install Flask
    ```
2.  **Executar a Aplicação:** Na pasta raiz do projeto (`aula0516`), execute o arquivo principal a partir do terminal:
    ```bash
    python app.py
    ```
3.  **Acessar no Navegador:** A aplicação estará disponível em `http://127.0.0.1:5000` ou `http://localhost:5000`.
