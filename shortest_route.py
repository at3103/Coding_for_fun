#Shortest route between departure and destination in a perfect grid city


def perfectCity(departure, destination):
    
    l = [departure, destination]
    ans = 0.0

    for i in range(2):
        if math.floor(l[0][i]) == math.floor(l[1][i]):
            j=0
            temp = []
            if int(l[j][i]) != l[j][i]: 
                t = l[not j][i] - 2 * math.floor(l[j][i]) + l[j][i]
                temp.append(t)
                t =  2 * math.ceil(l[j][i]) - l[not j][i]  - l[j][i]
                temp.append(t)
                ans+=min(temp)
                
        else:
            ans+=abs(l[0][i]-l[1][i])
                
    return ans


