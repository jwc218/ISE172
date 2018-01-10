
from social_network import SocialNetwork
from sys import maxint
import gzip
from copy import deepcopy

class ActorGraph (SocialNetwork):
    def __init__(self, languageFilter, ratingFilter, voteFilter, genreFilter, display = None):
        '''
        languageFilter must be a set of languages
        ratingFilter must be a tuple of two floats (lower bound, upper bound)
        voteFilter must be a tuple of two integers (lower bound, upper bound)
        genreFilter must be a tuple of two sets (genreSet, string), string
        should be either 'in' or 'out', if 'in': the genres in the genreSet
        will be taken into account; if 'out': genres other than the ones in
        the genreSet will be considered.
        '''
        self.languageFilter = languageFilter
        self.ratingFilter = ratingFilter
        self.voteFilter = voteFilter
        self.genreFilter = genreFilter
        self.movieList = []
        self.actorDict = {}
        SocialNetwork.__init__(self, display)

    def _parse(self, actorPath='./reduced_actors_and_actresses.list.gz',
                    languagePath='./language.list.gz',
                    ratingsPath='./ratings.list.gz',
                    genresPath='./genres.list.gz'):
        '''
        This function parses language.list, ratings.list and genres.list
        sequentially.
        builds self.movie which is a dictionary of movie class objects with,
        the following attributes. language = English; rate >= 8.0;
        tag != {short, adult, documentary}; votes>= 5000
        '''
        self.actorPath = actorPath
        self.languagePath = languagePath
        self.ratingsPath = ratingsPath
        self.genresPath = genresPath
        #parse ratings.list
        ratingFile = gzip.open(self.ratingsPath, 'r')
        rlb, rub = self.ratingFilter
        vlb, vub = self.voteFilter
        if vub==None:
            vub = maxint
        for line in ratingFile:
            tline = line.split()
            vote = int(tline[1])
            rate = float(tline[2])
            movie = ' '.join(s for s in tline[3:])
            #do not accept TV series, their name are given between quotes
            if movie.startswith('"') or rate < rlb or rate > rub or vote < vlb or vote > vub:
                pass
            else:
                self.movieList.append(movie)
        ratingFile.close()
        print 'ratings.list parsed!', len(self.movieList), 'movies'
        #parse language.list
        languageFile = gzip.open(self.languagePath, 'r')
        l = {}
        for line in languageFile:
            movie, tab, lang = line.partition('\t')
            movie = movie.strip()
            lang = lang.strip()
            if movie in l:
                l[movie].add(lang)
            else:
                l[movie] = set([lang])
        languageFile.close()
        ml2 = deepcopy(self.movieList)
        for m in ml2:
            if m not in l or len(l[m].intersection(self.languageFilter)) == 0:
                self.movieList.remove(m)
        print 'language.list parsed!', len(self.movieList), 'movies'
        #parse genres.list
        genreFile = gzip.open(genresPath, 'r')
        genreSet, type = self.genreFilter
        for line in genreFile:
            tline = line.split()
            tag = tline[-1]
            movie = ' '.join(s for s in tline[:-1])
            #what happens when a movie has two tags one is in
            #the genreSet and the other is not? We just remove it!
            if type == 'out':
                if tag in genreSet and movie in self.movieList:
                    self.movieList.remove(movie)
            else:
                if not tag in genreSet and movie in self.movieList:
                    self.movieList.remove(movie)
        genreFile.close()
        print 'genre.list parsed!', len(self.movieList), 'movies'
        #parse actors.list
        actorFile = gzip.open(self.actorPath, 'r')
        flag = False
        for line in actorFile:
            if len(line.split()) == 0:
                actor = None
                flag = False
            elif flag == False:
                actor, tab, rest = line.partition('\t')
                actor = actor.strip()
                rest = rest.strip()
                movie, space, rest = rest.partition('  ')
                movie = movie.strip()
                flag = True
                self.actorDict[actor] = [movie]
            else:
                empty, tabs, movie= line.partition('\t\t\t')
                movie, space, rest = movie.partition('  ')
                movie = movie.strip()
                if not movie.startswith('"'):
                    self.actorDict[actor].append(movie)
        ad = deepcopy(self.actorDict)
        for a in ad:
            if len(set(self.actorDict[a]).
                   intersection(set(self.movieList))) == 0:
                del self.actorDict[a]
        print 'actors.list parsed!', len(self.actorDict), 'actors'
        actorFile.close()

    def _create_graph(self):
        self._parse()
        for a1 in self.actorDict:
            print a1
            for a2 in self.actorDict:
                if a2 <= a1:
                    continue
                for m in self.actorDict[a1]:
                    if m in self.actorDict[a2]:
                        key1, label1 = self._get_name(a1)
                        key2, label2 = self._get_name(a2)
                        if key1 != None and key2 != None:
                            self.add_connection(key1, key2, label1, label2)
                        break

    def _get_name(self, key):
        try:
            key = key.encode('ascii', 'ignore')
        except UnicodeDecodeError:
            return None, None
        illegalCharList = [' ', '.', '-', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', ',',"'"]
        if ',' in key:
            transpose = ''.join(key.split(',')[1]+ ' ' + key.split(',')[0])
        else:
            transpose = key
        erase = False
        name = ''
        for i in range(len(transpose)):
            if transpose[i] == '(':
                erase = True
            if transpose[i] == ')':
                erase = False
                continue
            if erase == True:
                continue
            else:
                name = name + transpose[i]
        for c in key:
            if c in illegalCharList:
                key = key.replace(c,'')
        return key, name

    def visualize(self, layout = 'dot'):
        self._create_graph()
        print self.to_string()
        self.set_layout(layout)
        self.display()

    def save_to_file(self, filename, layout = 'dot'):
        self._create_graph()
        print self.to_string()
        self.set_layout(layout)
        self.set_display_mode('file')
        self.display(basename = filename, format = 'png')

if __name__ == '__main__':
    lFilter = set(['English'])
    rFilter = (8.5, 10.0)
    vFilter = (100000,None)
    gFilter = (set(['Short', 'Documentary', 'Adult']), 'out')
    ag = ActorGraph(lFilter, rFilter, vFilter, gFilter)
    ag.save_to_file(filename = 'graph', layout = 'fdp')
