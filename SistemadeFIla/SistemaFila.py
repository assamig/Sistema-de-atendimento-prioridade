import json


class Queue:
    def __init__(self):
        self.nome_arquivo = "persistencia_fila.json"
        try:
           f =  open(self.nome_arquivo, "r")
           self.items = json.load(f)
           f.close()
        except FileNotFoundError:
            self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        self._salvar()

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.items.pop(0)
        self._salvar()
        return item
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)
    def _salvar(self):
        with open(self.nome_arquivo, "w", encoding="utf-8") as archive:
            json.dump(self.items, archive, indent=4, ensure_ascii=False)


