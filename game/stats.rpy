init python:
    class Statistics(object):
        def __init__(self, smarts, charm, fitness, trickery, empathy):
            self.stats = dict()
            self.stats['smarts'] = smarts
            self.stats['charm'] = charm
            self.stats['fitness'] = fitness
            self.stats['trickery'] = trickery
            self.stats['empathy'] = empathy

        @property
        def Output(self):
            return "Your stats: Smatrs: " + str(self.stats['smarts']) + " Charm: " + str(self.stats['charm']) + " Fitness: " + str(self.stats['fitness']) + " Trickery: " + str(self.stats['trickery']) + " Empathy: " + str(self.stats['empathy'])


label initialize:
    define stats = Statistics(2,2,2,2,2)
    return


label increase_smarts:

    if stats.stats['smarts'] >= 4:
        $ stats.stats['smarts'] = 5
        "Your Smatrs maxed out!"
    else:
        $ stats.stats['smarts'] += 1
        "Your Smatrs increased!"

    return


label increase_fitness:

    if stats.stats['fitness'] >= 4:
        $ stats.stats['fitness'] = 5
        "Your Fitness maxed out!"
    else:
        $ stats.stats['fitness'] += 1
        "Your Fitness increased!"

    return

label increase_charm:

    if stats.stats['charm'] >= 4:
        $ stats.stats['charm'] = 5
        "Your Charm maxed out!"
    else:
        $ stats.stats['charm'] += 1
        "Your Charm increased!"

    return

label increase_empathy:

    if stats.stats['empathy'] >= 4:
        $ stats.stats['empathy'] = 5
        "Your Empathy maxed out!"
    else:
        $ stats.stats['empathy'] += 1
        "Your Empathy increased!"

    return

label increase_trickery:

    if stats.stats['trickery'] >= 4:
        $ stats.stats['trickery'] = 5
        "Your Trickery maxed out!"
    else:
        $ stats.stats['trickery'] += 1
        "Your Trickery increased!"

    return


#Decreases

label decrease_smarts:

    if stats.stats['smarts'] <= 2:
        $ stats.stats['smarts'] = 1
        "Your Smatrs hit rock bottom!"
    else:
        $ stats.stats['smarts'] -= 1
        "Your Smatrs decreased!"

    return


label decrease_fitness:

    if stats.stats['fitness'] <= 2:
        $ stats.stats['fitness'] = 1
        "Your Fitness hit rock bottom!"
    else:
        $ stats.stats['fitness'] -= 1
        "Your Fitness decreased!"

    return

label decrease_charm:

    if stats.stats['charm'] <= 2:
        $ stats.stats['charm'] = 1
        "Your Charm hit rock bottom!"
    else:
        $ stats.stats['charm'] -= 1
        "Your Charm decreased!"

    return

label decrease_empathy:

    if stats.stats['empathy'] <= 2:
        $ stats.stats['empathy'] = 1
        "Your Empathy hit rock bottom!"
    else:
        $ stats.stats['empathy'] -= 1
        "Your Empathy decreased!"

    return

label decrease_trickery:

    if stats.stats['trickery'] <= 2:
        $ stats.stats['trickery'] = 1
        "Your Trickery hit rock bottom!"
    else:
        $ stats.stats['trickery'] -= 1
        "Your Trickery decreased!"

    return