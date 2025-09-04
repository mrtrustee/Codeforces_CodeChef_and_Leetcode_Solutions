def generate_hashtag(s):
    if not s.strip():
        return False
    result = "#"+ ''.join(i.capitalize() for i in s.split())
    return result if len(result)<= 140 else False