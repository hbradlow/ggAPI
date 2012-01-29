import mechanize
import BeautifulSoup

br = mechanize.Browser()
br.open("http://www.mycrysis.com/emre8888")
br.select_form(nr=0)
br['age'] = "22"
response = br.submit()

soup = BeautifulSoup.BeautifulSoup(response.read())
print soup
