def initial_state():
    return (0, 0, 0)

def is_goal(s):
    # Goal test: Check if `a==4` and `b==4`
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s

    # Pour from 8-liter to 5-liter
    t = 5 - y
    if x > 0 and t > 0:
        if x > t:
            yield (((x - t, 5, z)), t)
        else:
            yield (((0, y + x, z)), x)
            
    #Pour from the 8-liter bottle to the 3-liter bottle.
    t = 3 - z
    if x > 0 and t > 0:
        if x > t:
            yield (( (x - t,y, 3)), t)
        else:
            yield (( (0, y , z+x)), x) 
   
  
 # Pour from 5-liter to 8-liter
    t = 8 - x
    if y > 0 and t > 0:
        if y > t:
            yield (((x + t, y - t, z)), t)
        else:
            yield (((x + y, 0, z)), y)

    # Pour from 5-liter to 3-liter
    t = 3 - z
    if y > 0 and t > 0:
        if y > t:
            yield (( (x, y - t, z + t)), t)
        else:
            yield (((x, 0, z + y)), y)

    # Pour from 3-liter to 8-liter
    t = 8 - x
    if z > 0 and t > 0:
        if z > t:
            yield (((x + t, y, z - t)), t)
        else:
            yield (((x + z, y, 0)), z)

    # Pour from 3-liter to 5-liter
    t = 5 - y
    if z > 0 and t > 0:
        if z > t:
            yield (((x, y + t, z - t)), t)
        else:
            yield (((x, y + z, 0)), z)
   
   