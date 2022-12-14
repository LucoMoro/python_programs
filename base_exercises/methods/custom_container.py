class TagCloud:
    def __init__(self):
        self.__tags = {}
        #fixing __tags whit __ it means that we are setting tags private
    
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getItem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
       return iter(self.__tags)
    

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud["python"] = 10
print(cloud.__dict__)
print(cloud._TagCloud__tags)