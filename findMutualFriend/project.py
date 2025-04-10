#python 3

def makeFriendsFromFriends():
    """
    That is just a simple purpose with this project: Findind friends to suggest based on users' friend
    """
    friends = {
        'jean':['Amyr', 'Yvon', 'lambert'],
        'Amyr':['jean', 'Mathieu', 'Thomas'],
        'Lucien':['lambert','Euphrasie','Miracle']
    }

    suggestedFriend = []

    for friend in friends:
        for newFriend in friends[friend]:
            suggestedFriend.append(newFriend) 
    return suggestedFriend

def makeFriendsBasedOnCharacter():

    """
        Return array of friends based oneself's core values
    """
    coreQuality = ["upright", "disciplined", "honest"]

    friends = {
        "jean":{"respectful","positive", "angry", "talkative"},
        "Innocent":{"talkative", "hard worker", "disciplined", "honest"},
        "Afiavi": {"hard worker", "ambitious","angry", "honest"}
    }

    friendsFromQuality = []
    
    for friend in friends:
        
        for quality in friends[friend]:
            
            if quality in coreQuality:
                friendsFromQuality.append(friend)

    friendsFromQuality = set(friendsFromQuality)

    return friendsFromQuality
print(makeFriendsBasedOnCharacter())