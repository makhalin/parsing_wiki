def main():
    counter = []
    i = 0
    n = 10
    k = 0
    while i < n:
        counter.append(find_filosofia())
        if counter[i] != -1:
            k += 1
        i += 1
    print(counter)
    print('%f%%' % ((k * 100) / n))

def find_filosofia():
    from urllib.request import urlopen, build_opener
    from bs4 import BeautifulSoup
    import re    
    from time import time, sleep

    start = time()
    counter = 0
    opener = build_opener()
    link = 'http://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    link_end = 'http://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F'
    opener.addheaders = [('User-agent', 'Mozilla/7.0')]
    infile = opener.open(link)
    page = infile.read()
    soup = BeautifulSoup(page)
    titles = []
    try:
        if str(soup.title.string) == 'Философия — Википедия':
            return 0
        while link != link_end:
            if str(soup.title) not in titles:
                titles.append(str(soup.title))
                counter += 1
            else:
                counter = -1
                break
            block = soup.find(id='mw-content-text')
            block_str = str(block)
            for i in block.findAll('div', {'class':['dablink', 'thumb', 'infobox', 'metadata']}):
                block_str = block_str.replace(str(i), '')
            for i in block.findAll('table'):
                block_str = block_str.replace(str(i), '')
            for i in block.findAll('a', {'class':'new'}):
                block_str = block_str.replace(str(i), '')
            for i in block.findAll('sup', {'class':'reference'}):
                block_str = block_str.replace(str(i), '')
            for i in block.findAll('span', {'class':['ref-info', 'editsection']}):
                block_str = block_str.replace(str(i), '')
            for i in block.findAll('i'):
                block_str = block_str.replace(str(i), '')
            block = BeautifulSoup(re.sub('[^_]\(.*?\)', '', block_str))
            link = ''.join(['http://ru.wikipedia.org', block.find('a').get('href')])
            if str(soup.title.string) == 'Государство — Википедия':
                link = 'http://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BF%D0%B5%D1%82%D0%B5%D0%BD%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C'
                counter += 1
            infile = opener.open(link)
            page = infile.read()
            soup = BeautifulSoup(page)    
            
            finish = time()
            if (finish - start) < 0.5:
                sleep(0.5 - (finish - start))            
    except:
        counter = -1
    return counter

if __name__ == "__main__":
    main()
