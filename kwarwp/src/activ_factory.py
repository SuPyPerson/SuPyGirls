"""
############################################################
Memit - Serious Game in cavalier projection for memetics
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/03/17  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.1 $
:Home: `Labase http://labase.selfip.org/`__
:Copyright: 2011, `GPL http://is.gd/3Udt`__. 
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.1 $Revision$"[10:-1]
__date__    = "2013/03/17 $Date$"
"""

REPO = 'public/image/%s'

def _logger(*a):
    print(a)
        

if not '__package__' in dir():
    from html import IMG
    from html import TEXTAREA
    logger = log
    pass
else:
    logger = _logger
    pass

def noop(nop=''):
    pass
HANDLER = {"_NOOP_":'noop()'}
VKHANDLER = dict([(k,noop) for k in range(32,40)])

def uuid():
    r = jsptrand()
    return '%i'%(JSObject(jsptdate).getTime()*1000+r)

def jshandler(event):
    code = event.keyCode
    if code in VKHANDLER:
        VKHANDLER[code]()
    #alert(event.keyCode)
if not '__package__' in dir():
    doc.onkeypress=jshandler

def eventify(owner):
    #alert('owner :'+owner)
    HANDLER[owner]()
    
TRANS = "translate rotate scale skewX skewY matrix".split()

EVENT = ("onfocusin onfocusout onactivate onload onclick onkeydown onkeyup" + \
    " onmousedown onmouseup onmouseover onmousemove onmouseout").split()



class Dialog:
    def __init__(self, gui, img = REPO%'paje.png',  text = '', act = lambda x:None):
        self._rect=gui.rect(0,100, 800, 440, style= {
            'fillOpacity':'0.7', 'fill':'black'})
        self._area=gui.textarea(text,80,130, 700, 400)
        self._imag=gui.image(img,2,80, 32, 32)
        self._imag.addEventListener('click', self.action)
        self.act= act
    def hide(self):
        self._rect.style.visibility = 'hidden'
        self._area.style.visibility = 'hidden'
        self._imag.style.visibility = 'hidden'
        #self._area.setVisible(self._area,False)
    def show(self):
        self._rect.style.visibility = 'visible'
        self._area.style.visibility = 'visible'
        self._imag.style.visibility = 'visible'
        #self._area.setVisible(self._area,True)
    def get_text(self):
        return self._area.value
    def set_text(self, text):
        self._area.value = text
    def action(self, event):
        self.hide()
        self.act(self)

class Form:
    """ Collects demographic info and send results to the server
    """
    def __init__(self,gui=None):
        self._build_form(gui)
    def _build_form(self, gui):
        self.form = gui.rect(x=100,y=100, width=600,height=400,
                 style=dict(fill='navajowhite', fillOpacity= 0.8))
        logger('b form a')
        self.form.addEventListener('click', self._submmit)

    def _request_form(self, gui):
        logger('b form a')
        req = ajax()
        logger('b form')
        req.on_complete = self._on_complete
        req.set_timeout(8,self._err_msg)
        req.open('GET','/api/',True)
        #req.set_header('content-type', 'application/x-www-form-urlencoded')
        req.set_header("Content-Type","text/plain; charset=utf-8")
        req.send()
    def _on_complete(self,req):

        if req.status==200 or req.status==0:
            logger('req %s req text %s'%(dir(req),req.header))
            return
            ids = req.text.split('name="_xsrf"')[1][:200].split('"')
            logger('xsrf %s'%(ids))#,ids[7]))
        else:
            logger('error %s'%req.text)
    def _err_msg(self):
        logger('timeout after 8s')
    def _submmit(self,ev):
        self.form.setAttribute("visibility",'hidden')
        logger('submmit')
    '''
    '''
   

 
class GUI:
    def __init__(self,panel,data):
        self.args = {}
        self.panel =panel
        self.data = data
        for child in panel: # iteration on child nodes
                panel.remove(child)
        
    def get_args(self):
        args = self.args
        for key, value in self.args.items():
            args[key]= 'eventify(\\"%s\\")'%value
        self.args = {}
        p='"'
        if len(args) != 0:
            args = ', '+','.join(['%s = %s%s%s'%(k,p,v,p)
                                     for k, v in args.items()])
        else:
            args = ''
        return args
    def _get_kwargs(self,kw):
        trans =' '.join(
            [key + ['(%s)','%s'][isinstance(value, tuple)]%str(value)
             for key, value in kw.items() if key in TRANS])
        return trans and ', transform="%s"'%trans or ''
            
    def request(self, url = '/rest/studio/jeppeto?type=2', action = None, data=''):
        req = ajax()
        req.on_complete = action
        req.set_timeout(8,self._err_msg)
        req.open('GET',url,True)
        req.set_header("Content-Type","text/plain; charset=utf-8")
        req.send()
        pass

    def send_data(self, url = None, data = '', action = None, error = None):
        pass

    def textarea(self,text,x,y,w,h,style= {}):
        def dpx(d):
            return '%spx'%d
        attrs = dict (position = 'absolute', top=dpx(y), left=dpx(x) ,
            width=dpx(w) , height=dpx(h), color = 'navajowhite', border= 1,
            resize = 'none', background = 'transparent')
        attrs['top']= y
        attrs = {'position' : 'absolute', 'top':dpx(y), 'left':dpx(x),
            'width':dpx(w) , 'height':dpx(h), 'resize' : 'none','borderColor': 'darkslategrey',
            'color': 'navajowhite', 'border': 1, 'background' : 'transparent' }
        #t = TEXTAREA(text, style = {'position' : 'absolute', 'top':'100px', 'left':'40px'})#attrs)
        t = TEXTAREA(text, style = attrs)
        #d_rect=gui.rect(10,100, 540, 240, style= {'fill-opacity':'0.2', 'fill':'black'})
        self.data <= t
        return t
    
    def dialog(self, text, img = REPO%'paje.png', act = lambda x:None):
        t = Dialog(self,text=text, img=img, act=act)
        #t.setStyleAttribute('border',0)
        return t
    def remove(self, element):
        self.panel.removeChild(element)
    def text(self, text,x=150,y=25, font_size=22,text_anchor="middle",
      style= {}):
      element = svg.text(text,x=x,y=y,
      font_size=font_size,text_anchor=text_anchor,
      style=style)
      self.panel <= element
      return element
  
    def path(self, d,style={}, onMouseOver="noop",  onMouseOut="noop"):
        exec('element = svg.path(d=%s,style=%s%s)'%(
            str(d),str(style),self.get_args()))
        self.panel <= element
        return element
  
    def image(self,  href, x=0, y=0, width=100, height=50, **kw):
        exec('element = svg.image(href="%s", x=%i, y=%i, width=%i, height=%i%s)'%(
            href, x, y, width, height,self._get_kwargs(kw)))
        self.panel <= element
        return element
  
    def ellipse(self,  href, cx=0, cy=0, rx=100, ry=50, style= {}, **kw):
        exec('element = svg.ellipse(cx=%i, cy=%i, rx=%i, ry=%i,style=%s%s)'%(
            cx, cy, rx, ry,str(style),self.get_args()))
        self.panel <= element
        return element
  
    def rect(self, x=0, y=0, width=100, height=50,style={}):
        exec('element = svg.rect(x=%i, y=%i, width=%i, height=%i,style=%s%s)'%(
            x, y, width, height,str(style),self.get_args()))
        self.panel <= element
        return element
    
    def handler(self, key, handle):
        VKHANDLER[key] = handle
    def avatar(self):
        return Avatar(self)
    
    def _decorate(self, handler, **kw):
      self.args = {} #kw #dict(kw)
      #alert(' '.join([k for k,v in kw.items()]))
      for key, value in kw.items():
          handler_id = uuid()
          HANDLER[handler_id] = handler
          self.args[key] = handler_id
          #alert(key+':'+ self.args[key])
          x =self.args
      #alert(' ,'.join([k+':'+v for k,v in x.items()]))
      return self
    def click(self,handler):
      self._decorate(handler, onClick=handler)
      return self
    def over(self,handler):
      self._decorate(handler, onMouseOver=handler)
      return
