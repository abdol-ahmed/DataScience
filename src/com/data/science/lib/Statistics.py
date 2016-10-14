from com.data.science import reduce, math, plt
from collections import Counter

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,
               10 ,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9 ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,
               9  ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,7 ,7 ,7 ,7 ,
               7  ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,
               6  ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,
               4  ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,3 ,3 ,3 ,3 ,3 ,
               3  ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,
               2  ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,
               1  ,1 ,1 ,1]

def make_friend_counts_histogram(plt):
    friendCounts = Counter(num_friends)
    xs = range(max(num_friends)+1)
    ys = [friendCounts[x] for x in xs]
    plt.bar(xs, ys)  
    plt.axis([0, 101, 0, 25])          
    plt.xlabel("# of Friends")
    plt.ylabel("# of People")
    plt.title("Histogram of Friend Counts")
    plt.show()

def mean(x):
    return sum(x) / len(x)

def median(x):
    """finds the 'middle-most' value of x"""
    sortedValues = sorted(x);
    n = len(sortedValues)
    midPoint = n // 2; 
    isOdd =  n % 2
    return sortedValues[midPoint] if isOdd else (sortedValues[midPoint-1] + sortedValues[midPoint])/2

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() 
            if count == max_count]
      
num_points = len(num_friends)               # 204

largest_value = max(num_friends)            # 100
smallest_value = min(num_friends)           # 1

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]           # 1
second_smallest_value = sorted_values[1]    # 1
second_largest_value = sorted_values[-2]    # 49
    
if __name__ == "__main__":
    print "num_points", len(num_friends)
    print "largest value", max(num_friends)
    print "smallest value", min(num_friends)
    print "second_smallest_value", sorted_values[1]
    print "second_largest_value", sorted_values[-2]  
    print "mean(num_friends)", mean(num_friends)
    print "median(num_friends)", median(num_friends)
    print "quantile(num_friends, 0.10)", quantile(num_friends, 0.10)
    print "quantile(num_friends, 0.25)", quantile(num_friends, 0.25)
    print "quantile(num_friends, 0.75)", quantile(num_friends, 0.75)
    print "quantile(num_friends, 0.90)", quantile(num_friends, 0.90)
    print "mode(num_friends)", mode(num_friends)