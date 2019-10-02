name = input("Please enter your name:")
bday = input("Please enter your numerical  birthday (month/day):")

bdayParts = bday.split("/")
month = int(bdayParts[0])
day = int(bdayParts[1])

if (( month == 3 and day >= 21 ) or (month == 4 and day <=20)):
	zodiac = "Aries"
elif((month == 4 and day >= 21) or (month == 5 and day <= 21)):
	zodiac = "Taurus"
elif((month == 5 and day >= 22) or (month == 6 and day <= 21)):
	zodiac = "Gemini"
elif((month == 6 and day >= 22) or (month == 7 and day <= 23)):
	zodiac = "Cancer"
elif((month == 7 and day >= 24) or (month == 8 and day <= 23)):
	zodiac = "Leo"
elif((month == 8 and day >= 24) or (month == 9 and day <= 23)):
	zodiac = "Virgo"
elif((month == 9 and day >= 24) or (month == 10 and day <= 23)):
	zodiac = "Libra"
elif((month == 10 and day >= 24) or (month == 11 and day <= 22)):
	zodiac = "Scorpio"
elif((month == 11 and day >= 23) or (month == 12 and day <=22)):
	zodiac = "Sagittarius"
elif((month == 12 and day >= 23) or (month == 1 and day <=20)):
	zodiac = "Capricorn"
elif((month == 1 and day >= 21) or (month == 2 and day <=19)):
	zodiac = "Aquarius"
else:
	zodiac = "Pisces"

print("\n\n" + name + ", your zodiac sign is: " + zodiac + "\n")
