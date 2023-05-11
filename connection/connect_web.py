from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import sys
import utils.notifier
sys.path.append('../')

notifier = utils.notifier


def scraping_url(site_url):
    req = Request(
        url=site_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    try:
        page = urlopen(req).read()
    except HTTPError:
        notifier.notify('Erro ao se comunicar com a página')
    except URLError:
        notifier.notify('Servidor não encontrado')
    else:
        return BeautifulSoup(page, 'html.parser')
