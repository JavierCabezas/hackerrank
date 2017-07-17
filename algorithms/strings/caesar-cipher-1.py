A_int = ord('A')
Z_int = ord('Z')
a_int = ord('a')
z_int = ord('z')

def get_letter(letter, offset):
    offset = offset % 26
    ascii_letter = ord(letter)

    is_in_range = ascii_letter >= A_int and ascii_letter <= Z_int or ascii_letter >= a_int and ascii_letter <= z_int
    if not is_in_range:
        return letter

    is_lowercase = ascii_letter >= a_int and ascii_letter <= z_int
    if (offset + ascii_letter > z_int and is_lowercase):
        ascii_letter = (offset + ascii_letter) - z_int + a_int - 1
    elif (offset + ascii_letter > Z_int and not is_lowercase):
        ascii_letter = (offset + ascii_letter) - Z_int + A_int - 1
    else:
        ascii_letter = ascii_letter + offset

    return chr(ascii_letter)

n = int(input().strip())
string_to_cipher = input().strip()
offset = int(input().strip())

print("".join([get_letter(letter, offset) for letter in string_to_cipher]))