def parkingSpot(carDimensions, parkingLot, luckySpot):
    flag = True
    flag2 = True
    drive_in = 0
    if luckySpot[2] - luckySpot[0] + 1 == carDimensions[1]:
        drive_in = 1
    x_start = [0,luckySpot[0],len(parkingLot), luckySpot[2] + 1]
    y_start = [0,luckySpot[1], len(parkingLot[0]) , luckySpot[3] + 1 ]
    
    for x in range(x_start[drive_in],luckySpot[2]+1):
        for y in range(y_start[not drive_in],luckySpot[3]+1):
            if parkingLot[x][y] == 1:
                flag = False
                break
        if not flag:
            break
    if not flag:
        print len(parkingLot), len(parkingLot[0]), x_start[drive_in + 2]
        for x in range(luckySpot[0], x_start[drive_in + 2]):
            for y in range(luckySpot[1] ,y_start[(not drive_in) + 2]):
                if parkingLot[x][y] == 1:
                    flag2 = False
                    return flag

    return flag or flag2
        
        



        
carDimensions= [2, 1]
parkingLot= [[1,0,1], 
 [1,0,1], 
 [1,1,1]]
luckySpot=[1, 1, 2, 1]

# carDimensions= [3, 2]
# parkingLot= [[1,0,1,0,1,0], 
#  [1,0,0,0,1,0], 
#  [0,0,0,0,0,1], 
#  [1,0,0,0,1,1]]
# luckySpot= [1, 1, 2, 3]

print parkingSpot(carDimensions, parkingLot, luckySpot)