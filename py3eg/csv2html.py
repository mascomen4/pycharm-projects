#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys
import xml.sax.saxutils

def main():
    maxwidth, Format = process_options()
    if Format is not None:
        maxwidth = int(maxwidth)
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                        color = "lightgreen"
                elif count % 2:
                        color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, Format)
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth, Format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x),
                                                                   Format))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                            xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields

def print_end():
    print("</table>")

def process_options():
    x = None,None
    if len(sys.argv)==2:
        if sys.argv[1] in ('-h','--help'):
            print("usage: \n"
                "csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html \n"
                "\n"
                "maxwidth is an optional integer; if specified, it sets the maximum \n"
                "number of characters that can be output for string fields,\n"
                "otherwise a default of 100 characters is used.\n"
                "(maxwidth – необязательное целое число. Если задано, определяет\n"
                "максимальное число символов для строковых полей. В противном случае\n"
                "используется значение по умолчанию 100.)\n"
                "\n"
                "format is the format to use for numbers; if not specified it \n"
                "defaults to \".0f\". \n"
                "(format – формат вывода чисел. Если не задан, по умолчанию используется \n"
                "формат \".0f\".) ")
            return (None,None)
        else:
            maxwidth = sys.argv[1]
            return maxwidth
    elif len(sys.argv)==3:
        maxwidth = sys.argv[1]
        Format = sys.argv[2]
        return (maxwidth,Format)
    else:
        maxwidth = 100
        Format = ".0f"
        return (maxwidth, Format)
main()
