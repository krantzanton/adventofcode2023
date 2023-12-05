import re
with open('day2input.txt', 'r') as f:
    games = f.read().splitlines()
    


replacement = {
    ", " : " , ",
    "; " : " ; ",
    ": " : " : "
}
def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: replacements[mo.group()], text) 


def score(game):
    res = multiple_replace(replacement, game).split()
    print(res)
    maxrgb = [1,1,1]
    current_game = 0
    pointsA = 0
    red_green_blue = [12,13,14]
    for index, elem in enumerate(res):
        match elem:
            case ";":
                is_valid = all(ele >= 0 for ele in red_green_blue)
                if not is_valid:
                    pointsA -= current_game
                    break
                red_green_blue = [12,13,14]
            case "red":
                if int(res[index-1]) >= maxrgb[0]:
                    maxrgb[0] = int(res[index-1])
                red_green_blue[0] = red_green_blue[0] - int(res[index-1])
            case "green":
                if int(res[index-1]) >= maxrgb[1]:
                    maxrgb[1] = int(res[index-1])
                red_green_blue[1] = red_green_blue[1] - int(res[index-1])
            case "blue":
                if int(res[index-1]) >= maxrgb[2]:
                    maxrgb[2] = int(res[index-1])
                red_green_blue[2] = red_green_blue[2] - int(res[index-1])
            case "Game":
                current_game = int(res[index+1])
                pointsA += current_game
                
            case default:
                continue
    is_valid = all(ele >= 0 for ele in red_green_blue)
    if not is_valid:
        pointsA = 0

    pointsB = maxrgb[0] * maxrgb[1] * maxrgb[2]
        
    
    print(pointsA)
    print(pointsB)
    return (pointsA,pointsB)
    
summaA = sum([score(game)[0] for game in games])
summaB = sum([score(game)[1] for game in games])

print(summaA)
print(summaB)
