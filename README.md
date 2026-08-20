# Damped Harmonic Oscillator

A simple numerical solver for the damped harmonic oscillator using Python, NumPy, and Matplotlib.

The program numerically solves

$$
m\ddot{x} + b\dot{x} + kx = 0
$$

using the Euler method, rather than substituting time into the known analytical solution.

## Math

The second-order differential equation

$$
m\ddot{x} + b\dot{x} + kx = 0
$$

is rewritten as two coupled first-order differential equations: 

$$
\frac{dx}{dt} = v
$$

and

$$
\frac{dv}{dt}=-\frac{b}{m}v-\frac{k}{m}x
$$

The acceleration at each timestep is therefore

$$a_i = -\frac{b}{m}v_i - \frac{k}{m}x_i$$

Euler's method approximates the velocity and position at the next timestep using

$$v_{i+1} = v_i + a_i\Delta t$$

and

$$x_{i+1} = x_i + v_i\Delta t$$

The program repeats these calculations across the full simulation time.

## Inputs

The program asks for five values:

```text
m b k t dt
```

where:

* $m$ = mass
* $b$ = damping coefficient
* $k$ = spring constant
* $t$ = total simulation time
* $\Delta t$ = timestep

The simulation uses the inital conditions:

$$
x(0) = 1
$$

and

$$
v(0) = 0
$$

## Damping Regimes

The damping regime (**underdamped, critically damped,** or **overdamped**) is determined from the input values using

$$
b^2 - 4mk
$$


The detected damping regime is displayed in the title of the output figure.

## Output

The program displays two plots.

### Position vs. Time

The first plot shows the displacement $x(t)$ as a function of time. This shows how the oscillator approaches the equilibrium position over the course of the simulation.

### Phase Space

The second plot displays velocity against position ($v \text{ vs. } x$). For an underdamped oscillator, the phase-space trajectory spirals toward the equilibrium point $(x,v) = (0,0)$ as energy is dissipated.



## Future Improvements

Possible future extensions include:

* User-defined initial conditions $x(0)$ and $v(0)$
* Higher-accuracy numerical methods such as Runge-Kutta methods
* Comparison between numerical and analytical solutions
* Direct comparison of underdamped, critically damped, and overdamped systems
* Extension into a general numerical solver for ordinary differential equations
