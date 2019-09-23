from api.main import ApiRequests

def getStreams():
    url = 'https://api.twitch.tv/helix/streams'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7')
    return api.getRequest(url)

def getAnalytics(params):
    url = 'https://api.twitch.tv/helix/analytics/extensions'
    api = ApiRequests('opbw9ndhf2av3ekmy1h6kznxkvy4e7', 'xmu5iiokzfmtjelcnttitu30fnvl6q')
    return api.getRequest(url, params)

if __name__ == '__main__':
    # Streamers
    # streams = getStreams()
    # print(streams)

    searchParams = {
        "type": "overview_1",
        # "extension_id": "opbw9ndhf2av3ekmy1h6kznxkvy4e7"
    }
    analytics = getAnalytics(searchParams)
    print(analytics)