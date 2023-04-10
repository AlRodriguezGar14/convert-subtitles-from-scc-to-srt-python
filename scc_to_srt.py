#!/usr/bin/env python3.10

import argparse
from timecode_class import Timecode_Parser
from scc_codes import STANDARD_CHARACTERS, SPECIAL_CHARACTERS, EXTENDED_CHARACTERS



# From here http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/CC_CHARS.HTML
# http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/SCC_FORMAT.HTML


in_command = "94ae"
out_command = "942c"

# THis is only the concept idea of convertirn scc to srt 


def read_scc(path):
    # Open the SCC file for reading
    with open(path, 'r') as f:
        # Read the contents of the file line by line
        return f.readlines()



def convert_from_scc_to_srt(file, fps, drop_frame):

    in_timecode = ""
    in_timecode_totals = 0
    position = 0
    captions = {}
    line = []
    break_added = False
    
    #fps = input("Tell me, which is the output framerate?\n")
    
    match fps:
        case 23.0 | 23,976 | 23.98:
            fps = 23.976
        case 25.0:
            fps = 25.0
        case 24.0:
            fps = 24.0
        case 29.0 | 29.97:
            fps = 29.97
        case 30.0:
            fps = 30.0
        case _:
            print('No valid fps introduced. The default is 23.976')
            fps = 23.976

    
    for each_line in file:
        
        # Skips the empty lines
        if not each_line.strip():
            continue
        
        cc_line = each_line.split()
        

        if cc_line[0] == 'Scenarist_SCC':
            continue
        else:
            timecode = cc_line[0]

            converted_tc = Timecode_Parser(timecode, fps, drop_frame)
            #print(converted_tc)

# Avoid cc_line[1] as it is always the same command as cc_line[2] but repeated
        content = cc_line[2::]

        for i in content:

            match i[0:2]:

                case '91':
                    line.append(SPECIAL_CHARACTERS[i])

                case '92' | '13':
                    line.append(EXTENDED_CHARACTERS[i])

                case '94':
                    if i == in_command:
                        line.insert(0, f'{str(converted_tc).replace(".", ",")} --> ')
                        in_timecode = converted_tc.timecode
                        in_timecode_totals = converted_tc.total_frames
                    elif i == out_command:
                        in_tc = in_timecode
                        out_tc = converted_tc.timecode
                        if in_timecode_totals < converted_tc.total_frames:
                            line[0] = f'{in_tc} --> {out_tc}'
                        else:
                            line[0] = f'{out_tc} --> {in_tc}'
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
                    line.append(STANDARD_CHARACTERS[i[0:2]])
                    line.append(STANDARD_CHARACTERS[i[2:4]])


    return (captions, position)




def save_to_srt(captions, position, original_file):
    
    output = f'{original_file.removesuffix(".scc")}_converted.srt'

    # Write each caption to the output file
    with open(output, 'a') as f:
        for i in range(position):
            #print(f"{i + 1}\n{captions[f'line{i}']}")
            f.write(f'{i+1}\n{captions[f"line{i}"]}\n')

    print(f'Your file {output} has been generated succesfully')





if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Convert .scc files to .srt")
    parser.add_argument('path', type=str, help='Path to your .scc file')
    parser.add_argument('-f', '--fps', type=float, default=23.98, help='Output framerate. Default is 23.98')
    parser.add_argument('-df', '--drop_frame', action='store_true', help='Add it if you want to drop the frame')
    args = parser.parse_args()


    #path = input('Please, tell me the path to your file...\n')

    # read scc file
    try:
        file = read_scc(args.path)
    except:
        print('File not found')
        exit(1)

    # convert to srt
    captions, position = convert_from_scc_to_srt(file, args.fps, args.drop_frame)

    # save to srt 
    save_to_srt(captions, position, args.path)

    print(args.fps)





