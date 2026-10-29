# Changelog da TechBairro

## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.

## v3.3.2 (Aula 27)
### Adicionado
- README com requisitos, instalação e configuração do banco.
- Requisitos do arquivo.txt.
- Manual de uso em docs/manual_de_uso.md.
- Registro de testes em docs/registro_de_testes.md.

## v3.3.1 (Aula 21)
### Alterado
- O código monolítico do techbairrofoi reorganizado em arquitetura de camadas.
- A classe Clientefoi movida para o novo módulo cliente.py.
- A comunicação com o banco de dados SQLite foi isolada no novo módulo banco.py.
- As regras de negócio de validação foram centralizadas na classe ValidadorClientedentro do novo módulo validacao.py.
### Adicionado
- Criado o script de testes automatizados unitários testar_validacao.pypara validar as regras de negócio de forma isolada, sem interface gráfica e sem mexer no banco de dados.

## v3.3.0 ()
### Corrigido
- A lista da consulta é atualizada depois de excluir um cliente.
- A edição atualiza o cadastro existente pelo ID, sem adicionar outro registro.
- O atalho Delete só exclui o cliente selecionado e pede confirmação.
- A abertura de mais de uma janela de consulta é tratada para evitar atalhos ligados à janela errada.
### Adicionado
- Modo de edição identificado pelo ID do cliente, evitando criar um cadastro duplicado ao editar.
- Atalho Delete para excluir o cliente selecionado na consulta.
- Duplo clique em um cliente para abrir a edição.
- Confirmação antes de excluir um cadastro.


## v3.2.1 (Aula 18)
### Alterado
- O número da versão passou a ficar v3.2.1
### Adicionado
- Script scripts/gerar_pacote.py, que monta um arquivo .zip e deixa fora o que não deve ser distribuido
- Arquivo COMO_EXECUTAR.txt, com a nova versão explica os requisitos, forma de execultar e os dados que vão ser apresentados

## v3.2.0 (Aula 16)
### Alterado
- O banco agora é aberto pelo caminho completo (os.path + __file__),
  sempre na pasta do projeto, não importa de onde o programa seja executado.
### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

## v3.1 (Aula 15)
### Corrigido
- O Endereço voltou a ser obrigatório no cadastro.
- A validação de e-mail passou a recusar e-mail sem nome antes do @ ou sem ponto depois do @.
- A Consulta voltou a listar os clientes em ordem alfabética.
- A edição de um cliente passou a ser gravada no banco (faltava o commit).
- A exclusão só acontece quando o usuário responde Sim na confirmação.

## v3.0 (Aula 14)
### Alterado
- O GerenciadorClientes deixou de guardar os clientes numa lista em memória
  e passou a gravar no banco SQLite techbairro.db.
- Editar e excluir passaram a usar o id do cliente no banco (id_em_edicao),
  e não mais a posição na lista (indice_em_edicao).
- O contador de clientes passou a vir do banco ao abrir a aplicação.
### Adicionado
- Tratamento de erros do banco com try/except sqlite3.Error.

## v2.0 (Aulas 11 e 12)
### Adicionado
- Classes Cliente e GerenciadorClientes.
- Tela de Consulta com a lista de clientes e os botões Editar e Excluir.
- Confirmação antes de excluir um cliente.

## Antes da v2.0 (Aulas 5 a 10)
- Janela de cadastro com Tkinter, eventos dos botões e validação dos campos.

Histórico do código
O projeto usa Git. Para ver o histórico, rode na pasta do projeto:
git log --oneline
