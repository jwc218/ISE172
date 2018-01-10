

class HashDistionary:
    
    
    def processNewWord(self,newWord):
        
        adj=newWord.lower()
        if adj not in self.dictionary:
            self.dictionary[adj]=0
            
    
    
    def __init__(self):
        self.dictionary={}
        
        
        
    def getDictionary(self):
        return self.dictionary 