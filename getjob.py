from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  # remoteok
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      link = job.find("a", class_="preventLink")["href"]
      img = job.find('td', class_="image").find('a', 'preventLink').find("img", class_="logo", itemprop="image")
      if company:
        company = company.string.strip()
      if position:
        position = position.string.strip()
      if location:
        location = location.string.strip()
      if link:
        link = f"https://remoteok.com{link.strip()}"
      if img:
        img = img['data-src']
      else:
        img = "https://raw.githubusercontent.com/siwoo1123/image-storage/main/ni.png"
      if company and position and location and link and img:
        job = {
          'company': company,
          'position': position,
          'location': location,
          'link': link,
          'img': img
        }
        results.append(job)

  # weworkremotely
  url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("li", class_="feature")
    for job in jobs:
      company = job.find("span", class_="company")
      position = job.find("span", class_="title")
      location = job.find("span", class_="region")
      link = job.find_all("a")[1]["href"]
      img = job.find('div', class_="flag-logo")
      if company:
        company = company.string.strip()
      if position:
        position = position.string.strip()
      if location:
        location = location.string
      if link:
        link = f"https://weworkremotely.com{link.strip()}"
      if img:
        img = img['style'].replace('background-image:url(', '').replace(')', '')
      else:
        img = 'https://raw.githubusercontent.com/siwoo1123/image-storage/main/ni.png'
      if company and position and location and link and img:
        job = {
          'company': company,
          'position': position,
          'location': location,
          'link': link,
          'img': img
        }
        results.append(job)
  return results