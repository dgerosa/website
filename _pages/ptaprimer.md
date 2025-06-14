---
layout: archive
title: "A PTA primer"
permalink: /ptaprimer/
author_profile: true
---

> *Organized at the Birmingham GW Institute and led by Chris Moore, this journal club/mini class/group study introduces the basic physics of Pulsar Timing Array and some of the latest developments.*


The next few years are expected to be a golden age for pulsar timing array (PTA) science. The recent tentative claim of a detection of an astrophysical signal in the NANOGrav 12.5-year data set is expected to be confirmed, thereby opening a new observational window on supermassive black holes. In order to better follow these developments, we will run a spring journal club in which we aim to review some key papers in the field. 

We will meet at **2.00 pm on Fridays** starting on May 7th, 2021 and running for approximately 7 weeks.

### Agenda

A rough plan/agenda, plus minutes and useful references will be kept up to date on [this overleaf](https://www.overleaf.com/read/yfycjkwjdxgk)

The zoom link is available on our [wiki](http://gitlab.sr.bham.ac.uk/cmoore/GWastro_MeetingNotes/wikis/pta_jc) (Birmingham ASR login required). If you can’t see it, please ask either Chris or Davide.

*   Episode 1. The birth of an idea.
*   Episode 2. The basic physics of PTAs.
*   Episode 3. Correlations are key, the Hellings and Downs curve.
*   Episode 4. A practical theorem.
*   Episode 5. The astro side of things, predicting the nHz GW spectrum.
*   Episode 6: A first detection of nHz GWs?
*   Episode 7: Anisotropy.

### Episode 1. The birth of an idea

Led by Alberto.

*   Main paper for today:  
    [Foster and Backer. “Constructing a Pulsar Timing Array” (1990)](https://ui.adsabs.harvard.edu/abs/1990ApJ...361..300F/abstract).  
    This is one of the key papers suggesting a dedicated effort to time pulsars with the aim of detecting low-frequency GWs.
*   A couple of the earliest (if not the earliest?) papers suggesting pulsar timing as a means to detect GWs:  
    [Detweiler. “Pulsar timing measurements and the search for gravitational waves” (1979)](https://ui.adsabs.harvard.edu/abs/1979ApJ...234.1100D/abstract).  
    [Sazhin “Opportunities for detecting ultralong gravitational waves” (1978)](https://ui.adsabs.harvard.edu/abs/1978SvA....22...36S/abstract).
*   Early observational upper limits on GWs:  
    [Romani and Taylor. “An upper limit on the stochastic background of ultralow-frequency gravitational waves” (1983)](https://davidegerosa.com/wp-admin/post.php?post=4164&action=edit#page_6https://ui.adsabs.harvard.edu/abs/1983ApJ...265L..35R/abstract).  
    [Hellings and Downs. “Upper limits on the isotropic gravitational radiation background from pulsar timing analysis” (1983)](https://ui.adsabs.harvard.edu/abs/1983ApJ...265L..39H/abstract).
*   See also:  
    [Foster and Backer. “Results from the Berkeley-NRAO Pulsar Timing Array Experiment” (1989)](https://ui.adsabs.harvard.edu/abs/1989BAAS...21.1205F/abstract).

### Episode 2. The basic physics of PTAs

Led by Antoine

*   Main paper: [Detweiler. “Pulsar timing measurements and the search for gravitational waves”.  
    1979](https://ui.adsabs.harvard.edu/abs/1979ApJ...234.1100D/abstract)
*   We will review the basic physics that governs how PTAs work. In particular, we will review the  
    derivation of this equation that describes the Doppler response of a pulsar’s frequency to GWs:  
    $$(z(t,\Omega) = \frac{p^i p^j}{2(1+\Omega\cdot p)} \Delta h\_{ij}(t)$$
*   The earliest paper discussing the effect described by equation 1 seems to be [Kaufmann. “Redshift Fluctuations arising from Gravitational Waves”. 1970](https://ui.adsabs.harvard.edu/abs/1970Natur.227..157K/abstract)
*   This is another early and highly cited paper for this derivation [Estabrook and Wahlquist. “Response of Doppler spacecraft tracking to gravitational radiation.” 1975](https://ui.adsabs.harvard.edu/abs/1975GReGr...6..439E/abstract)
*   For another derivation of equation 1, see also appendix A of [Anholm et al. “Optimal strategies for gravitational wave stochastic background searches in pulsar timing data”. 2009](https://ui.adsabs.harvard.edu/abs/2009PhRvD..79h4030A/abstract)
*   We can also discuss order of magnitude estimates and scaling laws for the sensitivity and bandwidth
*   of PTAs: [Moore, Taylor, and Gair. “Estimating the sensitivity of pulsar timing arrays”. 2015](https://ui.adsabs.harvard.edu/abs/2015CQGra..32e5004M/abstract)

### Episode 3. Correlations are key: the Hellings and Downs curve

Led by Chris

*   Main paper: [Hellings and Downs. “Upper limits on the isotropic gravitational radiation background from pulsar timing analysis.” 1983](https://ui.adsabs.harvard.edu/abs/1983ApJ...265L..39H/abstract)
*   We aim to derive and understand the importance of the Hellings and Downs curve for PTAs  
    $$C(\theta) = \frac{1-\cos\theta}{2}\log\left(\frac{1-\cos\theta}{2}\right)-\frac{1}{6} \frac{1-\cos\theta}{2} + \frac{1}{3}$$  
    This equation describes the angular part of the correlated signal that is the target of stochastic PTA searches.
*   For a pedagogical discussion of the Hellings and Downs curve, see [Jenet and Romano. “Understanding the gravitational-wave Hellings and Downs curve for pulsar timing arrays in terms of sound and electromagnetic waves”. 2015](https://ui.adsabs.harvard.edu/abs/2015AmJPh..83..635J/abstract)
*   For similar calculations of generalised HD curves describing correlations in modified gravity scenarios with other GW polarisations, see [Lee, Jenet, and Price. “Pulsar Timing as a Probe of Non-Einsteinian Polarizations of Gravitational Waves”. 2008](https://ui.adsabs.harvard.edu/abs/2008ApJ...685.1304L/abstract)
*   For a nice treatment of correlations with spherical harmonics and nice visualisations, [Roebber and Holder. “Harmonic Space Analysis of Pulsar Timing Array Redshift Maps”. 2017](https://ui.adsabs.harvard.edu/abs/2017ApJ...835...21R/abstract)
*   For the analogous derivation of the “overlap reduction function” in the context of ground–based detectors see [Allen and Romano. “Detecting a stochastic background of gravitational radiation: Signal processing strategies and sensitivities”. 1999](https://ui.adsabs.harvard.edu/abs/1999PhRvD..59j2001A/abstract)

### Episode 4. A practical theorem

Led by Natalie

*   Main paper: [Phinney. “A Practical Theorem on Gravitational Wave Backgrounds”. 2001](https://ui.adsabs.harvard.edu/abs/2001astro.ph..8028P/abstract)
*   Turning towards the astro side of things, if you know about the properties of the population of binary black holes, and how this population evolves over cosmic time, how do you calculate the predicted PTA signal?

### Episode 5. The astro side of things: predicting the nHz GW spectrum

Led by Davide

*   Main paper: [Sesana. “Systematic investigation of the expected gravitational wave signal from supermassive black hole binaries in the pulsar timing band.” 2013](https://ui.adsabs.harvard.edu/abs/2013MNRAS.433L...1S)
*   We will discuss the ingredients entering the astro predictions of the expected PTA signal. This is also related to the question of whether we expect individual or stochastic sources.
*   A fairly early paper predicting \(h\_c(f = 10^{-8}\,\mathrm{Hz})\sim 5\times10^{-16} – 8\times 10^{-15}\) , [Sesana, Vecchio, and Colacino. “The stochastic gravitational-wave background from massive black hole binary systems: implications for observations with Pulsar Timing Arrays”. 2008](https://ui.adsabs.harvard.edu/abs/2008MNRAS.390..192S/abstract)
*   On the question of whether we expect single sources or a stochastic signal, we could read [Ravi et al. “Does a “Stochastic” Background of Gravitational Waves Exist in the Pulsar Timing Band?” 2012](https://ui.adsabs.harvard.edu/abs/2012ApJ...761...84R)
*   An optimistic paper that predicted louder signals, [McWilliams, Ostriker, and Pretorius. “The imminent detection of gravitational waves from massive black-hole binaries with pulsar timing arrays”. 2012](https://ui.adsabs.harvard.edu/abs/2012arXiv1211.4590M/abstract)

### Episode 6. A first detection of nHz GWs?

Led by Riccardo

*   Main paper: [Arzoumanian et al. “The NANOGrav 12.5 yr Data Set: Search for an Isotropic Stochastic Gravitational-wave Background”. 2020](https://ui.adsabs.harvard.edu/abs/2020ApJ...905L..34A/abstract)
*   We will discuss the first tentative signs of a detection of GWs by the NANOGrav PTA and what remains to be done before this a confident detection can be claimed.
*   When can we expect a clear detection from NANOGrav? [Pol et al. “Astrophysics Milestones For Pulsar Timing Array Gravitational Wave Detection”. 2020](https://ui.adsabs.harvard.edu/abs/2021ApJ...911L..34P/abstract)

### Episode 7. Anisotropy

Led by Geraint

*   We will discuss anisotropy in the SGWB in the PTA frequency band
*   Maybe [Taylor, Haasteren, and Sesana. “From Bright Binaries To Bumpy Backgrounds: Mapping Realistic Gravitational Wave Skies With Pulsar-Timing Arrays”. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.102h4039T/abstract)

### Other topics which we didn’t have time to cover

*   Pulsars. Seeing as pulsars, and millisecond pulsars in particular, are at the heart of this whole endeavour, we should really have reviewed what is known about them. What are they? Where are they? How many? How do we find, observe and study them?
    *   For a review, see [Lorimer. “Binary and Millisecond Pulsars”. 2008](https://ui.adsabs.harvard.edu/abs/2008LRR....11....8L/abstract)
    *   The discovery of pulsars, [Hewish et al. “Observation of a Rapidly Pulsating Radio Source”. 1968](https://ui.adsabs.harvard.edu/abs/1968Natur.217..709H/abstract)
    *   The discovery of a pulsar in a binary, [Hulse and Taylor. “Discovery of a pulsar in a binary system.” 1975](https://ui.adsabs.harvard.edu/abs/1975ApJ...195L..51H/abstract)
*   Into the wild: fundamental physics and exotica with PTAs. For example, see [Arzoumanian et al. “Searching For Gravitational Waves From Cosmological Phase Transitions With The NANOGrav 12.5-year dataset”. 2021.](https://ui.adsabs.harvard.edu/abs/2021arXiv210413930A/abstract)