import xml.sax
class Handler(xml.sax.ContentHandler):
  def __init__(self):
    self.CurrentData = ""
    self.user = '';
    self.url = '';
    self.password = ''
    self.param = ''

  def startElement(self,tag,attr):
    self.CurrentData = tag
    print('starttag:',tag)
  def endElement(self,tag):
    print('endtag:',tag)

  def characters(self,content):
    print(self.CurrentData+'-content:'+content)

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = Handler()
parser.setContentHandler(handler)
parser.parse('../config/database.xml')
