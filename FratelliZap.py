# Sites / Sistemas / Aplicativos
# Flask
# Django
# FastAPI
# Flet -> Python -> visual (frontend) / logica (backend)
# Kivy

# Framework -> biblioteca com regras específicas


import flet as ft

def main(pagina: ft.Page):
    pagina.title = "FratelliZap"
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função chamada quando uma nova mensagem é recebida pelo túnel
    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    # Inscreve a função acima para receber mensagens do túnel
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # Função chamada quando o botão de enviar mensagem é clicado
    def enviar_mensagem(evento):
        mensagem = f"{campo_nome.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()

    # Criar campo de mensagem
    campo_mensagem = ft.TextField(label="Escreva sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Criar área do chat
    chat = ft.Column()

    # Criar linha de mensagem
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])

    # Função chamada quando o botão de entrar no chat é clicado
    def entrar_chat(evento):
        pagina.pubsub.send_all(f"{campo_nome.value} entrou no chat")
        janela.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.add(linha_mensagem)
        pagina.update()

    # Campo para digitar o nome
    campo_nome = ft.TextField(label="Digite o seu nome", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    # Criar janela de diálogo
    janela = ft.AlertDialog(
        title=ft.Text("Bem-vindo ao Hashzap"),
        content=campo_nome,
        actions=[botao_entrar],
        on_dismiss=lambda e: print("Diálogo fechado")
    )

    # Função para abrir o diálogo
    def abrir_dialog(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()

    # Botão para iniciar o chat
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

    # Adicionar o botão de iniciar chat à página
    pagina.add(botao_iniciar)

# Executar o aplicativo
ft.app(target=main, port=8080)

