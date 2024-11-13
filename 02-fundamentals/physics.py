'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81         # m/s^2, normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62          # m/s^2, měsíční gravitace
SPEED_OF_LIGHT = 299792458   # m/s, rychlost světla ve vakuu
SPEED_OF_SOUND = 343         # m/s, rychlost zvuku při teplotě 20 °C v suchém vzduchu

# Výpočtové funkce
def weight_on_planet(mass, gravity):
    """Vypočítá váhu objektu o dané hmotnosti na tělese s danou gravitací."""
    return mass * gravity

def energy_from_mass(mass):
    """Vypočítá energii objektu na základě jeho hmotnosti podle E = mc^2."""
    return mass * SPEED_OF_LIGHT ** 2

def travel_time_sound(distance):
    """Vypočítá čas potřebný k překonání vzdálenosti zvukem ve vzduchu při 20 °C."""
    return distance / SPEED_OF_SOUND

def travel_time_light(distance):
    """Vypočítá čas potřebný k překonání vzdálenosti světlem ve vakuu."""
    return distance / SPEED_OF_LIGHT


''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''