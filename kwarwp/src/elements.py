"""
############################################################
Vitallino - Criador de Jogos Simplificado
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/02/27  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.2 $
:Home: `Labase http://labase.nce.ufrj.br/`__
:Copyright: 2011, `GPL http://is.gd/3Udt`__. 
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.2 $Revision$"[10:-1]
__date__    = "2013/02/09 $Date$"
"""
if '__package__' in dir():
    from parts import Cell
    import parts
    def _logger(*a):
        print(a)
    logger = _logger
    pass
else:
    logger = log

import sys
    
def execution(code):
    exec(code)
    
def inherit(base, child):
    overriden, inherited = dir(child), dir(base)
    for member in inherited:
        if member not in overriden:
            setattr(child, member, getattr(base,member))
    #child.m =  str(child.__class__)
    return base

class Way(Cell):
    def __init__(self, avatar, place, x, y, talk = '', me=None, **kw):
        #inherit(Cell(avatar, place, x, y, me=self),self)
        Cell.__init__(self, avatar, place, x, y, self)
        self.avatar,self.place = avatar, place
        self.thing, self.x, self.y, self.m = place, x, y, self

class Tar(Cell):
    def leave(self,thing, action, reverse =0):
        self.place.talk('Youre STUCK!!!')
        logger('Youre STUCK!!!')
    def __init__(self, avatar, place, x, y, talk = '', **kw):
        #inherit(Cell(avatar, place, x, y, me=self),self)
        Cell.__init__(self, avatar, place, x, y, self)
        pass

class Door(Cell):
    def __init__(self, avatar, place, x, y, talk = '', **kw):
        #inherit(Cell(avatar, place, x, y, me=self),self)
        Cell.__init__(self, avatar, place, x, y, self)
        logger(dir(self))
        self.thing, self.x, self.y, self.m = place, x, y, self
        place.x, place.y =  x, y

class Entry:
    def __init__(self, thing, entry, x, y):
        self.x, self.y, self.entry, self.thing = x, y, entry, thing
    def get_entry(self):
        return self.thing
    def get_direction(self):
        return self.entry.get_direction()
    def get_position(self):
        return (self.x, self.y)

class Trunk(Cell):
    def clear(self, load= None):
        logger( '%s.clear, position %d %d thing %s load %s'%(
            self.m, self.x, self.y, self.thing, load ))
        self.thing = load or PLACE#self.place
    def reset(self):
        self.move_entry = self.null_move_entry
        self.entry.reset()
    def get_direction(self):
        return self.entry.get_direction()
    def get_position(self,x=0, y=0):
        return (self.x, self.y)
    def enter(self,entry, destination ):
        self.place.talk('It is HEAVY!!')
        logger('It is HEAVY!!')
        entry.reset()
    def take(self,entry,direction ):
        self.place.talk('Hands Busy!!')
        logger('Hands Busy!!')
        entry.reset()
    def _move(self, loc):
        self.place.clear()
        self.x, self.y = loc.x, loc.y
        self.place = loc
        loc.clear(self)
        ##logger( 'actor,move, position thing %d %d %s'%(x, y, self.thing))
        avatar = self.avatar
        mx, my = self.thing.get_real_position(x=loc.x, y=loc.y)
        logger( '%s(trunk).move, position %d %d  entry%s real %d %d'%(
            self.m,loc.x, loc.y, loc, mx, my))
        avatar.move(mx, my)
    def move_entry(self,loc):
        pass
    def null_move_entry(self,loc):
        pass
    def move(self, loc):
        place = self.place
        self._move(loc)
        self.move_entry(place)
    def given(self,entry, destination):
        self.place.talk('No space to drop here!!')
        entry.reset()
        #self._move(destination)
        #self.thing.give(self, destination)
    def give(self, entry, direction):
        self.thing.give(self, direction)
    def taken(self,entry, destination):
        entry.take(self)
    def pushed(self,entry, destination ):
        def _move_entry(loc, entry= entry, self= self):
            entry.move(loc)
            self.move_entry = self.null_move_entry
        self.move_entry = _move_entry
        self.heading = entry.heading
        self.entry = entry
        logger( '%s(trunk).pushed,thing %s entry %s destination %s direction %s'%(
            self.m, self.thing, entry, destination, entry.heading))
        self.thing.push(self, entry)
    def __init__(self, avatar, place, x, y, talk = '', **kw):
        #inherit(Cell(avatar, place, x, y, me=self),self)
        Cell.__init__(self, avatar, place, x, y, self)
        self.avatar,self.place = avatar, place
        self.thing, self.x, self.y, self.m = place, x, y, self
    def rebase(self,base):
        place = Way(None,self, self.x, self.y)
        base[self.y][self.x]= place
        place.place = self.place
        place.thing = self
        self.place = place

class Rock(Cell):
    def clear(self, load= None):
        logger( '%s.clear, position %d %d thing %s load %s'%(
            self.m, self.x, self.y, self.thing, load ))
        self.thing = load or PLACE#self.place
    def reset(self):
        self.move_entry = self.null_move_entry
        self.entry.reset()
    def get_direction(self):
        return self.entry.get_direction()
    def get_position(self,x=0, y=0):
        return (self.x, self.y)
    def _move(self, loc):
        self.place.clear()
        self.x, self.y = loc.x, loc.y
        self.place = loc
        loc.clear(self)
        ##logger( 'actor,move, position thing %d %d %s'%(x, y, self.thing))
        avatar = self.avatar
        mx, my = self.thing.get_real_position(x=loc.x, y=loc.y)
        logger( '%s(rock).move, position %d %d  entry%s real %d %d'%(
            self.m,loc.x, loc.y, loc, mx, my))
        avatar.move(mx, my)
    def move_entry(self,loc):
        pass
    def null_move_entry(self,loc):
        pass
    def move(self, loc):
        place = self.place
        self._move(loc)
        self.move_entry(place)
    def given(self,entry, destination):
        self.place.talk('No space to drop here!!')
        entry.reset()
    def taken(self,entry, destination):
        self.place.talk('Too much heavy to take!!')
        logger('Too much Heavy to take!!')
        entry.reset()
    def enter(self,entry, destination ):
        logger('It is HEAVY!!')
        self.place.talk('It is HEAVY!!')
        entry.reset()
    def pushed(self,entry, destination ):
        def _move_entry(loc, entry= entry, self= self):
            entry.move(loc)
            self.move_entry = self.null_move_entry
        self.move_entry = _move_entry
        self.heading = entry.heading
        self.entry = entry
        logger( '%s(rock).pushed,thing %s entry %s destination %s direction %s'%(
            self.m, self.thing, entry, destination, entry.heading))
        self.thing.push(self, entry)
    def __init__(self, avatar, place, x, y, talk = '', **kw):
        Cell.__init__(self, avatar, place, x, y, self)
        #inherit(Cell(avatar, place, x, y, me=self),self)
        self.avatar,self.place = avatar, place
        self.thing, self.x, self.y, self.m = place, x, y, self
    def rebase(self,base):
        place = Way(None,self, self.x, self.y)
        base[self.y][self.x]= place
        place.place = self.place
        place.thing = self
        self.place = place

class Border(Cell):
    def enter(self,entry, destination ):
        self.place.talk('Cant go this way!!')
        logger('Cant go this way!!')
        entry.reset()
    def pushed(self,entry, destination ):
        self.place.talk('Cant go this way!!')
        logger('Cant go this way!!')
        entry.reset()
    def given(self,entry, destination ):
        self.place.talk('Cant give this way!!')
        logger('Cant give this way!!')
        entry.reset()
    def __init__(self, avatar, place, x, y, talk = '', **kw):
        #inherit(Cell(avatar, place, x, y, me=self),self)
        Cell.__init__(self, avatar, place, x, y, self)
        self.thing, self.x, self.y, self.m = place, x, y, self
        self.place = place #Way(None,place, self.x, self.y)
        #self.avatar,self.place, self.x, self.y = avatar, place, x, y

class cons_out:

    def __init__(self):
        self.value = ''
    def write(self,data):
        self.value += str(data)
        #logger('self.value %s'%self.value)
        
class Talker(Rock):

    def write(self,data):
        self.value += str(data)

    def _first_response(self, dialog):
        value = self.value = cons_out()
        sys_out, sys.stdout = sys.stdout, value
        sys_err, sys.stderr = sys.stderr, value
        logger('first response %s %s %s'%(dialog,sys.stdout,sys.stderr))
        action = dialog.get_text()
        action += self.challenge[1]
        logger('first response code %s'%action)
        #self.value = ''
        try:
            exec(action)
            pass
        except:
            logger('first response error %s'%self.value.value)
            self.challenge[0] = dialog.get_text()
            dialog.set_text(self.value.value)
            self._response = self._second_response
            self.place.talk('Something went wrong in your attempt!!')
            dialog.show()
        else:
            logger('first response else %s'%self.world.plan[0][0])
            self.challenge[0] = dialog.get_text()
            self.move(self.world.plan[0][0])
            self.place.talk('It looks like you did it!!')
            self._response = self._first_response
        sys.stdout = sys_out
        sys.stderr = sys_err
        logger('first response value error %s'%self.value.value)
            
    def _second_response(self, dialog):
        self._response = self._first_response
        self.place.talk('Bump me again to retry the Challenge!!')
           
    def response(self, dialog):
        self._response(dialog)
    def _challenge(self, entry):
        self.entry = entry
        self._response = self._first_response
        self.dialog = self.world.dialog(text=self.challenge[0], act=self.response)
        self.dialog.show()
        
    def enter(self,entry, destination ):
        self.place.talk('There is a Challenge for you!!')
        self._challenge(entry)
        logger('Cant go this way!!')
        entry.reset()
    def pushed(self,entry, destination ):
        self.place.talk('Cant go this way!!')
        logger('Cant go this way!!')
        entry.reset()
    def given(self,entry, destination ):
        self.place.talk('Cant give this way!!')
        logger('Cant give this way!!')
        entry.reset()
    def __init__(self, avatar, place, x, y, talk = '', **kw):
        #inherit(Cell(avatar, place, x, y, me=self),self)
        Cell.__init__(self, avatar, place, x, y, self)
        self.challenge = talk
        self.thing, self.x, self.y, self.m = place, x, y, self
        self.place = place #Way(None,place, self.x, self.y)
        self.world = self.place
        #self.avatar,self.place, self.x, self.y = avatar, place, x, y

