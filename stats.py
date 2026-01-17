def get_character_count_from_text(text):
    character_count_map = {}
    lower_case_text = text.lower()
    for character in lower_case_text:
        if character in character_count_map:
            character_count_map[character] += 1
        else:
            character_count_map[character] = 1
    return character_count_map


def get_num_words(text):
    words = text.split()
    return len(words)
