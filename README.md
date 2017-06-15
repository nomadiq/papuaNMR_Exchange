# papuaNMR_Exchange

## Nz Exchange Fitting

### Preamble

These python programs are used to perform a fitting of the equations that describe peak intensities as a function of R1 relaxation,  exchange rate (k) and exchange (mixing) time between two slowly exchanging conformations. In the Farrow paper below, these confirmations are labeled 'n' and 'u' (native versus unfolded). The nomenclature used for this fitting software is state 'A' and state 'B'. Four peaks appear in these experiments for each exchanging system. The intensity of these four peaks is labeled as:

* IAA: The intensity of system A that is recorded at position A
* IBB: The intensity of system B that is recorded at position B
* IAB: The intensity of system A that has moved to position B
* IBA: The intenisty of system B that has moved to position A

In the experiments described in the references only 15N is active during the mixing (exchange) period so the peak for 'A moving to B' is seen as a peak with the same 1H frequency as A but now a frequency of B for 15N. 

### Data Preparation

Data files need to be in CSV format. Example files are included in this directory, e.g. H76_noise.csv. This files looks like this:

t,IAA,IAAn,IBB,IBBn,IAB,IABn,IBA,IBAn

0.0232,1553000,49000,816700,49000,329600,49000,233100,49000
0.0432,1345000,49000,613200,49000,385400,49000,312600,49000
0.0632,1208000,47000,580400,47000,458200,47000,364200,47000
0.0832,1036000,45000,552800,45000,447300,45000,325900,45000
0.1032,979300,44000,483200,44000,483600,44000,368200,44000
0.1432,822400,41000,479500,41000,495600,41000,407100,41000
0.2232,572100,37000,319100,37000,437300,37000,297200,37000
0.3032,461800,34000,239900,34000,345300,34000,224200,34000
0.5832,169400,25500,63770,25500,95080,25500,77400,25500
0.8032,13060,23000,16940,23000,10,23000,10,23000

or nicely formated:

|     t(sec)    |      IAA      |       IAAn    |      IBB      |      IBBn     |      IAB      |       IABn    |      IBA      |      IBAn     |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------    |
|0.0232|1553000|49000|816700|49000|329600|49000|233100|49000|
|0.0432|1345000|49000|613200|49000|385400|49000|312600|49000|
|0.0632|1208000|47000|580400|47000|458200|47000|364200|47000|
|0.0832|1036000|45000|552800|45000|447300|45000|325900|45000|
|0.1032|979300|44000|483200|44000|483600|44000|368200|44000|
|0.1432|822400|41000|479500|41000|495600|41000|407100|41000|
|0.2232|572100|37000|319100|37000|437300|37000|297200|37000|
|0.3032|461800|34000|239900|34000|345300|34000|224200|34000|
|0.5832|169400|25500|63770|25500|95080|25500|77400|25500|
|0.8032|13060|23000|16940|23000|10|23000|10|23000|

### Fitting







**References:**

Farrow N, Zhang O, Forman-Kay J, Kay L. (1994) A heteronuclear correlation experiment for simultaneous determination of 15N longitudinal decay and chemical exchange rates of systems in slow equilibrium. J. Biomol. NMR. 4(5) 727-34.

Robson, S.A., Peterson, R., Bouchard, L.S., Villareal, V.A., Clubb, R.T. (2010) A heteronuclear zero quantum coherence Nz-exchange experiment that resolves resonance overlap and its application to measure the rates of heme binding to the IsdC protein. J. Am. Chem. Soc. 132, 9522-3.
