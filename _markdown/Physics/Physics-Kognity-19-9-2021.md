<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>

# Circuits, potential, and current

## A simple electric circuit contains the following components:
1.  **An electric cell**: Usually powered by an electrochemical process – whose function is to raise the electric potential energy of any charges between two points and to create an electric field between those points: The electric potential energy of any charges increases as they move through the cell. We often consider the cell to be the start and finish of a circuit.
2.  **Connecting conductors**: These are usually metal wires with an insulated covering that carry an electric current to locations that are not near the cell. We usually assume that in the connecting conductors there is negligible resistance and energy loss, but we know the energy loss is never zero. 
3.  **A resistor** (as a general case): A conductor that impedes (resists) the flow of the electric current and transforms any excess electric potential energy into some other form such as heat. The resistor may act as a heating device (if a thin tungsten wire, it may increase its temperature until it glows white hot), or it may power a motor, or a transmitter, or a receiver, or many other devices. For our purposes in a first example, we will assume that the resistor transforms electric potential energy into such large internal thermal energy that it is dissipated as light emitted to the surroundings: This is an incandescent (filament) lightbulb.


>#### Definition
>
>An electric **cell** increases the electric potential energy of any charge that flows through it.
>
>**Connecting conductors** (such as wires) are assumed to be made from metals that do not dissipate electric energy as charge passes through them. 
>
>**Resistors** are materials that impede (resist) internal charge flow and that transform electrical potential energy into some other form such as internal thermal energy.


### Kirchhoff's first law

In a more complex electric circuit such as **Figure 6**, there will be points in the electric circuit diagram shown by a dot indicating that two (or more) connecting conductors are joined. In **Figure 6** these are the points labelled R, S, W, and T. At these junctions the electric current will split into, or merge from, two (or more) charge streams.


$$\sum_{m=1}^{n} I_m = 0$$

where n is the total number of branches entering or leaving a single junction and the current in each of the branches is Im. The current flowing into a junction is defined as positive and the current flowing out of a junction is defined as negative. Kirchhoff's first law of electric circuits is also known as the junction rule.

### Kirchhoff's second law

When current flows through a resistor, electric potential energy will be transformed to internal thermal energy. We know this from the microscopic collision behaviour of the charge carriers in the atomic lattice. Therefore the electric potential where the charge enters a resistor must be greater than the electric potential where the charge leaves a resistor. The current will pass through the potential gradient such that there will be a potential difference across each resistor which drives a current through that resistor.


$$\sum_{m=1}^{n} V_m = 0$$


Here, n is the total number of cells or resistors encountered in the loop and the potential difference at each element is Vm. The potential difference is positive when moving in the direction of conventional current flow through a cell and a potential difference is negative when moving through a resistor in the direction of conventional current flow. Kirchhoff's second law of electric circuits is also known as the loop rule.

>#### Be aware
>
>We determine potential differences **across** electric circuit components.
>
>We determine currents **through** electric circuit components.

# Circuits and resistance

>#### Definition
>
>A potential difference applied across two points of a resistor (a conductor that has resistance) results in a current through it that varies inversely with the **resistance** of the resistor.
>
>In symbols, for a resistor with resistance R,  I=VR  where V  is the potential difference across it, and II is the current passing through it.
>
>The **resistance** of a conductor is the potential difference across it per unit current passing through it, or R=VI.


$$V \times A^{-1} = ohm = \Omega$$

> #### Definition
>
>The **resistivity**, ρ,ρ,  of a substance is the resistance per unit length of the material with a unit cross-section.
>
>The units of resistivity are Ω⋅m2⋅m−1=Ω⋅m


>#### Definition
>
>The **resistance** of an object – where current flows along its length – is proportional to its resistivity, proportional to its length, and inversely pro>portional to cross-sectional area.
>
>In symbols, $$R=\rho LA$$,  $$R=\rho LA$$, where rho is resistivity, L is the length along current flow, and A is the cross-sectional area.
>
>In your IB Physics data booklet you will see the formula written as: $$\rho =\frac{RA}{L}$$

## Resistance and temperature

One of the most common uses of electricity is for heating. Electrical energy from a power source is transformed in a resistor as internal thermal energy. As you know, internal thermal energy is the random kinetic energy and potential energy of the vibrations of the atoms in the metal lattice and kinetic energy of the mobile electrons. Therefore, increased internal energy would further inhibit the charge carrier drift through the lattice. This is a typical positive feedback loop in which the resistance increases further, at least until thermal equilibrium is reached and the energy generated internally is transferred to whatever is being heated at a constant rate. Resistors used for heating are usually large and rugged and designed to allow efficient thermal energy transfer to the object or fluid being heated.

>#### Definition
>
>**Ohm's law** states that for a metal held at constant temperature, the current flowing through it will be proportional to the potential difference across it.
>
>For an ohmic conductor at constant temperature $$I \propto V$$,  where I is the current through it, and V is the potential difference across it.


## Resistors in combination 

In electric circuits, there are often many resistors (and other components) that are interconnected in various configurations. In general, resistors may be arranged in two fundamentally different dispositions:

-   The same current flows through all resistors: There is no alternative branching of current flow in the resistor. Each resistor is connected to the next in sequence, as in a daisy-chain, and the potential difference across each resistor may vary (and depends on each resistor and the current through the set of resistors); this is called a **series circuit**.
-   The same potential difference is applied across all resistors: The current into the group of resistors is distributed among all of them and there is no sequential arrangement of resistors. The current through each resistor may vary (and depends on each resistor and the potential difference across the group); this is called a **parallel circuit**.



### In Series
$$R_{AB} = \sum_{m}R_{m}$$

### In parallel

$$R_{AB} = \sum_{m} \frac{1}{R_m}$$

## Variable resistors


### Potentiometers

Electrical appliances need to produce a variable potential difference such as increasing the audio volume on a music speaker, brightening a light bulb, or varying the speed of an electric fan. This is done with a variable potential divider, also known as a potentiometer. This component is nothing more than a resistor with a potential difference across it, but with a third connecting point that can be moved along the length of the resistor

### Light-dependent resistors

Sometimes potential dividers are used in sensors to trigger an alarm. For example, a light-dependent resistor (LDR) is a device whose resistance decreases when illuminated. When connected in series with another resistor, the pair becomes a potential divider. When light falls on the LDR, the resistance will decrease.



# Circuits and energy

>#### Definition
>
>The **electric power** transformed by a device in a circuit is equal to the product of the potential difference across it and the current through it.
>
>In symbols, the electric power transformed by a device, **P**, is:
>
>$$P = I V$$
>
>Here, I is the current through the device, and V is the potential difference across it.


$$P = I^2R$$



