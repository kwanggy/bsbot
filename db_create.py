from model import *

db.drop_all()
db.create_all()

'''
# create mock user data
user1 = User(twtid="ltae9110", lang="en", regcode="1234")
user1.active = False

# create mock lol data
lol1 = Lol("devty")
lol1.lastgame = '5678'


# append
user1.lols.append(lol1)

print user1.lols[0].lolname
print lol1.users[0].twtid


db.session.add(user1)
db.session.add(lol1)
db.session.commit()
'''

