import os

def gerar_boletim_salvar(aluno):
   
    # Criar pasta 'boletins' se não existir
    if not os.path.exists("boletins"):
        os.makedirs("boletins")

    nome_arquivo = f"boletins/Boletim_{aluno.get('ra')}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"=== Boletim de {aluno.get('nome')} ===\n\n")

        # Notas
        notas = aluno.get("notas", {})
        if notas:
            f.write("📘 Notas:\n")
            for materia, nota in notas.items():
                f.write(f"{materia}: {nota}\n")
            media = sum(notas.values()) / len(notas)
            f.write(f"\nMédia geral: {media:.2f}\n")
        else:
            f.write("Nenhuma nota registrada.\n")

        # Frequência
        frequencia = aluno.get("frequencia", 0)
        f.write(f"\n📅 Frequência: {frequencia} dias\n")
        f.write("\n--- Fim do Boletim ---\n")

    # Também mostrar na tela
    print(f"\n✅ Boletim gerado e salvo em '{nome_arquivo}'")
    print(f"=== Boletim de {aluno.get('nome')} ===")
    if notas:
        for materia, nota in notas.items():
            print(f"{materia}: {nota}")
        print(f"Média geral: {media:.2f}")
    else:
        print("Nenhuma nota registrada.")
    print(f"Frequência: {frequencia} dias")
    print("--- Fim do Boletim ---\n")
