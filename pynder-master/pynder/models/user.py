import itertools
import datetime
import dateutil.parser
import six

from pynder.models.base import Model
from pynder.constants import GENDER_MAP, SIMPLE_FIELDS, VALID_PHOTO_SIZES
from pynder.models.message import Message


class User(Model):

    def __init__(self, data, session):
        self._session = session
        self._data = data
        self.id = data['user']['_id']
        self.name = data['user']['name']
        self.bio = data['user']['bio']
        self.birth_date = data['user']['birth_date']
        self.birth_date = dateutil.parser.parse(self.birth_date)
        self.ping_time = data['user']['ping_time']

        self._photos = data['user']['photos']
        self.schools = len(data['user']['schools'])
        self.jobs = len(data['user']['jobs'])

        # print(self._data)

    @property
    def instagram_username(self):
        if "instagram" in self._data:
            return self._data['instagram']['username']

    @property
    def instagram_photos(self):
        if "instagram" in self._data['user']:
            return 1
        return 0

    @property
    def spotify_connected(self):
        return 0

    @property
    def gender(self):
        return GENDER_MAP[int(self._data['gender'])]

    @property
    def common_likes(self):
        return [p for p in self._data['common_likes']]

    @property
    def common_connections(self):
        return [p for p in self._data['common_friends']]

    @property
    def thumbnails(self):
        return self.get_photos(width=84)

    @property
    def photos(self):
        return self.get_photos()

    @property
    def photos_count(self):
        return len(self._photos)

    @property
    def distance_km(self):
        if 'distance_km' in self._data:
            return self._data['user']['distance_km']
        elif 'distance_mi' in self._data:
            return self._data['user']['distance_mi'] * 1.60934
        else:
            return -1

    @property
    def distance_mi(self):
        if 'distance_mi' in self._data['user']:
            return self._data['user']['distance_mi']
        elif 'distance_km' in self._data:
            return self._data['user']['distance_km'] / 1.60934
        else:
            return -1

    @property
    def age(self):
        today = datetime.date.today()
        return (today.year - self.birth_date.year -
                ((today.month, today.day) <
                 (self.birth_date.month, self.birth_date.day)))

    @property
    def share_link(self):
        return self._session._api.share(self.id)['link']

    def __unicode__(self):
        return u"{n} ({a})".format(n=self.name, a=self.age)

    def __str__(self):
        return six.text_type(self).encode('utf-8')

    def __repr__(self):
        return repr(self.name)

    def report(self, cause, text=""):
        return self._session._api.report(self.id, cause, text)

    def get_photos(self, width=640):
        if int(width) not in VALID_PHOTO_SIZES:
            raise ValueError("Unsupported width")
        return itertools.chain.from_iterable([[processed_photo['url'] for processed_photo in photo.get("processedFiles", []) if processed_photo['width'] == int(width)] for photo in self._photos])

    def like(self):
        return self._session._api.like(self.id)['match']

    def superlike(self):
        return self._session._api.superlike(self.id)['match']

    def dislike(self):
        return self._session._api.dislike(self.id)


class RateLimited(User):

    pass


class Match(Model):

    def __init__(self, match, _session):
        self._session = _session
        self.id = match["_id"]
        self.user, self.messages = None, []
        self.match_date = datetime.datetime.strptime(
         match["created_date"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        if 'person' in match:
            user_data = _session._api.user_info(
                match['person']['_id'])['results']
            user_data['_id'] = match['person']['_id']
            self.user = User(user_data, _session)
            self.messages = [Message(m, user=self.user)
                             for m in match['messages']]

    def message(self, body):
        return self._session._api.message(self.id, body)['_id']

    def message_gif(self, giphy_id):
        return self._session._api.message_gif(self.id, giphy_id)['_id']

    def report(self, cause, text=""):
        return self._session._api.report(self.id, cause, text)

    def delete(self):
        return self._session._api._delete('/user/matches/' + self.id)

    def __repr__(self):
        return "<Unnamed match>" if self.user is None else repr(self.user)
