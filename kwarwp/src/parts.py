"""
############################################################
Vitallino - Criador de Jogos Simplificado
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/02/27  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.1 $
:Home: `Labase http://labase.nce.ufrj.br/`__
:Copyright: 2013, `GPL http://is.gd/3Udt`__. 
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.1 $Revision$"[10:-1]
__date__    = "2013/02/09 $Date$"
"""
WIND = [(0, -1), (1, 0), (0, 1), (-1, 0)]
PLACE = None
NOTHING = None

if '__package__' in dir():
    def _logger(*a):
        print(a)


    logger = _logger
    pass
else:
    logger = log


def inherit(base, child):
    overriden, inherited = dir(child), dir(base)
    for member in inherited:
        if member not in overriden:
            setattr(child, member, getattr(base, member))
    # child.m =  str(child.__class__)
    return base


class Cell:
    def __init__(self, avatar, place, x, y, me=None, **kw):
        # inherit(Entrance(place, x, y),self)
        self.avatar, self.place = avatar, PLACE
        self.thing, self.x, self.y, self.m = place, x, y, me or self

    def talk(self, message):
        PLACE.talk(message)

    def rebase(self, base):
        return None

    def move(self, loc):
        logger('nothing here, just dust!')

    def clear(self, load=None):
        logger('%s.clear, position %d %d thing %s load %s' % (
            self.m, self.x, self.y, self.thing, load))
        self.thing = load or PLACE  # self.place
        self.m.thing = load or PLACE  # self.place

    def get_real_position(self, x=0, y=0):
        return self.place.get_position(x=x, y=y)

    def get_position(self, x=0, y=0):
        return self.place.get_position(x=x, y=y)

    def enter(self, entry, destination):
        self.thing.enter(entry, destination)
        logger('%s.enter,thing %s self %s destination %s' % (self.m, self.thing, self, destination))

    def leave(self, entry, direction):
        self.place.leave(entry, direction)

    def pushed(self, entry, destination):
        logger('%s.pushed,thing %s entry %s destination %s' % (self.m, self.thing, entry, destination))
        self.thing.pushed(entry, destination)

    def push(self, entry, direction):
        self.place.push(entry, direction)

    def taken(self, entry, destination):
        logger('%s.taken,thing %s self %s destination %s' % (self.m, self.thing, self, destination))
        self.thing.taken(entry, destination)

    def take(self, entry, direction):
        self.place.take(entry, direction)

    def given(self, entry, destination):
        logger('%s.given,thing %s entry %s self %s destination %s' % (
            self.m, self.thing, entry, self, destination))
        self.thing.given(entry, destination)

    def give(self, entry, direction):
        self.place.give(entry, direction)


class Queuer:
    def __init__(self, actor=None):
        self.queue = []
        self.actor = actor

    def run_command(self, command, **keyword_parameters):
        # logger(command, keyword_parameters)
        self.queue.append([command, keyword_parameters])

    def step(self):
        command, keyword_parameters = self.queue.pop(0)
        # command,keyword_parameters = self.queue[0]
        logger(command, keyword_parameters)
        PLACE.talk('')
        command(**keyword_parameters)
        if not self.queue:
            logger('New stepper: ', self.actor)
            self.actor.stop()


class Actor:
    def reset(self):
        pass

    def talk(self, message):
        PLACE.talk(message)

    def leave(self, entry, direction):
        self.place.leave(entry, direction)

    def clear(self, load=None):
        logger('%s.clear, position %d %d thing, load %s %s' % (
            self, self.x, self.y, self.thing, load))
        self.thing = load or Nothing()  # NOTHING

    def get_entry(self):
        return self

    def get_direction(self, back=False):
        self.heading = (self.avatar.get_direction() + int(self.back) * 2) % 4
        return self.heading

    def set_direction(self, back=False):
        self.back = back
        return self

    def get_real_position(self, x=0, y=0):
        return self.place.get_position(x=x, y=y)

    def get_position(self):
        return self.x, self.y

    def take(self, loc):
        loc.move(self)

    def give(self, loc):
        # self.thing = self.thing.thing = self.thing.place = self.place.place
        self.thing.move(loc)

    def move(self, loc):
        self.place.clear()
        # self.x, self.y, loc.thing, self.thing = loc.x, loc.y, self, loc or self.thing
        self.x, self.y = loc.x, loc.y
        loc.clear(self)
        self.place = loc
        # logger( 'actor,move, position thing %d %d %s'%(x, y, self.thing))
        avatar = self.avatar
        mx, my = self.place.get_real_position(x=loc.x, y=loc.y)
        logger('actor.move, position %d %d  entry%s real %d %d' % (loc.x, loc.y, loc, mx, my))
        avatar.move(mx, my)
        self.thing.move(self)

    def run_command(self, command, **keyword_parameters):
        PLACE.talk('')
        command(**keyword_parameters)

    def stop(self):
        logger('Now stepper is : ', self)
        self.stepper = self

    def _backward(self, a=0):
        self.thing.leave(entry=self, direction=self.set_direction(back=True))

    def _forward(self, a=0):
        logger('_forward %s' % self.thing)
        self.thing.leave(entry=self, direction=self.set_direction())

    def _left(self, a=0):
        self.avatar.go_left()

    def _right(self, a=0):
        self.avatar.go_right()

    def _take(self, a=0):
        self.thing.take(entry=self, direction=self.set_direction())

    def _give(self, a=0):
        self.thing.give(entry=self, direction=self.set_direction())

    def _pull(self, a=0):
        self.thing.push(entry=self, direction=self.set_direction(back=True))

    def _push(self, a=0):
        self.thing.push(entry=self, direction=self.set_direction())

    def go_step(self):
        logger('Stepper : %s' % self.stepper)
        self.stepper.step()

    def go_backward(self, a=0):
        self.stepper.run_command(self._backward)

    def go_forward(self, a=0):
        self.stepper.run_command(self._forward)

    def go_left(self, a=0):
        self.stepper.run_command(self._left)

    def go_right(self, a=0):
        self.stepper.run_command(self._right)

    def go_take(self, a=0):
        self.stepper.run_command(self._take)

    def go_give(self, a=0):
        self.stepper.run_command(self._give)

    def go_pull(self, a=0):
        self.stepper.run_command(self._pull)

    def go_push(self, a=0):
        self.stepper.run_command(self._push)

    def step(self):
        me = self

        class nQueuer:
            def __init__(self, actor=me):
                self.queue = []
                self.actor = actor

            def run_command(self, command, **keyword_parameters):
                # logger(command, keyword_parameters)
                self.queue.append([command, keyword_parameters])

            def step(self):
                command, keyword_parameters = self.queue.pop(0)
                # command,keyword_parameters = self.queue[0]
                logger(command, keyword_parameters)
                PLACE.talk('')
                command(**keyword_parameters)
                if not self.queue:
                    logger('New stepper: %s stepper %s' % (self.actor, self.actor.stepper))
                    self.actor.stepper = self.actor
                    self.actor.stop()

        self.stepper = Queuer()
        self.stepper.actor = self
        PLACE.solver(self)

    def __init__(self, avatar, place, x, y, **kw):
        logger('actor,init', avatar, place, x, y)
        self.avatar, self.place, self.x, self.y = avatar, place, x, y
        self.thing = Nothing()  # NOTHING
        self.stepper = self
        logger('actor,init %d %d %s' % (self.x, self.y, dir(self.thing)))
        self.heading = self.back = None


class Place:
    def clear(self, load=None):
        logger('ERROR, SHOUlD NOT CALL')
        pass

    def get_position(self, x=0, y=0):
        return x * 32 + 100 - 32, y * 32 + 100 - 32

    def get_real_position(self, x=0, y=0):
        return self.get_position(x=x, y=y)

    def get_next(self, thing, direction):
        x, y = thing.get_position()
        dx, dy = WIND[direction.get_direction()]
        self.pos = (x + dx, y + dy)
        px, py = self.pos
        locus = self.plan[py][px]
        return locus

    def taken(self, entry, destination):
        # logger('nothing here!')
        entry.take(destination)

    def take(self, entry, direction):
        locus = self.get_next(entry, direction)
        logger('%s.take locus %s entry %s dir %d lpos %d %d' % (
            'Place', locus, entry, direction.get_direction(), locus.x, locus.y))
        locus.taken(entry, locus)

    def given(self, entry, destination):
        logger('place.given entry %s destination %s' % (entry, destination))
        # entry.given(entry, destination)
        entry.move(destination)

    def give(self, entry, direction):
        locus = self.get_next(entry, direction)
        logger('%s.give locus %s entry %s dir %d lpos %d %d' % (
            'Place', locus, entry, direction.get_direction(), locus.x, locus.y))
        locus.given(entry, locus)

    def pushed(self, entry, destination):
        entry.move(destination)

    def enter(self, entry, destination):
        entry.move(destination)

    def leave(self, entry, direction):
        locus = self.get_next(entry, direction)
        logger('%s.leave locus %s entry %s dir %d lpos %d %d' % (
            'Place', locus, entry, direction.get_direction(), locus.x, locus.y))
        locus.enter(entry, locus)

    def push(self, entry, direction):
        locus = self.get_next(entry, direction)
        logger('%s.push locus %s entry %s thing %s lpos %d %d' % (
            'Place', locus, entry, locus.thing, locus.x, locus.y))
        locus.pushed(entry, locus)

    def talk(self, message):
        self.legend.text = message
        # logger(self.legend.textContent)

    def __init__(self, plan, solver):
        global PLACE
        PLACE = self
        self.plan = plan
        self.solver = solver
        self.legend = self.pos = None
        self.nothing = Nothing(self)


class Nothing(Place):
    def __init__(self, place=None):
        self.place = place or PLACE
        self.plan = PLACE.plan

    def give(self, entry, direction):
        logger('nothing here, bare!')
        # entry.give(destination)

    def move(self, loc):
        pass
