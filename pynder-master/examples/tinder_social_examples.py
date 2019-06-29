import pynder
import csv
import itertools
X_Auth_Token = '5de0371f-9e2a-4397-a961-f3b1cf9dda8d'
session = pynder.Session(XAuthToken=X_Auth_Token)

users = session.nearby_users()

for user in itertools.islice(users, 30):
    # print(user.name)
    # print(user.age)
    # print(user.bio)
    # print(user.distance_mi)
    # print(user.schools)
    # print(user.jobs)
    # print(user.photos_count)
    # print(len(user.instagram_photos) > 0)
    print(user.spotify_connected)

    with open('people.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        row = [user.name, user.age, user.bio, user.distance_mi, user.schools, user.jobs, user.photos_count, user.instagram_photos, user.spotify_connected]
        writer.writerow(row)


csvFile.close()



