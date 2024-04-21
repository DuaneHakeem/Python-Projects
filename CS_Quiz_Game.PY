#Greeting
print("Welcome to my cyber security quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()
    
print("Okay! Let's play :)")
score = 0
#Q1
answer = input("What is a common method used by cybercriminals to gain unauthorized access to sensitive information by tricking individuals into providing their personal data? ")
if answer.lower() == "phishing":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
#Q2
answer = input("What is the term for a malicious software program that can replicate itself and spread to other computers or systems without the user's consent? ")
if answer.lower() == "worm":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")
#Q3
answer = input("What is the process of converting data into an unreadable format to prevent unauthorized access, often used to secure sensitive information during transmission or storage? ")
if answer.lower() == "encryption":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
#Q4 
answer = input("What security measure involves verifying the identity of a user or system before granting access to resources or information? ")
if answer.lower() == "authentication":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
#Q5
answer = input("What is the practice of disguising a message or communication to make it appear as if it comes from a trusted or legitimate source, often used by attackers to deceive recipients? ")
if answer.lower() == "spoofing":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
#Result
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
