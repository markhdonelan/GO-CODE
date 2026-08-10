ship_parts = [
    {
        "Name": "Engine",
        "Tech Level": 1,
        "Size": 2,
        "Cost": 10,
        "Mandatory": True,
    },
    {
        "Name": "Shield Generator",
        "Tech Level": 1,
        "Size": 1,
        "Cost": 10,
        "Mandatory": False,
    },
    {
        "Name": "Cargo Bay",
        "Tech Level": 1,
        "Size": 1,
        "Cost": 1,
        "Mandatory": False,
    },
]


def main() -> None:
    print("Welcome to your Python game!")
    answer = input("Do you want to play the game? ").strip().lower()

    if answer == "yes":
        print("good!")
        print("Ship parts data:")
        print(ship_parts)
        answer = input("Do you want to design a starship?").strip().lower()
        if answer == "yes":
            print("ok let's do it!")
        else:
            print("ok we won't")
    else:
        print("ok we won't play the game")


if __name__ == "__main__":
    main()
