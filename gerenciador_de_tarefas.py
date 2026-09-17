class ArrayList:
    def __init__(self):
        self.LEN = 3 
        self.arrayList = [None] * self.LEN
        self.insertPosition = 0

    def insert(self, data):
        if self.isMemoryFull():
            print("\n[Aviso] Memória cheia! Realocando para um novo array...")
            self.increaseMemory()        
        self.arrayList[self.insertPosition] = data
        self.insertPosition += 1

    def remove_at(self, position):
        if self.isEmpty():
            print("\n[Erro] A lista está vazia.")
            return None       
        if position < 0 or position >= self.insertPosition:
            print("\n[Erro] Posição inválida.")
            return None
        removed_data = self.arrayList[position]
        for i in range(position, self.insertPosition - 1):
            self.arrayList[i] = self.arrayList[i + 1]
        self.insertPosition -= 1
        self.arrayList[self.insertPosition] = None        
        return removed_data

    def isMemoryFull(self):
        return self.insertPosition == len(self.arrayList)
    
    def isEmpty(self):
        return self.insertPosition == 0

    def increaseMemory(self):
        newArray = [None] * (2 * len(self.arrayList))
        self.copyElements(newArray, self.arrayList)
        self.arrayList = newArray

    def copyElements(self, newArray, oldArray):
        for position in range(self.insertPosition):
            newArray[position] = oldArray[position]

    def display(self):
        if self.isEmpty():
            print("Nenhuma tarefa no momento.")
            return      
        for position in range(self.insertPosition):
            print(f"[{position}] - {self.arrayList[position]}")


def main():
    lista_tarefas = ArrayList()
    print(" 📋 GERENCIADOR DE TAREFAS ")

    while True:
        print("\n--- MENU ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir/Remover Tarefa")
        print("4. Sair")
        
        comando = input("Escolha uma opção (1-4): ").strip()
        
        if comando == "1":
            tarefa = input("Digite a descrição da tarefa: ").strip()
            if tarefa:
                lista_tarefas.insert(tarefa)
                print(f"✅ Tarefa '{tarefa}' adicionada com sucesso!")
            else:
                print("⚠️ A tarefa não pode ser vazia.")
                
        elif comando == "2":
            print("\n--- SUAS TAREFAS ---")
            lista_tarefas.display()
            print("--------------------")
            
        elif comando == "3":
            if lista_tarefas.isEmpty():
                print("⚠️ Não há tarefas para remover.")
                continue
                
            lista_tarefas.display()
            try:
                indice = int(input("Digite o número (ID) da tarefa para concluir: "))
                removida = lista_tarefas.remove_at(indice)
                if removida:
                    print(f"🗑️ Tarefa '{removida}' concluída e removida!")
            except ValueError:
                print("⚠️ Entrada inválida. Por favor, digite um número inteiro.")
                
        elif comando == "4":
            print("🚀 Encerrando o programa. Até logo!")
            break
            
        else:
            print("⚠️ Comando não reconhecido. Tente novamente.")


if __name__ == "__main__":
    main()
