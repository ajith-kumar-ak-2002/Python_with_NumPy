### Python with NumPy

## Basic of Numpy
* find size of the array
* find shape of the array
* find Dimensions of the array
* Data type
* Individual Item Size
* Total Bytes of the array

## Indexing & Slicing in NumPy
* 1D Indexing
* 2D Indexing
* 1D Slicing
* 2D Slicing

## NumPy Functions for array Creation 
* np.array -- 1D & 2D (Returns Arrays)
* np.zeros -- 1D & 2D (Return Only Zeros)
* np.ones  -- 1D & 2D (Returns only ones)
* np.full  -- 1D & 2D (Creates an array filled with a constant value.)
* np.arange -- 1D & 2D ( np.arange(start, stop, step) )
* ### np.linspace
     * Syntax ----- np.linspace(start, stop, num=50, endpoint=True, retstep=False) 
     * start – starting value
     * stop – ending value
     * num – how many values you want
     * endpoint=True – include stop value or not
     * retstep=True – also return spacing between values
* np.eye ( Creates an identity matrix where diagonal elements are 1, rest are 0 )

### Arrays Reshaping
* reshape --- it converts 1D array to 2D array
* flatten --- 2D Converts into One 1D its creates a copy from original
* ravel --- if User Change in copyed file also in original also may change
* newaxis --- it converts into rowa to column and column to row
* resize --- Resizes array even if shape doesn’t match. It repeats data if needed

### Random Number Generator
* rand            * It gives Float Value
* randint         * It Gives Integer Value
* randn           * Create 5 natural-looking random numbers
* rand seed       * Fixes the random values so results are the same every time
* rand Choice     * Selects random items from a list or array

### NumPy Boolean Indexing & Filtering
* Basic Boolean Indexing           ----- Basic Boolean Indexing
* Multiple Conditions             -------Combine conditions using & (AND), | (OR), ~ (NOT)
* Where Function                     ------Find indices where condition is True, or replace values
* Filtering 2D Arrays                 -------Apply conditions to 2D arrays (tables/matrices)
* One Real Life Example                 ------ Temperature data
