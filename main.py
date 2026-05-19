# Veckouppgift 2

########################################
# 1 Diskutera i grupp
########################################
"""
Programmmet frågar användaren efter priset på en vara. Om priset är över 100 kr får användaren 10% i rabatt.
Om priset är över 300 kr får användaren ytterligare 25% i rabatt, totalt 35%.

Programmet är rättat och "förbättrat" genom att en if/ else sats beräknar den totala rabatten direkt och
notifierar användaren. Den avslutande printsatsen är rättad så att variabeln final_price omvandlas till en
sträng för att konkateneras korrekt i strängen.
"""
is_member = False
discount_level1 = 100
discount_level2 = 300
total_discount = 0

price = input("Välkommen, vad kostar varan: ")
price = float(price)

if discount_level1 < price <= discount_level2:
    print("Grattis! Du har avancerat till nivå 1 och får 10% i rabatt.")
    total_discount = total_discount + 10

elif price > discount_level2:
    print("Grattis! Du har avancerat till nivå 2 och får 10% + 25% = 35% i rabatt.")
    total_discount = total_discount + 35

final_price = price * (100 - total_discount) / 100
print("Efter rabatter blir priset.... " + str(final_price) + " kronor.")


########################################
# 2 Balder
########################################
"""
1. Tre värden medger test av en längd under tillåten, exakt värde och en som är längre. 
2. Det är bra att testa gränsvärden. I detta fall är gränsen 130 cm och blir därför det 
    testade värdet i if-satsen. Om något blir fel i en if-sats är det ofta < > och = i
    förhållande till gränsvärdet.
3. Det finns ingen anledning att lägga till 129 centimeter då det redan finns ett test
    för mindra än 130 centimeter.
"""

user_length = input("Hur lång är du i centimeter: ")
user_length = int(user_length) # cast string to integer
length_limit_to_ride = 130

if user_length < length_limit_to_ride:
    print(f"Du får inte åka")
else:
    print(f"Du får åka")


########################################
# 3 Sportresultat
########################################

program_version = int(input("\nVilken version av programmet vill du köra (1 - 3): "))

print("\nMatchen är över, nu ska vi räkna ut resultatet!")

goals_tottenham = int(input("Hur många mål gjorde Tottenham? "))
goals_Liverpool = int(input("Hur många mål gjorde Liverpool? "))

# version 1
if program_version == 1:
    if goals_tottenham < goals_Liverpool:
        print("Liverpool vann!")
    else:
        print("Tottenham vann!")

# version 2
elif program_version == 2:
    if goals_tottenham < goals_Liverpool:
        print("Liverpool vann!")
    elif goals_tottenham > goals_Liverpool:
        print("Tottenham vann!")
    else:
        print("Det blev oavgjort!")

# version 3
# Lämpliga test 2 - 1, 1 - 2 och 2 - 2
elif program_version == 3:
    score_difference = 0
    if goals_tottenham < goals_Liverpool:
        score_difference = goals_Liverpool - goals_tottenham
        print(f"Liverpool vann med {score_difference} mål!")
    elif goals_tottenham > goals_Liverpool:
        score_difference = goals_tottenham - goals_Liverpool
        print(f"Tottenham vann med {score_difference} mål!")
    else:
        print(f"Det blev oavgjort, {goals_tottenham} - {goals_Liverpool}!")


########################################
# 4 Temperaturomvandling
########################################

program_version = int(input("\nVilken version av programmet vill du köra (1 - 3): "))

# version 1
if program_version == 1:
    temperature_celcius = input("Skriv in en temperatur i grader Celcius: ")
    temperature_farenheit = round((1.8 * float(temperature_celcius) +32), 2)
    print(f"Det blir {temperature_farenheit} grader Farenheit.")

# version 2
if program_version == 2:
    conversion_type = input("Vill du omvandla från Celcius (C) eller Farenheit (F): ")

    if conversion_type.lower() == "c":
        temperature_celcius = input("Skriv in en temperatur i grader Celcius: ")
        temperature_farenheit = round((1.8 * float(temperature_celcius) + 32), 2)
        print(f"Det blir {temperature_farenheit} grader Farenheit.")
    elif conversion_type.lower() == "f":
        temperature_farenheit = input("Skriv in en temperatur i grader Farenheit: ")
        temperature_celcius = round((float(temperature_farenheit) - 32) / 1.8, 2)
        print(f"Det blir {temperature_celcius} grader Celcius.")

# version 3
if program_version == 3:
    conversion_type = input("Vill du omvandla från Celcius (C) eller Farenheit (F): ")

    if conversion_type.lower() == "c":
        temperature_celcius = input("Skriv in en temperatur i grader Celcius: ")
        temperature_farenheit = round((1.8 * float(temperature_celcius) + 32), 2)
        print(f"Det blir {temperature_farenheit} grader Farenheit.")
        if float(temperature_celcius) < 10:
            print(f"Det är bäst att ta på vinterkläder.")
        elif float(temperature_celcius) > 20:
            print(f"Det är bäst att packa badkläder.")

    elif conversion_type.lower() == "f":
        temperature_farenheit = input("Skriv in en temperatur i grader Farenheit: ")
        temperature_celcius = round((float(temperature_farenheit) - 32) / 1.8, 2)
        print(f"Det blir {temperature_celcius} grader Celcius.")
        if float(temperature_celcius) < 10:
            print(f"Det är bäst att ta på vinterkläder.")
        elif float(temperature_celcius) > 20:
            print(f"Det är bäst att packa badkläder.")


########################################
# 5 Miniräknare
########################################

user_number_1 = int(input("Ange tal 1: "))
user_number_2 = int(input("Ange tal 2: "))
user_number_3 = int(input("Ange tal 3: "))

print(f"\nSumman av de tre talen = {user_number_1 + user_number_2 + user_number_3}")

# Highest number
if user_number_1 >= user_number_2 and user_number_1 >= user_number_3:
    highest_number = user_number_1
elif user_number_2 >= user_number_1 and user_number_2 >= user_number_3:
    highest_number = user_number_2
else:
    highest_number = user_number_3

print(f"Det högsta talet är {highest_number}")

# Lowest number
if user_number_1 <= user_number_2 and user_number_1 <= user_number_3:
    lowest_number = user_number_1
elif user_number_2 <= user_number_1 and user_number_2 <= user_number_3:
    lowest_number = user_number_2
else:
    lowest_number = user_number_3

# Middle number
if (user_number_1 == user_number_2 == user_number_3 or
        user_number_1 != user_number_2  and
        user_number_1 != user_number_3 and
        user_number_2 != user_number_3):
    middle_number = user_number_1 + user_number_2 + user_number_3 - highest_number - lowest_number
    print(f"Talet i mitten är {middle_number }")

# Two or three even
if user_number_1 == user_number_2 == user_number_3:
    print(f"Samtliga tre tal ({user_number_1}) är lika")
elif user_number_1 == user_number_2 or user_number_1 == user_number_3:
    print(f"Två tal ({user_number_1}) är lika")
elif user_number_2 == user_number_3 or user_number_2 == user_number_3:
    print(f"Två tal ({user_number_2}) är lika")

"""
Testmatris
__________________________________________________________
- t1 | t2 | t3 | Störst | Två lika | Tre lika | Mellerst -
----------------------------------------------------------
  1  | 2  | 3  |   3    |    -     |     -    |    2     |
  1  | 3  | 2  |   3    |    -     |     -    |    2     |
  3  | 2  | 1  |   3    |    -     |     -    |    2     |
  -1 | -3 | -1 |   -1   |    -1    |     -    |    -     |
  9  | 9  | 9  |   9    |    -     |     9    |    9     |
  32 | 32 | 16 |   32   |    32    |     -    |    -     |

"""
