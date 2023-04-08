# From here http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/CC_CHARS.HTML
# http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/SCC_FORMAT.HTML

standard_characters = {
        '20': ' ',
        'a1': '!',
        'a2': '"',
        '23': '#',
        'a4': '$',
        '25': '%',
        '26': '&',
        'a7': '\'',
        'a8': '(',
        '29': ')',
        '2a': 'á',
        'ab': '+',
        '2c': ',',
        'ad': '-',
        'ae': '.',
        '2f': '/',
        'b0': '0',
        '31': '1',
        '32': '2',
        'b3': '3',
        '34': '4',
        'b5': '5',
        'b6': '6',
        '37': '7',
        '38': '8',
        'b9': '9',
        'ba': ':',
        '3b': ';',
        'bc': '<',
        '3d': '=',
        '3e': '>',
        'bf': '?',
        '40': '@',
        'c1': 'A',
        'c2': 'B',
        '43': 'C',
        'c4': 'D',
        '45': 'E',
        '46': 'F',
        'c7': 'G',
        'c8': 'H',
        '49': 'I',
        '4a': 'J',
        'cb': 'K',
        '4c': 'L',
        'cd': 'M',
        'ce': 'N',
        '4f': 'O',
        'd0': 'P',
        '51': 'Q',
        '52': 'R',
        'd3': 'S',
        '54': 'T',
        'd5': 'U',
        'd6': 'V',
        '57': 'W',
        '58': 'X',
        'd9': 'Y',
        'da': 'Z',
        '5b': '[',
        'dc': 'é',
        '5d': ']',
        '5e': 'í',
        'df': 'ó',
        'e0': 'ú',
        '61': 'a',
        '62': 'b',
        'e3': 'c',
        '64': 'd',
        'e5': 'e',
        'e6': 'f',
        '67': 'g',
        '68': 'h',
        'e9': 'i',
        'ea': 'j',
        '6b': 'k',
        'ec': 'l',
        '6d': 'm',
        '6e': 'n',
        'ef': 'o',
        '70': 'p',
        'f1': 'q',
        'f2': 'r',
        '73': 's',
        'f4': 't',
        '75': 'u',
        '76': 'v',
        'f7': 'w',
        'f8': 'x',
        '79': 'y',
        '7a': 'z',
        'fb': 'ç',
        '7c': '÷',
        'fd': 'Ñ',
        'fe': 'ñ',
        '7f': '',
        '80': '',
}


special_characters = {
    '91b0': '®',
    '9131': '°',
    '9132': '½',
    '91b3': '¿',
    '91b4': '™',
    '91b5': '¢',
    '91b6': '£',
    '9137': '♪',
    '9138': 'à',
    '91b9': ' ',
    '91ba': 'è',
    '913b': 'â',
    '91bc': 'ê',
    '913d': 'î',
    '913e': 'ô',
    '91bf': 'û'
}


extended_characters = {
    '9220': 'Á',
    '92a1': 'É',
    '92a2': 'Ó',
    '9223': 'Ú',
    '92a4': 'Ü',
    '9225': 'ü',
    '9226': '‘',
    '92a7': '¡',
    '92a8': '*',
    '9229': '’',
    '922a': '—',
    '92ab': '©',
    '922c': '℠',
    '92ad': '•',
    '92ae': '“',
    '922f': '”',
    '92b0': 'À',
    '9231': 'Â',
    '9232': 'Ç',
    '92b3': 'È',
    '9234': 'Ê',
    '92b5': 'Ë',
    '92b6': 'ë',
    '9237': 'Î',
    '9238': 'Ï',
    '92b9': 'ï',
    '92ba': 'Ô',
    '923b': 'Ù',
    '92bc': 'ù',
    '923d': 'Û',
    '923e': '«',
    '92bf': '»',
    '1320': 'Ã',
    '13a1': 'ã',
    '13a2': 'Í',
    '1323': 'Ì',
    '13a4': 'ì',
    '1325': 'Ò',
    '1326': 'ò',
    '13a7': 'Õ',
    '13a8': 'õ',
    '1329': '{',
    '132a': '}',
    '13ab': '\\',
    '132c': '^',
    '13ad': '_',
    '13ae': '¦',
    '132f': '~',
    '13b0': 'Ä',
    '1331': 'ä',
    '1332': 'Ö',
    '13b3': 'ö',
    '1334': 'ß',
    '13b5': '¥',
    '13b6': '¤',
    '1337': '|',
    '1338': 'Å',
    '13b9': 'å',
    '13ba': 'Ø',
    '133b': 'ø',
    '13bc': '┌',
    '133d': '┐',
    '133e': '└',
    '13bf': '┘',
}


in_command = "94ae"
out_command = "942c"

# THis is only the concept idea of convertirn scc to srt 
# Open the SCC file for reading
with open('caps.scc', 'r') as f:
    # Read the contents of the file line by line
    new_line = f.readlines()



position = 0
captions = {}
line = []
break_added = False


for each_line in new_line:
    
    # Skips the empty lines
    if not each_line.strip():
        continue
    
    cc_line = each_line.split()
    

    if cc_line[0] == 'Scenarist_SCC':
        continue
    else:
        timecode = cc_line[0]

# Avoid cc_line[1] as it is always the same command as cc_line[2] but repeated
    content = cc_line[2::]






    for i in content:
        comparer = i[0:2]
        match i[0:2]:

            case '91':
                line.append(special_characters[i])

            case '92' | '13':
                line.append(extended_characters[i])

            case '94':
                if i == in_command:
                    line.insert(0, f'{timecode} --> ')
                elif i == out_command:
                    line[0] = line[0] + timecode
                    if '\n' not in line[1]:
                        line[0] = line[0] + '\n'
                    
                    if '♪' in line and line[len(line) -1] != '♪':
                        line.append('♪')
                    
                    line.append('\n')

                    captions[f'line{position}'] = "".join(line)
                    break_added = False
                    position += 1

                    line = []

                elif i == '9470' and break_added == False:
                    if not break_added:
                        line.append('\n')
                        break_added = True

                else:
                    continue

            case _:
                line.append(standard_characters[i[0:2]])
                line.append(standard_characters[i[2:4]])

# i = 0
# while i < position:
#     print(captions[f'line{i}'])
#     i += 1

# Use a for loop to iterate through the range of positions
for i in range(position):
    print(f"{i + 1}\n{captions[f'line{i}']}")

    # Write each caption to the output file
    with open('output.srt', 'a') as f:
        f.write(f'{i+1}\n{captions[f"line{i}"]}\n')
