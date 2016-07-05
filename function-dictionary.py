def createDictionary ():
    ''' Return a tiny spanish dictionary'''
    spanish = dict ()
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['four'] = 'cuatro'
    spanish['five'] = 'cinco'
    return spanish

def main ():
    dictionary = createDictionary ()
    print (dictionary ['one'])
    print (dictionary ['two'])
    print (dictionary ['three'])

main ()
