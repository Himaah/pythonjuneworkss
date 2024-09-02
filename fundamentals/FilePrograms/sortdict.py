placements={"testing":5,"python":6}
def get_value(key):
    return placements.get(key)
srt=sorted(placements,key=get_value,reverse=True)
print(srt)
