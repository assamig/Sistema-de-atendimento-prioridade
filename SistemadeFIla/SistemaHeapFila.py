import heapq as hp
import json
import rich
from rich import print


class heapMaximo():
    def __init__(self):
        self.nome_arquivo = "pacientes_prioridade.json"
        try:
            f = open(self.nome_arquivo, "r")
            self.heap = json.load(f)
            f.close()
            self.heap = [tuple(x) for x in self.heap]
            self.contador = 0
        except FileNotFoundError:
            self.heap = []
            self.contador = 0

    def inserir(self, item, prioridade):
        if prioridade == 5:
                    prioridadestr = "EMERGENCIA"
        elif prioridade == 4:
             prioridadestr = "MUITA URGENCIA"
        elif prioridade == 3:
             prioridadestr = "URGENCIA"
        elif prioridade == 2:
             prioridadestr = "POUCA URGENCIA"
        elif prioridade == 1:
             prioridadestr = "NAO URGENCIA"
        else:
             print("[bold red]Digite uma opção válida![bold red]")
             return None
        hp.heappush(self.heap, (-prioridade, self.contador, item, prioridadestr))
        self.contador += 1
        self._salvar()


    def remover(self):
        if not self.heap:
            return None
        prioridade, _, item, prioridadestr = hp.heappop(self.heap)
        self._salvar()
        return item, -prioridade, prioridadestr


    def peek(self):
         if len(self.heap) == 0:
              print("[bold green]Sem clientes para exibir[bold green]")
         else:
              prioridade, _, item, prioridadestr = self.heap[0]
              return item, -prioridade, prioridadestr
    
    def _salvar(self):
        with open(self.nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(self.heap, f, indent=4, ensure_ascii=False)





