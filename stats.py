def get_num_words(text: str) -> str:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, str]:
    counts = {}

    for char in text:
        char = char.lower()  # Turn character to lowercase
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    return counts


def sort_on(d):
    # Sort by the dictionary key "num"
    return d["num"]


def chars_dict_to_sorted_list(chars_counts: dict[str, str]) -> list[dict[str, str]]:
    chars_list = []

    # Populate the list of counts and sort them
    for char, count in chars_counts.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
