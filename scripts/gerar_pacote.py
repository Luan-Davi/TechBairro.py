
# ============================================================
# GERAR PACOTE DA VERSÃO (Aula 18)
# ============================================================
#
# Monta o arquivo .zip da versão que será publicada,
# deixando de fora o que NÃO deve ser distribuído.

import os
import zipfile

# ============================================================
# CONFIGURAÇÃO DO PACOTE
# ============================================================

# Este script fica na pasta scripts/;
# o projeto é a pasta de cima.
PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)

# Versão igual à constante VERSAO do techbairro.py
VERSAO = "3.3.2"

# Pastas que NÃO entram no pacote
PASTAS_FORA = [
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "dist",
]

# Tipos de arquivo que NÃO entram no pacote
EXTENSOES_FORA = [
    ".md",
    ".db",
    ".pyc",
    ".pyo",
]

# Arquivos específicos que NÃO entram no pacote
ARQUIVOS_FORA = [
    ".gitignore",
]

# O pacote é salvo na pasta dist/ do projeto
PASTA_DIST = os.path.join(PASTA_DO_PROJETO, "dist")
os.makedirs(PASTA_DIST, exist_ok=True)

# Nome e caminho do pacote
NOME_PACOTE = f"TechBairro-{VERSAO}"
CAMINHO_PACOTE = os.path.join(PASTA_DIST, NOME_PACOTE + ".zip")

# ============================================================
# MONTAGEM DO PACOTE
# ============================================================

print(f"Gerando {NOME_PACOTE}.zip")
print()

incluidos = 0
deixados_de_fora = 0

# Abre o ZIP para escrita
with zipfile.ZipFile(
    CAMINHO_PACOTE, "w", zipfile.ZIP_DEFLATED
) as pacote:

    # Percorre a pasta do projeto e suas subpastas
    for pasta_atual, subpastas, arquivos in os.walk(PASTA_DO_PROJETO):

        # Impede a entrada nas pastas excluídas
        subpastas[:] = [
            pasta for pasta in subpastas
            if pasta not in PASTAS_FORA
        ]

        for nome in arquivos:

            caminho = os.path.join(pasta_atual, nome)
            relativo = os.path.relpath(caminho, PASTA_DO_PROJETO)

            extensao = os.path.splitext(nome)[1].lower()

            # Verifica se o arquivo deve ficar de fora
            if nome in ARQUIVOS_FORA or extensao in EXTENSOES_FORA:
                print(f"  fora      {relativo}")
                deixados_de_fora += 1
                continue

            # Não inclui o próprio ZIP que está sendo gerado
            if os.path.abspath(caminho) == os.path.abspath(CAMINHO_PACOTE):
                continue

            # Adiciona o arquivo ao pacote
            destino = os.path.join(NOME_PACOTE, relativo)
            pacote.write(caminho, destino)

            print(f"  incluído  {relativo}")
            incluidos += 1

print()
print(f"Arquivos incluídos: {incluidos}")
print(f"Arquivos deixados de fora: {deixados_de_fora}")
print(f"Pacote salvo em: {CAMINHO_PACOTE}")
