#bla bla bla
# bla bla bla
''' Program description '''

import locale
locale.setlocale(locale.LC_ALL, "")
import os
import optparse
import datetime

def main():
    opts, paths = parse_arguments()

    count = [0,0]
    if not opts.recursive:
        filenames = []
        dirnames = []
        for path in paths:
            if os.path.isfile(path):
                continue
            for name in os.listdir(path):
                if (not opts.hidden) and name.startswith('.'):
                    continue
                fullname = os.path.join(path, name)
                if fullname.startswith('./'):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    dirnames.append(fullname)
                count[0] += len(filenames)
                count[1] += len(dirnames)
        process_lists(opts, filenames, dirnames)
    else:
        for path in paths:
            if os.path.isfile(path):
                continue
            for root, dirs, files in os.walk(path):
                if not opts.hidden:
                    dirs[:] = [name for name in dirs
                               if not name.startswith('.')]
                for file in files:
                    if (not opts.hidden) and name.startswith('.'):
                        continue
                    fullname = os.path.join(root, file)
                    if fullname.startswith('./'):
                        fullname = fullname[2:]
                    filenames.append(fullname)
                count[0] += len(filenames)
                count[1] += len(dirs)
        process_lists(opts, filenames, [])
    # Зачем здесь n?
    print('{0} file{1}, {2} director{3}'.format(
        '{0}'.format(count[0]) if count[0] else 'no',
        's' if count[0] != 1 else '',
        '{0}'.format(count[1]) if count[1] else 'no',
        'ies' if count[1] != 1 else 'y'))
    

def parse_arguments():
    usage = '''%prog [options] [path1 [path2 [... pathN]]]

The path are the optional; if not given . is used.'''
    
    parser = optparse.OptionParser()
    parser.add_option('-H', '--hidden', action='store_true', default=False,
                      help='show hidden files [default: off]' )
    parser.add_option('-m', '--modified', action='store_true', default=False,
                      help='show last modified date/time [default: off]')
    parser.add_option('-o', '--order', action='store', dest='order', type='str',
                     help=("order by ('name', 'n', 'modified', 'm',"
                      "'size', 's')\n [default: %default]"), default='name')
    parser.add_option('-s', '--size', action='store_true', default=False,
                    help='show sizes [default: off]')
    parser.add_option('-r', '--recursive', action='store_true', default=False,
                     help='recurse into subdirectories [default: off]')
    opts, paths = parser.parse_args()
    if not paths:
        paths = ['.']
    return opts, paths


def process_lists(opts, filenames, dirnames):
    keys_lines = []
    for filename in filenames:
        modified = ''
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(filename))
                            .isoformat(' ')[:19] + ' ')
            except EnvironmentError:
                modified = '{0:>19}'.format('unknown')
        size = ''
        if opts.size:
            try:
                size = '{0:>15}'.format(os.path.getsize(filename))
            except EnvironmentError:
                size = '{0:>15}'.format('unknown')
        if os.path.islink(filename):
            filename += ' -> ' + os.path.realpath(name)
        if opts.order in {'m', 'modfied'}:
            orderkey = modified
        elif opts.order in {'s', 'size'}:
            orderkey = size
        else:
            orderkey = filename
        keys_lines.append((orderkey, '{0}{1}{2}'.format(modified,
                                                            size, filename)))
    size = '' if not opts.size else ' ' * 20
    modified = '' if not opts.modified else ' ' * 15
    for dirname in sorted(dirnames):
        filenames.append((dirname, '{0}{1}{2}/'.format(modified, size, dirname)))
    for key, line in sorted(keys_lines):
        print(line)
        
main()
