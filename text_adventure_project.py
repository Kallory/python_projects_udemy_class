print('''
                           (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\\
                            (_)                 /  \  /\\
                    ________[_]________      /\/    \/  \\
           /\      /\        ______    \    /   /\/\  /\/\\
          /  \    //_\       \    /\    \  /\/\/    \/    \\
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \\
 /\/\/\/       //_______\       \|__|      \\
/      \      /XXXXXXXXXX\                  \\
        \    /_I_II  I__I_\__________________\\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~
''')


print("Welcome to Kodesk mountains!")
print("You must find the lost gem!\n")
print("You leave your cozy cabin in the woods and see the vast Kodesk Mountains before you.")
print("You head up the trail to find the lost gem and come to a fork in the road.")
chosen_direction = input("Do you turn left or right?\n")

if chosen_direction.upper() != "left":
    print("you died!")
