import random
from libraries import champions,runesmain,runesyellow,runesred,runesblue,runesgreen,runeslblue,skills,skillsr,items,summs

role = random.choice(list(champions.keys()))

if role in champions:
    champ = (random.choice(champions[role]))
    print(champ)
else:
    print(f"No such role as {role} you retard")

print("")
summsp = random.sample(summs["all"], 2)
if role != "jungle":
    print(summsp)
else:
    print(random.choice(summs["all"]))
    print(summs["jg"])

rune = random.choice(list(runesmain.keys()))

secondaries = []
for tree in runesmain:
    if tree != rune:
        secondaries.append(tree)
secondary = random.choice(secondaries)

print("")
if rune  == "yellow":
    print("Runes:")
    print(random.choice(runesmain["yellow"]))
    print(random.choice(runesyellow["yellow1"]))
    print(random.choice(runesyellow["yellow2"]))
    print(random.choice(runesyellow["yellow3"]))
elif rune  == "red":
    print("Runes: ")
    print(random.choice(runesmain["red"]))
    print(random.choice(runesred["red1"]))
    print(random.choice(runesred["red2"]))
    print(random.choice(runesred["red3"]))
elif rune  == "blue":
    print("Runes: ")
    print(random.choice(runesmain["blue"]))
    print(random.choice(runesblue["blue1"]))
    print(random.choice(runesblue["blue2"]))
    print(random.choice(runesblue["blue3"]))
elif rune  == "green":
    print("Runes: ")
    print(random.choice(runesmain["green"]))
    print(random.choice(runesgreen["green1"]))
    print(random.choice(runesgreen["green2"]))
    print(random.choice(runesgreen["green3"]))
elif rune  == "lblue":
    print("Runes: ")
    print(random.choice(runesmain["lblue"]))
    print(random.choice(runeslblue["lblue1"]))
    print(random.choice(runeslblue["lblue2"]))
    print(random.choice(runeslblue["lblue3"]))
else: print("")

print("")
print(f"Secondary : {secondary}")



if secondary  == "yellow":
    rowrandom = random.sample(list(runesyellow.keys()), 2)
    print(random.sample(runesyellow[rowrandom[0]], 1))
    print(random.sample(runesyellow[rowrandom[1]], 1))
elif secondary  == "red":
    rowrandom = random.sample(list(runesred.keys()), 2)
    print(random.sample(runesred[rowrandom[0]], 1))
    print(random.sample(runesred[rowrandom[1]], 1))
elif secondary  == "blue":
    rowrandom = random.sample(list(runesblue.keys()), 2)
    print(random.sample(runesblue[rowrandom[0]], 1))
    print(random.sample(runesblue[rowrandom[1]], 1))
elif secondary  == "green":
    rowrandom = random.sample(list(runesgreen.keys()), 2)
    print(random.sample(runesgreen[rowrandom[0]], 1))
    print(random.sample(runesgreen[rowrandom[1]], 1))
elif secondary  == "lblue":
    rowrandom = random.sample(list(runeslblue.keys()), 2)
    print(random.sample(runeslblue[rowrandom[0]], 1))
    print(random.sample(runeslblue[rowrandom[1]], 1))
else:
    print("idk how this happened")
    

if champ == "Udyr":
    skillr = random.choice(skillsr)
    print("")
    print(f"Skill to max: {skillr}")
else:
    skil = random.choice(skills)
    print("")   
    print(f"skill to max: {skil}") 


print("Items: ")
print(random.choice(items["Legendary"]))
print(random.choice(items["Legendary"]))
print(random.choice(items["Legendary"]))
print(random.choice(items["Legendary"]))
print(random.choice(items["Legendary"]))
print(random.choice(items["Boots"]))







#credit to revity303 for figuring out secondary runes