import os
from Cadastro import carregar_dados_alunos, carregar_dados_professores
from gerar_boletim import gerar_boletim_salvar
import json

# ==========================================================
# === RELATÓRIO DO ALUNO ===
# ==========================================================
# Relatorios.py - relatorio_aluno (corrigido)

from Cadastro import carregar_dados
from gerar_boletim import gerar_boletim_salvar  # se existir

def relatorio_aluno(ra_aluno=None):
    usuarios = carregar_dados()
    alunos = [u for u in usuarios if u.get("tipo") == "aluno"]

    if not alunos:
        print("⚠️ Nenhum aluno cadastrado no sistema.")
        return

    if not ra_aluno:
        ra_aluno = input("Digite o RA do aluno: ").strip()

    aluno = next((a for a in alunos if a.get("ra") == ra_aluno), None)

    if aluno is None:
        print(f"❌ Nenhum aluno encontrado com RA {ra_aluno}.")
        return

    print('\n==============================')
    print('     RELATÓRIO DO ALUNO')
    print('==============================')
    print(f"Nome: {aluno.get('nome','-')}")
    print(f"RA: {aluno.get('ra','-')}")
    print(f"Turma: {aluno.get('turma','-')}")
    disciplinas = aluno.get('disciplinas', [])
    print(f"Disciplinas: {', '.join(disciplinas) if disciplinas else '-'}")
    print(f"Frequência: {aluno.get('frequencia','-')}")

    notas = aluno.get("notas", {})
    if notas:
        print("\n📘 Boletim:")
        media = sum(notas.values()) / len(notas) if notas else 0
        for materia, nota in notas.items():
            print(f" - {materia}: {nota}")
        print(f"Média geral: {media:.2f}")
    else:
        print("\n📘 Boletim: Nenhuma nota registrada.")
    print('==============================\n')

    # salva ou gera boletim, se módulo existir
    try:
        gerar_boletim_salvar(aluno)
    except Exception:
        pass

# ==========================================================
# === RELATÓRIO DO PROFESSOR ===
# ==========================================================
def relatorio_professor(email_prof=None):
    """
    Gera relatório completo de um professor cadastrado no sistema.
    Mostra nome, e-mail, turmas e disciplinas que leciona.
    Também salva o relatório em arquivo .txt.
    """

    professores = carregar_dados_professores()

    if not professores:
        print("⚠️ Nenhum professor cadastrado no sistema.")
        return

    if not email_prof:
        email_prof = input("Digite o e-mail institucional do professor: ").strip().lower()

    professor = next((p for p in professores if p["email"].lower() == email_prof), None)

    if professor is None:
        print(f"❌ Nenhum professor encontrado com o e-mail {email_prof}.")
        return

    print('\n==============================')
    print('     RELATÓRIO DO PROFESSOR')
    print('==============================')
    print(f"Nome: {professor['nome']}")
    print(f"E-mail: {professor['email']}")
    print(f"Turmas responsáveis: {', '.join(professor.get('turmas', []))}")
    print(f"Disciplinas: {', '.join(professor.get('disciplinas', []))}")
    print(f"Reclamações pendentes: {professor.get('reclamacoes', 'Nenhuma')}")
    print('==============================\n')

    # Criar pasta 'relatorios' se não existir
    if not os.path.exists("relatorios"):
        os.makedirs("relatorios")

    nome_arquivo = f"relatorios/Relatorio_Professor_{professor['nome'].replace(' ', '_')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"=== RELATÓRIO DO PROFESSOR ===\n\n")
        f.write(f"Nome: {professor['nome']}\n")
        f.write(f"E-mail: {professor['email']}\n")
        f.write(f"Turmas responsáveis: {', '.join(professor.get('turmas', []))}\n")
        f.write(f"Disciplinas: {', '.join(professor.get('disciplinas', []))}\n")
        f.write(f"Reclamações pendentes: {professor.get('reclamacoes', 'Nenhuma')}\n")
        f.write("\n--- Fim do Relatório ---\n")

    print(f"✅ Relatório salvo em '{nome_arquivo}'\n")
