# Desafio Nunes Sports - Sistema de Gerenciamento de Produtos

Este é um desafio de desenvolvimento proposto pela empresa Nunes Sports, que busca avaliar a criatividade, capacidade de resolução de problemas, implementação, qualidade de código, organização, boas práticas, conceitos de Clean Code, SOLID e preocupação com desenvolvimento para grandes volumes transacionais.

## Objetivo

Desenvolver uma solução para atender ao requisito do projeto da Nunes Sports. O objetivo é criar um sistema para exibição, criação, edição e deleção dos produtos vendidos pela empresa. O foco está na implementação, qualidade de código e organização, utilizando as ferramentas e linguagens de preferência do desenvolvedor.

## Requisitos

1. **Base de Dados:**
   - Utilizar PostgreSQL como banco de dados.
   - Criar uma tabela chamada `produtos` com os seguintes campos:
     - Nome do produto
     - Código do produto
     - Descrição do produto
     - Preço do produto

2. **Página Web (CRUD):**
   - Desenvolver uma página web utilizando a tecnologia de preferência do candidato.
   - A página deve permitir:
     - Exibição dos produtos em uma tabela.
     - Criação de novos produtos.
     - Edição dos produtos existentes.
     - Deleção de produtos.
   - Todas as ações na página devem refletir no banco de dados.

3. **Modelo de Entrega:**
   - Definir um modelo de entrega para o projeto, considerando as ferramentas de mercado atuais.
   - Utilizar Docker para facilitar a distribuição e execução da aplicação.

4. **Compartilhamento de Código e Controle de Versão:**
   - Pensar em estratégias para o compartilhamento de código, considerando boas práticas.
   - Utilizar um sistema de controle de versão (Git) e incluir um arquivo `.gitignore` adequado.

## Ferramentas Recomendadas

- Linguagem de Programação: Livre escolha.
- Tecnologia Web: Livre escolha (Django é sugerido, mas não obrigatório).
- Banco de Dados: PostgreSQL.
- Controle de Versão: Git.
- Entrega e Execução: Docker.

## Instruções

1. Faça um fork deste repositório.
2. Desenvolva sua solução.
3. Documente seu código e processo de desenvolvimento.
4. Entregue o projeto de acordo com o modelo definido.

## Estrutura do Projeto

A estrutura do projeto fica a critério do desenvolvedor, mas é recomendado seguir as boas práticas e organizações usuais na linguagem escolhida.

## Avaliação

O projeto será avaliado considerando os seguintes critérios:

- Criatividade na implementação.
- Qualidade do código.
- Organização do projeto.
- Boas práticas de desenvolvimento.
- Utilização adequada das tecnologias escolhidas.
- Implementação do CRUD conforme requisitos.

Boa sorte! Estamos ansiosos para ver sua solução.
# Instruções de Uso

Siga estas instruções para configurar, executar e utilizar a solução desenvolvida para o Desafio - Sistema de Gerenciamento de Produtos.

## Pré-requisitos

- [Docker](https://www.docker.com/) instalado na máquina.

## Configuração Inicial

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/desafio-nunes-sports.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd desafio-nunes-sports
   ```

3. Crie um arquivo de ambiente `.env` na raiz do projeto com as configurações necessárias:

   ```env
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=nome_do_banco
   DB_USER=usuario_do_banco
   DB_PASSWORD=senha_do_banco
   ```

   Certifique-se de substituir as variáveis conforme a configuração do seu ambiente.

## Execução da Aplicação

1. Inicie o ambiente Docker:

   ```bash
   docker-compose up -d
   ```

2. Execute as migrações do Django para criar a estrutura do banco de dados:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. Acesse a aplicação em seu navegador:

   [http://localhost:8000](http://localhost:8000)

## Utilização da Página Web

1. Na página inicial, você verá uma tabela com os produtos cadastrados (inicialmente vazia).
2. Para criar um novo produto, clique no botão de criação e preencha os campos necessários.
3. Para editar um produto existente, clique no botão de edição na linha correspondente ao produto desejado.
4. Para deletar um produto, clique no botão de deleção na linha correspondente ao produto desejado.

Todas as ações realizadas na página refletirão no banco de dados PostgreSQL.

## Encerrando a Aplicação

Para encerrar a aplicação e liberar os recursos:

```bash
docker-compose down
```

## Compartilhamento de Código

O código desenvolvido pode ser compartilhado através do seu próprio repositório no Git, seguindo as práticas recomendadas.

**Observação:** Certifique-se de manter as informações sensíveis (como chaves de acesso ao banco de dados) seguras e não incluídas no repositório.

Seja criativo e boa sorte! Estamos ansiosos para ver a sua solução.
