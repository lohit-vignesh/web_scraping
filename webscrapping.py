from bs4 import BeautifulSoup

import requests

def get_all_a_tags(url):
    content = bs4_contents(url)
    a_tags = content.find_all('a')
    h_links = []
    with open('href.txt','a') as file:
        for anchor_tag in a_tags:
            href = anchor_tag.get('href')
            if href != None and href != '#':
                file.write(href+'\n')
                h_links.append(href)
    return h_links
                
    
def bs4_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup


def complete_link(url,list):
    full_links = []
    for atag in list:
        if atag.startswith("http"):
            full_links.append(atag)
        else:
            abs_url = url + atag
            full_links.append(abs_url)
    return full_links


def get_content(url):
    body_contents = bs4_contents(url)
    body = body_contents.get_text()
    with open('content.txt', 'w') as f:
        f.write(body)
    return body


def get_all_data(url):
    visited = []
    atags = get_all_a_tags(url)
    full_links = complete_link(url,atags)
    with open('atags.txt','a') as f:       
        for link in full_links:
            atwt = get_all_a_tags(link)
            atwt_full_links = complete_link(link,atags)
            for at in atwt_full_links:
                f.write(at+'\n')
                print(at)
            

def main():
    # Init All Website links
    all_links = 'https://www.bootlabstech.com'

    # Get all Tags from the webpage source
    get_all_data(all_links)

    # Form Proper URLs based on tags



if __name__ == "__main__":
    main()
