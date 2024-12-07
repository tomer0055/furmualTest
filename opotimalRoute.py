from dot import dot
import math
import numpy as np
from scipy.interpolate import CubicSpline
class optimalRoute:
    @staticmethod
    def sort_bt_distance(dots_array):
        for i in range(len(dots_array)):
            for j in range(i + 1, len(dots_array)):
                if dots_array[i].distance_to(dots_array[j]) > dots_array[j].distance_to(dots_array[i]):
                    dots_array[i], dots_array[j] = dots_array[j], dots_array[i]
        return dots_array

    def __init__(self, leftLayout, rightLayout):      
        self.leftLayout=self.sort_bt_distance(leftLayout)
        self.rightLayout = self.sort_bt_distance(rightLayout)
        self.casualRouteGraph = []
        self.op=[]
    @staticmethod
    def sort_bt_distance_continuous(dots_array):
        sorted_array = [dots_array[0]]
        dots_array = dots_array[1:]
        while dots_array:
            last_dot = sorted_array[-1]
            next_dot = min(dots_array, key=lambda dot: last_dot.distance_to(dot))
            sorted_array.append(next_dot)
            dots_array.remove(next_dot)
        return sorted_array

    def find_Slope(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            return 0
        return (y2 - y1) / (x2 - x1)  
    def find_Y_Intercept(self, x1, y1, slope):
        # y = mx + b
        return y1 - slope * x1
    def find_X_Intercept(self, y1, x1, slope):
        # x = (y - b) / m
        return (y1 - x1) / slope
    def find_X_between_two_functions(self, slope1, slope2, y_intercept1, y_intercept2):
        if(slope1==slope2):
            raise Exception("Slopes are equal")
        # x = (b2 - b1) / (m1 - m2)
        return (y_intercept2 - y_intercept1) / (slope1 - slope2)
    def find_Y_with_SlopeAndX(self, slope1, x1, y1, x):
        # y = m1 * x - m1 * x1 + y1
        return slope1*(x-x1)+y1

    def casualRoute(self):
        for i in range(len(self.leftLayout)):
            dot_right_1 = self.rightLayout[i]
            dot_left_1 = self.leftLayout[i]
            x1 = (dot_left_1.x+dot_right_1.x)/2
            y1 = (dot_left_1.y+dot_right_1.y)/2
            dot_middle = dot(x1, y1, "middle")
            self.casualRouteGraph.append(dot_middle)
   
        return self.sort_bt_distance_continuous(self.casualRouteGraph)
    def find_Middle_Dot(self, dot_left, dot_right):
        x = (dot_left.x + dot_right.x) / 2
        y = (dot_left.y + dot_right.y) / 2
        return dot(x, y, "middle")
    #leave this function as it is didnt use it just so you know the idea just found better way to do it
    def optimalRouteC(self):
        if(self.op==[]):
            self.op = self.casualRoute()
        op = self.op
        print("Calculating optimal route")
        length = len(op)
        extend = []
        i=0
        while(i+2 != length-1):
            dot_1 = op [i]
            dot_2 = op[(i+1)%length]
            dot_3 = op[(i+2)%length]
            
            slope1=self.find_Slope(dot_1.x, dot_1.y, dot_2.x, dot_2.y) #find slope between dot_1 and dot_2
            slope2=self.find_Slope(dot_2.x, dot_2.y, dot_3.x, dot_3.y) #find slope between dot_2 and dot_3
            if(abs(slope1-slope2)>0.001):
                distance=dot_1.distance_to(dot_3)
                numofpoints=math.ceil(distance/10)
                for j in range(1, numofpoints):
                    x = dot_1.x + j * (dot_3.x - dot_1.x) / numofpoints #x_L= x? + j*(x_R-x_L)/numofpoints
                    y = dot_1.y + j*(dot_3.y-dot_1.y)/numofpoints
                    extend.append(dot(x, y, "middle"))
 
            i=i+1
        # op.extend(extend)
        self.op= self.sort_bt_distance_continuous(extend)
        return self.op
    
    def MultiOptimalRoute(self,loops):
        
        for j in range(loops):
            self.optimalRouteC()
        
    
    def smooth_route(self):
        if(self.casualRouteGraph==[]):
            self.casualRoute()
        x = [dot.x for dot in self.casualRouteGraph]
        y = [dot.y for dot in self.casualRouteGraph]
        t = np.linspace(0, 1, len(self.casualRouteGraph))
        spline_x = CubicSpline(t, x)
        spline_y = CubicSpline(t, y)
        t_smooth = np.linspace(0, 1, 50000) 
        return [dot(spline_x(t), spline_y(t), "smooth") for t in t_smooth]        
        
        
     
            
        