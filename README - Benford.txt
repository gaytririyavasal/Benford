

PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

For this assignment you'll build a Wordle wordlist by reading words from a file and build some tools that might help a Wordle player. This assignment is designed to test some of the skills from the two parts of the Week-11 material: file manipulation and tuples/sets/dictionaries. It has two major tasks corresponding to these parts.

Task 1: Building a Wordle wordlist. File words file contains a very long sorted series of lowercase English words, one per line. You should copy/download this file to your own computer. Complete the following function, which reads words from the file, filters them, returns a list of words that pass the filter. Filtering means the following: discard any words that are not five letters long, have any repeating letters, or end in 's'. Your resulting list will stay sorted if you add words to the end of the list you're creating. You can assume that there are no non-letter or upper case characters in the file (which is true). You can assume that the file exists. It would be a good idea to strip each word of extra whitespace. Finally, return a pair consisting of the wordlist and its length.

def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """
    ...

Note: Sometimes Windows has an issue with filenames that don't incude an extension; Linus and MacOS don't have that issue. If you are on a Windows system and find that you can't create a text file without the .txt extension, go ahead and add it and test your program on that file. You're not submitting your test code anyway, so it shouldn't really matter for this assignment; just don't hardcode the filename in the code you're submitting.

Task 2: Querying Your Wordlist. As a player makes guesses in Wordle, they gain information about what letters are and are not in the solution and where some of those letters fall in the answer. Often, one of the hardest things about playing Wordle is thinking of new guesses that use that information strategically. But computers are great at that sort of thing. In this task, you'll write four functions that would be very handy to have available when playing Wordle.

Complete the four functions below; these take your wordlist (the list you created in task1) and other information as parameters. The comments explain the semantics. There are also examples in the Sample Output section below of calls to these function. Be careful of the types; note that these return sets, not lists. (We chose to return sets mainly to give you additional practice with something besides lists.)

def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include. 
    """
    ...

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude. 
    """
    ... 

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    ...

def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    ...

Note that the file you submit need only contain the definitions of the functions called for, and any subsidiary functions you write. It shouldn't contain your test code, though you should certainly test it either in the Python interactive loop, or by running a test program.

Note also that sets and dictionaries are unordered. That means, if you run the same commands I did below, you may see the answers in different order. That's fine! Python makes no guarantees about the order in which the elements of sets or dictionaries will be printed; if order mattered you'd need to use a list or other data structure. But it doesn't matter in this assignment.

Sample Output:

Below are some sample calls to the function you are defining, run in the Python interactive loop.

> python
Python 3.6.9 (default, Mar 15 2022, 13:55:28) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from WordleAssistant import *
>>> wordlist, count = createWordlist( 'new-wordlist' )
>>> count
2094
>>> for i in range(10): print( wordlist[i], end = " ")
... 
abhor abide abler abode abort about above abuse ached acing >>> print()

>>> setABC = containsAll( wordlist, 'abc' )
>>> setABC
{'cobra', 'bract', 'brace', 'black', 'beach', 'basic', 'cabin', 'bacon', 'scuba', 'cable', 'batch'}
>>> setXYZ = containsAll( wordlist, 'xyz' )
>>> setXYZ
set()
>>> someWords = containsNone( wordlist, 'abcdefghijklmn' )
>>> someWords
{'strop', 'proxy', 'syrup', 'prosy', 'rusty', 'worst', 'spurt', 'soupy', 'story', 'spout', 'sport'}
>>> someMoreWords = containsNone( wordlist, 'abcdefghijklmnopqrstuvw' )
>>> someMoreWords
set()
>>> posDict = {'a':0, 'y':4}
>>> posWords = containsAtPositions( wordlist, posDict )
>>> posWords
{'angry', 'agony', 'artsy', 'aptly', 'amity', 'amply'}
>>> print( containsAtPositions( wordlist, {'a':0, 'b': 1 } ))
{'about', 'abode', 'abhor', 'abler', 'abort', 'above', 'abuse', 'abide'}
>>> possibleWords = getPossibleWords( wordlist, {'a':0, 'b':1}, "o", "v" )
>>> possibleWords
{'about', 'abode', 'abort', 'abhor'}
>>> 
