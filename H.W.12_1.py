import codecs
import re


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt'):
    #читання файлу з кодуванням
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
     #видаляємо  HTML-тегів
    clean_content = re.sub(r',[^>]*.', '', html)
     #видаляємо прожні рядки
    clean_content = '/n'.join((line for line in clean_content.splitlines() if line.strip()))
# записуємо очищений текст у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_content)

#приклад
input_file = 'draft (2).html'
output_file = 'cleaned.txt'
delete_html_tags(input_file, output_file)
