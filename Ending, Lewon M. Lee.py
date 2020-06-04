import time


def storyline3():
    story3_while = True
    while story3_while:
        time.sleep(3)
        print("Finally, as you defeat the final monster, you reach the one door and escape the terrible mansion. "
              "You immediately go to the\ncity to tell people of your findings. Fortunately, you took some "
              "photos while on your time there to prove\nto people that you weren't making it up. Days later, "
              "your report on these creatures made headlines,\nand panic over what they should do about this "
              "house rose. And questions were created, left unanswered: 'Who could have done such a thing to these\n"
              "poor people?', 'Are these the only monsters that exist?', 'What are they?', and more.\nNone of these"
              " questions could be answered because no one knew what to say. 'These monsters look as if they came "
              "from a nightmare', one person said. \nAnd there is no way that all of these monsters stayed within the"
              " house, some may have escaped. \nMeaning there were these creatures roaming around the world, "
              "secretely waiting for the chance to attack...\n")
        time.sleep(5)
        storyline3_finished = input("\nAre you finished the story? (press 'enter' when done)")
        if storyline3_finished == 'yes':
            story3_while = False
        else:
            story3_while = False
        time.sleep(2)
        print("\nCREDITS:\nWriting: Lewon \nProgram: PyCharm \nLanguage: Python \nCoding: Lewon ")
        time.sleep(3)
        print("\nThank you for playing...\nTHE END")
