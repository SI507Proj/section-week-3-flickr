import json


class Photo(object):
    def __init__(self, photo_diction):
        self.owner = {
            'username' : photo_diction['owner']['username'],
            'realname' : photo_diction['owner']['realname'],
            'location' : photo_diction['owner']['location']
        }
        self.title = photo_diction['title']['_content']
        self.tags = []
        for tag in photo_diction['tags']['tag']:
            self.tags.append(tag['raw'])
        self.id = photo_diction['id']
        self.date_taken = photo_diction['dates']['taken']
        self.url = photo_diction['urls']['url'][0]['_content']
        self.license = photo_diction['license']

    def __str__(self):
        return self.title

    def __repr__(self):
        return'ID: {}, Title: {}, URL: {}'.format(self.id, self.title, self.url)
        # return 'Title: {1}, ID {0}, URL: {3}'.format(self.id, self.title, self.url)

    def __contains__(self, test_string):
        return (
            test_string in self.tags
            or test_string in self.title
        )
      

response_diction = {}
with open('sample_diction.json', 'r') as f:
    f_string = f.read()
    response_diction = json.loads(f_string)
    # print(response_diction)

photo = Photo(response_diction['photo'])
print(photo)
print(repr(photo))
print(isinstance(photo, Photo))
if 'Nature' in photo:
    print('Nature exists in photo')