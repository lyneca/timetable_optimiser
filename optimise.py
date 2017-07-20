from parse import parse, Class, Unit
import tkinter as tk
import math

SLOT_WIDTH = 15

units = parse('times.txt')
slots = []

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

def fill_timetable():
    """
    Your optimisation code here!
    All the units that are in times.txt are in the list 'units'.
    To get the possible classes in a unit (in this example, the first unit in the list):
    >>> units[0].classes

    To render a specific class into the timetable:
    >>> render(units[0].classes[0])

    To render all possible classes from a unit:
    >>> render(units[0])

    To get all classes that cover a particular timeslot:
    >>> get_classes_on_time(0, 13)  # 0 = Monday, 13 = 1:00pm
    """
    pass
    

# App code

def pad(s, n):
    return '0'*(n-len(str(s))) + str(s)

def get_classes_on_time(day, time):
    """
    Gets all the classes that cover a particular timeslot.
    get_classes_on_time(0, 13) -> Monday 1:00pm
    get_classes_on_time(3, 9) -> Thursday 9:00am

    """
    out = []
    for unit in units:
        for c in unit.classes:
            if c.multiple:
                for c in c.times:
                    if not days.index(c.day_full) == day: continue
                    if c.time <= time < c.time + c.hours:
                        out.append(unit.name + ' ' + c.code)
            if not days.index(c.day_full) == day: continue
            if c.time <= time < c.time + c.hours:
                out.append(unit.name + ' ' + c.code)
    return out

def render(u, c = None):
    if c:
        x = days.index(c.day_full)
        y = c.time - 8
        for j in range(math.ceil(c.hours)):
            slots[x][y+j].text(u.name)
    else:
        [render(u, x) for x in u.classes]

class TimeSlot:
    def __init__(self, master, x, y):
        self.frame = tk.Label(
            master,
            borderwidth=1,
            width=SLOT_WIDTH,
            relief='groove',
            text=' '
        )
    def text(self, s):
        self.frame['text'] = s


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.create_timetable()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text='Quit',
            command=self.quit)
        self.constraints_frame = tk.Frame(
            self,
            width=200,
            height=270,
            borderwidth=2,
            relief='sunken'
        )
        self.timetable_frame = tk.Frame(
            self,
            width=400,
            height=300,
            borderwidth=2,
            relief='sunken'
        )
        self.constraints_frame.grid(row=0,column=0)
        self.timetable_frame.grid(row=0,column=1)
        self.quit_button.grid(row=1,column=0)

    def create_timetable(self):
        for x in range(5):
            slots.append([])
            for y in range(13):
                slot = TimeSlot(self.timetable_frame, x, y)
                slot.frame.grid(row=y+1, column=x+1)
                slots[x].append(slot)
        self.row_labels = []
        self.column_labels = []
        for x in range(5):
            slot = tk.Label(
                self.timetable_frame,
                width=SLOT_WIDTH,
                borderwidth=1,
                relief='groove',
                text=days[x]
            )
            slot.grid(row=0, column=x+1)
            self.column_labels.append(slot)
        for y in range(13):
            slot = tk.Label(
                self.timetable_frame,
                borderwidth=1,
                relief='groove',
                text=(pad(y+8, 2) + ':00')
            )
            slot.grid(row=y+1, column=0)
            self.row_labels.append(slot)


app = Application()
app.master.title('Timetable Optimiser')
app.master['borderwidth'] = 2
app.master['relief'] = 'groove'
fill_timetable()
app.mainloop()

