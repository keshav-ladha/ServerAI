import os, random, time   #os to open a music file , random to select random music from the file and time to make the program sleep for a while.

command = ""  #to store the command written by nodeJs
while True:
    with open("commands.txt", 'r') as f:
        command = f.read()  #reads the command written by nodeJs
    with open("commands.txt", 'w') as f:
        f.write("")#after reading and storing the command this would make the file completely empty

    if "play music" in command:   #sample function that open a music file if 'play music' is the command
        os.chdir("<Music Directory Path>")   #change the path to the place where all songs are located
        len = len(os.listdir())-1    #number of songs in the music folder
        value = random.randint(0,len)
        music_dir = '<Music Directory Path>'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[value]))
    time.sleep(2)          #sleeps for 2 secs after running once