
morse_code_rules = {
    'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 'H': '····', 'I': '··', 'J': '·---',
    'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-',
    'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··',
    '0': '-----', '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····', '6': '-····', '7': '--···', '8': '---··', '9': '----·',
    '.': '·-·-·-', ',': '--··--', '?': '··--··', "'": '·----·', '!': '-·-·--', '/': '-···-', '(': '-·--·', ')': '-·--·-', '&': '·-···', ':': '---···',
    ';': '-·-·-·', '=': '-···-', '+': '·-·-·', '-': '-····-', '_': '··--·', '"': '·-··-·', '$': '···-··-', '@': '·--·-·'
}

still_on = True

while still_on:
    text = input('Please enter text you want to convert to Morse Code: ')
    letter = ''
    translated_text = ''
    for pos in range(0, len(text)):
        if text[pos].upper() in morse_code_rules:
            translated_text += morse_code_rules[text[pos].upper()]
        elif text[pos] == ' ':
            translated_text += ' / '


    print(f"{text} translate to: {translated_text}")
    another_text = input("Would you like to convert another text? (Y/N): ").upper()
    if another_text == 'N':
        still_on = False










