import os

import os

def gerar_boletim_salvar(aluno):
    """
    Gera o boletim de um aluno e salva em arquivo .txt na pasta 'boletins'.
    Mostra todas as informações no console.

    Args:
        aluno (dict): Deve conter:
            - 'nome': str
            - 'ra': str
            - 'notas': dict {materia: nota}
            - 'faltas': int (quantidade de faltas)
            - 'total_aulas': int (opcional, padrão 100)
    """

    # Criar pasta 'boletins' se não existir
    pasta_boletins = "boletins"
    os.makedirs(pasta_boletins, exist_ok=True)

    # Dados do aluno
    ra = aluno.get('ra', 'desconhecido')
    nome = aluno.get('nome', 'Aluno desconhecido')
    notas = aluno.get('notas', {})
    faltas = aluno.get('faltas', 0)
    total_aulas = aluno.get('total_aulas', 100)

    # Calcula presença começando em 100% e diminuindo com faltas
    percentual_frequencia = 100 - (faltas / total_aulas) * 100
    aulas_presentes = total_aulas - faltas

    # --- Construção do boletim ---
    linhas = [
        f"=== Boletim de {nome} (RA: {ra}) ===\n",
    ]

    # Notas
    if notas:
        linhas.append("📘 Notas:")
        for materia, nota in notas.items():
            linhas.append(f"{materia}: {nota}")
        media = sum(notas.values()) / len(notas) if notas else 0
        linhas.append(f"\nMédia geral: {media:.2f}\n")
    else:
        linhas.append("📘 Boletim: Nenhuma nota registrada.\n")

    # Frequência
    linhas.append(f"📅 Frequência: {percentual_frequencia:.2f}% ({aulas_presentes}/{total_aulas} aulas presentes)")

    linhas.append("\n--- Fim do Boletim ---\n")

    # --- Salvar em arquivo ---
    nome_arquivo = os.path.join(pasta_boletins, f"Boletim_{ra}.txt")
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("\n".join(linhas))
        print(f"\n✅ Boletim gerado e salvo em '{nome_arquivo}'")
    except Exception as e:
        print(f"❌ Erro ao salvar o boletim: {e}")

    # --- Exibir no console ---
    print("\n".join(linhas))


# ==========================
# Exemplo de uso
# ==========================
if __name__ == "__main__":
    aluno_exemplo = {
        "nome": "Kaue Zuza",
        "ra": "123456",
        "notas": {"Algoritmos": 8, "Estatística": 9, "Engenharia de Software": 8.5},
        "faltas": 8,
        "total_aulas": 100
    }
    gerar_boletim_salvar(aluno_exemplo)
