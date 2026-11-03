# 객체로 구성된 게임월드

#계층적 구조를 갖는 겡미 월드
world = [ [], [] ]

# 게임 월드에 객체를 담는 함수
def add_object(o, depth = 0):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
        
    world.remove(o)

# 게임 로직
def update():
    for layer in world:
        for o in layer:
            o.update()

# 게임 렌더링
def rander():
    for layer in world:
        for o in layer:
            o.draw()
