# ============================================================
# VALIDAÇÃO (Aula 21)
# ===============================================================
#
# Responsabilidade: as regras de negócio do cadastro (RF01a RF03).
# Este arquivo não sabe nada de janela nem de banco.

# Classe responsável por conferir se um cliente pode ser gravado


# MUDOU NA AULA 21: era uma função solta no techbairro.
# agora é um método do ValidadorCliente
def email_parece_valido(email):

    # Verifica se existe @ no e-mail
    if "@" not in email:

        return False


    # Divide o e-mail em usuário e domínio
    usuario, _, dominio = email.partition("@")


    # Verifica se existe usuário e ponto no domínio
    if usuario == "" or "." not in dominio:   # CORRIGIDO (BUG 2): era and, precisa ser or

        return False


    return True

    # # Verifica se o e-mail parece válido     Reserva
    # if not email_parece_valido(
    #     valores["E-mail"]
    # ):

    #     status.config(
    #         text="E-mail inválido: use o formato nome@dominio.com",
    #         fg="red"
    #     )

    #     return


class ValidadorCliente:

    # Confere todas as regras do cliente.
    #
    # Retorna a mensagem do primeiro problema encontrado,
    # ou None se o cliente estiver válido.

    def validar(self, cliente):
        
        # RF01: lista com os campos vazios, com o nome que aparece na tela
        vazios = []
    
        if cliente.nome == "":
            vazios.append("Nome")
        if cliente.telefone == "":
            vazios.append("Telefone")
        if cliente.email == "":
            vazios.append("E-mail")
        if cliente.endereco == "":
            vazios.append("Endereço")
        
        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"


        # RF02: o telefone precisa ter somente números
        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        # RF03: o e-mail precisa estar no formato nome@dominio.com
        if not email_parece_valido(cliente.email):
            return "E-mail inválido: use o formato nome@dominio.com"
        # Nenhum problema encontrado
        return None

        
       