def process_text():
    text = input("Enter your Text: ")
    choice = input("how to show your text? (1: Normal, 2: revers)")
    if choice == "1":
        print(text)
    elif choice == "2":
        print(text[::-1])
    else:
        print("invalid input!")

process_text()