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
REPO = '/lib/image/%s'
WIND = [(0, -1), (1, 0), (0, 1), (-1, 0)]
NN, EE, SS, WW = WIND


def inherit(base, child):
    overriden, inherited = dir(child), dir(base)
    for member in inherited:
        if member not in overriden:
            setattr(child, member, getattr(base, member))
    # child.m =  str(child.__class__)
    return base


# class Entrance:
#    def __init__(self, place, x, y):
#        self.thing, self.x, self.y, self.m = place, x, y, str(self.__class__)

class Way:
    def __init__(self, avatar, place, x, y, me=None, **kw):
        # inherit(Entrance(place, x, y),self)
        self.avatar, self.place = avatar, place
        self.thing, self.x, self.y, self.m = place, x, y, me or self
        self._action = None

    def rebase(self, base):
        return None

    def get_position(self, x=0, y=0):
        return self.place.get_position(x=x, y=y)

    def _support(self):
        self.place = Way(None, self.place, self.x, self.y)

    def enter(self, entry, action, position=None):
        self._action, thing, x, y = action, self.thing, self.x, self.y

        def _move(x, y, entry, act=action, me=self.m):
            me.thing = entry.get_entry()
            print('%s._move, position %d %d thing %s' % (me, x, y, me.thing))
            act(self.x, self.y, me)

        pos = (x, y)
        if position is not None:
            position = pos
        thing.enter(entry, action=_move, position=position)
        print('%s.enter,thing %s self %s position %s' % (self.m, self.thing, self, position))

    def leave(self, entry, action, reverse=0):
        def _left(x, y, loc, act=action, me=self.m):
            me.thing = self.place
            act(x, y, loc)

        self.place.leave(entry, action=_left, reverse=reverse)

    def pushed(self, entry, action, position=None, reverse=0):
        self._action, thing, x, y = action, self.thing, self.x, self.y

        def _tpushed(x, y, entry, act=action, me=self.m):
            me.thing = entry.get_entry()
            print('%s._tpushed, position %d %d thing %s' % (me, x, y, me.thing))
            act(self.x, self.y, me)

        thing.pushed(entry, action=_tpushed, position=position, reverse=reverse)
        print('%s.enter,thing %s self %s position %s' % (self.m, self.thing, self, position))

    def push(self, entry, action, reverse=0):
        def _pusher_moved(x, y, loc, move_pusher=action, me=self.m):
            me.thing = self.place
            move_pusher(x, y, loc)

        print('%s.push entry %s lpos %d %d' % ('Place', entry, self.x, self.y))
        self.place.push(entry, action=_pusher_moved, reverse=reverse)


class Tar:
    def leave(self, thing, action, reverse=0):
        print('Youre STUCK!!!')

    def __init__(self, avatar, place, x, y, **kw):
        inherit(Way(avatar, place, x, y, me=self), self)


class Door:
    def __init__(self, avatar, place, x, y, **kw):
        inherit(Way(avatar, place, x, y, me=self), self)
        place.x, place.y = x, y


class Entry:
    def __init__(self, thing, entry, x, y):
        self.x, self.y, self.entry, self.thing = x, y, entry, thing

    def get_entry(self):
        return self.thing

    def get_direction(self):
        return self.entry.get_direction()

    def get_position(self):
        return self.x, self.y


class Trunk:
    def enter(self, entry, action, position=None):
        print('It is HEAVY!!')

    def pushed(self, entry, action, position=None, reverse=1):
        def _trunk_pushed(x, y, loc, move_pusher=action, me=self.m):
            self.x, self.y, self.thing = x, y, loc or self.thing
            self.place, previous_location = loc or self.place, self.place
            previous_location.thing = entry
            mx, my = self.thing.get_position(x=x, y=y)
            px, py = previous_location.get_position(x=x, y=y)
            print('trunk.pushed, me %s position %d %d  entry%s real %d %d' % (me, x, y, loc, mx, my))
            me.avatar.move(me, x, y)
            # move_pusher(px,py, previous_location)
            previous_location.place.enter(entry, action=move_pusher, position=position)

        theentry = Entry(self.m, entry, self.x, self.y)
        print('%s.pushed,thing %s entry %s position %s' % (
            self.m, self.thing, theentry, position))
        self.place.place.push(theentry, action=_trunk_pushed, reverse=reverse)

    def __init__(self, avatar, place, x, y, **kw):
        inherit(Way(avatar, place, x, y, me=self), self)
        self.avatar, self.place = avatar, place
        self.thing, self.x, self.y, self.m = place, x, y, self

    def rebase(self, base):
        place = Way(None, self, self.x, self.y)
        base[self.y][self.x] = place
        self.place, self.place.place = place, self.place


class Border:
    def enter(self, entry, action, position=None):
        print('Cant go this way!!')

    def push(self, entry, action, position=None):
        print('Cant go this way!!')

    def __init__(self, avatar, place, x, y, **kw):
        inherit(Way(avatar, place, x, y, me=self), self)
        self.thing, self.x, self.y, self.m = place, x, y, self
        self.place = Way(None, place, self.x, self.y)
        # self.avatar,self.place, self.x, self.y = avatar, place, x, y


class Actor:
    def get_entry(self):
        return self

    def get_direction(self):
        return self.avatar.get_direction()

    def get_position(self):
        return self.x, self.y

    def move(self, x, y, loc=None):
        self.x, self.y = x, y
        self.thing = loc or self.thing
        # print( 'actor,move, position thing %d %d %s'%(x, y, self.thing))
        avatar = self.avatar
        mx, my = self.thing.get_position(x=x, y=y)
        print('actor,move, position %d %d  entry%s real %d %d' % (x, y, loc, mx, my))
        avatar.move(mx, my)

    def go_backward(self):
        self.thing.leave(self, action=self.move, reverse=2)

    def go_forward(self):
        self.thing.leave(self, action=self.move)

    def go_take(self):
        self.thing.leave(self, action=self.move, reverse=2)

    def go_give(self):
        self.thing.leave(self, action=self.move)

    def go_pull(self):
        self.thing.push(self, action=self.move, reverse=2)

    def go_push(self):
        self.thing.push(self, action=self.move)

    def __init__(self, avatar, place, x, y, **kw):
        print('actor,init', avatar, place, x, y)
        self.avatar, self.place, self.x, self.y = avatar, place, x, y
        self.thing = place
        place.gui.handler(38, self.go_forward)
        place.gui.handler(40, self.go_backward)
        place.gui.handler(34, self.go_pull)
        place.gui.handler(33, self.go_push)
        place.gui.handler(35, self.go_take)
        place.gui.handler(36, self.go_give)
        print('actor,init %d %d %s' % (self.x, self.y, dir(self.thing)))


class NullSprite:
    def move(self, place, x, y):
        pass

    def __init__(self, *a):
        pass


class Inventory:
    def list(self):
        ES, FS = NullSprite, Sprite
        invent = {'.': [Way, ES, None], ' ': [Border, ES, None], '&': [Door, ES, None],
                  '@': [Tar, FS, 'piche.gif'], '$': [Trunk, FS, 'tronco.gif']}
        return invent


SIMPLE = ('..$$$&...' + '.' * 10 + ('\n' + '.' * 19) * 12)


# p = [['%s%d%d'%(p,x,y) for x, p in enumerate(' %s '%row)] for y, row in enumerate(border)]

class Place:
    def get_position(self, x=0, y=0):
        return x * 32 + 100 - 32, y * 32 + 100 - 32

    def get_next(self, thing, reverse=0):
        x, y = thing.get_position()
        dx, dy = WIND[thing.get_direction() - reverse]
        self.pos = (x + dx, y + dy)
        px, py = self.pos
        locus = self.plan[py][px]
        return locus

    def pushed(self, thing, action, position=None, reverse=0):
        # print( 'place,enter,thing position %s %s'%(thing, position))
        x, y = position  # or (self.x, self.y)
        # print( 'place,enter, position %d %d'%(x, y))
        action(x, y, thing)

    def enter(self, thing, action, position=None):
        # print( 'place,enter,thing position %s %s'%(thing, position))
        x, y = position  # or (self.x, self.y)
        # print( 'place,enter, position %d %d'%(x, y))
        action(x, y, thing)

    def leave(self, entry, action, reverse=0):
        locus = self.get_next(entry, reverse=reverse)

        def _left(x, y, entry, act=action, loc=locus):
            act(x, y, loc=loc)

        print('%s.leave locus %s lpos %d %d' % ('Place', locus, locus.x, locus.y))
        locus.enter(entry, action=_left, position=(locus.x, locus.y))

    def push(self, entry, action, reverse=0):
        locus = self.get_next(entry, reverse=reverse)

        def _ppushed(x, y, entry, act=action, loc=locus):
            act(x, y, loc=loc)

        print('%s.push locus %s lpos %d %d' % ('Place', locus, locus.x, locus.y))
        locus.pushed(entry, action=_ppushed, position=(locus.x, locus.y), reverse=reverse)

    def __init__(self, gui, inventory, plan=SIMPLE, **kw):
        self.gui = gui
        self._load(plan, gui, inventory)
        x, y = self.x, self.y
        actor = Actor(gui.avatar(), self, x, y)
        self.actor = actor
        door = self.plan[y][x]
        print('place,init xy %s actor %s door %s' % ((x, y), actor, door))
        actor.move(x, y, self)
        actor.thing = door
        self.pos = None

    def _load(self, plan, gui, IV):
        def line(y, row):
            # x = ['%s%d%d'%(p,x,y) for x, p in enumerate(' %s '%row)]
            PART, ICON, IMGE = 0, 1, 2
            me = self
            x = [IV[p][PART](IV[p][ICON](gui, IV[p][IMGE], me, x, y), me, x, y)
                 for x, p in enumerate(' %s ' % row)]
            return x

        w = len(plan.split('\n')[0])
        border = [' ' * w]
        border.extend(plan.split('\n'))
        border.extend([' ' * w])
        self.plan = []
        for y, row in enumerate(border):
            self.plan += [line(y, row)]
            for x, cell in enumerate(self.plan[y]):
                cell.rebase(self.plan)
        # print(self.plan)
        plan = self.plan
        print([(p[1], p[1].x) for p in plan])


def go(dc, pn, svg):
    # Setup main scenario
    for child in pn:  # iteration on child nodes
        pn.remove(child)
    image = svg.rect(x=10, y=10, width=780, height=580, style={'fill': 'forestgreen'})
    image = svg.rect(x=100, y=100, width=600, height=400, style={'fill': 'navajowhite'})
    legend = svg.text('Welcome to Kuarup!', x=350, y=45,
                      font_size=20, text_anchor="middle",
                      style={"stroke": "gold", 'fill': "gold"})


def main(dc, pn, asvg):
    go(dc, pn, asvg)
    inv = Inventory()
    place = Place(asvg, inventory=inv.list())
