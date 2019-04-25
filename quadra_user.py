class User:
    def __init__(self, _id, discord_id, name, tag, cash, love, xp, level, exp_time, life_time):
        self.dbid = _id
        self.id = discord_id
        self.name = name
        self.tag = tag
        self.cash = cash
        self.love = love
        self.xp = xp
        self.level = level
        self.exp_time = exp_time
        self.life_time = life_time


class Quadra_user:
    def __init__(self, database):
        self.database = database

    def getUser(self, user):
        curs = self.database.cursor()
        swt = curs.execute("select * from users WHERE discord_id = "+str(user.id))
        if swt: return parsingUser(curs.fetchall()[0])
        else: return self.newUser(self, user)

    def newUser(self, user):
        curs = self.database.cursor()
        sql = """insert into users(discord_id, name, tag)
                 values (%d, %s, %s)"""%(user.id, user.name, user.discriminator)
        curs.execute(sql)
        curs.execute("select * from users WHERE discord_id = " + str(user.id))
        return parsingUser(curs.fetchall()[0])


def parsingUser(data):
    return User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])



