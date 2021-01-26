# import requests
# url_topnews = ('http://newsapi.org/v2/top-headlines?'
#        'country=in&'
#        'apiKey=606014a906f14ea59a48b33381c5f972')
#
# response = requests.get(url_topnews)
# news_details = response.json()
# for i in range(len(news_details['articles'])):
#        print(news_details['articles'][i]['title'])
#        print(news_details['articles'][i]['description'])
#        print(news_details['articles'][i]['url'])
#        print(news_details['articles'][i]['urlToImage'])
#        print(news_details['articles'][i]['publishedAt'])
#        print(news_details['articles'][i]['content'])
#        break

nums = [3,2,3]
target = 6
list_add = []
for i in range(len(nums)-1):
       for j in range(i):
           print(nums[i],nums[j])
           if nums[i] + nums[j] == target:
                  list_add.append(i)
                  list_add.append(j)
print(list_add)


