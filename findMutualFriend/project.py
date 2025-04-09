#python 3
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
print(suggestedFriend)