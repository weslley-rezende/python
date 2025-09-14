# ===================== MENU DE EXERCÍCIOS =====================

# ---------- Exercício 1 ----------
def exercicio1():
    lista = [1, 3, 4, 5, 6]
    if 2 in lista:
        print("O valor 2 está presente na lista.")
    else:
        print("O valor 2 não está presente na lista.")


# ---------- Exercício 2 ----------
def exercicio2():
    lista = [1, 3, 4, 5, 6]
    dicionario = {num: num * 2 for num in lista}
    print("Dicionário gerado:", dicionario)


# ---------- Exercício 3 ----------
def exercicio3():
    def passo_a_passo():
        print("\n--- Passo a Passo da Solução ---")
        print("1. Receber o IP como string (ex: '1.1.1.1').")
        print("2. Percorrer cada caractere da string.")
        print("3. Substituir '.' por '[.]'.")
        print("4. Concatenar tudo em nova string.\n")

    def ajustar_ip_for(ip):
        novo_ip = ""
        for char in ip:
            novo_ip += "[.]" if char == "." else char
        return novo_ip

    def explicacao_replace():
        print("\n--- Explicação do replace() ---")
        print("replace('antigo', 'novo') substitui todas ocorrências.\n")

    def ajustar_ip_replace(ip):
        return ip.replace(".", "[.]")

    while True:
        print("\n===== AJUSTAR ENDEREÇO IP =====")
        print("a) Passo a passo")
        print("b) Usar for e if")
        print("c) Explicar replace()")
        print("d) Usar replace()")
        print("0) Voltar")

        opcao = input("Escolha: ").lower()
        if opcao == "a":
            passo_a_passo()
        elif opcao == "b":
            ip = input("Digite o IP: ")
            print("Saída:", ajustar_ip_for(ip))
        elif opcao == "c":
            explicacao_replace()
        elif opcao == "d":
            ip = input("Digite o IP: ")
            print("Saída:", ajustar_ip_replace(ip))
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ---------- Exercício 4 ----------
def exercicio4():
    numeros = [12, 342, 345, 2, 8, 7896]

    def contar_pares(nums):
        return sum(1 for n in nums if len(str(n)) % 2 == 0)

    while True:
        print("\n===== CONTAR NÚMEROS COM DÍGITO PAR =====")
        print("a) Executar função")
        print("b) Explicar len()")
        print("0) Voltar")

        opcao = input("Escolha: ").lower()
        if opcao == "a":
            print("Lista:", numeros)
            print("Quantidade:", contar_pares(numeros))
        elif opcao == "b":
            print("len() retorna o tamanho de um objeto, ex: len('1234')=4")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ---------- Exercício 5 ----------
def exercicio5():
    meu_array = [1, 2, 3, 2, 1, 4, 10]

    def contar_elementos(arr):
        d = {}
        for n in arr:
            d[n] = d.get(n, 0) + 1
        return d

    def soma_unicos(arr):
        return sum(n for n, q in contar_elementos(arr).items() if q == 1)

    while True:
        print("\n===== SOMAR ELEMENTOS ÚNICOS =====")
        print("a) Mostrar contagem")
        print("b) Somar únicos")
        print("0) Voltar")

        opcao = input("Escolha: ").lower()
        if opcao == "a":
            print("Contagem:", contar_elementos(meu_array))
        elif opcao == "b":
            print("Soma:", soma_unicos(meu_array))
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ---------- Exercício 6 ----------
def exercicio6():
    def elemento_unico(array):
        for num in array:
            if array.count(num) == 1:
                return num
        return None

    while True:
        print("\n===== ELEMENTO ÚNICO =====")
        print("1 - Usar array exemplo")
        print("2 - Inserir array")
        print("0 - Voltar")

        opcao = input("Escolha: ")
        if opcao == "1":
            arr = [1, 2, 2, 1, 3, 3, 4]
            print("Array:", arr)
            print("Único:", elemento_unico(arr))
        elif opcao == "2":
            try:
                arr = list(map(int, input("Digite números separados por espaço: ").split()))
                print("Único:", elemento_unico(arr))
            except:
                print("Entrada inválida.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ---------- Exercício 7 ----------
def exercicio7():
    lista = [1, 5, 33, 8, 77, 43, 124, 6, 8, 99]

    def menor(arr): return min(arr)
    def maior(arr): return max(arr)
    def soma_menor_maior(arr): return min(arr) + max(arr)
    def soma_total(arr): return sum(arr)
    def media(arr): return sum(arr) / len(arr)

    while True:
        print("\n===== ANÁLISE DE ARRAY =====")
        print("1 - Menor número")
        print("2 - Maior número")
        print("3 - Menor+Maior")
        print("4 - Soma total")
        print("5 - Média")
        print("6 - Mostrar lista")
        print("7 - Nova lista")
        print("0 - Voltar")

        opcao = input("Escolha: ")
        if opcao == "1":
            print("Menor:", menor(lista))
        elif opcao == "2":
            print("Maior:", maior(lista))
        elif opcao == "3":
            print("Menor+Maior:", soma_menor_maior(lista))
        elif opcao == "4":
            print("Soma:", soma_total(lista))
        elif opcao == "5":
            print("Média:", media(lista))
        elif opcao == "6":
            print("Lista:", lista)
        elif opcao == "7":
            try:
                lista = list(map(int, input("Digite números: ").split()))
            except:
                print("Entrada inválida.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ---------- Exercício 8 ----------
def exercicio8():
    lista = []

    while True:
        print("\n===== LISTA =====")
        print("1 - Adicionar 10")
        print("2 - Adicionar 20")
        print("3 - Adicionar 30")
        print("4 - Remover 20")
        print("5 - Remover 10")
        print("6 - Explicar append")
        print("7 - Explicar pop")
        print("8 - Explicar insert")
        print("9 - Explicar sort")
        print("10 - Explicar count")
        print("11 - Explicar sum")
        print("12 - Mostrar lista")
        print("0 - Voltar")

        opcao = input("Escolha: ")
        if opcao == "1":
            lista.append(10)
        elif opcao == "2":
            lista.append(20)
        elif opcao == "3":
            lista.append(30)
        elif opcao == "4":
            if 20 in lista: lista.remove(20)
        elif opcao == "5":
            if 10 in lista: lista.remove(10)
        elif opcao == "6":
            print("append(x): adiciona no final")
        elif opcao == "7":
            print("pop(): remove último")
        elif opcao == "8":
            print("insert(i,x): insere em posição")
        elif opcao == "9":
            print("sort(): ordena lista")
        elif opcao == "10":
            print("count(x): quantas vezes aparece")
        elif opcao == "11":
            print("sum(): soma valores")
        elif opcao == "12":
            print("Lista:", lista)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ---------- Exercício 9 ----------
def exercicio9():
    dicionario = {}

    while True:
        print("\n===== DICIONÁRIO =====")
        print("1 - Adicionar a:10")
        print("2 - Adicionar b:3")
        print("3 - Alterar b:4")
        print("4 - Adicionar c:56")
        print("5 - Remover b=3")
        print("6 - Remover b=4")
        print("7 - Explicar update")
        print("8 - Explicar pop")
        print("9 - Explicar get")
        print("10 - Explicar keys")
        print("11 - Explicar values")
        print("12 - Explicar items")
        print("13 - Mostrar dicionário")
        print("0 - Voltar")

        opcao = input("Escolha: ")
        if opcao == "1": dicionario["a"] = 10
        elif opcao == "2": dicionario["b"] = 3
        elif opcao == "3": dicionario["b"] = 4
        elif opcao == "4": dicionario["c"] = 56
        elif opcao == "5":
            if dicionario.get("b") == 3: dicionario.pop("b")
        elif opcao == "6":
            if dicionario.get("b") == 4: dicionario.pop("b")
        elif opcao == "7": print("update(): adiciona/atualiza")
        elif opcao == "8": print("pop(): remove chave")
        elif opcao == "9": print("get(): pega valor")
        elif opcao == "10": print("keys(): chaves")
        elif opcao == "11": print("values(): valores")
        elif opcao == "12": print("items(): pares")
        elif opcao == "13": print("Dicionário:", dicionario)
        elif opcao == "0": break
        else: print("Opção inválida.")


# ---------- Exercício 10 ----------
def exercicio10():
    def verifica_string(s):
        encontrado_b = False
        for char in s:
            if char == 'b': encontrado_b = True
            elif char == 'a' and encontrado_b: return False
        return True

    while True:
        print("\n===== SEQUÊNCIA a/b =====")
        print("1 - Testar 'abababab'")
        print("2 - Testar 'bababa'")
        print("3 - Testar 'aaaaabbbb'")
        print("4 - Digitar string")
        print("0 - Voltar")

        opcao = input("Escolha: ")
        if opcao == "1": print(verifica_string("abababab"))
        elif opcao == "2": print(verifica_string("bababa"))
        elif opcao == "3": print(verifica_string("aaaaabbbb"))
        elif opcao == "4":
            s = input("Digite string a/b: ")
            print(verifica_string(s))
        elif opcao == "0": break
        else: print("Opção inválida.")


# ---------- Exercício 11 ----------
def exercicio11():
    def encontrar_faltante(array):
        n = len(array)
        soma_esperada = (n * (n + 1)) // 2
        return soma_esperada - sum(array)

    while True:
        print("\n===== NÚMERO FALTANTE =====")
        print("1 - Digitar array")
        print("2 - Usar exemplo")
        print("0 - Voltar")

        op = input("Escolha: ")
        if op == "1":
            arr = list(map(int, input("Digite números separados por vírgula: ").split(",")))
            print("Faltante:", encontrar_faltante(arr))
        elif op == "2":
            arr = [0, 2, 3, 4, 5, 6, 7, 8]
            print("Exemplo:", arr)
            print("Faltante:", encontrar_faltante(arr))
        elif op == "0": break
        else: print("Opção inválida.")


# ---------- Exercício 12 ----------
def exercicio12():
    from collections import Counter
    def encontrar_mais_frequente(array):
        elemento, freq = Counter(array).most_common(1)[0]
        return elemento, freq

    while True:
        print("\n===== MAIS FREQUENTE =====")
        print("1 - Digitar array")
        print("2 - Usar exemplo")
        print("0 - Voltar")

        op = input("Escolha: ")
        if op == "1":
            arr = list(map(int, input("Digite números separados por vírgula: ").split(",")))
            print("Mais frequente:", encontrar_mais_frequente(arr))
        elif op == "2":
            arr = [1, 2, 3, 3, 3, 4, 5]
            print("Exemplo:", arr)
            print("Mais frequente:", encontrar_mais_frequente(arr))
        elif op == "0": break
        else: print("Opção inválida.")


# ---------- Exercício 13 ----------
def exercicio13():
    from collections import Counter

    def lista_para_dicionario(array): return Counter(array)
    def encontrar_chave_igual_valor(dic):
        for k, v in dic.items():
            if k == v: return k
        return None

    while True:
        print("\n===== LISTA -> DICIONÁRIO =====")
        print("1 - Digitar lista")
        print("2 - Usar exemplo")
        print("0 - Voltar")

        op = input("Escolha: ")
        if op == "1":
            arr = list(map(int, input("Digite números separados por vírgula: ").split(",")))
            dic = lista_para_dicionario(arr)
            print("Dicionário:", dic)
            print("Chave==Valor:", encontrar_chave_igual_valor(dic))
        elif op == "2":
            arr = [1, 2, 2, 3, 3, 4, 4, 4, 5, 7, 1]
            dic = lista_para_dicionario(arr)
            print("Exemplo:", arr)
            print("Dicionário:", dic)
            print("Chave==Valor:", encontrar_chave_igual_valor(dic))
        elif op == "0": break
        else: print("Opção inválida.")


# ------------------- MENU PRINCIPAL -------------------
def menu_principal():
    print("\n===================================")
    print("  Programa Bolsa Futuro Digital ")
    print("  Atividade final módulo 1 ")
    print("  Aluno: Weslley Rezende")
    print("===================================\n")

    while True:
        print("=== MENU DE EXERCÍCIOS ===")
        print("1 - Verificar Elementos em uma Lista") 
        print("2 - Converter Lista para Dicionário")
        print("3 - Ajustar um Endereço IP")
        print("4 - Contar Números com Dígito Par")
        print("5 - Somar Elementos Únicos de um Array")
        print("6 - Retornar o Elemento Que Aparece Uma Vez")
        print("7 - Funções de Análise de um Array de Números Inteiros")
        print("8 - Manipulação de uma Lista")
        print("9 - Manipulação de um Dicionário")
        print("10 - Verificação de Sequência em uma String")
        print("11 - Encontrar o Único Número que Faltou em um Array")
        print("12 - Encontrar o Elemento com Mais Frequência em um Array")
        print("13 - Converter Uma Lista em Dicionário")
        print("0 - Sair")

        opcao = input("Escolha: ")
        if opcao == "1": exercicio1()
        elif opcao == "2": exercicio2()
        elif opcao == "3": exercicio3()
        elif opcao == "4": exercicio4()
        elif opcao == "5": exercicio5()
        elif opcao == "6": exercicio6()
        elif opcao == "7": exercicio7()
        elif opcao == "8": exercicio8()
        elif opcao == "9": exercicio9()
        elif opcao == "10": exercicio10()
        elif opcao == "11": exercicio11()
        elif opcao == "12": exercicio12()
        elif opcao == "13": exercicio13()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()
