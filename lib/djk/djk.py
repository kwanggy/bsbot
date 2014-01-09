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
        #opening each language djk files 
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
            
            #botcmd;champions;gametype;...
            cursecTitle = langfile[lang[i]].readline().rstrip('\n').split(';')
            #length of each section
            cursecLen = langfile[lang[i]].readline().rstrip('\n').split(';')

            #read versin of djk
            self.djkString[lang[i]]['version'] = curversion
            if(len(cursecTitle) == 1):
                print langfiles[i] + ': section title line is incorrect'
                continue

            #read section titles
            self.djkString[lang[i]]['secTitle'] = cursecTitle
            if(len(cursecLen) == 1):
                print langfiles[i] + ': section length line is incorrect'
                continue

            #read lines for each section
            self.djkString[lang[i]]['secLen'] = cursecLen
            if len(cursecLen) != len(cursecTitle):
                print langfiles[i] + ': has different number of arguments in section header'
                continue

            #for loop by number of sections
                #nested for loop by number of sections length
            for index, j in enumerate(cursecTitle):
                try:
                    count = cursecLen[index]
                except IndexError:
                    print langfiles[i] + ': problem caused by using characters in for loop range'
                    continue
                
                if (cursecTitle[index] == 'champions') or (cursecTitle[index] == 'maps') :
                    try:
                        for k in range(0,int(count)):
                            tempstring = langfile[lang[i]].readline().rstrip('\n')
                            tempstring = tempstring.split(';')
                            self.djkString[lang[i]][j][int(tempstring[0])] = tempstring[1]
                    except ValueError:
                        print langfiles[i] + ': tried to cast characters into integer'
                        continue
                    
                else:
                    try:
                        for k in range(0,int(count)):
                            self.djkString[lang[i]][j][k] = langfile[lang[i]].readline().rstrip('\n')
                    except ValueError:
                        print langfiles[i] + ': tried to cast characters into integer'
                        continue

if __name__ == '__main__':
    mydjk = djkReader('en_v1.djk', 'kr_v1.djk')
    print mydjk.djkString['kr']['version']
    print mydjk.djkString['kr']['secTitle']
    print mydjk.djkString['kr']['secLen']
    print mydjk.djkString['kr']['bot_command']
    print mydjk.djkString['kr']['champions']
    print mydjk.djkString['kr']['maps']
    print mydjk.djkString['kr']['twt_format']
    print '-----------------------------------------'
    print mydjk.djkString['en']['version']
    print mydjk.djkString['en']['secTitle']
    print mydjk.djkString['en']['secLen']
    print mydjk.djkString['en']['bot_command']
    print mydjk.djkString['en']['champions']
    print mydjk.djkString['en']['maps']
    print mydjk.djkString['en']['twt_format']
