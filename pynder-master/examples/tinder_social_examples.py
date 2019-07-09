import pynder
import csv
import itertools
X_Auth_Token = '59723ad4-dbf5-4954-8a7a-de61e553ff50'
session = pynder.Session(XAuthToken=X_Auth_Token)

session.profile

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

    with open('man.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        row = [user.name, user.age, user.bio, user.distance_mi, user.schools, user.jobs, user.photos_count, user.instagram_photos, user.spotify_connected]
        writer.writerow(row)


csvFile.close()



