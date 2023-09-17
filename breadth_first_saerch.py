from collections import deque
# import pprint

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["jonny", "thom"]
graph["thom"] =[]
graph["jonny"] =[]
graph["alice"] =[]
graph["anuj"] =[]
graph["peggy"] = []

# pprint.pprint(graph)
# pprint.pprint(search_queue)


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if (person_is_seller(person)):
                print('Person '+ person + ' is mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('No mango seller found!')
    return False


search("you")