while True:
    word = input("Type a 4 character word: ")

    if len(word) > 4 or len(word) < 4:
        print(word + " Has " + str(len(word)) + " characters")
    else:
        print("Word : " + word + " read successfully")
        break
