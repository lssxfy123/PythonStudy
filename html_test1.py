#html解析
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.Events = {}
        self._tag = ''
        self._counter = 0    

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs and attrs[0][0] == 'class' and attrs[0][1] == 'event-title':
            self._tag = 'title'
      
        if tag == 'time' and attrs and attrs[0][0] == 'datetime':
            self._tag = 'datetime'

        if tag == 'span' and attrs and attrs[0][0] == 'class' and attrs[0][1] == 'event-location':
            self._tag = 'location'

    #def handle_endtag(self, tag):
        #print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        if self._tag == 'title':
            self.Events[self._counter] = {'title' : data.strip('\n')}

        if self._tag == 'datetime':
            self.Events[self._counter]['time'] = data.strip('\n')

        if self._tag == 'location':
            self.Events[self._counter]['location'] = data.strip('\n')
            self._counter += 1
        self._tag = ''

    
    def printEvents(self):
        for k in self.Events:
            print('title : %s Time : %s Location %s' % (self.Events[k]['title'], self.Events[k]['time'], self.Events[k]['location']))

    #def handle_comment(self, data):
     #   print('<!--', data, '-->')

    #def handle_entityref(self, name):
      #  print('&%s' % name)

    #def handle_charref(self, name):
     #   print('&#%s' % name)


def getHtml(url):
    req = request.Request(url)
    with request.urlopen(req) as f:
        #data = f.read();
        #print('Status: ', f.status, f.reason)
        #for k, v in f.getheaders():
        #    print('%s : %s' % (k, v))
        #print('Data : ', data.decode('utf-8'))
        return f.read().decode('utf-8')


if __name__ == '__main__':
    #getHtml('https://www.python.org/events/python-events/')
    parser = MyHTMLParser()
    parser.feed(getHtml('https://www.python.org/events/python-events/'))
    parser.printEvents()

