from selenium import webdriver
from bs4 import BeautifulSoup

urls = [
'https://www.youtube.com/channel/UCKy1dAqELo0zrOtPkf0eTMw',
'https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw',
'https://www.youtube.com/channel/UCWVuy4NPohItH9-Gr7e8wqw',
'https://www.youtube.com/channel/UCbu2SsF-Or3Rsn3NxqODImw',
'https://www.youtube.com/channel/UC0vBXGSyV14uvJ4hECDOl0Q',
'https://www.youtube.com/channel/UC7nz6QUPAbGcE6r8bhvK8Hw',
'https://www.youtube.com/channel/UCkWQ0gDrqOCarmUKmppD7GQ',
'https://www.youtube.com/channel/UCVYamHliCI9rw1tHR1xbkfw',
'https://www.youtube.com/channel/UC9fSZHEh6XsRpX-xJc6lT3A',
'https://www.youtube.com/channel/UCIkLWMNCYzsI6cVQHJgEIqQ',
'https://www.youtube.com/channel/UCix7HIJ74fUDlHDkAAcyRPA',
'https://www.youtube.com/channel/UCftcLVz-jtPXoH3cWUUDwYw',
'https://www.youtube.com/channel/UChnN9MPURwKV2PbEoT2vhTQ',
'https://www.youtube.com/channel/UCheoCqHDwPcfS9Jrgz8siQw',
'https://www.youtube.com/channel/UCFfCqe7b9YiDk2ZiAG8UIGA',
'https://www.youtube.com/channel/UCTzLRZUgelatKZ4nyIKcAbg',
'https://www.youtube.com/channel/UCdBK94H6oZT2Q7l0-b0xmMg',
'https://www.youtube.com/channel/UCVW5_U7e5ruoIQ6FzUE7wRA',
'https://www.youtube.com/channel/UCwGX2cE21VPBEJ49hcprP9w',
'https://www.youtube.com/channel/UCKVei70N69V3V5wBQixHZbg',
'https://www.youtube.com/channel/UCv1yVR7b2Vaym2Zk1mI1urw',
'https://www.youtube.com/channel/UCCphfRu8VyLA_Af6vY40H0w',
'https://www.youtube.com/channel/UCuaErUDVKd4ftDWsImhCQuw',
'https://www.youtube.com/channel/UCr_pADpnsYU0vstpsKhroCA',
'https://www.youtube.com/channel/UC7dLvCYNwhYe-l__yczFp1Q',
'https://www.youtube.com/channel/UCT4J70qT-6HE94d_bAjGg4A'
]

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    for url in urls[:5]:
        driver.get('{}/videos'.format(url))
        
        #Strips the content encodes it and now can be made into bs object
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml') #parser for bs

        #Extract out the relevant details
        channels = driver.find_element_by_css_selector("#text.ytd-channel-name").text
        titles = soup.findAll('a',id='video-title')
        views = soup.findAll('span', class_="style-scope ytd-grid-video-renderer")
        print('Channel: {}'.format(channels))
        i = 0
        j = 1 
        for title in titles[:10]:
            print('\n{}) {}\t{}\t{}'.format(j,title.text,views[i].text,views[i+1].text))
            i += 2
            j += 1
        print('----------------------------------------------------------------------------------------------------')
    return driver

test = main()

#Get first 10 titles
'''for title in titles:
        count += 1
        print(title.text)
        if count == 10:
            break'''