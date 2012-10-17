#!/usr/bin/python -O

def sep_extensions(filelist, extension):
    keep_files = []
    for filename in filelist:
        name = filename.split('.')
        if name[len(name) - 1] == extension:
            keep_files.append(filename)

    return keep_files

def show_list(list_of_items):
    counter = 1
    for item in list_of_items:
        print str(counter) + '. ' + item
        counter += 1

    return len(list_of_items)
