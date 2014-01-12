from model import db, Lol

class LolModel(object):
    def __init__(self):
        pass

    def getLols(self):
        return Lol.query.filter_by().all()

    def getLolByLolname(self, lolname):
        return Lol.query.filter_by(lolname=lolname).first()

    def setLastGame(self, lolname, curLastGame):
        lol = self.getLolByLolname(lolname)
        if not lol:
            return False
        lol.lastgame - curLastGame
        db.session.commit()
        return True


    def addNewLol(self, lolid, lolname, lastgame):
        print 'addNewLol called: ' + lolname
        newLol = Lol(lolid, lolname, lastgame)
        db.session.add(newLol)
        db.session.commit()

        return Lol.query.filter_by(lolname=lolname).first()
        
