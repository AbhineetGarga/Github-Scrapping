import requests
from bs4 import BeautifulSoup as bs

'''An empty list to  store urls'''
urls= []


'''First function to allow user to add first Username to list'''
def scrape():
    git_user = input("Enter your GitHub username: ")
    urls.append(f"https://github.com/{git_user}")
    more()


'''Second function to allow user to add second and more Username to list'''
def more():
    user= input("Press 'y/n' to add url/carry the list")
    if user.lower() == 'y':
        scrape()
    elif user.lower() == 'n':
        print("Your image is ready")


scrape()

'''Time to find the requiered data from the website'''

for url in urls:
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    image = soup.find('img', attrs={'class': 'avatar'})['src']
    repositories = soup.find('span', {'class':'Counter'})['title']
    print(f"Image of url {url}")
    print(image)
    print(f"Number od repositories in url {url}")
    print(repositories)