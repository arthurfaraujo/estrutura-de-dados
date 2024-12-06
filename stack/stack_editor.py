from typing import Any
from stack.linked_stack import Stack
import os

class EditorError(Exception):
    def __init__(self, msg: str) -> None:
      super().__init__(msg)

class StackEditor:
    def __init__(self) -> None:
        self.__stacks: list[Stack] = [Stack()]
        self.__selected: int = 0
    
    @property
    def selected(self) -> int:
        return self.__selected
    
    @selected.setter
    def selected(self, value: int) -> None:
        if value > 0 and value <= len(self.__stacks):
            self.__selected = value - 1
        else:
          raise EditorError('invalid index')        

    def __create(self) -> None:
        self.__stacks.append(Stack())
      
    def __clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self) -> None:
        self.__menu()

    def __menu(self) -> None:
        while True:
            self.__clear()
            print('Editor de pilhas v1.0')
            print('=' * 35)

            print(f'Pilha selecionada: {
                  self.__selected + 1} de {self.__size()}')
            print(self.__stacks[self.__selected])
            print('=' * 35)

            print('(e) Empilhar')
            print('(d) Desempilhar')
            print('(t) Tamanho')
            print('(o) Obter topo')
            print('(v) Pilha vazia?')
            print('(r) Criar pilha')
            print('(n) Inverter pilha')
            print('(z) Esvaziar pilha')
            print('(c) Concatenar pilhas')
            print('(m) Escolher outra pilha')
            print('(n) Conversão dec/bin pilha')
            print('(s) Sair')
            print('=' * 35)

            escolha = input("Insira sua opção: ").strip()
            
            match escolha:
              case 'e':
                self.__stacks[self.__selected].push(int(input('Digite o valor do novo nó: ')))
              case 'd':
                print('Valor removido: ', self.__stacks[self.__selected].pop())
                input('Continuar? (enter)')
              case 't':
                print('Tamanho da pilha: ', len(self.__stacks[self.__selected]))
                input('Continuar? (enter)')
              case 'o':
                print('Topo da pilha: ', self.__stacks[self.__selected].peek())
                input('Continuar? (enter)')
              case 'v':
                print('Pilha vazia? ', 'Sim' if self.__stacks[self.__selected].is_empty() else 'Não')
                input('Continuar? (enter)')
              case 'r':
                self.__create()
              case 'm':
                self.selected = int(input(f'Pilha desejada de 1 a {len(self.__stacks)}: '))
              case _:
                raise EditorError('invalid option')
            
            

    def __size(self) -> int:
        return len(self.__stacks)
