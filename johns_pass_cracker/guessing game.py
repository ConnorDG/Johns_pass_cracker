"""
    Guessing Game
    Connor Gibson
    1.0.1
    changes:
        1.0.1: minor changes
"""
from random import randint

print("Help the alien back to hits home planet by guessing the right number")
print(r"""
       ______
      /_.  ._ 
     (( \\// ))
      \\ \/ //
       \\/\//
  \\\  ( '' )  ///
   )))  \__/  (((
  (((.'__||__'.)))
   \\  )    (  //
    \\/.'  '.\//
     \/ |,,| \/
        |  |
        |  |
        //\\ 
       //  \\
      ||    ||
      ||    ||
      ||    ||
   ___))    ((___
  (____)    (____)

""")
out = randint(1, 101)
while True:
    guess = int(input("guess the number: "))
    if guess == out:
        print("\nGreat Job, the alien can return home")
        print(r"""
                _____
             ,-       -.
            / o       o \ 
           /   \     /   \ 
          /     )- -(     \ 
         /     ( 6 6 )     \ 
        /       \ " /       \ 
       /         )=(         \ 
      /   o   .-- - --.   o   \ 
     /    I  /  -   -  \  I    \ 
 .--(    (_}y/\       /\y{_)    )--.
(     .___l\/__\_____/__\/l___,     )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| 
         `==.___________.==' 
        """)
        break
    elif out > guess:
        print("guess again, you guess was low")
    elif out < guess:
        print("guess again, you guess was high")
input("press enter to quit")