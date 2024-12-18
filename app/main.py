def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        while True:
            text = input("Enter new line of content: ")
            if text.lower() == "stop":
                break
            else:
                file.write(text + "\n")


if __name__ == "__main__":
    main()
