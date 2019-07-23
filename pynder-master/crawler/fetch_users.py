import pynder
import csv
import itertools
X_Auth_Token = '59723ad4-dbf5-4954-8a7a-de61e553ff50'
session = pynder.Session(XAuthToken=X_Auth_Token)

session.profile

users = session.nearby_users()

for user in itertools.islice(users, 30):
    with open('users.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        row = [user.name, user.age, user.bio, user.distance_mi, user.schools, user.jobs, user.photos_count, user.instagram_photos, user.spotify_connected]
        writer.writerow(row)
        user.unlike()
csvFile.close()



