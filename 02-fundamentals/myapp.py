import physics

# Vstupní hodnoty
mass = 70  # Hmotnost v kg
distance = 1000  # Vzdálenost v metrech

# Vypočet váhy na Zemi a Měsíci
weight_earth = physics.weight_on_planet(mass, physics.EARTH_GRAVITY)
weight_moon = physics.weight_on_planet(mass, physics.MOON_GRAVITY)
print(f"Váha na Zemi: {weight_earth} N")
print(f"Váha na Měsíci: {weight_moon} N")

# Energie objektu podle jeho hmotnosti
energy = physics.energy_from_mass(mass)
print(f"Energie objektu při rychlosti světla o hmotnosti {mass} kg: {energy} J")

# Čas pro cestu zvukem a světlem
time_sound = physics.travel_time_sound(distance)
time_light = physics.travel_time_light(distance)
print(f"Čas pro překonání {distance} m zvukem: {time_sound} s")
print(f"Čas pro překonání {distance} m světlem: {time_light} s")
