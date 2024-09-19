# Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. A interface da aplicação deve incluir um campo de entrada 
# de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na 
# tela, mostrando todas as tarefas que foram incluídas até o momento. A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado

import flet as ft

# Criação da função
def main(page: ft.Page):
    page.title = "Aplicação blocos de notas"

    texto_input = ft.TextField(label='Informe o que deseja!')
    lista_textos = ft.Column()

    def adicionar_texto(e):
        if texto_input.value:
            # Adiciona o texto informado à lista
            lista_textos.controls.append(ft.Text(texto_input.value))
            # Limpa o campo de texto
            texto_input.value = "" 
            # Atualiza a página 
            page.update()  

    # Criação do botão
    botao_adicionar = ft.ElevatedButton("Clique para adicionar", on_click=adicionar_texto)

    tela = ft.Column(
        controls=[
            texto_input,
            botao_adicionar,
            lista_textos
        ]
    )

    # Tudo que vai ser adicionado em tela
    page.add(tela)

# Iniciando a função
ft.app(target=main)