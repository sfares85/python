# Mad libs where libs get Mad
#  Start Below:

# Number: 6
# Noun(plural): chocolate milks
# Name: noug alrainy
# Any sentence: I would like to eat a bowl full of jelly.
# Verb: run

#     It was 6 o'clock when I hears a knock at the door.
#     I opened the door and there was a box full of chocolate milk with a note saying "From Mr. Noug Alrainy".
#     Just as I closed the door I heard a scream "I WOULD LIKE TO EAT A BOWL FULL OF JELLY.".
#     I froze in place and all I could do was run.
print('Mad libs where libs get Mad')
print('Start Below:\n')
print('')
#taking user input
Number =int(input("Number: "))
Noun = input("Noun(plural): ")
Name = input("Name: ")
Name = Name.capitalize()
Any_sentence = input("Any sentence: ")
Any_sentence = Any_sentence.upper()
verb = input("Verb: ")
#final statment
print('\n\n    It was %d o\'clock when I hears a knock at the door.\n    I opened the door and there was a box full of %s with a note saying "From Mr. %s".\n    Just as I closed the door I heard a scream "%s".\n    I froze in place and all I could do was %s.' % (Number,Noun,Name,Any_sentence,verb))