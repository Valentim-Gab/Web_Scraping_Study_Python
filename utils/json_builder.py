import os
import json
import sys
import utils.notifier

sys.path.append('../')

notifier = utils.notifier


def add_object_to_json(name, price):
    json_element = '\t{' + f'\n\t\t"name": "{name}",\n\t\t"price": {price}' + '\n\t},\n'

    return json_element


def save_json_file(json_file):
    try:
        if os.path.exists('data.json'):
            with open('data.json', 'r') as file:
                old_json = json.load(file)

            new_json = json.loads(json_file)
            simulation = True

            for item_new in new_json:
                # Simulação será feita aqui:
                if simulation:
                    item_new['price'] = 60.00
                    simulation = False

                for item_old in old_json:
                    if (item_new['name'] == item_old['name']
                            and item_new['price'] != item_old['price']):
                        notifier.notify(f'O preço do produto {item_new["name"]}'
                                        f'\nAlterou de: £{item_old["price"]:.2f} para £{item_new["price"]:.2f}.')

        with open('data.json', 'w') as file:
            file.write(json_file)

    except FileNotFoundError:
        notifier.notify('Arquivo JSON não encontrado.')
    except PermissionError:
        notifier.notify('Acesso ao arquivo não autorizado.')
    except json.JSONDecodeError:
        notifier.notify('Ocorreu um erro na decodificação JSON.')
    except Exception:
        notifier.notify('Ocorreu um erro.')
    else:
        notifier.notify('Json salvo com sucesso!\nO Scraping foi finalizado.')
