# Pesquisa de satisfação no atendimento - TudoWeb
import sys

# Padrão: 50 entrevistados. Para testes: python pesquisa_tudoweb.py 10
TOTAL_ENTREVISTADOS = int(sys.argv[1]) if len(sys.argv) > 1 else 50

excelente = 0
bom = 0
ruim = 0

print("=" * 45)
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("=" * 45)

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")

    nome = input("Nome: ").strip()

    # Validação da idade
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                break
            print("Idade inválida. Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    # Validação da opinião
    while True:
        print("Opinião sobre o atendimento:")
        print("  1 - EXCELENTE")
        print("  2 - BOM")
        print("  3 - RUIM")
        try:
            opiniao = int(input("Digite a opção (1, 2 ou 3): "))
            if opiniao in (1, 2, 3):
                break
            print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite apenas 1, 2 ou 3.")

    # Estruturas de decisão para contabilizar a opinião
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    else:
        ruim += 1

# Resultado final
print("\n" + "=" * 45)
print("          RESULTADO DA PESQUISA")
print("=" * 45)
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"a) Respostas EXCELENTE: {excelente}")
print(f"b) Respostas RUIM: {ruim}")
print("=" * 45)
