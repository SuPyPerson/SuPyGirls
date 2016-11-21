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
:Copyright: 2011, `GPL http://is.gd/3Udt`__. 
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.1 $Revision$"[10:-1]
__date__    = "2013/02/09 $Date$"
"""
if '__package__' in dir():
    from parts import Actor, Place
    from elements import *
    from kwarwp_factory import REPO, Dialog


    def _logger(*a):
        print(a)


    logger = _logger
    pass
else:
    logger = log
    pass


class NullSprite:
    def move(self, place, x, y):
        pass

    def __init__(self, *a):
        pass


CHALL1 = '''"""During Kuarup, Tchuk carried several trunks,
noted down in several ways. Help Paje, the Shaman, to hit
the final score of Tchuk, making the necessary conversions
"""
\nsmall_trunk = 1
\naverage_trunks  = [2,3]
\nlarge_trunk = "4"
\ntotal  = small_trunk  + average_trunks + large_trunk\n
'''
TEST1 = '''
\nassert total == 10, \'Your total was not 10, was %s\'%total \n'''

nCHALL1 = '''"""
Durante o Kuarup, Tchuk carregou varios troncos,
anotados de diversas maneiras. Ajude o Paje a acertar
a pontuacao final de Tchuk, fazendo as conversoes necessarias
"""
\ntronco_pequeno = 1
\ntroncos_medios = [2,3]
\ntronco_grande = "4"
\ntotal = tronco_pequeno + troncos_medios + tronco_grande\n'''
nTEST1 = '''
\nassert total == 10, \'O seu total nao foi 10, foi %s\'%total\n'''
'''
'''


class Builder:
    def build_actor(self, gui, place, x, y):
        # x, y = self.x, self.y
        door = place.plan[y][x]
        actor = Actor(gui.avatar(), door, x, y)
        place.actor = actor
        logger('place,init xy %s actor %s door %s' % ((x, y), actor, door))
        actor.move(door)
        solv = 'def solver(a):\n    a.go_forward'
        dialog = gui.dialog(text=solv, act=lambda dl: alert(dl.get_text()))
        dialog.hide()
        # actor.place = door
        # actor.thing = door
        gui.handler(13, actor.go_step)
        gui.handler(38, actor.go_forward)
        gui.handler(40, actor.go_backward)
        gui.handler(34, actor.go_pull)
        gui.handler(33, actor.go_push)
        gui.handler(35, actor.go_take)
        gui.handler(36, actor.go_give)

    def build_place(self, plan, gui, IV, solver):
        def line(y, row, me):
            # x = ['%s%d%d'%(p,x,y) for x, p in enumerate(' %s '%row)]
            PART, IMGE, TALK = 0, 1, 2
            enum_row = enumerate(' %s ' % row)
            x = [IV[p][PART](
                self.sprite(gui, IV[p][IMGE], me, x, y), me, x, y, IV[p][TALK])
                 for x, p in enum_row]
            return x

        self.place = Place([], solver)
        w = len(plan.split('\n')[0])
        border = [' ' * w]
        border.extend(plan.split('\n'))
        border.extend([' ' * w])
        self.plan = []
        logger('self.plan = []')
        for y, row in enumerate(border):
            self.plan += [line(y, row, self.place)]
            for x, cell in enumerate(self.plan[y]):
                cell.rebase(self.plan)
        # logger(self.plan)
        plan = self.plan
        self.place.plan = plan
        logger('self.place.plan = plan')
        self.place.legend = gui.text('Welcome to Kuarup!', x=350, y=45,
                                     font_size=20, text_anchor="middle",
                                     style={"stroke": "gold", 'fill': "gold"})
        logger([(p[1], p[1].x) for p in plan])
        self.place.dialog = gui.dialog
        return self.place

    def build_land(self, gui):
        # Setup main scenario background
        # image = gui.rect(x=10,y=10, width=780, height=580,style={'fill':'forestgreen'})
        image = gui.image(href=REPO % 'forest.jpg',
                          x=0, y=0, width=900, height=600)
        # image = gui.rect(x=100,y=100, width=600, height=400,style={'fill':'navajowhite'})
        image = gui.rect(x=100, y=100, width=608, height=416, style={'fill': 'url(#EMFimage1)'})

    def build(self, pn, gui, inventory, plan, solver):
        # Setup main scenario
        logger('build(self, pn, gui, inventory, plan, solver)')
        self.build_land(gui)
        logger('self.build_land')
        place = self.build_place(plan, gui, inventory, solver)
        logger('self.build_place(plan, gui, inventory, solver)')
        self.build_actor(gui, place, place.x, place.y)
        logger('self.build_actor(gui, place, place.x, place.y)')
        return place

    def build_inventory(self, FS=NullSprite):
        self.sprite = FS
        ES = NullSprite
        tk = [CHALL1, TEST1]
        return {'.': [Way, None, tk], ' ': [Border, None, tk], '&': [Door, None, tk], '@': [Tar, 'piche.gif', tk],
                '$': [Trunk, 'tronco.gif', tk], '*': [Rock, 'pedra.gif', tk], '!': [Talker, 'paje.png', tk]}
