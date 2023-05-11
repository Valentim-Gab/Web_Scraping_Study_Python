import re
import utils.json_builder as json_builder
import connection.connect_web as connect_web
import utils.notifier as notifier

     
def main():
    global name
    bs = connect_web.scraping_url('https://books.toscrape.com/')
    regex = re.compile(r'<h3><a href=".*"(\s+)?title="(.+?)">(.+?)<\/a><\/h3>')
    regex_price = r'((\w*_)?)price_\w+'
    json_file = ''
    
    try:
        titles = bs.findAll('article', {'class': 'product_pod'})

        for title in titles:
            h3_element = title.find('h3')

            if regex.match(str(h3_element)):
                a_element = h3_element.find('a')
                
                if a_element and 'title' in a_element.attrs:
                    name = a_element['title']
                else:
                    print("Atributo 'title' não encontrado.")
                         
            price = title.find('p', {'class': re.compile(regex_price)}).text
            price = str(price).lstrip('£')
            json_file += json_builder.add_object_to_json(name, price)
            
    except AttributeError:
        notifier.notify('Tag não encontrada')
    else:
        json_file = json_file.rstrip(',\n')
        json_file = f'[\n{json_file}\n]'
        
        json_builder.save_json_file(json_file)


if __name__ == '__main__':
    main()
