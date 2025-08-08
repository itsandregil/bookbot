def get_num_words(text: str) -> str:
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict[str, str]:
    counts = {}

    for char in text:
        char = char.lower()  # Turn character to lowercase
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    return counts


def sort_on(items):
    return items["num"]


def get_sorted_chars(chars_counts: dict[str, str]) -> list[dict[str, str]]:
    chars_list = []

    # Populate the list of counts
    for char, count in chars_counts.items():
        chars_list.append({"char": char, "num": count})

    # Sort values by their count
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
