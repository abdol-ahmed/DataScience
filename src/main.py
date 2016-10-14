from collections import defaultdict
"""Count words."""
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    words = s.split(" ");
    
    wordCounts = defaultdict(int);                               
    for word in words:
        wordCounts[word]+= 1;
        
    sortedDict = sorted(wordCounts.items(), key=lambda x:(-x[1], x[0]))
    result = [(w,c) for w, c in sortedDict]

    return result[:n]


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()