import wikipedia

while True:
    article = input("Let me shoot you some quick info, what do you want to learn more about? \n")
    try:
        article = wikipedia.page(article)
    except:
        print(article, "Not found, please try again")
        continue
    print(wikipedia.summary(article))
    print("Info drawn from: ", article.url)
