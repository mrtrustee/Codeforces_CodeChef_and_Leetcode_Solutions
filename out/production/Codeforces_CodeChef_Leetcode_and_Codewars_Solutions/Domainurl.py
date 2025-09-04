def domain(url):
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    return url.split("/")[0].split(".")[0]