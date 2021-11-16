zip_divs= soup.find_all('div', attrs={'class':class_name})
zip_divs = zip_divs[3:]
zip_links = []
base_zip_url = 'https://www.cms.gov'
for div in zip_divs:
    zip_url = base_zip_url + div.find_next('a').attrs['href']
    zip_links.append(zip_url)
