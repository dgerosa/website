---
layout: archive
title: "Codes and data"
permalink: /codes/
author_profile: true
---

{% include base_path %}

Public codes and datasets supporting my publications and other software I've contributed to. There’s a bit of everything here: black holes, machine learning, laTex workflows.

- **[precession](https://github.com/dgerosa/precession): Dynamics of spinning black-hole binaries with python.**
Public python module to perform post-Newtornian evolution of precessing exploiting multi-timescale methods. The code is described in [arXiv:1605.01067](https://arxiv.org/abs/1605.01067) (v1) and [arXiv:2304.04801](https://arxiv.org/abs/2304.04801) (v2), and has by now been used in many papers by us and others.

- **[filltex](https://github.com/dgerosa/filltex):  Automagically fill LaTex bibliography.** 
Are you tired of copying bibtex records when writing papers? We got you covered. This is a web-scraping tool to automatically download citation records from both ADS and INSPIRE and automagically fill bib files. Usage from the terminal is straightforward, and our code is also integrated with TexShop.

- **[writeapaper](https://github.com/dgerosa/writeapaper): templates and github action for scientific papers.**
This is a template github repository to write scientific papers. Templates for the journals I commonly use are provided, and a github action compiles the paper at every commit and deploys it to an orphan branch. So much better (and free!) than overleaf.

- **[spinprecession](https://github.com/dgerosa/precession): Black-hole binary inspiral: a precession-averaged approach.**
Some animations and data on black-hole binary spin precession. Supporting
[arXiv:1411.0674](https://arxiv.org/abs/1411.0674),
[arXiv:1506.03492](https://arxiv.org/abs/1506.03492),
[arXiv:1506.09116](https://arxiv.org/abs/1506.09116),
[arXiv:1711.10038](https://arxiv.org/abs/1711.10038),
[arXiv:1811.05979](https://arxiv.org/abs/1811.05979),
[arXiv:2003.02281](https://arxiv.org/abs/2003.02281),
[arXiv:2012.07147](https://arxiv.org/abs/2012.07147),
[arXiv:2405.14945](https://arxiv.org/abs/2405.14945).

- **[QLUSTER](https://github.com/mdmould/qluster): Quick clusters of merging black holes.** Toy model for the evolution of black hole binaries in star clusters, with a specific focus on hierarchical mergers. The code is described in [arXiv:2305.04987](https://arxiv.org/abs/2305.04987). Key results were reported in [arXiv:2305.04987](https://arxiv.org/abs/2305.04987) and [arXiv:2305.04987](https://arxiv.org/abs/2305.04987).

- **[expandLHS](https://github.com/m-boschini/expandLHS): “LHS in LHS”: a new expansion strategy for Latin hypercube sampling in simulation design.** Algorithm and implementation to expand and existing Latin Hypercube sampling while keeping its space-filling properties. Supporting [arXiv:2509.00159](https://arxiv.org/abs/2509.00159).

- **[pAGN](https://github.com/DariaGangardt/pAGN): The one-stop solution for AGN disc modeling.** Great public code to easily compute 1D models of AGN disks. Supporting [arXiv:2304.13063](https://arxiv.org/abs/2304.13063).

- **[surfinBH](https://github.com/vijayvarma392/surfinBH): *sur*rogate *fin*al *B*lack *H*ole properties for mergers of binary black holes.** Public python module to estimate post-merger masses, spins, and kicks for generic systems. Supporting
[arXiv:1809.09125](https://arxiv.org/abs/1809.09125),
[arXiv:1809.09125](https://arxiv.org/abs/1809.09125).

- **[postmerger](https://github.com/cpacilio/postmerger): Ringdown amplitude fits.** Surrogate models for the ringdown amplitudes, fitted to numerical-relativity simulations. Supporting
[arXiv:2408.05276 ](https://arxiv.org/abs/2408.05276 ),
[arXiv:2504.17021](https://arxiv.org/abs/2504.17021).

- **[skywalker](https://github.com/dgerosa/skywalker): Things I like in Python.**
This is a python module made mostly for myself, where I collect useful functions and tricks to be imported from everywhere.

- **[gwdet](https://github.com/dgerosa/gwdet): Detectability of gravitational-wave signals from compact binary coalescences.**
Python module to compute the probability that a gravitational-signal will be detected averaging over sky location and detector antenna pattern, using a simple SNR cut. Initially develped for [arXiv:1806.08365](https://arxiv.org/abs/1806.08365) then used in many papers.

- **[pdetclassifier](https://github.com/dgerosa/pdetclassifier): Gravitational-wave selection effects using neural-network classifiers**
Training samples and pre-trained neural networks to estimate the LIGO/Virgo detectability. Supporting
[arXiv:2007.06585](https://arxiv.org/abs/2007.06585).

- **[surrkick](https://github.com/dgerosa/surrkick): Black-hole kicks from numerical-relativity surrogate models.**
Python module to extract black-hole recoils from waveform approximants by directly integrating the linear momentum flux in gravitational waves. Supporting
[arXiv:1802.04276](https://arxiv.org/abs/arXiv:1802.04276).

- **[sfts](https://github.com/rodrigo-tenorio/sfts): Scalable data-analysis framework for long-duration gravitational waves from compact binaries using short Fourier transforms** Compute faster inner products with SFTs! You're going to need it when gravitational-wave signals get too long. Supporting
[arXiv:2502.11823](https://arxiv.org/abs/2502.11823).

- **[pymcpop-gw](https://github.com/CosmoStatGW/pymcpop-gw): Sampling the full hierarchical population posterior distribution in gravitational-wave astronomy**. Successfull PyMC sampling of the full gravitational-wave poulation likelihood, withour marginalizing over the single-event parameters. Supporting
[2502.12156](https://arxiv.org/abs/2502.12156).

- **[gwlabel](https://github.com/dgerosa/gwlabel): Which is which? Identification of the two compact objects in gravitational-wave binaries.** Separate the two components in a gravitational-wave binary using spectral clustering, which is a flavor of semi-supervised machine learning. Supporting
[2409.07519](https://arxiv.org/abs/2409.07519).

- **[marcumQ](https://github.com/dgerosa/marcumq): Marcum-Q function with scipy.** This is a scipy wrapper to evaluate the generalized Marcum-Q function. It turns out they are useful to compute selection effects in gravitational-wave astronomy. Supporting
[2404.16930](https://arxiv.org/abs/2404.16930).

- **[popodds](https://github.com/mdmould/popodds): One to many: comparing single gravitational-wave events to astrophysical populations.** The right way to compare many simulated gravitational wave sources against a single gravitational-wave event. Don't overplot, compute detection-weighted Bayes factors. Supporting
[2305.18539](https://arxiv.org/abs/2305.18539)

- **[gw_catalog_mining](https://github.com/stevertaylor/gw_catalog_mining)**: Mining gravitational-wave catalogs to understand binary stellar evolution: a new hierarchical bayesian framework** What are we going to do with thousands of gravitational wave observations? Maybe Gaussain process emulators and hierarchical analyses. Supporting: [1806.08365](https://arxiv.org/abs/1806.08365).

- **[GPRHBA](https://github.com/kazewong/GPRHBA): Machine-learning interpolation of population-synthesis simulations to interpret gravitational-wave observations: a case study.** An early sampler for the gravitational population likelihood, using interpolation of some population-synthesis simulations as the targeted model. Supporting
[1909.06373](https://arxiv.org/abs/1909.06373). 

- **[spops](https://github.com/dgerosa/spops): *S*pinning black-hole binary *Pop*ulation *S*ynthesis.**
Database containing population synthesis simulations computed with `Startrack` and post-processed with `precession`, together with a simple python code to query it. Supporting 
[arXiv:1808.02491](https://arxiv.org/abs/1808.02491),
[arXiv:1902.00021](https://arxiv.org/abs/1902.00021),
[arXiv:1909.06373](https://arxiv.org/abs/1909.06373),
[arXiv:2005.04243](https://arxiv.org/abs/2005.04243).

- **[binaryBHexp](https://github.com/vijayvarma392/binaryBHexp): The binary black hole explorer.**
On-the-fly visualization of precessing binary black holes. Use ours, or do your own with our code. Supporting
[1811.06552](https://arxiv.org/abs/1811.06552).

- **[updowninjections](https://github.com/ViolaDeRenzis/updowninjections): Parameter estimation of binary black holes in the endpoint of the up-down instability.** 
Bilby posterior samples of binaries that were aligned but are now precessing. Supporting 
[arXiv:2304.13063](https://arxiv.org/abs/2304.13063),

- **[twoprecessingspins](https://github.com/ViolaDeRenzis/twoprecessingspins). Characterization of merging black holes with two precessing spins.**
Bilby posterior samples of >100 LIGO/Virgo injections with two large, misaligned spins. Supporting 
[arXiv:2207.00030](https://arxiv.org/abs/2207.00030),
[arXiv:2405.14945](https://arxiv.org/abs/2405.14945).

- **[lisa-mbhb-cats-and-samps](https://github.com/RiccardoBuscicchio/lisa-mbhb-cats-and-samps): Stars or gas? Constraining the hardening processes of massive black-hole binaries with LISA.** Posteriors of LISA massive black-hole binaries from the `Balrog` code. Supporting
[2409.13011](https://arxiv.org/abs/2409.13011).

- **[WDsatellites](https://zenodo.org/records/3668905): Milky Way Satellites Shining Bright in Gravitational Waves.** LISA white dwarf posteriors from satellites of the Milky Way. Supporting
[2002.10465](https://arxiv.org/abs/2002.10465).

- **[generalizedchip](https://github.com/dgerosa/generalizedchip): A generalized precession parameter $$\chi_{\rm p}$$ to interpret gravitational-wave data.**
Python script to compute various definitions of $$\chi_{\rm p}$$. Supporting
[arXiv:2011.11948](https://arxiv.org/abs/2011.11948). 
Now outdated, use [precession](https://github.com/dgerosa/precession).

- **[GWpriors](https://github.com/vitale82/GWpriors): Impact of bayesian priors on the characterization of binary black hole coalescences**
Posterior samples of the LIGO 01 events with different priors. Supporting
[1707.04637](https://arxiv.org/abs/1707.04637), [1712.06635](https://arxiv.org/abs/1712.06635)

- **[corecollapse](https://github.com/dgerosa/corecollapse): Numerical simulations of stellar collapse in scalar-tensor theories of gravity**
Animations and data release on core-collapse simulations in scalar-tensor theories of gravity. Supporting
[arXiv:1602.06952](https://arxiv.org/abs/1602.06952).

- **[welovespins](https://web.archive.org/web/20240913222959/http://superstring.mit.edu/welcome.html): Gravitational-wave astrophysics with effective-spin measurements: asymmetries and selection biases**
Estimate your own effective-spin posterior with the recipe presented. Supporting [1805.03046](https://arxiv.org/abs/1805.03046).

