from model import db, User, Post, Album

import app_config as config

class UserModel(object):
    def __init__(self):
        pass

    def getUserById(self, id):
        return User.query.filter_by(id=id).first()

    def getUserByLolid(self, lolid):
        return User.query.filter_by(lolid=lolid).first()
    
    def getUserByLolname(self, lolname):
        return User.query.filter_by(lolname=lolname).first()

    def getUserByTwtid(self, twtid):
        return User.query.filter_by(twtid=twtid).first()

    def lookup_lastgame(self, lolid):
        userExist = self.getUserByLolid(lolid)
        if userExist == None:
            return None
        return userExist.lastgame

    def logIn(self, email, passwd):
        emailExist = self.getUserByEmail(email)
        if emailExist == None:
            return None
        if emailExist.passwd != passwd:
            return False
        return emailExist.id

    def addNewUser(self, email, passwd):
        emailExist = self.getUserByEmail(email)
        if emailExist != None:
            return False
        user = User(email,passwd)
        db.session.add(user)
        db.session.commit()
        return True

    def addAlbum(self, albumname, userid):
        userExist = self.getUserById(userid)
        if userExist == None:
            return False
        album = Album(albumname)
        db.session.add(album)
        userExist.albums.append(album)
        db.session.commit()
        return True
    
    def addPost(self, title, text, picurl, folder, filename, albumid):
        albumExist = self.getAlbumById(albumid)
        if albumExist == None:
            return False
        post = Post(title,text,picurl,folder,filename)
        db.session.add(post)
        albumExist.posts.append(post)
        db.session.commit()
        return True

    def deleteAlbum(self, albumid):
        albumExist = self.getAlbumById(albumid)
        if albumExist == None:
            return False
        user = self.getUserById(albumExist.userid)
        user.albums.remove(albumExist)
        posts = Post.query.filter_by(albumid=albumid).all()
        for post in posts:
            db.session.delete(post)
        db.session.delete(albumExist)
        db.session.commit()
        return True 

    def deletePost(self,postid):
        postExist = self.getPostById(postid)
        if postExist == None:
            return False
        album = self.getAlbumById(postExist.albumid)
        album.posts.remove(postExist)
        db.session.delete(postExist)
        db.session.commit()
        return True