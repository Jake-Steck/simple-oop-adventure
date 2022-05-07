
import time

class Basic:
    def instructions():
        print("""*** Welcome to the North American Adventure Game! ***
        To play this game, choose from the list of adventures that will be prompted.
                            \nAre you ready to play?  """)
        input("\nIf you are ready press enter")


class Location:

    def display_locations():
        locations = ["Canada", "USA", "Mexio", "Don't travel"]
        print("\nHere are the following locations you can travel to:")
        num = 1
        for location in locations:
            print(num, "-", location)
            num += 1

        pick = input("Which location do you want to travel to? (Enter corresponding number): ")
        if pick == "1":
            Interactions.canada()
        elif pick == "2":
            Interactions.usa()
        elif pick == "3":
            Interactions.mexico()
        else:


class Interactions:

    def canada():
        print("welcome to Canada! Eh!")
        print("We have just made it to Toronto International Airport!")
        time.sleep(1)
        print("\nOh what do we see here...? I think it is a person! Lets see what they have to say...")
        time.sleep(1)
        print("\nMan: Hi! Welcome to Toronto, we are glad to see you. Why don't we go and get some food")
        input("Press enter to continue")
        Interactions.resturant()

    def resturant():
        menu = ["Plain Poutine", "Bacon Poutine", "Veggie Poutine", "Loaded Poutine"]
        print("Man: This is one of Toronto's best resturants: NomNom Poutine")
        time.sleep(1)
        want_to_know = input("\nMan: Do you want to know what poutine (y/n)? If (n) then you will continue to the resturant")
        if want_to_know.lower() == "y":
            print("\nMan: Classic poutine is made of a plate of hot and crispy French fries, topped with chunks of just melting fresh cheese curds, and smothered in a savory and salty gravy!")
        elif want_to_know.lower() == "n":
            print("\nMan: Ok! On to ordering!")
        else:
            print("Invalid input.")

        input("\nPress enter to continue")

        print("Here is the menu")
        num = 1
        for item in menu:
            print(num, "-", item)
            num+=1
        Interactions.menu_choice()

    def menu_choice():
        choice = input("What item do you want? (Enter corresponding number): ")

        if choice == "1":
            print("Man: Mmmm smells so good!")
            time.sleep(.5)
            print("Man: Anyways, eat up!")
        elif choice == "2":
            print("Man: Yum!")
            time.sleep(.5)
            print("Man: Anyways, eat up!")
        elif choice == "3":
            print("Man: Mmmm!")
            time.sleep(.5)
            print("Man: Anyways, eat up!")
        elif choice == "4":
            print("Man: My favorite!")
            time.sleep(.5)
            print("Man: Anyways, eat up!")
        else:
            print("That item isn't on the menu!")
            Interactions.menu_choice()

        time.sleep(1)
        Interactions.leave_canada()


    def leave_canada():
        print("We're going to miss our flight! We need to go!")
        time.sleep(1)
        print("Man: Bye! It was nice to meet you! See you soon! Eh!")
        input("Press enter to continue")
        Location.display_locations()


    def mexico():
        print("\n¡Bienvenidos a México! (Welcome to Mexico!)")
        time.sleep(1)
        print("\nWe have arrived at Cancun Internation Airport")
        time.sleep(1)
        print("\nWhats that I see over there?....It seems to be a bus to the beach!")
        time.sleep(1)
        go_to_beach = input("\nWould you like to go to the beach!? (y/n) ")
        if go_to_beach.lower() == "y":
            Interactions.beach()
        elif go_to_beach.lower() == "n":
            print("Well then... back to the airport...")
            input("Press enter to continue")

            Locations.display_locations()

    def beach():
        time.sleep(.5)
        print("Wow it is so warm and tropical here")
        ask_jetski = input("\nLook over there, there are jetskis. Do you want to go on them? (y/n): ")
        if ask_jetski.lower() == "y":
            print("\nOk lets go...")
            for i in range(4):
                print("Jetskiing....")
                time.sleep(.5)
            print("Oh wasn't that fun!")
        elif ask_jetski.lower() == "n":
            print("Ok then. Onto our next activity...")
        else:
            print("Invalid. Moving onto next activity")
        input("Press enter to continue")

        Interactions.snorkle()

    def snorkle():
        time.sleep(.5)
        print("\nLets go snorkling!")
        print("Here, put on this gear")
        time.sleep(1)
        touch_ray = input("Wow look at this! Its a sting-ray.. Do you want to try and touch it? (y/n): ")
        if touch_ray.lower() == "y":
            print("OUCH! THAT HURT A LOT!")
        elif touch_ray.lower() == "n":
            print("I think you made the right decision")
        else:
            print("Invalid, continuing")

        time.sleep(1)
        print("\nOh no! Its time to head back to the airport...")
        input("Press enter to continue")

        Location.display_locations()

    def usa():
        print("Welcome to the United States of America!")
        time.sleep(1)
        print("We have landed at John F. Kennedy International Airport, located in the Big Apple!")
        time.sleep(1)
        statue_of_liberty = input("How about we go sightseeing... how does the statue of liberty sound? Want to go? (y/n): ")
        if statue_of_liberty.lower() == "y":
            print("Wow it is so cool here.")
            time.sleep(.5)
            walk = input("Look over there. Want to go to the top? (y/n): ")
            print("\nWow, it is such a good view from up here, it is nice and breezy too!")
            input("Press enter to continue")
        elif statue_of_liberty.lower() == "n":
            print("Ok, we can take the ferry back to Manhatten.")
        else:
            print("Invalid. Taking a ferry back to Manhatten")

        print("Lets go get a hot dog from the vendors on the street..")
        time.sleep(1)
        print("\nMmmm so good. ")
        time.sleep(1)
        print("Oh no! It is time to go back to the airport... :( It has been very fun.")
        input("Press enter to continue")
        Location.display_locations()

def main():
    name = input("What is your name? ")
    print("\nHi,", name, "my name is Jake, and I am your travel guide!")
    input("\nPress enter to continue")
    Basic.instructions()
    Location.display_locations()


main()
