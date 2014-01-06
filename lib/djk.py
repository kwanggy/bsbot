#class for easy implementation of djkString dictionary
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


class djkReader():
    djkString = AutoVivification()
    def __init__(self, *langfiles):
        langfile = {} 
        lang = []
        #opening language djk files 
        for location in langfiles:
            temp = location.split('/')[len(location.split('/'))-1]
            temp = temp[0] + temp[1]
            lang.append(temp)
            langfile[temp] = open(location, 'r')

        #upload each djk content to memory
        for i in range(0,len(langfiles)): 
            #rstrip is needed for getting rid of '\n' in the strings
            curversion = langfile[lang[i]].readline().rstrip('\n')  #string of version
            #IF CONTENT IS EMPTY, IT WILL RETURN ''
            if curversion == '':
                print langfiles[i] + ': empty file'
                continue
            cursecTitle = langfile[lang[i]].readline().rstrip('\n') #botcmd;champions;gametype;...
            cursecLen = langfile[lang[i]].readline().rstrip('\n')   #length of each section

            self.djkString[lang[i]]['version'] = curversion
            if(len(cursecTitle.split(';')) == 1):
                print langfiles[i] + ': section title line is incorrect'
                continue
            self.djkString[lang[i]]['secTitle'] = cursecTitle.split(';')
            if(len(cursecLen.split(';')) == 1):
                print langfiles[i] + ': section length line is incorrect'
                continue
            self.djkString[lang[i]]['secLen'] = cursecLen.split(';')
           
            if len(cursecLen.split(';')) != len(cursecTitle.split(';')):
                print langfiles[i] + ': has different number of arguments in section header'
                continue

            #for loop by number of sections
                #nested for loop by number of sections length
            for index, j in enumerate(cursecTitle.split(';')):
                try:
                    count = cursecLen.split(';')[index]
                except IndexError:
                    print langfiles[i] + ': problem caused by using characters in for loop range'
                    continue
                try:
                    for k in range(0,int(count)):
                        self.djkString[lang[i]][j][k] = langfile[lang[i]].readline().rstrip('\n')
                except ValueError:
                    print langfiles[i] + ': tried to cast characters into integer'
                    continue

if __name__ == '__main__':
    mydjk = djkReader('krtest.djk','notest.djk','entest.djk','nptest.djk','dftest.djk')
    print mydjk.djkString['kr']['version']
    print mydjk.djkString['kr']['secTitle']
    print mydjk.djkString['kr']['secLen']
    print mydjk.djkString['kr']['bot_command']
    print mydjk.djkString['kr']['champions']
    print mydjk.djkString['kr']['gametype']
    print mydjk.djkString['kr']['format']
    print '-----------------------------------------'
    print mydjk.djkString['en']['version']
    print mydjk.djkString['en']['secTitle']
    print mydjk.djkString['en']['secLen']
    print mydjk.djkString['en']['bot_cand']
    print mydjk.djkString['en']['chaons']
    print mydjk.djkString['en']['gampe']
    print mydjk.djkString['en']['foat']
    print '-----------------------------------------'
    print mydjk.djkString['no']['version']
    print mydjk.djkString['no']['secTitle']
    print mydjk.djkString['no']['secLen']
    print mydjk.djkString['no']['bot_cand']
    print mydjk.djkString['no']['chaons']
    print mydjk.djkString['no']['gampe']
    print mydjk.djkString['no']['foat']
    print '-----------------------------------------'
    print mydjk.djkString['np']['version']
    print mydjk.djkString['np']['secTitle']
    print mydjk.djkString['np']['secLen']
    print mydjk.djkString['np']['bot_cand']
    print mydjk.djkString['np']['chaons']
    print mydjk.djkString['np']['gampe']
    print mydjk.djkString['np']['foat']
