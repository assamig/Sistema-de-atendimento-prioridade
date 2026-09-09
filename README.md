# Sobre o Projeto
* O Projeto é um sistema de atendimento por prioridade, feito inteiramente em Python e utilizando estruturas de dados como Fila (FIFO), Heap e persistência de dados em JSON.
* Funcionalidades: O sistema cadastra pacientes por ordem de chegada e suas informações, tria os pacientes de acordo com o seu nível de prioridade, consulta pacientes pelo seu grau de urgência, guarda as informações dos pacientes sendo possível consultar paciente específico e sua informação.

# Sobre as Estruturas
* O objetivo do Projeto é mostrar a interação fluída entre as duas estruturas de dados, na qual cada uma tem sua função, sendo elas:

## Fila (FIFO)
* Estrutura usada para o cadastro por ordem de chegada dos pacientes. Pacientes que chegarem primeiro, serão encaminhados primeiros para a triagem por ordem de chegada, cadastrando suas informações no sistema e os colocando na fila de triagem de acordo com os que vão chegando primeiro.
* A fila tem um limite de 10 pessoas, ao atingir o limite, a triagem deve começar imediatamente, mas pode se optar por ir triando os pacientes que estão na fila ou se atingir o limite
* Imagem de demonstração:

  <img width="442" height="357" alt="image" src="https://github.com/user-attachments/assets/92d37c5b-2bfe-477a-bc1a-daf406f5cb56" />

* Obs: perceba que Pedro chegou primeiro que João na fila, logo Pedro irá para a triagem primeiro


## HeapMax 
* Estrutura usada na triagem dos pacientes e definir seus níveis de prioridade, onde aqui se usa um HeapMax, para definir a prioridade pelo maior tipo de urgência e para isso, foi usado a biblioteca heapq, que por ser naturalmente um HeapMin, coloquei os valores instanciados como negativo para funcionar como prioridade máxima ao invés de mínima.
* Imagem de demonstração:
  <img width="1340" height="636" alt="image" src="https://github.com/user-attachments/assets/d7e8bf72-031e-4496-a4d1-b9f2e5f5282d" />
* Obs: Pedro foi triado primeiro por ter chegado primeiro na fila, porém a prioridade dele é inferior comparada a prioridade de João, que tem maior urgência, e isso é confirmado quando se consulta a lista dos pacientes por prioridade, veja aqui:

  <img width="368" height="197" alt="image" src="https://github.com/user-attachments/assets/7d8eaaa1-4d42-46dd-b50b-27edf8c9626a" />

* Pelo fato de João ter uma prioridade maior, ele passou na frente de Pedro.

## Persistência dos dados em JSON.

* O sistema conta com uma persistência de dados feita em JSON, sustentada em três arquivos
  > Arquivo da persistência da Fila (FIFO)
  
  > Arquivo da persistência de Clientes Cadastrados
  
  > Arquivo da persistência da HeapMax

  * O Arquivo de persistência da Fila (FIFO) salva os clientes que estão na Fila para serem triados
  * O Arquivo de persistência dos Clientes Cadastrados salva os clientes que foram cadastrados no sistema no momento inicial do atendimento na fila por ordem de chegada, guardando as informações dos clientes para que possam ser consultadas, como o nome, CPF e endereço.
  * O Arquivo de persistência do Heap guarda os clientes que foram triados de acordo com sua prioridade.

  ### Como as classes FIFO e Heap se conectam para que a persistência de prioridade capte aquele cliente exato cadastrado e salvar sua prioridade no sistema?

  Um dos problemas surgidos durante a criação do sistema era como os dados dos clientes iam se ligar para se referenciar a aquele exato cliente, e primeiro começa com as classes:

  * Quando inicia um atendimento, e cadastra um cliente, preenchendo suas informações, como por exemplo:
    > Nome: Maria
    > CPF: 12345678910
    > Endereço: Rua 123

    Ele salva no arquivo de persistência da Fila (FIFO), somente o nome do cliente



