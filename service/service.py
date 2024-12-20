from queue.linked_queue import Queue

class Service:
  def __init__(self) -> None:
    self.__waiting_list = Queue()
    self.__service_list = Queue()
    self.__current_token = 1
    
  def print_screen(self) -> None:
    screen = 'Clínica médica - Atendimento\n============================'
    screen += '\n1. Obter senha de atendimento'
    screen += '\n2. Chamar paciente p/ cadastro'
    screen += '\n3. Chamar paciente p/ consultório'
    screen += '\n4. Consultar a posição atual'
    screen += '\n5. Painel de atendimento'
    screen += '\n6. Sair'
    print(screen)
  
  def get_token(self) -> str:
    token = self.__current_token
    self.__current_token += 1
    
    return f'N{token:03d}'
    
ser = Service()
ser.print_screen()

print(ser.get_token())
    