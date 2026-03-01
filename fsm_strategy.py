# импорты для машины конечных состояний
from aiogram.fsm.state import State, StatesGroup
class Sostavlenije_Zamekti(StatesGroup):
    tekst_zametki=State()
    tema1_zametki=State()
    tema2_zametki=State()
    tema3_zametki=State()
    tema4_zametki=State()
    tema5_zametki=State()
class Poisk_ZametKi(StatesGroup):
    tema_zametki=State()
class Sbornik_ZametKi(StatesGroup):
    tema_sbornika=State()
class Projekt_V_Arhiv(StatesGroup):
    bukva_arhiv_projekta=State()
    artikul_arhiv_projekta=State()