from classes import Unit, Class
import sys

def error(n, m):
    print('Error in unit %s:\n  %s' % (n, m))
    sys.exit()

def parse(f):
    lines = open(f).read().split('\n')
    # Remove comments and blank lines:
    lines = [x.split('#')[0] for x in lines if len(x) > 0 and not x[0] == '#']
    name = ''
    units = []
    hours = 0
    for line in lines:
        if not line[0] == '\t':
            if name:
                units.append(Unit(name, classes))
                hours = 0
            name = line.strip()
            classes = []
        else:
            line = line.strip()
            if line.split(' ')[-1].startswith('hour'):
                hours = float(line.split()[0])
            else:
                if hours == 0:
                    error(name, 'Need to specify hours before listing classes.')
                try:
                    classes += [Class(x, hours) for x in line.split()]
                except SyntaxError as e:
                    error(name, e.msg)
    return units 

if __name__ == '__main__':
    # print('\n'.join([str(x) for x in parse('times.txt')[0].classes]))
    print(parse('times.txt'))
