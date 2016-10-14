from matplotlib import pyplot as plt
'''
Created on 07-Oct-2016
@author: aahmed
'''
from collections import Counter

def make_chart_simple_line_chart(plt):
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid');
     
    # add a title
    plt.title("Nominal GDP")

    # add a label to the y-axis
    plt.ylabel("Billions of $")
    plt.xlabel("Years")
    
    plt.show()

def make_chart_simple_bar_chart(plt):
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    plt.bar(xs, num_oscars)
    plt.ylabel("# of Academy Awards")
    
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
    plt.title("My Favorite Movies")
    plt.show();
    
def make_chart_histogram(plt):
    grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
    decile = lambda grade: grade // 10 * 10 
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()], # shift each bar to the left by 4
            histogram.values(),                # give each bar its correct height
            8)                                 # give each bar a width of 8
    plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105,
                                               # y-axis from 0 to 5
    plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()
    
def make_chart_misleading_y_axis(plt, mislead=True):
    mentions = [500, 505]
    years = [2013, 2014]
    
    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years) 
    plt.ylabel("# of times I heard someone say 'data science'")
    plt.ticklabel_format(useOffset=False)
    plt.axis([2012.5,2014.5,499,506])
    plt.title("Look at the 'Huge' Increase!")
    plt.show() 
    
def make_chart_several_line_charts(plt):
    variance     = [1,2,4,8,16,32,64,128,256]
    bias_squared = [256,128,64,32,16,8,4,2,1]
    total_error  = [x + y for x, y in zip(variance, bias_squared)]
    
    xs = range(len(variance))
    
    plt.plot(xs, variance, 'g-', label='Variance')
    plt.plot(xs, bias_squared, 'r-.', label='Bias Squared')
    plt.plot(xs, total_error, 'b:', label='Total Error')
    
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")

    plt.show()
    
def make_chart_scatter_plot(plt):

    friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    
    plt.scatter(friends, minutes)
    
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, 
             xy=(friend_count, minute_count), # put the label with its point
             xytext=(5, -5), # but slightly offset
             textcoords='offset points')
    
    
    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.draw()
    
    
if __name__ == '__main__':
    make_chart_simple_line_chart(plt)
    
    make_chart_simple_bar_chart(plt)
    
    #make_chart_histogram(plt)
    
    #make_chart_misleading_y_axis(plt)
    
    #make_chart_several_line_charts(plt)
    
    #make_chart_scatter_plot(plt)