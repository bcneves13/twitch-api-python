from flask import Flask, escape, request
from api.main import ApiRequests

app = Flask(__name__)
# https://api.twitch.tv/kraken/streams/
def Authenticate():
    url = 'https://api.twitch.tv/kraken/user'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', '7qmgfucyal2m674n4e5i8nj7zarxro')
    return api.getRequest(url)
@app.route('/')
def getStreams():
    url = 'https://api.twitch.tv/kraken/streams'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', '7qmgfucyal2m674n4e5i8nj7zarxro')
    return api.getRequest(url)

def getStreamById(user_id):
    url = f'https://api.twitch.tv/kraken/streams/{user_id}'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', '7qmgfucyal2m674n4e5i8nj7zarxro')
    return api.getRequest(url)

def getStreamByUser(user_id):
    url = f'https://api.twitch.tv/kraken/streams/{user_id}'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', '7qmgfucyal2m674n4e5i8nj7zarxro')
    return api.getRequest(url)

def getUsers(users):
    url = f'https://api.twitch.tv/kraken/users?login={",".join(users)}'
    print(url)
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', '7qmgfucyal2m674n4e5i8nj7zarxro')
    return api.getRequest(url)

def getAnalytics(params):
    url = 'https://api.twitch.tv/helix/analytics/extensions'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', '7qmgfucyal2m674n4e5i8nj7zarxro')
    return api.getRequest(url, params)


# def 
# if __name__ == '__main__':
#     # auth = Authenticate()
#     # print(auth)
#     # Streamers

#     # streams = getStreams()
#     # # print(streams)
#     # for stream in streams['streams']:
#     #     print(stream.keys())
#     #     live_stream_data = getStreamById(stream['channel']['_id'])
#     #     print(live_stream_data['stream'].keys())
#     # Precisa de uma extensão instalada por streamer para pegar seus dados em csv
#     # searchParams = {
#     #     "type": "overview_v2",
#     #     # "extension_id": "opbw9ndhf2av3ekmy1h6kznxkvy4e7"
#     # }
#     # analytics = getAnalytics(searchParams)
#     # print(analytics)
#     streamers = ['shiphtur', 'imaqtpie']
#     users = getUsers(streamers)
#     print(users)
    