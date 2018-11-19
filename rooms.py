import random
done = []
room_name = []
print("Enter the number of students in each room:")
rooms = {
            'Room_1' : 8,
            'Room_6' : 10,
            'Room_7' : 6,
            'Room_8' : 6,
            'Room_9' : 4,
            'Room_10' : 6,
            'Room_11' : 6,
            'Room_12' : 8,
        }
i = 0
for room in rooms:
    print(room)
    rooms[room] = int(input())
    i += 1
for room in rooms:
    room_name.append(room)
final = open("final_rooms.txt","w+")
initial = open("student_names.txt", "r")
contents = initial.read()
contents = contents.split()
a = len(contents)
while True:
    name = random.choice(contents)
    contents.pop(contents.index(name))
    done.append(name)
    if len(done) == a:
        break
count = 0
x = 0
while i < len(done):

    if i == count and x<len(room_name):
        final.write("List of students in " + room_name[x] + "\n")
        print("List of students in " + room_name[x] + "\n")
        count = count + rooms[room_name[x]]
        x = x + 1
    final.write( done[i] + "\n")
    print(done[i] + "\n")
    i = i + 1
