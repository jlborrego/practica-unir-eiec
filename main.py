import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_SORT_ORDER = "asc"  # Default sort order is ascending

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    sort_order = DEFAULT_SORT_ORDER

    # Check for command line arguments
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        sort_order = sys.argv[3].lower() == "desc"
    else:
        print("Use: python script.py <file_number> <delete_duplicates: yes|no> <order: asc|desc>")
        print("The file must be specified as the first argument")
        print("The second argument indicates whether duplicates should be removed")
        sys.exit(1)

    print(f"The words from the file {filename} will be read")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_words = sort_list(word_list, ascending=(sort_order == "asc"))
    print(sorted_words)
    print(sort_list(word_list))
