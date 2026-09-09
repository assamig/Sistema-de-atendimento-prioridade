from SistemaFila import Queue
from SistemaHeapFila import heapMaximo
import os
import time
import json
import rich
from rich import print

fila = Queue()
heapMax = heapMaximo()

arquivo1 = open("pacientes_prioridade.json", "r")
dados = json.load(arquivo1)
arquivo1.close()


arquivo2 = open("pacientes_cadastrados.json", "r")
dados2 = json.load(arquivo2)
arquivo2.close()

def salvar_dados1():
     with open("pacientes_prioridade.json", "w", encoding="utf-8") as info:
          json.dump(dados, info, indent=4, ensure_ascii=False)


def salvar_dados():
     with open("pacientes_cadastrados.json", "w", encoding="utf-8") as info:
          json.dump(dados2, info, indent=4, ensure_ascii=False)
    

def cadastrar_paciente(nome, cpf, endereco):
     paciente = {
          "nome": nome,
          "cpf": cpf,
          "endereco": endereco
     }
     dados2.append(paciente)
     salvar_dados()




def triagem():
    while True:
        if fila.size() == 0:
            print("[bold green]Sem pacientes na fila para exibir.[bold green]")
            menu()
            return
        else:

            ultima_pessoa = fila.peek()
            print("[bold green]-------[bold green]")
            print("[bold green]TRIAGEM[bold green]")
            print("[bold green]-------[bold green]")
            print(f"PRÓXIMO PACIENTE: {ultima_pessoa}")
            time.sleep(5)
            print("[bold red]5 = EMERGÊNCIA - Caso gravissímo com necessidade de atendimento imediato e risco de morte.[bold red]")
            print("[orange1]\n4 = MUITA URGÊNCIA - Caso grave e risco significativo de evoluir para morte. Atendimento urgente.[orange1]")
            print("[yellow]\n3 = URGÊNCIA - Caso de gravidade moderada, necessidade de atendimento médico sem risco imediato.[yellow]")
            print("[bold green]\n2 = POUCA URGÊNCIA - Caso para atendimento preferencial nas unidades de atenção básica.[bold green]")
            print("[blue1]\n1 = NÃO URGÊNCIA - Caso de atendimento básico, de acordo com horário de chegada. Queixas como crônicas, resfriados, confusões, escoriações, dor de garganta, ferimentos que não requerem fechamento e entre outros.[blue1]")
            try:
                prioridade = int(input("Digite o nível de prioridade do paciente ou qualquer letra para voltar para o MENU: "))
                fila.dequeue()
                heapMax.inserir(ultima_pessoa, prioridade)
                print("[bold green]Paciente triado com sucesso para o atendimento.✅[bold green]")
            except ValueError:
                print("[bold green]Voltando[bold green]", end="")
                retisencia()
                menu()
                
                
               
            
            





def abrir_fila():
    while True:
        print("[bold green]---------------------[bold green]")
        print("[bold green]CADASTRO DE PACIENTES[bold green]")
        print("[bold green]---------------------[bold green]")
        nome = input("Digite o nome do paciente ou F para sair: ").upper().strip()
        if nome == "F":
            print("[bold green]Saindo[bold green]", end="")
            retisencia()
            menu()
            return
        cpf = input("Informe o CPF do paciente: ")
        if len(cpf) > 11 or len(cpf) < 11:
           print("[bold red]Digite um CPF válido![bold red]")
        else:
            endereco = input("Informe o endereço do paciente: ").upper().strip()
            fila.enqueue(nome)
            cadastrar_paciente(nome, cpf, endereco)
            print(f"[bold green]Número de pessoas na fila -> {fila.size()}.[bold green]")
            print("[bold green]Máximo de pessoas na fila: 10. [bold green]")
            if fila.size() == 10:
              print("[bold green]A fila de pessoas já atingiu o máximo, inicie a triagem[bold green]")
              triagem()





def carregar_pacientes_prioridade():
    if len(dados) == 0:
        print("[bold green]Sem pacientes para exibir.[bold green]")
        time.sleep(2)
    else:
        print("[bold green]------------------------------------------[bold green]")
        print("[bold green]PACIENTES A SEREM ATENDIDOS POR PRIORIDADE:")
        print("[bold green]------------------------------------------[bold green]")
        for indice, i in enumerate(heapMax.heap, start=1):
            p, _, nome, prioridadestr = i
            if prioridadestr == "EMERGENCIA":
                print(f"[bold red]{indice}.NOME: {nome} - PRIORIDADE: {prioridadestr}[bold red]")
            elif prioridadestr == "MUITA URGENCIA":
                print(f"[orange1]{indice}.NOME: {nome} - PRIORIDADE: {prioridadestr}[orange1]")
            elif prioridadestr == "URGENCIA":
                print(f"[yellow]{indice}.NOME: {nome} - PRIORIDADE: {prioridadestr}[yellow]")
            elif prioridadestr == "POUCA URGENCIA":
                print(f"[bold green]{indice}.NOME: {nome} - PRIORIDADE: {prioridadestr}[bold green]")
            elif prioridadestr == "NAO URGENCIA":
                print(f"[blue1]{indice}.NOME: {nome} - PRIORIDADE: {prioridadestr}[blue1]")
                



def carregar_pacientes_cadastrados():
    if len(dados2) == 0:
        print("[bold green]Sem pacientes para exibir.[bold green]")
        time.sleep(2)
        menu()
    else:
        while True:
            print("[bold green]---------------------[bold green]")
            print("[bold green]PACIENTES CADASTRADOS:[bold green]")
            print("[bold green]---------------------[bold green]")
            for indice, paciente in enumerate(dados2, start=1):
                print(f"[bold green]{indice}°. NOME: {paciente['nome']} - CPF: {paciente['cpf']}[bold green]")
            print("[bold green]\n--------------------------------[bold green]")
            print("[bold green]1.Pesquisar paciente🔎.[bold green]")
            print("[bold green]2.Remover paciente❌.[bold green]")
            print("[bold green]3.Esvaziar lista.[bold green]")
            print("[bold green]4.Voltar.")
            entrada = int(input("Digite sua opção: "))
            try:
                if entrada == 1:
                    buscar = input("Digite o CPF do paciente que deseja buscar: ")
                    if buscar in [paciente['cpf'] for paciente in dados2]:
                        print("[bold green]Paciente encontrado.✅")
                        print(f"[bold green]NOME: {next(paciente['nome'] for paciente in dados2 if paciente['cpf'] == buscar)} - CPF: {buscar} - ENDEREÇO: {next(paciente['endereco'] for paciente in dados2 if paciente['cpf'] == buscar)}[bold green]")
                        time.sleep(2)
                        continue
                    else:
                        print("[bold red]Paciente não encontrado.[bold red]")
                        continue
                elif entrada == 2:
                    try:
                        remocao = int(input("Digite o índice do paciente que deseja remover: ")) - 1
                        dados2.pop(remocao)
                        remocao = heapMax.remover()
                        salvar_dados()
                        print("[bold green]Paciente removido com sucesso. ❌[bold green]")
                        time.sleep(2)
                    except IndexError:
                        print("[bold red]Digite um índice válido[bold red]")
                    except ValueError:
                        print("[bold red]Digite um índice válido[bold red]")
                elif entrada == 3:
                    print("[bold green]Tem certeza que deseja esvaziar a lista de pacientes cadastrados?[bold green]")
                    confirm = input("Digite S para Sim | N para Não: ").upper().strip()
                    if confirm == "S":
                        dados2.clear()
                        dados.clear()
                        salvar_dados1()
                        salvar_dados()
                        print("[bold green]Lista esvaziada com sucesso![bold green]")
                        menu()
                    elif confirm == "N":
                        carregar_pacientes_cadastrados()
                    else:
                        print("[bold red]Digite uma opção válida![bold red]")
                elif entrada == 4:
                    print("[bold green]Voltando[bold green]", end="")
                    retisencia()
                    menu()
                else:
                    print("[bold red]Digite uma opção válida![bold red]")
            except ValueError:
                print("[bold red]Digite uma opção válida![bold red]")
                
                

        



def retisencia():
    retisencia = ['[bold green].[bold green]']
    ponto = ''.join(retisencia)
    for i in range(3):
        print(ponto, end="", flush=True)
        time.sleep(1)



def menu():
    while True:
        print("[bold green]\n--------------------------------------------[bold green]")
        print("[bold green]BEM VINDO AO SISTEMA DE ATENDIMENTO DE SAÚDE[bold green]")
        print("[bold green]--------------------------------------------[bold green]")
        print("[bold green]1.Cadastrar pacientes.[bold green]")
        print("[bold green]2.Encaminhar para triagem.[bold green]")
        print("[bold green]3.Consultar lista de pacientes por prioridade.[bold green]")
        print("[bold green]4.Consultar pacientes cadastrados.[bold green]")
        print("[bold green]5.Sair.[bold green]")
        
        try:
                entrada = int(input("Digite sua opção: "))
                if entrada == 1:
                    abrir_fila()
                elif entrada == 2:
                    triagem()
                elif entrada == 3:
                    carregar_pacientes_prioridade()
                elif entrada == 4:
                    carregar_pacientes_cadastrados()
                elif entrada == 5:
                    print("[bold green]Saindo[bold green]", end="")
                    retisencia()
                else:
                    print("[bold red]Digite uma opção válida![bold red]")
        except ValueError:
            print("[bold red]Digite uma opção válida![bold red]")



menu()