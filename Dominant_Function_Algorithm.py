## TIME LOG SUMMARY:
## Thursday,  16 May 2024:  2:22  // Choosing Problem; Finding Help / Mathematical Understanding; Setting Up Initial Functions and Graphing
## Friday,    17 May 2024:  0:43  // Coding Time Tracker + Improving Functionality and Readability of Exisitng Code; Further Research / Study
## Monday,    20 May 2024:  3:00  // Created Test File; Created Plots and Heat Maps for Critical Curve, Dominating Function and Perturbing Function
## Wednesday, 22 May 2024:  0:05  // Cleaned Up Code; Tested New Rouches_Theorem Function Call
## Thursday,  23 May 2024:  5:45  // Finished Plot for Reference; Refined Test Cases; Debugging; Testing; Enhanced Readability (Incl. Adding Creating create_complex_graph_example function); Further Work on Rouches_Theorem Function
## Friday,    24 May 2024:  1:30  // Attempted to Enhance Test File Robustness; Review Code

## Time Log Variable Initialization
time = 0
total_time_spent = []

## Time Logs by Day (Organized Chronologically by Date)
May16 = 142
total_time_spent.append(May16)

May17 = 43
total_time_spent.append(May17)

May20 = 155
total_time_spent.append(May20)

May22 = 5
total_time_spent.append(May22)

May23 = 345
total_time_spent.append(May23)

May24 = 90
total_time_spent.append(May24)

## Sum Total Time Logged in Project
for day in range(len(total_time_spent)):
    time += total_time_spent[day]

## Convert Time Log to Hours and Minutes, Then Print Statement
total_hours = time // 60
total_minutes = time % 60
remaining_time = 600 - time
remaining_hours = remaining_time // 60
remaining_minutes = remaining_time % 60

if remaining_hours > 0 and remaining_minutes > 0:
    print(f"""\033[31mTotal Time Spent on Coding Project = {total_hours} hours and {total_minutes} minutes. 
This means of the original 10 hours required, you need to complete another {remaining_hours} hours and {remaining_minutes} minutes.\n\33[0m""")
    
else:
    print(f"\033[37mTime Check for 10 Hours Spent on Project:  {total_hours} hours and {total_minutes} minutes\033[0m \n"
"   \033[32mCongratulations!!  You are ALL DONE!! :)\33[0m")



## Begin Remainder of Project Code
import numpy as np
import matplotlib.pyplot as plt


def dominant_part(z,  a, b, n, k):
    """
    dominant_part() Inputs:
        -- Parameter Values a, n and k From the Polynomial
        -- The Critical Curve Value z Being Evaluated
    THEN Returns the Value of the Analytic Portion of the Harmonic Polynomial
    """
    
    term1 = z ** n
    term2 = b / (z ** k)

    return term1 + term2 - 1


def perturbing_part(z, a, b, n, k):
    """
    perturbing_part() Inputs:
        -- Parameter Values b and k From the Polynomial
        -- The Critical Curve Value z Being Evaluated
    THEN Returns the Value of the Analytic Portion of the Harmonic Polynomial
    """

    return a / (z ** k)


def additional_polynomial(x, y, a, b, n, k, j, c, d):
    """
    additional_polynomial() Inputs:
        -- Free Variables:  x, y
        -- Input Parameters:  a, b, n, k, j, c, d
    THEN Returns the Full, Unparameterized Equation for the Critical Curve
    """

    return -d + (((b - a) * c + 0.12 * x**4) / (x**2 + y**2)**4 - \
                 (0.72 * x**2 * y**2) / (x**2 + y**2)**4 + (0.12 * y**4) / (x**2 + y**2)**4)
    

def plot_critical_curve(additional_polynomial, a, b, n, k, j, c, d, x_range, y_range, points):
    """
    plot_critical_curve() Inputs:
        -- The Equation Defining the Critical Curve (additional_polynomial in Mathematica Notebooks)
        -- Parameter Values:  a, b, n, k, j, c, d
        -- Ranges of Values:  x,_range, y_range
        -- Number of Points to Check Within Meshgrid
    THEN Outputs a Graph of the Critical Curve (in Purple)
    """
    
    ## Generate Meshgrid of x and y Values to Check
    x = np.linspace(x_range[0], x_range[1], points)
    y = np.linspace(y_range[0], y_range[1], points)
    X, Y = np.meshgrid(x, y)

    ## Evaluate Additional Polynomial Function at Each Point In Meshgrid to See if it Lies Along Critical Curve
    Z = additional_polynomial(X, Y, a, b, n, k, j, c, d)

    ## Plot the Surface
    plt.figure(figsize = (10, 8))
    plt.contour(X, Y, Z, levels = [0], colors = ["purple"])
    plt.title("Critical Curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


def plot_rouches_theorem(eq_function, a, b, n, k, j, c, d, x_range, y_range):
    """
    plot_rouches_theorem() Inputs:
        -- Parameter Values:  a, b, n, k, j, c, d
        -- Ranges of Values:  x, y
        -- Number of Points to Check Within Meshgrid
    THEN Outputs a Graph Depicting the Dominant and Perturbing Functions Along the Chosen Path
    NOTE:  A Printed Statement Will Also Be Output Immediately Before the Graph to Determine:
            -- If dominating_part is Greater Than perturbing_part() for ALL Values Checked
                -- If So, Prints Statement Indicating Such
                -- If Not, Returns Index, Point Along Critical Curve (in Complex Form)
                   of First Instance Where dominating_part !> perturbing_part AND
                   the Corresponding Values of dominate_part and perturbing_part
                -- Will Still Output Graph No Matter What (i.e., No Error Raised, So Read Terminal Carefully!)
    """

    ## Generate All Points to Check (Includes MANY More Points Than Plot of Critical Curve
    ##    this is because only the points within 'threshold' distance of the critical curve will be used.)
    points = 80000000  ## Quick Number:  1 - 10 Million; Ideal Balance:  40 - 100 Million; More Exact:  1 Billion
    x = np.linspace(x_range[0], x_range[1], int(np.sqrt(points)))
    y = np.linspace(y_range[0], y_range[1], int(np.sqrt(points)))
    X, Y = np.meshgrid(x, y)

    ## Evaluate Function's Magnitude (Modulus) on Grid/Plot
    Z = X + 1J * Y
    curve_values = additional_polynomial(X, Y, a, b, n, k, j, c, d)
    
    # Define Margin Around Critical Curve to Check and Apply Them Accordingly
    threshold = 0.000000001 ## Threshold Value Can Be More Specific With Higher points Value.  For Reference:  If points = 40 million, threshold Should Be About 0.0001.
    indices = np.abs(curve_values) < threshold
    Z_curve = Z[indices]

    ## Calculate Magnitude of Each Point Along Critical Curve
    Z_curve_magnitude = np.abs(Z_curve)

    ## Evaluate Dominant and Perturbing Functions Using Magnitudes (Moduli)
    dom_values = dominant_part(Z_curve_magnitude, a, b, n, k)
    per_values = perturbing_part(Z_curve_magnitude, a, b, n, k)

    ## Check Whether Dominant Function's Magnitude is Greater Than Perturbing Function's Magnitude
    dom_magnitudes = np.abs(dom_values)
    per_magnitudes = np.abs(per_values)
    is_dominant_greater = np.all(dom_magnitudes > per_magnitudes)
    is_perturbing_greater = np.all(per_magnitudes > dom_magnitudes)
    violation_index = np.where(dom_magnitudes <= per_magnitudes)[0]
    

    ## Print Result (Based on Checks Immediately Above)
    if is_dominant_greater:
        print("\033[35mThe magnitude of the DOMINATING function is greater than the magnitude of the perturbing function for all evaluated points.\033[0m")
    elif is_perturbing_greater:
        print("\033[33mThe PERTURBING function is greater than the dominant function at all evaluated points... did you mix them up?\033[0m")
    else:
        first_violation = violation_index[0]
        print(f"\033[31mThe magnitude of the dominant function is NOT greater than the magnitude of the perturbing function at index {first_violation}, z = {Z_curve[first_violation]}, Dominant Magnitude: {dom_magnitudes[first_violation]}, Perturbing Magnitude: {per_magnitudes[first_violation]}\033[0m")

    ## Set Plot Dimensions
    plt.figure(figsize=(17, 9.5))

    ## Plot the Real and Imaginary Parts of the Critical Curve
    plt.subplot(1, 2, 1)
    plt.scatter(np.real(Z_curve), np.imag(Z_curve), color='purple', s=1, label="Critical Curve", alpha=0.6)
    plt.xlabel("Real Component")
    plt.ylabel("Imaginary Component")
    plt.legend()
    plt.grid(True)

    ## Plot the Dominant and Perturbing Functions
    plt.subplot(1, 2, 2)
    plt.scatter(np.real(Z_curve), dom_magnitudes, color='blue', s=1, label="Dominating Function Magnitude", alpha=0.6)
    plt.scatter(np.real(Z_curve), per_magnitudes, color='red', s=1, label="Perturbing Function Magnitude", alpha=0.6)
    plt.xlabel("Real Component")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_complex_graph_example(a, b, k, n, z = 3):
    """
    plot_complex_graph_example() INPUTS:
        -- Parameter Values:  a, b, k, n
        -- z Is Defaulted to 3 Unless Specified in main()
    THEN Outputs a Graph Demonstrating Complex Graphs
    """

    ## Definition of Path in Complex Plane
    theta = np.linspace(0, 2*np.pi, 100)
    radius = abs(z) * (1 + np.cos(theta))
    path = radius * np.exp(1J * theta)

    ## Evaluate the Function Along the Path
    dominant_results = dominant_part(path, a, n, k)
    perturbing_results = perturbing_part(path, b, k)

    ## Plot the Real and Imaginary Parts of the Function Values
    plt.plot(np.real(path), np.imag(path), label = "Path in the Complex Plane")
    plt.plot(np.real(dominant_results), np.imag(dominant_results), label = "Perturbing Function")
    plt.plot(np.real(perturbing_results), np.imag(perturbing_results), label = "Dominant Perturbing Function")
    plt.xlabel("Real Component")
    plt.ylabel("Imaginary Component")
    plt.title("Complex Graph Example")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")

    ## Scope of x-axis and y-axis
    plt.xlim(-30, 30)
    plt.ylim(-30, 30)

    plt.show()


## Main Portion to Execute Code
def main():
    """
    The Purpose of main() Is To:
        (1) Receive User Input for Values of a, b, n, k
        (2) Set Scope For Future Graphs
        (3) Define All Other Variables Dependent Upon a, b, n, k
        (4) Call complex_graph_example(), plot_critical_curve(), plot_rouches_theorem()
    """

    ## For PyTest (Also Need to Comment Out Section Below Where Variables are Input):
    a = 2 *100000
    b = 1 * 100000
    n = 3
    k = 1

    ## Input Parameter Values and Ensure They Are Correctly Entered
    try:
        # a = float(input("Please enter value for a:  "))
        # b = float(input("Please enter value for b:  "))
        # n = int(input("Please enter value for n:  "))
        # k = int(input("Please enter value for k:  "))

        ## Set Scope and/or Constant z Value While Testing and Number of Points in Meshgrid
        s = 25
        points = 2000

        ## Set Dependent Paramters to be Introduced Later
        j = (3 * n / (50 * k)) * (1 + b / a)
        c = (k ** 2 / n ** 2) * j
        d = j / (a + b)

        ## Define Range for Plotting
        x_range = (-s, s)
        y_range = (-s, s)

        ## Visual Explanation/Example of Complex Graphing
        # plot_complex_graph_example(a, b, k, n)

        ## Plot Critical Curve 
        # plot_critical_curve(additional_polynomial, a, b, n, k, j, c, d, x_range, y_range, points)

        ## Visually Confirm Rouche's Theorem Applies
        plot_rouches_theorem(additional_polynomial, a, b, n, k, j, c, d, x_range, y_range)

    ## In Case Parameter Value Isn't Entered Correctly
    except ValueError as e:
        print(f"Invalid input: {e}")


main()