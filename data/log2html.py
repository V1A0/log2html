# -*- coding: utf8 -*-
import argparse
import os
from progress.bar import Bar

# - - - - - - - - - - - - - - - - - - M A I N   F U N C - - - - - - - - - - - - - - - - - - #
def add_data():
    # - - - - - - - - - - - - DEFAULT html page - - - - - - - - - - - - #
    def defdat(part, file_name):

        # - - - - - - - - FIND PLACE FOR TABLE - - - - - - - - - #
        with open("default.txt", 'r', encoding="utf8") as def_data:
            for num, line in enumerate(def_data, 1):
                if '<!--LOG-TABLE-HERE-->' in line:
                    ent_l = num-1 #start line (for past tabe)
                    end_l = -1*(num-1) #end line (for past tabe)
        def_data.close()
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


        with open("default.txt", 'r', encoding="utf8") as def_data:

            # - - - - - - - ADD 1'ST TEMPLATE PART - - - - - - - - #
            if part == 1:
                html = open(file_name, 'w', encoding="utf8")
                all_lines = def_data.readlines()
                tail = all_lines[:ent_l]
                for line in tail:
                    html.write(line)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - #

            # - - - - - - - ADD 2'ND TEMPLATE PART - - - - - - - #
            elif part == 2:
                html = open(file_name, 'a', encoding="utf8")

                html.write("<tr span=\"2\" align=center style=\"background:Green; color:White\"><td align=\"right\"> TOTAL ONLINE TIME </td><th></th><td>" +
                           str(online_c // 60) + "h " + str(online_c - (online_c // 60)*60) + "m </td></tr>\n")
                dat = def_data.readlines()
                tail = dat[end_l:]
                for line in tail:
                    html.write(line)
                html.write("\n<!-- Converted to HTML using log2html"
                           "\nGitHub: github.com/V1A0/log2html"
                           "\nCopyright © 2019 Vladimir Ageenko (V1A0)"
                           "\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of"
                           "\nthis software and associated documentation files (the \"Software\"), to deal in"
                           "\nthe Software without restriction, including without limitation the rights to"
                           "\nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies"
                           "\nof the Software, and to permit persons to whom the Software is furnished to "
                           "\nso, subject to the following conditions:"
                           "\n\nThe above copyright notice and this permission notice shall be included in all"
                           "\ncopies or substantial portions of the Software."
                           "\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"
                           "\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"
                           "\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"
                           "\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"
                           "\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"
                           "\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE"
                           "\nSOFTWARE.-->")
            # - - - - - - - - - - - - - - - - - - - - - - - - - - -#

            # - - - - - - - WRONG PART OF TEMPLATE PART - - - - - - - #
            else:
                print(
                    "Incorrect \"part\" in defdat( )\n" + " " * 27 + "^ here"
                    "\n1 - html, header, meta, title and start of main part"
                    "\n2 - close all that things and add hoster image"
                    "\nexample: defdat(1)")
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

        # - - - - - - - FILE CLOSING - - - - - - - #
        html.close()
        def_data.close()
        # - - - - - - - - - - - - - - - - - - - - -#

    # - - - - - - - - - - - - END OF DEFAULT html page - - - - - - - - - - - - #


    # Zeroing
    hour = 0
    minute = 0
    p_supertime = 0
    n_line = 0
    online_c = 0
    # - - - - - - - - #

    # Get filename without ".txt"
    file_name = args.fle[0:-4] + ".html"

    # Open -f [file]
    contents = open(args.fle, 'r', encoding="utf8")


    #[!] - - Generate  HTML TEMPLATE - - [!]#
    try:
        defdat(1, file_name)
    except:
        print("\n[!] ERROR in defdat() [!]"
              "\nProblem must be in:"
              "\n  1) Have no default.txt"
              "\n  2) Have no \"<!--LOG-TABLE-HERE-->\" in default.txt"
              "\n  3) Can't create html file")
        return IOError
    #[!] - - - - - - - - - - - - - - - - [!]#

    # - - - - - - - - - - - - - CONVERTING PROCESS - - - - - - - - - - - - - #
    for line in contents.readlines():

        # "\n" lines counter & filter
        if line == "\n":
            n_line += 1

        # "START" lines filter
        elif "START:" in line:
            n_line += 1

        # IF IT'S NOTE ABOUT ONLINE
        else:

            # Time of note = [last time]
            supertime = int((int(line[0:2:1]) + int(line[3:5:1]) * 30 + int(line[6:10:1]) * 365) * 1440 +
                            (int(line[11:13:1]) * 60 + int(line[14:16:1])))

            # Open html file
            html = open(file_name, 'a', encoding="utf8")

            # If it's not [the first line] and ( [time of last note] != [time of previous note]-1 )
            # Generate the lost notes
            if (p_supertime != 0) and (p_supertime != (supertime - 1)):

                # While [time of new note] != [time of previous note]-1
                while (supertime != p_supertime + 1) and ((hour * 60 + minute) < 1439) and (supertime > p_supertime):

                    # [time of previous note]+1
                    p_supertime += 1

                    # Get time of [time of previous note]
                    year = p_supertime // 525600
                    month = (p_supertime - year * 525600) // 43200
                    day = (p_supertime - year * 525600 - month * 43200) // 1440
                    hour = (p_supertime - year * 525600 - month * 43200 - day * 1440) // 60
                    minute = (p_supertime - year * 525600 - month * 43200 - day * 1440 - hour * 60)

                    # Write ho html file
                    html.write("<tr span=\"2\" style=\"background:Black; color:Red\"><td>" +
                               str("{0:0>2}-{1:0>2}-2019 {3:0>2}:{4:0>2}".format(day, month, year, hour, minute)) +
                               "</td><th></th><td>NO DATA</td></tr>\n")
                    bar.next()

            # IF (time == 00:00) OR (it's not the first line)
            if (supertime == int((int(line[0:2:1]) + int(line[3:5:1]) * 30 + int(line[6:10:1]) * 365) * 1440)) or (p_supertime != 0):
                bar.next()

                # Add information about activity (if-elif-else)
                if "Online" in line:
                    html.write("<tr span=\"2\" style=\"background:Green; color:White\"><td>" + str(
                        line[0:16:1]) + "</td><th></th><td>Online</td></tr>\n")
                    online_c += 1

                elif "[!]" in line:
                    html.write("<tr span=\"2\" style=\"background:Black; color:Red\"><td>" + str(
                        line[0:16:1]) + "</td><th></th><td>NO DATA</td></tr>\n")
                else:
                    html.write("<tr span=\"2\" style=\"background:Khaki; color:Black\"><td>" + str(
                        line[0:16:1]) + "</td><th></th><td>" + str(line[19:(len(line) - 1):1]) + "</td></tr>\n")

            # Set [time of previous note] = [time of note]
            p_supertime = int((int(line[0:2:1]) + int(line[3:5:1]) * 30 + int(line[6:10:1]) * 365) * 1440 +
                              (int(line[11:13:1]) * 60 + int(line[14:16:1])))

            html.close()

    defdat(2, file_name) # Add 2'nd part of file
    bar.finish() # Stop progress bar
    print('[*] Log successful converted to HTML [*]')

# - - - - - - - - - - - - - - - - - - END OF MAIN FUNC - - - - - - - - - - - - - - - - - - #


# Clean terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Set progress bar
bar = Bar('Converting', max = 1440, bar_prefix = ' [', bar_suffix = '] ', empty_fill = '_')

# - - - - - - - O P T I O N S - - - - - - - #
# Turning on "-f file"
opt = argparse.ArgumentParser(description='Print an argument several times')
opt.add_argument('-f', '--file', dest='fle', type=str,
                    default='/', metavar='file.txt',
                    help='Enter the way to txt file (C:/Users/User/home/file.txt)')

args = opt.parse_args()
# - - - - - - - END OF  OPTIONS - - - - - - #


# - - - - - - - - S T A R T - - - - - - - - #
# NORMAL MOD
try:
    add_data()
except:
    # No file data
    if str(args) == 'Namespace(fle=\'/\')':
        print("\n      [!] FATAL ERROR [!]"
              "\n[?] File path not specified [?]"
              "\nUse -h for see help  |  Example: py log2html.py -h"
              "\nSet file by -f       |  Example: py log2html.py -f C:/Users/...[your way].../file.txt")
    # - - - - - - -

    # Unknown error
    else:
        print('[!] Unknown error [!]')
    # - - - - - - -

# DEBUGMOD 
#add_data()
#bar.finish() # Stop progress bar
#print('[*] Log successful converted to HTML [*]')