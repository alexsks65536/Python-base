'''
    Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
    (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации вида:
    (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
    raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
    parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
    Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
'''
import re

raw = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open("nginx_log.txt", encoding='utf-8') as f:
    for str in f:
        print(re.findall(raw, str))
