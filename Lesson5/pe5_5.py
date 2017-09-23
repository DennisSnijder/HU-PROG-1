def get_average_word_length(sentence: str) -> float:
    word_count: int = 0
    character_count: int = 0

    for word in sentence.split(' '):
        word_count += 1
        character_count += len(word)

    return character_count / word_count


user_input = input("Enter a sentence to get the average word count: ")

print(get_average_word_length(user_input))
