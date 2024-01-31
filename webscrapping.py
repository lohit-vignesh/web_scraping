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
                if 'wpriver' not in href:
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


def get_title(link):
    page_content = bs4_contents(link)
    title_tag = page_content.find_all('title')
    title = title_tag[0]
    return title


def get_content(url):
    body_contents = bs4_contents(url)
    body = body_contents.get_text()
    with open('content.txt', 'a') as f:
        f.write(str(get_title(url)))
        if body != None:
            f.write(body)


def get_all_links(url):
    visited = []
    atags = get_all_a_tags(url)
    full_links = complete_link(url,atags)
    with open('atags.txt','a') as f:       
        for link in full_links:
            if link not in visited:
                atwt = get_all_a_tags(link)
                atwt_full_links = complete_link(link,atags)
                visited.append(link)
                f.write(link+'\n')
                get_content(link)
                for at in atwt_full_links:
                    if at not in visited:
                        f.write("   "+at+'\n')
                        visited.append(at)
                        get_content(at)                   
                        # print(at)
    for i in visited:
        print(i)

def main():
    # Init All Website links
    all_links = 'https://www.bootlabstech.com/'

    # Get all Tags from the webpage source
    get_all_links(all_links)

    # Form Proper URLs based on tags



if __name__ == "__main__":
    main()
