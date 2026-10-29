# TechBairro

A TechBairro é um sistema de cadastro de clientes desenvolvido em Python para ajudar a associação de moradores a organizar as informações dos seus clientes.

**Versão atual:** 3.3.0 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar, editar e excluir clientes cadastrados.
- Armazenar os dados em um banco de dados SQLite.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows 10 ou superior, ou outro sistema compatível com Python e Tkinter |
| Python | Python instalado (Python 3.12.0) |
| Tkinter | Necessário para abrir a interface gráfica |
| Bibliotecas externas | Nenhuma |
| Internet | Necessária para baixar o projeto; não é necessária para o uso normal após a instalação |

## Instalação

### Opção 1 — Baixar usando Git

1. Instale o Python e o Git, caso ainda não estejam instalados.
2. Abra o terminal e execute:

```bash
git https://github.com/Luan-Davi/TechBairro.py
cd techbairro
```

3. Confira a versão do Python:

```bash
python --version
```

4. Confira o Tkinter:

```bash
python -m tkinter
```

Se aparecer uma janela de demonstração, feche-a e continue.

5. Confira o arquivo de dependências:

```bash
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` informa que o projeto não possui bibliotecas externas para instalar.

6. Execute o sistema:

```bash
python techbairro.py
```

A janela de cadastro da TechBairro deverá abrir. No terminal, confira a mensagem `Banco em uso` e o caminho do arquivo do banco de dados.

### Opção 2 — Baixar pelo GitHub

1. Abra a página do repositório no GitHub.
2. Clique em **Code** e depois em **Download ZIP**.
3. Extraia o arquivo ZIP para uma pasta do computador.
4. Abra essa pasta no terminal do VS Code ou no Explorador de Arquivos, utilizando a opção de abrir o terminal na pasta.
5. Execute os testes e a instalação das dependências descritos na opção anterior.
6. Execute `python techbairro.py`.

A janela de cadastro deverá abrir e o terminal deverá informar `Banco em uso`, seguido do caminho do banco utilizado.

## Configuração do banco de dados

A TechBairro utiliza o SQLite para guardar os clientes. O arquivo `techbairro.db` é criado automaticamente pelo programa quando o banco ainda não existe, conforme a configuração do projeto.

O caminho exibido no terminal após a mensagem `Banco em uso` indica qual arquivo está sendo utilizado. Confira esse caminho para evitar confundir bancos diferentes.

O arquivo do banco não deve ser enviado ao GitHub, pois pode conter dados pessoais dos clientes. Mantenha-o protegido e excluído do versionamento pelo `.gitignore`.

Para fazer uma cópia de segurança, feche o programa e copie o arquivo `techbairro.db` para uma pasta segura, com acesso restrito. Guarde a cópia separada da pasta principal do projeto.

## Como usar

Consulte o [Manual de uso](docs/manual_de_uso.md) para aprender a cadastrar, consultar, alterar e excluir clientes.

## Estrutura do projeto

- `techbairro.py` — arquivo principal que inicia o sistema.
- `cliente.py` — arquivo da classe que representa os dados de um cliente, caso esteja presente nesta versão.
- `gerenciador_clientes.py` — arquivo responsável pelo gerenciamento dos clientes, caso esteja presente nesta versão.
- `techbairro.db` — banco de dados criado durante o uso; não deve ser enviado ao GitHub.
- `requirements.txt` — informa as dependências externas do projeto.
- `CHANGELOG.md` — histórico das alterações de cada versão.
- `docs/manual_de_uso.md` — instruções para a pessoa que utiliza o sistema.

## Autor

Luan Mouzinho  
Curso Técnico em Desenvolvimento de Sistemas  
Senac DF