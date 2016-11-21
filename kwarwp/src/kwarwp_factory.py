"""
############################################################
Vitallino - Criador de Jogos Simplificado
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/01/09  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.1 $
:Home: `Labase http://labase.nce.ufrj.br/`__
:Copyright: 2011, `GPL http://is.gd/3Udt`__. 
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.1 $Revision$"[10:-1]
__date__    = "2013/01/09 $Date$"
"""
ND = {}


def _logger(*a):
    print(a)


if '__package__' not in dir():
    import svg
    from html import TEXTAREA

    logger = log
    pass
else:
    logger = _logger
    pass

REPO = '/lib/image/%s'


def noop(nop=''):
    pass


HANDLER = {"_NOOP_": 'noop()'}
VKHANDLER = dict([(k, noop) for k in range(32, 40)])


def uuid():
    r = jsptrand()
    return '%i' % (JSObject(jsptdate).getTime() * 1000 + r)


def jshandler(event):
    code = event.keyCode
    if code in VKHANDLER:
        VKHANDLER[code]()
        # alert(event.keyCode)


if '__package__' not in dir():
    doc.onkeypress = jshandler


def eventify(owner):
    # alert('owner :'+owner)
    HANDLER[owner]()


class Dialog:
    def __init__(self, gui, img=REPO % 'paje.png', text='', act=lambda x: None):
        self._rect = gui.rect(0, 100, 800, 440, style={
            'fillOpacity': '0.7', 'fill': 'black'})
        self._area = gui.textarea(text, 80, 130, 700, 400)
        self._imag = gui.image(img, 2, 80, 32, 32)
        self._imag.addEventListener('click', self.action)
        self.act = act

    def hide(self):
        self._rect.style.visibility = 'hidden'
        self._area.style.visibility = 'hidden'
        self._imag.style.visibility = 'hidden'
        # self._area.setVisible(self._area,False)

    def show(self):
        self._rect.style.visibility = 'visible'
        self._area.style.visibility = 'visible'
        self._imag.style.visibility = 'visible'
        # self._area.setVisible(self._area,True)

    def get_text(self):
        return self._area.value

    def set_text(self, text):
        self._area.value = text

    def action(self, event):
        self.hide()
        self.act(self)


class GUI:
    def __init__(self, panel, data):
        self.args = {}
        self.panel = panel
        self.data = data
        for child in panel:  # iteration on child nodes
            panel.remove(child)

    def get_args(self):
        args = self.args
        for key, value in self.args.items():
            args[key] = 'eventify(\\"%s\\")' % value
        self.args = {}
        p = '"'
        if len(args) != 0:
            args = ', ' + ','.join(['%s = %s%s%s' % (k, p, v, p)
                                    for k, v in args.items()])
        else:
            args = ''
        return args

    def textarea(self, text, x, y, w, h, style=None):
        if style is None:
            style = {}

        def dpx(d):
            return '%spx' % d

        attrs = dict(position='absolute', top=dpx(y), left=dpx(x),
                     width=dpx(w), height=dpx(h), color='navajowhite', border=1,
                     resize='none', background='transparent')
        attrs['top'] = y
        attrs = {'position': 'absolute', 'top': dpx(y), 'left': dpx(x),
                 'width': dpx(w), 'height': dpx(h), 'resize': 'none', 'borderColor': 'darkslategrey',
                 'color': 'navajowhite', 'border': 1, 'background': 'transparent'}
        # t = TEXTAREA(text, style = {'position' : 'absolute', 'top':'100px', 'left':'40px'})#attrs)
        t = TEXTAREA(text, style=attrs)
        # d_rect=gui.rect(10,100, 540, 240, style= {'fill-opacity':'0.2', 'fill':'black'})
        self.data <= t
        return t

    def dialog(self, text, img=REPO % 'paje.png', act=lambda x: None):
        t = Dialog(self, text=text, img=img, act=act)
        # t.setStyleAttribute('border',0)
        return t

    def remove(self, element):
        self.panel.removeChild(element)

    def text(self, text, x=150, y=25, font_size=22, text_anchor="middle",
             style=ND):
        element = svg.text(text, x=x, y=y,
                           font_size=font_size, text_anchor=text_anchor,
                           style=style)
        self.panel <= element
        return element

    def path(self, d, style=ND, onMouseOver="noop", onMouseOut="noop"):
        exec('element = svg.path(d=%s,style=%s%s)' % (
            str(d), str(style), self.get_args()))
        self.panel <= element
        return element

    def image(self, href, x=0, y=0, width=100, height=50):
        exec('element = svg.image(href="%s", x=%i, y=%i, width=%i, height=%i%s)' % (
            href, x, y, width, height, self.get_args()))
        self.panel <= element
        return element

    def rect(self, x=0, y=0, width=100, height=50, style=ND):
        exec('element = svg.rect(x=%i, y=%i, width=%i, height=%i,style=%s%s)' % (
            x, y, width, height, str(style), self.get_args()))
        self.panel <= element
        return element

    def handler(self, key, handle):
        VKHANDLER[key] = handle

    def avatar(self):
        return Avatar(self)

    def _decorate(self, handler, **kw):
        self.args = {}  # kw #dict(kw)
        # alert(' '.join([k for k,v in kw.items()]))
        for key, value in kw.items():
            handler_id = uuid()
            HANDLER[handler_id] = handler
            self.args[key] = handler_id
            # alert(key+':'+ self.args[key])
            x = self.args
        # alert(' ,'.join([k+':'+v for k,v in x.items()]))
        return self

    def click(self, handler):
        self._decorate(handler, onClick=handler)
        return self

    def over(self, handler):
        self._decorate(handler, onMouseOver=handler)
        return self


class Avatar:
    def _load_images(self, img, gui):
        cardinames = [c for c in 'nesw']
        self.images = []
        for direction in cardinames:
            line = []
            for step in range(3):
                im = gui.image(href=img % (direction, step),
                               x=100, y=100, width=32, height=32)
                im.setAttribute("visibility", 'hidden')
                line.append(im)
            self.images.append(line)
        self.heading = 1
        self.current = 0

    def _show(self):
        self.current = (self.current + 1) % 3
        self.avatar.setAttribute("visibility", 'hidden')
        self.avatar = self.images[self.heading][self.current]
        self.avatar.setAttribute('x', self.x)
        self.avatar.setAttribute('y', self.y)
        self.avatar.setAttribute("visibility", 'visible')

    def move(self, x, y):
        self.x, self.y = x, y
        self._show()

    def get_direction(self):
        return self.heading

    def go_left(self):
        self.heading = (self.heading - 1) % 4
        self._show()

    def go_right(self):
        self.heading = (self.heading + 1) % 4
        self._show()

    def __init__(self, gui):
        VKHANDLER[37] = self.go_left
        VKHANDLER[39] = self.go_right
        logger('Avatar,init')
        self.x, self.y = 0, 0
        self.heading = 0
        self._load_images(REPO % 'smkp-%s0%d.gif', gui)
        self.avatar = self.images[self.heading][self.current]


class NullAvatar:
    def move(self, x, y):
        pass

    def setAttribute(self, a, b):
        pass

    def __init__(self, *a):
        pass


NULLAVATAR = NullAvatar()


class Sprite:
    def _show(self, x, y):
        lx, ly = x, y
        self.avatar.setAttribute('x', lx)
        self.avatar.setAttribute('y', ly)
        self.avatar.setAttribute("visibility", 'visible')

    def move(self, x, y):
        # self.place, self.x, self.y = place, x, y
        # mx, my = place.get_real_position(x=self.x,y=self.y)
        logger('%s,spr_move, real %d %d' % (self, x, y))
        self._show(x, y)

    def __init__(self, gui, img, place, x, y):
        if not (img is None):
            self.avatar = gui.image(href=REPO % img,
                                    x=100, y=100, width=32, height=32)
            mx, my = place.get_real_position(x=x, y=y)
            self.move(mx, my)
        else:
            self.avatar = NULLAVATAR


class NullSprite:
    def move(self, place, x, y):
        pass

    def __init__(self, *a):
        pass
