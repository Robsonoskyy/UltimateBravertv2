import random

champions = {
    "top": ["Aatrox", "Camille", "ChoGath", "Darius", "DrMundo", "Fiora", "Gangplank",
            "Garen", "Gnar", "Gwen", "Illaoi", "Irelia", "Jax", "Kennen",
            "Kled", "Malphite", "Mordekaiser", "Nasus", "Olaf", "Ornn",
            "Pantheon", "Poppy", "Renekton", "Riven", "Sett", "Shen",
            "Sion", "TahmKench", "Teemo", "Tryndamere", "Urgot",
            "Volibear", "Warwick", "Yorick"],

    "jungle": ["Amumu", "BelVeth", "Briar", "Diana", "Ekko", "Elise", "Evelynn",
               "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern",
               "JarvanIV", "Karthus", "Kayn", "Kindred", "LeeSin",
               "Lillia", "MasterYi", "Nidalee", "Nocturne", "Nunu",
               "Rammus", "RekSai", "Rengar", "Sejuani", "Shaco",
               "Skarner", "Taliyah", "Trundle", "Udyr", "Vi",
               "Viego", "Wukong", "XinZhao", "Zac"],

    "mid": ["Ahri", "Akali", "Anivia", "Annie", "AurelionSol", "Azir",
            "Cassiopeia", "Corki", "Ekko", "Fizz", "Galio", "Heimerdinger",
            "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux",
            "Malzahar", "Naafiri", "Neeko", "Orianna", "Qiyana",
            "Ryze", "Sylas", "Syndra", "Talon", "TwistedFate",
            "Veigar", "VelKoz", "Vex", "Viktor", "Vladimir",
            "Xerath", "Yasuo", "Yone", "Zed", "Ziggs", "Zoe"],

    "adc": ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal",
            "Jhin", "Jinx", "KaiSa", "Kalista", "KogMaw",
            "Lucian", "MissFortune", "Nilah", "Samira",
            "Sivir", "Tristana", "Twitch", "Varus",
            "Vayne", "Xayah", "Zeri"],

    "support": ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum",
                "Janna", "Karma", "Leona", "Lulu", "Milio",
                "Morgana", "Nami", "Nautilus", "Pyke",
                "Rakan", "Renata", "Senna", "Seraphine",
                "Sona", "Soraka", "Swain", "Taric",
                "Thresh", "Yuumi", "Zilean", "Zyra"]
}

runesmain = {
    "yellow": ["PTA", "Lethal Tempo", "Fleet", "Conq"],

    "red": ["Electrocute", "Dark Harvest", "Hail of Blades"],

    "blue": ["Aery", "Comet", "Phase Rush"],

    "green": ["Grasp", "Aftershock", "Guardian"],

    "lblue": ["Glacial Augment", "Spellbook", "First Strike"]
}

runesyellow = {
    "yellow1": ["Absorb Life", "Triumph", "Presence of Mind"],
    "yellow2": ["Legend: Alacrity", "Legend: Haste", "Legend: Bloodline"],
    "yellow3": ["Coup de Grace", "Cut Down", "Last Stand"],
}

runesred = {
    "red1": ["Cheap Shot", "Taste of Blood", "Sudden Impact"],
    "red2": ["Zombie Ward", "Ghost Poro", "Eyeball Collection"],
    "red3": ["Treasure Hunter", "Relentless Hunter", "Ultimate Hunter"],
}

runesblue = {
    "blue1": ["Nullifying Orb", "Manaflow Band", "Nimbus Cloak"],
    "blue2": ["Transcendence", "Celerity", "Absolute Focus"],
    "blue3": ["Scorch", "Waterwalking", "Gathering Storm"],
}

runesgreen = {
    "green1": ["Demolish", "Font of Life", "Shield Bash"],
    "green2": ["Conditioning", "Second Wind", "Bone Plating"],
    "green3": ["Overgrowth", "Revitalize", "Unflinching"],
}

runeslblue = {
    "lblue1": ["Hexflash", "Magical Footwear", "Cash Back"],
    "lblue2": ["Triple Tonic", "Biscuit Delivery", "Time Warp Tonic"],
    "lblue3": ["Cosmic Insight", "Approach Velocity", "Jack of All Trades"]
}



summs = {
    "all": ["Flash", "Ignite", "Teleport", "Ghost", "Heal", "Barrier", "Exhaust", "Cleanse"], 
    "jg": ["Smite"]
    
}

skills = ["q", "w", "e"]
skillsr = ["q","w","e","r"]

role = input("What role?: ").lower().strip()

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
print("Secondary:")



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







#credit to revity303 for figuring out secondary runes