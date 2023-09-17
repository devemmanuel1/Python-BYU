 # In this program I added a sentence to the end of the story.
print("\n \n \n # In this program you are expected to enter the corresponding words in the spaces provided # \n \n \n The other day, I was really in trouble. It all started when I saw a very [adjective] [animal] [verb] down the hallway. [exclamation]! I yelled. But all I could think to do was to [verb] over and over. Miraculously, that caused it to stop, but not before it tried to [verb] right in front of my family. # But lucky enough I grabbed a knife and chopped off its head. \n \n \n \n ")



adjective = input('enter an adjective eg. (wild): ')
animal = input('enter the name of animal: eg. (tiger): ')
verb = input('enter a verb eg. (walk):  ')
exclamation = input('enter an exclamation eg. (yikes): ').capitalize()
verb = input('enter a verb eg. (run): ')
verb = input('enter a verb eg. (jump): ')


print(f"\n \n The other day, I was really in trouble. It all started when I saw a very {adjective} {animal.capitalize()} {verb} down the hallway. {exclamation}! I yelled. But all I could think to do was to {verb} over and over. Miraculously, that caused it to stop, but not before it tried to {verb} right in front of my family. But lucky enough I grabbed a knife and chopped off its head.")