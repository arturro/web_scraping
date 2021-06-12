from pprint import pformat
from datetime import datetime
import logging
import os
import requests
from lxml import etree, html

from django.core.management.base import BaseCommand, CommandError
from lxml.etree import ParserError

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Pobiera wyniki z lotto'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--dry_run', type=str, help='debug mode/only dry run.', )
        parser.add_argument('-f', '--file', type=str, help='parse content from file', )
        parser.add_argument('-u', '--url', type=str,
                            help='url for example: https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2021-06-09,10', )

    def _get_html_from_url(self, url):
        """
        Zwraca pobrana tresc z podanej strony
        """
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
        }
        self.data_src = f'url: {url}'

        try:
            log.debug(f'Rozpoczynam pobieranie danych: {self.data_src}')
            response = requests.get(url, headers=headers)
            log.debug(f'Rozpoczynam pobieranie danych: {self.data_src}')

            if response.status_code != 200:
                log.error(f'bład pobierania danych: {self.data_src}, status_code: {response.status_code}')
                raise CommandError(f'get_lotto_results failed, status_code: {response.status_code}')
            else:
                log.debug(f'Poprawnie pobrano dane: {self.data_src}')
            return response.content
        except requests.RequestException as exc:
            log.exception(f'bład pobierania danych ze strony: {self.data_src}')
            raise CommandError('get_lotto_results failed')
        except ParserError:
            log.exception(f'bład pobierania danych ze strony: {self.data_src}')
            raise CommandError('get_lotto_results failed')

    def _get_html_from_file(self, file):
        self.data_src = f'file: {file}'
        with open(file) as page_file:
            page_content = page_file.read()
        log.debug(f'Pobieram strone z: {file}')
        log.debug(page_content[:100])
        return page_content

    def _parse_date(self, date_str):
        """
        Parsuje string typu: 'Czw., 10.06.2021, godz. 21:50' do datetime
        """
        tmp = date_str.split(',')
        date_tmp = tmp[1].strip()
        hour_tmp = tmp[2][-5:]
        date_time_str = f'{date_tmp} {hour_tmp}'
        date_time_obj = datetime.strptime(date_time_str, '%d.%m.%Y %H:%M')
        log.debug(f'date_time_obj: {date_time_obj}')
        return date_time_obj

    def _parse_result_item(self, result_item):
        """
        Parsuje pojedynczy div z wynikiem, zwraca dict z nr losowania i wylosowane liczby
        """
        result = {}
        # log.debug(etree.tostring(result_item))
        result['number'] = result_item.xpath('.//p[@class="result-item__number"]/text()')[0]
        log.debug(pformat(result))
        result['items'] = [item.strip() for item in
                           result_item.xpath('.//div[@class="scoreline-item circle"]/text()')]
        return result

    def _parse_content(self, content):
        tree = html.fromstring(content)
        log.debug(f'parsuje strone: {self.data_src}')

        game_main_boxes = tree.xpath('//div[@class="game-main-box skip-contrast"]')
        for game_main_box in game_main_boxes:
            # log.debug(game_main_box)
            # log.debug(etree.tostring(game_main_box))
            date_text = game_main_box.xpath('.//p[@class="sg__desc-title"]/text()')
            if date_text:
                date_time_obj = self._parse_date(date_text[0])
            else:
                log.error('Nie moge sparsowac daty')

            result_items = game_main_box.xpath('.//div[@class="result-item"]')
            log.debug(f'result_items: {result_items}')
            for result_item in result_items:
                log.debug(f'result_item: {result_item}')
                result_data = self._parse_result_item(result_item)
                result_data['date'] = date_time_obj
                log.debug(pformat(result_data))
                break

    def handle(self, *args, **options):
        # https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2021-06-09,10
        self.default_url = 'https://www.lotto.pl/lotto/wyniki-i-wygrane'
        self.test_file = os.path.join('lotto', 'lotto.html')

        self.url = options['url']
        self.file = options.get('file', self.test_file)
        self.dry_run = options['dry_run']
        log.debug(f'self.url: {self.url}')
        log.debug(f'self.file: {self.file}')
        log.debug(f'self.dry_run: {self.dry_run}')
        self.data_src = ''

        try:
            if self.url:
                content = self._get_html_from_url(self.url)
            elif self.file:
                content = self._get_html_from_file(self.file)
            else:
                content = self._get_html_from_file(self.test_file)

            self._parse_content(content)

        except ParserError:
            log.exception(f'bład pobierania danych ze strony: {self.data_src}')
            raise CommandError('get_lotto_results failed')

        except Exception as exc:  # reszta błedów...
            log.exception('bład pobierania danych z lotto')
            raise CommandError('get_lotto_results failed')
        log.info(f'Poprawnie wczytano dane ze strony {self.data_src}')
        self.stdout.write(self.style.SUCCESS('Successfully get lotto results'))
