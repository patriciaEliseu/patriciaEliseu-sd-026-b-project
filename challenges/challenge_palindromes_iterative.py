def is_palindrome_recursive(word, low_index, high_index):
    word = word.lower()
    if len(word) == 0:
        return False
    elif len(word) <= 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    elif word[0] == word[-1]:
        return is_palindrome_recursive(word[1:-1], word[0], word[-1])
    else:
        return False


def merge_sort(word: str) -> str:
    if len(word) > 1:
        mid = len(word) // 2
        left = merge_sort(word[:mid])
        right = merge_sort(word[mid:])
        word = (left, right)
    return word
