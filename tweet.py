# list of user name
def username_tweet_(testcase, n):
    test_count = 0
    tweet_names = []
    
    while test_count < testcase:
        count = 0
        while count < n:
            name = str(input())
            tweet_names.append(name)
            count += 1

        test_count += 1
    return tweet_names


# count tweet
def tweet_count(tweet_names):
    counte = {}
    for name in tweet_names:
        if name not in counte:
            counte[name] = 1
        else:
            counte[name] += 1
    return counte

    

# find most tweet
def most_tweet(counte):
    repeat = counte.values()
    lookup = set(repeat)
    
    for item in lookup:
        duplicate = ([(k, v) for k,v in sorted(counte.items()) if v == item])      
        if len(duplicate) > 1:
            for k,v in duplicate:
                print (k,v)

        max_v = max(counte.values())
        temp_max = [(k,v) for k,v in sorted(counte.items()) if v == max_v]       

        if temp_max != duplicate:
            for k,v in temp_max:
                print (k,v)



# main function 
if __name__ == "__main__":
    testcase = int(input())
    n = int(input())
    tweet_names = username_tweet_(testcase, n)
    counte = tweet_count(tweet_names)
    most_tweet(counte)
    

