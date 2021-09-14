print("WELCOME TO THE GAME OF QUIZ")
score = 0

# Question 1
answer1 = input("what is the example of volatile memory? \n a. RAM \n b. DVD \n c. Hard Disk \n d. Pen drive \n Answer: ")
if answer1 == "a" or answer1 == "RAM":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is RAM.")
    print("score: ", score)
    print("\n")

# Question 2
answer2 = input("Which temperature tranceducer has positive and negative temperature coefficient? \n a. Thermocouple \n b. RTD \n c. Thermistor \n d. All above \n Answer: ")
if answer2 == "c" or answer2 == "Thermistor":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Thermistor.")
    print("score: ", score)
    print("\n")

# Question 3
answer3 = input("....... resistance offered by LDR in the absence of light \n a. Low \n b. Very low \n c. Constant \n d. Dark \n Answer: ")
if answer3 == "d" or answer2 == "Dark":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Dark.")
    print("score: ", score)
    print("\n")

# Question 4
answer4 = input("The Earth day is observed on? \n a. Feb 16 \n b. April 4 \n c. April 22 \n d. Sep 17 \n Answer: ")
if answer4 == "c" or answer4 == "April 22":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is April 22.")
    print("score: ", score)
    print("\n")


# Question 5
answer5 = input("Name a clinical trial in which blood is transfused from recovered COVID-19 patients to a coronavitus patient who is in critical condition? \n a. Plasma Therapy \n b. Solidarity 4 \n c. Ramdesivir \n d. Hydroxychloroquine \n Answer: ")
if answer5 == "a" or answer5 == "Plasma Therapy":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Plasma Therapy.")
    print("score: ", score)
    print("\n")

# Question 6
answer6 = input("What is main aim of Kyoto Protocol? \n a. Petrol Conservation \n b. Earthquake control \n c. Global warming \n d. Conservation of wetlands \n Answer: ")
if answer6 == "c" or answer6 == "Global warming":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Global warming.")
    print("score: ", score)
    print("\n")

# Question 7
answer7 = input("Noise Pollution is measured in ......? \n a. Decibal \n b. Amperes \n c. Fathoms \n d. Ohm \n Answer: ")
if answer7 == "a" or answer7 == "Decibal":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Decibal.")
    print("score: ", score)
    print("\n")    
    
# Question 8
answer8 = input("DDT is ......? \n a. Green house gas \n b. Non-Degradable pollutant \n c. Degradable pollutant \n d. None of above \n Answer: ")
if answer8 == "b" or answer8 == "Non-Degradable pollutant":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Non-Degradable pollutant.")
    print("score: ", score)
    print("\n")

# Question 9
answer9 = input("Who was the brother of Ravan in Ramayana who helped lord Rama in War which was in between Lord Rama and Ravan? \n a. Vibhishan \n b. Kumbhkarn \n c. Aahiravan \n d. None of above \n Answer: ")
if answer9 == "a" or answer9 == "Vibhishan":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Vibhishan.")
    print("score: ", score)
    print("\n")

# Question 10
answer10 = input("In historical Ramayana Who was the father of Lord Rama? \n a. Dasharath \n b. Valmiki \n c. Vashisht \n d. None of above \n Answer: ")
if answer10 == "a" or answer10 == "Dasharath":
    score += 1
    print("score: ", score)
    print("correct!!! well played.")
    print("\n")
else:
    print("Incorrect!!! The answer is Dasharath.")
    print("score: ", score)
    print("\n")

# FINAL MESSAGE
if score <= 4:
    print("Your total score is:", score, "-Better luck next time!!!")
if score >= 5:
    print("Your total score is:", score, "Very Good!!!")