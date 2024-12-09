from typing import Any
from stack.linked_stack import Stack
from stack.linked_stack import StackError
import os


def decToBin(num: int) -> None:
    bins = Stack()

    while True:
        if num // 2 == 1:
            bins.push(num % 2)
            bins.push(1)
            break
        else:
            bins.push(num % 2)
            num = num // 2

    for b in bins:
        print(b, end='')
    print()


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

    def get_stack(self, index: int) -> Stack:
        index -= 1
        if index >= 0 and index < len(self.__stacks):
            return self.__stacks[index]
        else:
            raise IndexError('invalid index')

    def get_selected_stack(self) -> Stack:
        return self.__stacks[self.__selected]

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
            print('(b) Conversão dec/bin pilha')
            print('(i) Inverter string usando pilha')
            print('(p) Verificar palíndromo')
            print('(s) Sair')
            print('=' * 35)

            option = input("Insira sua opção: ").strip()

            try:
                self.resolve_option(option)
            except StackError as se:
                print('Erro: ', se)
            except EditorError as ee:
                print('Erro: ', ee)
            except ValueError as ve:
                print('Erro: ', ve)

            input('Pressione enter: ')

    def resolve_option(self, option: str) -> None:
        match option:
            case 'e':
                self.get_selected_stack().push(
                    int(input('Digite o valor do novo nó: ')))

            case 'd':
                print('Valor removido: ',
                      self.get_selected_stack().pop())

            case 't':
                print('Tamanho da pilha: ', len(
                    self.get_selected_stack()))

            case 'o':
                print('Topo da pilha: ',
                      self.get_selected_stack().peek())

            case 'v':
                print(
                    'Pilha vazia? ', 'Sim' if self.get_selected_stack().is_empty() else 'Não')

            case 'r':
                self.__create()

            case 'n':
                self.get_selected_stack().invert()

            case 'z':
                self.get_selected_stack().empty()

            case 'c':
                print(
                    'Como desejar concatenar:\n(a) Alterando a selecionada\n(g) Gerando uma nova')

                if (choice := input("Insira sua opção: ").strip()) == 'a':
                    stack2 = self.get_stack(
                        int(input(f'Segunda pilha para concatenar de 1 a {len(self.__stacks)}: ')))
                    self.get_selected_stack().concat(stack2)

                elif choice == 'g':
                    stack2 = self.get_stack(
                        int(input(f'Segunda pilha para concatenar de 1 a {len(self.__stacks)}: ')))
                    new_stack = Stack.join(self.get_selected_stack(), stack2)
                    print('Pilha concatenada: ', new_stack)
                    self.__stacks.append(new_stack)

            case 'm':
                self.selected = int(
                    input(f'Pilha desejada de 1 a {len(self.__stacks)}: '))

            case 'b':
                decToBin(int(input('Inteiro para converter: ')))

            case 's':
                choice = input('Deseja mesmo sair (s ou n)? ')

                if choice == 's':
                    self.__clear()
                    exit()

                if choice != 'n':
                    raise EditorError('invalid option')

            case 'i':
                string = input('String para inverter: ')
                stack = Stack()

                for char in string:
                    stack.push(char)

                for char in stack:
                    print(char, end='')
                print()

            case 'p':
                user_string = ''.join([s for s in input('String para testar palídromo: ') if s.isalpha()])
                inverted = Stack()

                for char in user_string.lower():
                    if char.isalpha():
                        inverted.push(char)

                string = ''.join([s for s in inverted])

                print(f'{user_string} {'é palíndromo' if string ==
                      user_string else 'não é palíndromo'}')

            case _:
                raise EditorError('invalid option')

    def __size(self) -> int:
        return len(self.__stacks)
