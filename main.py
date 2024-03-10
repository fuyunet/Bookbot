def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        dict = character_count(file_contents)
        list_dict = sorted_converted_dict(dict)

        print_report(f,num_words ,list_dict)

def sort_on(dict):
    return dict["num"]

def get_num_words(text: str):
    words = text.split()
    return len(words)

def character_count(text: str):
    text_lower = text.lower()
    dict = {}
    for char in text_lower:
        if char.isalpha():
            if not char in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict

def sorted_converted_dict(dict: dict):
    list_dict = []
    for key in dict:
        list_dict.append({'name': key, "num": dict[key]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def print_report(f, num_words: int, list_dict: list):
    print("--- Begin report of " + f.name + " ---")
    print(str(num_words) + " words found in the document" + '\n'*2)
    for dict in list_dict:
        print("The '" + dict["name"] + "' character was found " + str(dict["num"]) + " times")
    print("--- End report ---")

main()
