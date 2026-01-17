from stats import get_character_count_from_text, get_num_words


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print()

    character_count_map = get_character_count_from_text(text)
    alpha_character_count_mapping_list = get_alpha_character_count_mapping_list(
        character_count_map
    )

    print_character_count_mapping_list(alpha_character_count_mapping_list)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_alpha_character_count_mapping_list(character_count_map):
    alpha_character_count_mapping_list = []
    for character in character_count_map:
        if character.isalpha() == True:
            alpha_character_count_mapping_list.append(
                {"name": character, "num": character_count_map[character]}
            )
    alpha_character_count_mapping_list.sort(key=sort_on, reverse=True)

    return alpha_character_count_mapping_list


def sort_on(dict):
    return dict["num"]


def print_character_count_mapping_list(alpha_character_count_mapping_list):
    for character in alpha_character_count_mapping_list:
        print(f"The '{character['name']}' character was found {character['num']} times")


if __name__ == "__main__":
    main()
