'''
Created on May 11, 2019

https://www.datamuse.com/api/

@author: BA030483
'''
from datamuse import datamuse
api = datamuse.Datamuse()

text = "Fun of the world is a fruit with no seeds and me when I have to poop."
text = "Life is like a rolling fruit.  It rolls along, and then a smart thing eats it and rolls along."
# text = "Mary had a little lamb.  It's fleece was white as snow."
# text = input("Enter some text:  ")


for word in text.split():
    result = word
    synonyms = api.words(ml=word,qe='ml',md='p',max=5) # Entertaining of first globe is equally yield far nary sow ampersands too when i get mous poop. 
#     synonyms = api.words(rel_syn=word,max=1)  # Play of the man is amp yield with no seeds and me once one bear to poop.
    if len(synonyms) > 0:
        part_of_speech = synonyms[0]['tags'][-1]
        for i in range(1,len(synonyms)):
            if synonyms[i]['score'] > 1000 and synonyms[i]['tags'][-1] == part_of_speech:
                result = synonyms[i]['word']
                if word[0].isupper():
                    result = result.capitalize()
                break
    print(result + ' ', sep=' ', end='')

# orange_rhymes = api.words(rel_rhy='orange', max=5)
# orange_near_rhymes = api.words(rel_nry='orange', max=5)
#   
# foo_complete = api.suggest(s='foo', max=10)
# 
# from datamuse_demo import scripts
# foo_df = scripts.dm_to_df(foo_complete)
