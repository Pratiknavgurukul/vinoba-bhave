import random, datetime

# get student names and create a list
sfile = open('data/students.txt')
students = sfile.read().strip()
students = students.split('\n')

# get rooms and create a dictionary with capacity and list of students
# format - {
#     '1': {
#         'capacity': 9,
#         'students': []
#     },
#     '2': {
#         'capacity': 10,
#         'students': []
#     }
# }
rfile = open('data/rooms.txt')
rooms = rfile.read().strip()
rooms = [room.split('-') for room in rooms.split('\n')]
rooms = {room[0].strip(): {'capacity': int(room[1].strip()), 'students': []} for room in rooms}

# loop over the keys of the dictionary of rooms
# check the capacity of the each room
# take a random sample from the student list according to the capacity of the room
# make sure to remove the student names assigned to this room from the original list
file_contents = []
for room_key in rooms.keys():
    room = rooms[room_key]
    file_contents.append('# Room {0}'.format(room_key))
    capacity = room['capacity']
    capacity = capacity if capacity <= len(students) else len(students)
    rstudents = random.sample(students, capacity)
    file_contents = file_contents + rstudents
    file_contents.append('\n')
    filter(lambda x: students.pop(students.index(x)), rstudents)
    rooms[room_key]['students'] = rstudents
file_contents = '\n'.join(file_contents)

# write the file content
afile = open('data/alloted.txt', 'w')
afile.write(file_contents)
afile.close()
