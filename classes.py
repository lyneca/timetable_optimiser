import math

days = {
    'M': 'Monday',
    'T': 'Tuesday',
    'W': 'Wednesday',
    'R': 'Thursday',
    'F': 'Friday'
}

class Unit:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return __repr__(self)

class Class:
    def __init__(self, code, hours):
        if '+' in code:
            self.multiple = True
            self.times = [Class(x, hours) for x in code.split('+')]
            return

        if not len(code) == 4:
            raise SyntaxError('Invalid class code \'%s\'.' % code)
        self.multiple = False
        self.code = code
        self.day = code[0]
        self.time = int(code[1:3])
        self.group = code[3]
        self.hours = hours
        self.day_full = days[self.day]

    def __repr__(self):
        return self.code
    
    def __str__(self):
        return '%s: Class %s, %s %s:00-%s:00' % (
                self.code, self.group, self.day_full, self.time, math.floor(self.time + self.hours)
        )
