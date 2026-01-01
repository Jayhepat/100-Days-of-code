def determine_color(s: str) -> str:
    if len(s) != 2:
        return "Invalid input"

    col = s[0].lower()
    if col < 'a' or col > 'h':
        return "Invalid input"

    if not s[1].isdigit():
        return "Invalid input"
    row = int(s[1])
    if row < 1 or row > 8:
        return "Invalid input"

    col_num = ord(col) - ord('a') + 1

    if (col_num + row) % 2 == 0:
        return "Black"
    else:
        return "White"


if __name__ == "__main__":
    s = input().strip()
    print(determine_color(s))

    
