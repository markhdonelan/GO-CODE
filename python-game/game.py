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
        "Name": "3rd Gen ECM",
        "Tech Level": 11,
        "Size": 5,
        "Cost": 100,
        "Mandatory": False,
    },
    {
        "Name": "Cargo Bay",
        "Tech Level": 1,
        "Size": 1,
        "Cost": 1,
        "Mandatory": True,
    },
    {
        "Name": "Laser Cannon",
        "Tech Level": 1,
        "Size": 3,
        "Cost": 30,
        "Mandatory": False,
    },
    {
        "Name": "Point Defense System",
        "Tech Level": 3,
        "Size": 3,
        "Cost": 90,
        "Mandatory": False,
    },
    {
        "Name": "Life Support System",
            "Tech Level": 1,
            "Size": 2,
            "Cost": 20,
            "Mandatory": True,
        },
]


def main() -> None:
    print("Welcome to your Python game!")
    answer_game = input("Do you want to play the game? ").strip().lower()

    if answer_game == "yes":
        print("good!")
        print("Ship parts data:")
        print(ship_parts)

        while True:
            answer_design = input("What tech level is your starship? ").strip()
            try:
                answer_design = int(answer_design)
                break
            except ValueError:
                print("Please enter a valid integer.")

        print(f"Your starship tech level is {answer_design}.")

        print("Matching ship parts:")
        for part in ship_parts:
            if part["Tech Level"] <= answer_design:
                print(part)

        if answer_design >= 1:
            print("ok let's do it!")
        else:
            print("ok we won't")
    else:
        print("ok we won't play the game")


if __name__ == "__main__":
    main()
