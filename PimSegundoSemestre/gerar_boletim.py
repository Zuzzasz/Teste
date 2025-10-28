import os

def gerar_boletim_salvar(aluno, imprimir=True):
    # Criar pasta 'boletins' se não existir
    pasta_boletins = "boletins"
    os.makedirs(pasta_boletins, exist_ok=True)

    # Dados do aluno
    ra = aluno.get('ra', 'desconhecido')
    nome = aluno.get('nome', 'Aluno desconhecido')
    notas = aluno.get('notas', {})
    faltas = aluno.get('faltas', 0)
    total_aulas = aluno.get('total_aulas', 0)

    # Calcula frequência
    aulas_presentes = aluno.get('presencas', 0)
    percentual_frequencia = (aulas_presentes / total_aulas * 100) if total_aulas > 0 else 0

    # Construção do boletim
    linhas = [f"=== Boletim de {nome} (RA: {ra}) ===\n"]

    # Notas
    if notas:
        linhas.append("📘 Notas:")
        for materia, nota in notas.items():
            linhas.append(f" - {materia}: {nota}")
        media = sum(notas.values()) / len(notas)
        linhas.append(f"\n🧮 Média geral: {media:.2f}\n")
    else:
        media = 0
        linhas.append("📘 Boletim: Nenhuma nota registrada.\n")

    # Frequência
    linhas.append("📅 Frequência:")
    linhas.append(f" - Total de aulas: {total_aulas}")
    linhas.append(f" - Presenças: {aulas_presentes}")
    linhas.append(f" - Faltas: {faltas}")
    linhas.append(f" - Percentual de presença: {percentual_frequencia:.2f}%")

    # Situação final
    if media >= 6 and percentual_frequencia >= 75:
        situacao = "✅ Aprovado"
    elif percentual_frequencia < 75:
        situacao = "⚠️ Reprovado por falta"
    else:
        situacao = "❌ Reprovado por nota"
    linhas.append(f"\n📊 Situação final: {situacao}")
    linhas.append("\n--- Fim do Boletim ---\n")

    # Salva o boletim no arquivo
    nome_arquivo = os.path.join(pasta_boletins, f"Boletim_{ra}.txt")
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    # Se solicitado, imprime no console
    if imprimir:
        print("\n".join(linhas))
