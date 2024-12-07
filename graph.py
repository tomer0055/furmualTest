import dot;
import matplotlib.pyplot as plt
class graph:
    def __init__(self, layoutLeft, layoutRight, optimalRoute):
        self.layoutLeft = layoutLeft
        self.layoutRight = layoutRight
        self.optimalRoute = optimalRoute
    def zoom(self, factor):
        """Zoom in or out by a percentage; negative is out."""
        x_min, x_max, y_min, y_max = plt.axis()
        x_delta = (x_max - x_min) * factor / 100
        y_delta = (y_max - y_min) * factor / 100
        plt.axis((x_min + x_delta, x_max - x_delta,
                  y_min + y_delta, y_max - y_delta))

    def draw(self):
        print("Drawing graph")
        # Data for layoutLeft
        x_left = [d.x for d in self.layoutLeft]
        y_left = [d.y for d in self.layoutLeft]
        colors_left = [d.color for d in self.layoutLeft]

        # Data for layoutRight
        x_right = [d.x for d in self.layoutRight]
        y_right = [d.y for d in self.layoutRight]
        colors_right = [d.color for d in self.layoutRight]

        x_optimal = [d.x for d in self.optimalRoute]
        y_optimal = [d.y for d in self.optimalRoute]
        colors_optimal = [d.color for d in self.optimalRoute]


        # Create the figure
        plt.figure(figsize=(10, 10))

        # Scatter plot for layoutLeft
        plt.scatter(x_left, y_left, color=colors_left, s=10, alpha=0.7, label="Layout Left")
        for i, d in enumerate(self.layoutLeft):
            plt.text(d.x, d.y, f'L{i}', fontsize=9, ha='right')


        # Scatter plot for layoutRight
        plt.scatter(x_right, y_right, color=colors_right, s=10, alpha=0.7, label="Layout Right")
        for i, d in enumerate(self.layoutRight):
            plt.text(d.x, d.y, f'R{i}', fontsize=9, ha='right')

        plt.scatter(x_optimal, y_optimal, color=colors_optimal, s=10, alpha=0.7, label="Optimal Route")
        # for i, d in enumerate(self.optimalRoute):
        #     plt.text(d.x, d.y, f'M{i}', fontsize=9, ha='right')
        
        
        
        
        
        # Title and labels
        
        
        
        

        plt.plot(x_optimal, y_optimal, color='green', linestyle='-', linewidth=1, label="Optimal Route Line")
        
        
        
        plt.title("Dots on graph representing cones and optimal path")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")



        # Scaling and axis limits
        margin = 30
        all_x = x_left + x_right
        all_y = y_left + y_right
        plt.xlim(min(all_x) - margin, max(all_x) + margin)
        plt.ylim(min(all_y) - margin, max(all_y) + margin)
        plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
       

        self.zoom(0.1)
        

        # Legend and display
        plt.tight_layout()
        plt.legend(fontsize=1)
        plt.show()