# age = 16
# if age >= 18:
#     print("Adult")
# else:
#     print("Teen")

# for i in range(5):
#     print("Score:", i)

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Ryusei")


# def say(message):
#     print(message)

# say("fuck off")
# say("I hate u")


# for i in range(100):
#     if i == 42:
#         print("Hurray")
#     else:
#         print("we seek it")


# def add(a, b):
#     return a + b

# result = add(458357357345, 48329058329573457)
# print(result)

# name1 = "Tomioka Giyu: "
# power1 = 100

# def water_breathing_eleven_form(user):
#     print(user, "Total Concentration, Water Breathing: Eleven Form")

# water_breathing_eleven_form(name1)

# name2 = "Akaza: "
# power2 = 150

# def blood_demon_art(user):
#     print(user, "Jutsushiki Tenkai: Hakaigatsu Rashin")

# blood_demon_art(name2)

# if power1 >= power2:
#     print("Giyu Wins")
# else:
#     print("Akaza Wins")


giyu = {
    "Name": "Tomioka Giyu", 
    "Power": 100, 
    "Type": "Hashira",
    }
tanjiro = {
    "Name": "Kamado Tanjiro", 
    "Power": 90, 
    "Type": "Hinoe",
    "Sun Boost": 50,
    }

akaza = {
    "Name": "Akaza",
    "Power": 210,
    "Type": "Uppermoon",
    "Regen": 30,
}

slayers = [giyu, tanjiro]
demon = akaza


def fight(slayers, demon):
    total_good = 0
    for slayer in slayers:
        total_good += slayer["Power"]
        if "Sun Boost" in slayer:
            total_good += slayer["Sun Boost"]

    total_evil = demon["Power"]
    if "Regen" in demon:
        total_evil += demon["Regen"]

    print(f"Team Power: {total_good}")
    print(f"Demon Power: {total_evil}")
    print(f"⚔️ БИТВА ⚔️")
    print(f"Истребители: {', '.join(s['Name'] for s in slayers)}")
    print(f"Демон: {demon['Name']}")
    print(f"Сила команды: {total_good}")
    print(f"Сила демона: {total_evil}")
    print("-" * 30)


if total_good > total_evil:
    print("They can win")
elif total_good == total_evil:
    print("Draw")
else:
    print("They cannot win")

fight(slayers, demon)
