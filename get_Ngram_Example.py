# This is a simple example script showing how to read in some cribs from the 
# n-grams list given the crib word lengths
# Due to the size of the ngram data, it is worthwhile creating a bespoke 
# list of words to use, especially for short words 
#
# clearly you can do more sophisticated cutting, faster fucitons etc ... 
#
# Good Luck
#
import os

# create a dictionary of all the possible n-grams and their file locations
ngram_files = {}
for root, dirs, files in os.walk(os.path.join(".", "ngrams")):
    for file in files:
        path = os.path.join(root, file)
        key = file[0:-4]
        if key in ngram_files:
            ngram_files[key].append(path)
        else:
            ngram_files[key] = [path]

# The google n-grams have many words that can be cut, 
# This process has been started in the files in ./cutwords
# get lists of cut words
my_word_list = []
my_cribs_path = os.path.join(".", "cutwords")
for files in os.listdir(my_cribs_path):
    file_path = os.path.join(my_cribs_path, files)
    with open(file_path, 'r') as content:
        data = content.read()
        for word in data.split():
            my_word_list.append(word)
my_word_list_set = set(my_word_list)


def in_my_word_list(words=[]):
    '''
    Checks if a list of words are in my_word_list_set
    '''
    for word in words:
        if word not in my_word_list_set:
            return False
    return True

# get n_grams, and cut words to those in my_word_list
def get_cribs(ngram=[]):
    '''
    ngram a list of integers specfying the length of each word
    returns a list of cribs that match the word lengths 
    AND are in my_word_list
    '''
    return_cribs = []
    files_to_read = ngram_files["_".join(str(x) for x in ngram)]
    for file in files_to_read:
        with open(file, 'r') as content:
            for line in content.readlines():
                if in_my_word_list(line.split()[0:-1]):
                    return_cribs.append(line.rstrip())
    return return_cribs


# test for some cribs word lengths
hits = get_cribs([1, 2])
for hit in hits:
    print(hit)

hits = get_cribs([6, 4, 2])
for hit in hits:
    print(hit)