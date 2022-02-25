# Lock
def lock(name):
    idx = nodes.index(name) + 1
    c1 = idx * 2
    c2 = idx * 2 + 1
    if status[name] == "lock" or status[name] == "fail":
        return "false"
    else:
        p = idx//2
        status[nodes[p-1]] = "fail"
        status[name] = "lock"
        return "true"

# Unlock
def unlock(name):
    if status[name] == "lock":
        status[name] = "unlock"
        return "true"
    else:
        return "false"

# Upgrade
def upgrade(name):
	idx = nodes.index(name) + 1
	c1 = idx * 2
	c2 = idx * 2 + 1
	if c1 in range(1, n) and c2 in range(1, n):
		if status[nodes[c1-1]] == "lock" and status[nodes[c2-1]] == "lock":
			status[nodes[c1-1]] = "unlock"
			status[nodes[c2-1]] = "unlock"
			status[nodes[idx-1]] = "lock"
			return "true"
		else:
			return "false"

def setqueries(queries):
    d = []
    for j in queries:
        i = j.split()
        d.append(i[1])
        d.append(int(i[0]))

    status = {}
    for j in range(0, len(d)-1, 2):
        status[d[j]] = 0
    return status, d

def outputfunc(name, code):
	result = "false"
	if code == 1:
		result = lock(name)
	elif code == 2:
		result = unlock(name)
	elif code == 3:
		result = upgrade(name)
	return result


# if __name__ == '__main__':

n = int(input())
m = int(input())
apis = int(input())

nodes = []
queries = []
for i in range(n):
    place = input()
    nodes.append(place)

for q in range(apis):
    places = input()
    queries.append(places)

status, d = setqueries(queries)

for j in range(0, len(d) - 1, 2):
	print(outputfunc(d[j], d[j + 1]), end = " ")
