#Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), 
#where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.
#Return True if the circle and rectangle are overlapped otherwise return False.
#In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.
#23nd two weekly contest
#第3題

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        #circle funtion (x-h)-^2 + (y-k)^2 = r^2

        #cover
        if x2 >= (radius + x_center) and y1 <= (y_center - radius) and x1 <= (x_center - radius) and y2 >= (radius + y_center):
            return 1
        
        #check x
        if (pow(radius, 2) - pow(x1 - x_center, 2) >= 0):
            if pow(radius, 2) - pow(x1 - x_center, 2) == 0:
                n = y_center
                if  y1 <= n <= y2:
                    return 1
            else:    
                n = pow(radius, 2) - pow(x1 - x_center, 2)
                n = pow(n, 0.5)
                if (y_center + n) <= y2 and y1 <= (y_center - n):
                    return 1
                elif (y_center - n) <= y1 <= (y_center + n):
                    return 1
                elif (y_center - n) <= y2 <= (y_center + n):
                    return 1
        if (pow(radius, 2) - pow(x2 - x_center, 2) >= 0):
            if pow(radius, 2) - pow(x2 - x_center, 2) == 0:
                n = y_center
                if  y1 <= n <= y2:
                    return 1
            else:  
                n = pow(radius, 2) - pow(x2 - x_center, 2)
                n = pow(n, 0.5)
                if (y_center + n) <= y2 and y1 <= (y_center - n):
                    return 1
                elif (y_center - n) <= y2 <= (y_center + n):
                    return 1
                elif (y_center - n) <= y1 <= (y_center + n):
                    return 1
        #check y
        if (pow(radius, 2) - pow(y1 - y_center, 2) >= 0):
            if pow(radius, 2) - pow(y1 - y_center, 2) == 0:
                n = x_center
                if  x1 <= n <= x2:
                    return 1
            else:
                n = pow(radius, 2) - pow(y1 - y_center, 2)
                n = pow(n, 0.5)
                if (x_center + n) <= x2 and x1 <= (x_center - n):
                    return 1
                elif (x_center - n) <= x1 <= (x_center + n):
                    return 1
                elif (x_center - n) <= x2 <= (x_center + n):
                    return 1
        if (pow(radius, 2) - pow(y2 - y_center, 2) >= 0):
            if pow(radius, 2) - pow(y2 - y_center, 2) == 0:
                n = x_center
                if  x1 <= n <= x2:
                    return 1
            else:
                n = pow(radius, 2) - pow(y2 - y_center, 2)
                n = pow(n, 0.5)
                if (x_center + n) <= x2 and x1 <= (x_center - n):
                    return 1
                elif (x_center - n) <= x2 <= (x_center + n):
                    return 1
                elif (x_center - n) <= x1 <= (x_center + n):
                    return 1
        return 0