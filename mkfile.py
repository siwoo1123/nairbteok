def makefile(q, jobs):
  file = open(f"nairbteok_{q}.csv", 'w')
  file.write("company, position, location, link\n")
  for job in jobs:
    file.write(f"{job['company'].replace(',', '/')}, {job['position'].replace(',', '/')}, {job['location'].replace(',', ' ')}, {job['link'].replace(',', '/')}\n")
  file.close()