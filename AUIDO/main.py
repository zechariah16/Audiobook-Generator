import pyttsx3

try:
    # Open the file and read its lines
    with open("book.txt", 'r') as book:
        book_text = book.readlines()
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

    # Ask user for voice preference
    options = input("What voice do you want? if male type m, if female type f: ")

    # Determine voice choice
    if options == "m":
        choice = 0
    else:
        choice = 1

    # Set voice properties
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    engine.setProperty('rate', 125)  # setting up new voice rate

    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level between 0 and 1

    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[choice].id)  # changing index, changes voices. 0 for male, 1 for female

    # Iterate through lines and read them aloud
    for line in book_text:
        engine.say(line)
        engine.runAndWait()

    # Saving the spoken text to an audio file
    # On Linux, make sure 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(' '.join(book_text), 'tests.mp3')
    engine.runAndWait()

except FileNotFoundError:
    print("Error: 'book.txt' not found. Make sure the file exists in the correct location.")
