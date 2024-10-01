#  Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. O formulário deve incluir três campos: 
# um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem. Após o usuário preencher esses campos, deve haver um 
# botão de envio. Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando 
# que o formulário foi enviado com sucesso.

import flet as ft

def main(page: ft.Page):
    page.title = 'aplicação de formulário'

    name_input = ft.TextField(label='Informe seu nome', autofocus=True)
    email_input = ft.TextField(label='Informe seu e-mail')
    message_input = ft.TextField(label='Informe a mensagem', multiline=True)

    # Para mensagem de confirmação
    confir_message = ft.Text()

    def clickMenssage(e):
        if name_input.value and email_input.value and message_input.value:
            confir_message.value = 'Formulário enviado com sucesso'
            confir_message.color = 'green'
            # limpar campo
            name_input.value = ''
            email_input.value = ''
            message_input.value = ''
        else:
            confir_message.value = 'Favor, preencha o campo corretamente.'
            confir_message.color = 'red'

        page.update()

    button = ft.ElevatedButton('Clique', on_click=clickMenssage)
   

    element = ft.Column(
        controls=[
            name_input,
            email_input,
            message_input,
            button, 
            confir_message
        ]
    )

    page.add(element)

ft.app(target=main)