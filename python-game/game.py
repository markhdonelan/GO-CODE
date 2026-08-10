def main() -> None:
    print("Welcome to your Python game!")
    answer = input("Do you want to play the game? ").strip().lower()

    if answer == "yes":
        print("good!")
        answer = input("Do you want to design a starship?").strip().lower()
        if answer == "yes": 
            print("ok let's do it!")
        else:
            print("ok we won't")                          
    else:
        print("ok we won't play the game")


if __name__ == "__main__":
    main()
