# from timesync.models import Todo
import datetime
import itertools


def overlap(first_inter,second_inter):
    for f,s in ((first_inter,second_inter), (second_inter,first_inter)):
        for time in (f["starting_time"], f["ending_time"]):
            if s["starting_time"] < time < s["ending_time"]:
                return True
    else:
        return False



def ifMatching():
    overlapping = []

    sample_task = [2,'Workout', '13:00', '17:00']
    todos_array = [[2, 'Workout', '04:45', '21:45'], [3, 'Study', '14:40', '16:40'], [2, 'Cook', '04:42', '07:42']]
    
    sample_task.append(int(sample_task[2]))
    sample_task.append(int(sample_task[3]))
   
    for todo in todos_array:
    #    todos_array.append([todo.user_id, todo.title, todo.description, todo.start_time, todo.end_time])
        todo.append(int(todo[2])
        todo.append(int(todo[3])
   
    for todo in todos_array:
       if overlap([sample_task[4],sample_task[5]], [todo[4],todo[5]]) and sample_task[1] == todo[1]:
           overlapping.append(todo)

        
    # if overlap ((datetime.time(4, 45), datetime.time(6, 45)),(datetime.time(6, 45), datetime.time(4,45)))
    # print(todos_array[0])


    return overlapping

print(ifMatching())