from win10toast import ToastNotifier


def notify(message):
    toaster = ToastNotifier()
    icon_path = "assets/icons/esfera.ico"

    try:
        if toaster.show_toast(title='Análise de Livros', msg=message, icon_path=icon_path, duration=5):
            print('\n' + message + '\n')
        else:
            print('Ocorreu um erro ao notificar o usuário')
    except Exception as e:
        print("Erro ao exibir notificação:", e)

