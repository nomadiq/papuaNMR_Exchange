# papuaNMR_Exchange

## Nz Exchange Fitting

### Preamble

These python programs are used to perform a fitting of the equations that describe peak intensities as a function of R1 relaxation,  exchange rate (k) and exchange (mixing) time between two slowly exchanging conformations. In the Farrow paper below, these confirmations are labeled 'n' and 'u' (native versus unfolded). The nomenclature used for this fitting software is state 'A' and state 'B'. Four peaks appear in these experiments for each exchanging system. The intensity of these four peaks is labeled as:

IAA: The intensity of system A that is recorded at position A
IBB: The intensity of system B that is recorded at position B
IAB: The intensity of system A that has moved to position B
IBA: The intenisty of system B that has moved to position A

In the experiments described in the references only 15N is active during the mixing (exchange) period so the peak for 'A moving to B' is seen as a peak with the same 1H frequency as A but now a frequency of B for 15N. 

### Data Preparation

### Fitting







**References:**

Farrow N, Zhang O, Forman-Kay J, Kay L. (1994) A heteronuclear correlation experiment for simultaneous determination of 15N longitudinal decay and chemical exchange rates of systems in slow equilibrium. J. Biomol. NMR. 4(5) 727-34.

Robson, S.A., Peterson, R., Bouchard, L.S., Villareal, V.A., Clubb, R.T. (2010) A heteronuclear zero quantum coherence Nz-exchange experiment that resolves resonance overlap and its application to measure the rates of heme binding to the IsdC protein. J. Am. Chem. Soc. 132, 9522-3.
