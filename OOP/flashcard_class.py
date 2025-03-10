class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning


    def __str__(self):
        return self.word + ":" + self.meaning


flash = []
char = 1

while(char != 0):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of the word: ")
    obj = Flashcard(word, meaning)
    flash.append(obj)

    char = int(input("Enter zero for exiting flashcard app and other positive number for creating the new one: "))

    if(char <= 0):
        break

print("Flashcards")
count = 1
for i in flash:
    print(f"Flashcard #{count}")
    print(i)
    count += 1