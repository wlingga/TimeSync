from timesync.models import Todo
import datetime
import itertools

def timeOverlap(intA, intB):
    startTimeA, endTimeA = intA
    startTimeB, endTimeB = intB

    minStartTimeA = int((startTimeA.split(":")[0]))*60 + int((startTimeA.split(":")[1]))
    minEndTimeA = int((endTimeA.split(":")[0]))*60 + int((endTimeA.split(":")[1]))

    minStartTimeB = int((startTimeB.split(":")[0])) * 60 + int((startTimeB.split(":")[1]))
    minEndTimeB = int((endTimeB.split(":")[0])) * 60 + int((endTimeB.split(":")[1]))

    if minStartTimeA >= minStartTimeB and minEndTimeA <= minEndTimeB:
        return True
    elif minStartTimeA <= minStartTimeB and minEndTimeA >= minStartTimeB:
        return True
    elif minStartTimeA >= minStartTimeB and minEndTimeA >= minEndTimeB:
        return True
    return False

def isMatching(my_todo, todo_list):
    overlapping = []

    for mystuff in my_todo:
        for todo in todo_list:
            if timeOverlap((mystuff.start_time, mystuff.end_time), (todo.start_time, todo.end_time)) and mystuff.title == todo.title and mystuff.id != todo.id:
                overlapping.append(todo)

    return overlapping