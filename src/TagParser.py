def getAll(soup, tag):
	tags = soup.findAll(tag)
	return tags