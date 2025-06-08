---
layout: archive
title: "More"
permalink: /more/
author_profile: true
---

{% include base_path %}


Here you'll find:

- **[Codes and data.](#codes-and-data)** 
Public codes and datasets supporting my publications. There’s a bit of everything here: black holes, supernovae, machine learning, laTex workflows.

- **[Notes.](#notes)**
If I don’t remember how to do something, sometimes I write it down here. Hopefully these are useful to others, some of them are probably (surely) outdated.

- **[Teaching.](#teaching)**
Materials I developed for my classes. With a huge thanks to all my students!

- **[Events](#events)**
This is a log of conferences and workshops I organized, together with the related material (like slides) when available.

- **[Others](#others)**
Yet more things on this website...

---

## Codes and data

- **[precession](https://github.com/dgerosa/precession): Dynamics of spinning black-hole binaries with python.**
Public python module to perform post-Newtornian evolution of precessing exploiting multi-timescale methods. The code is described carefully [arXiv:1605.01067](https://arxiv.org/abs/1605.01067) (v1) and [arXiv:2304.04801](https://arxiv.org/abs/2304.04801) (v2), and has by now been used in many papers by us and others.

- **[writeapaper](https://github.com/dgerosa/writeapaper): templates and github action for scientific papers.**
This is a template github repository to write scientific papers. Templates for the journals I commonly use are provided, and a github action compiles the paper at every commit and deploys it to an orphan branch. So much better (and free!) than overleaf.

- **[filltex](https://github.com/dgerosa/filltex):  Automagically fill LaTex bibliography.** 
Are you tired of copying bibtex records when writing papers? We got you covered. This is a web-scraping tool to automatically download citation records from both ADS and INSPIRE and automagically fill bib files. Usage from the terminal is straightforward, and our code is also integrated with TexShop.

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

- **[skywalker](https://github.com/dgerosa/skywalker): Things I like in Python.**
This is a python module made mostly for myself, where I collect useful functions and tricks to be imported from everywhere.

- **[gwdet](https://github.com/dgerosa/gwdet): Detectability of gravitational-wave signals from compact binary coalescences.**
Python module to compute the probability that a gravitational-signal will be detected averaging over sky location and detector antenna pattern, using a simple SNR cut. Initially develped for [arXiv:1806.08365](https://arxiv.org/abs/1806.08365) then used in many papers.

- **[QLUSTER](https://github.com/mdmould/qluster): Quick clusters of merging black holes.** Toy model for the evolution of black hole binaries in star clusters, with a specific focus on hierarchical mergers. The code is described in [arXiv:2305.04987](https://arxiv.org/abs/2305.04987). Key results were reported in [arXiv:2305.04987](https://arxiv.org/abs/2305.04987) and [arXiv:2305.04987](https://arxiv.org/abs/2305.04987).

- **[pdetclassifier](https://github.com/dgerosa/pdetclassifier): Gravitational-wave selection effects using neural-network classifiers**
Training samples and pre-trained neural networks to estimate the LIGO/Virgo detectability. Supporting
[arXiv:2007.06585](https://arxiv.org/abs/2007.06585).

- **[corecollapse](https://github.com/dgerosa/corecollapse): Numerical simulations of stellar collapse in scalar-tensor theories of gravity**
Animations and data release on core-collapse simulations in scalar-tensor theories of gravity. Supporting
[arXiv:1602.06952](https://arxiv.org/abs/1602.06952).

- **[surrkick](https://github.com/dgerosa/surrkick): Black-hole kicks from numerical-relativity surrogate models.**
Python module to extract black-hole recoils from waveform approximants by directly integrating the linear momentum flux in gravitational waves. Supporting
[arXiv:1802.04276](https://arxiv.org/abs/arXiv:1802.04276).

- **[spops](https://github.com/dgerosa/spops): *S*pinning black-hole binary *Pop*ulation *S*ynthesis.**
Database containing population synthesis simulations computed with `Startrack` and post-processed with `precession`, together with a simple python code to query it. Supporting 
[arXiv:1808.02491](https://arxiv.org/abs/1808.02491),
[arXiv:1902.00021](https://arxiv.org/abs/1902.00021),
[arXiv:1909.06373](https://arxiv.org/abs/1909.06373),
[arXiv:2005.04243](https://arxiv.org/abs/2005.04243).

- **[generalizedchip](https://github.com/dgerosa/generalizedchip): A generalized precession parameter $$\chi_{\rm p}$$ to interpret gravitational-wave data.**
Python script to compute various definitions of $$\chi_{\rm p}$$. Supporting
[arXiv:2011.11948](https://arxiv.org/abs/2011.11948). 
Now outdated, use [precession](https://github.com/dgerosa/precession).

- **[updowninjections](https://github.com/ViolaDeRenzis/updowninjections): Parameter estimation of binary black holes in the endpoint of the up-down instability.** 
Bilby posterior samples of binaries that were aligned but are now precessing. Supporting 
[arXiv:2304.13063](https://arxiv.org/abs/2304.13063),

- **[twoprecessingspins](https://github.com/ViolaDeRenzis/twoprecessingspins). Characterization of merging black holes with two precessing spins.**
Bilby posterior samples of >100 LIGO/Virgo injections with two large, misaligned spins. Supporting 
[arXiv:2207.00030](https://arxiv.org/abs/2207.00030),
[arXiv:2405.14945](https://arxiv.org/abs/2405.14945).

- **[sfts](https://github.com/rodrigo-tenorio/sfts): Scalable data-analysis framework for long-duration gravitational waves from compact binaries using short Fourier transforms** Compute faster inner products with SFTs! You're going to need it when gravitational-wave signals get too long. Supporting
[arXiv:2502.11823](https://arxiv.org/abs/2502.11823).

- **[pymcpop-gw](https://github.com/CosmoStatGW/pymcpop-gw): Sampling the full hierarchical population posterior distribution in gravitational-wave astronomy**. Successfull PyMC sampling of the full gravitational-wave poulation likelihood, withour marginalizing over the single-event parameters. Supporting
[2502.12156](https://arxiv.org/abs/2502.12156).

- **[gwlabel](https://github.com/dgerosa/gwlabel): Which is which? Identification of the two compact objects in gravitational-wave binaries.** Separate the two components in a gravitational-wave binary using spectral clustering, which is a flavor of semi-supervised machine learning. Supporting
[2409.07519](https://arxiv.org/abs/2409.07519).

- **[lisa-mbhb-cats-and-samps](https://github.com/RiccardoBuscicchio/lisa-mbhb-cats-and-samps): Stars or gas? Constraining the hardening processes of massive black-hole binaries with LISA.** Posteriors of LISA massive black-hole binaries from the `Balrog` code. Supporting
[2409.13011](https://arxiv.org/abs/2409.13011).

- **[marcumQ](https://github.com/dgerosa/marcumq): Marcum-Q function with scipy.** This is a scipy wrapper to evaluate the generalized Marcum-Q function. It turns out they are useful to compute selection effects in gravitational-wave astronomy. Supporting
[2404.16930](https://arxiv.org/abs/2404.16930).





postmerger (both papers)


https://github.com/kazewong/GPRHBA


One to many: comparing single gravitational-wave events to astrophysical populations

https://github.com/mdmould/popodds

pAGN: The one-stop solution for AGN disc modeling
Great public code to easily compute 1D models of AGN disks. Supporting arXiv:2304.13063.



WDsatellites: Milky Way Satellites Shining Bright in Gravitational Waves. LISA white dwarf posteriors. Supporting arXiv:2002.10465.

binaryBHexp: The binary black hole explorer
On-the-fly visualization of precessing binary black holes. Use ours, or do your own with our code. Supporting arXiv:1811.06552.

surfinBH: SURrogate FINal Black Hole properties for mergers of binary black holes 
Public python module to estimate post-merger masses, spins, and kicks for generic systems. Supporting arXiv:1809.09125  arXiv:2307.03435 [gr-qc].

GWpriors: Impact of bayesian priors on the characterization of binary black hole coalescences
Full posterior samples of the LIGO 01 events with different priors. Supporting arXiv:1707.04637.

https://github.com/vitale82/GWpriors

gw_catalog_mining: Mining gravitational-wave catalogs
What are we going to do with thousands of gravitational wave observations? Maybe Gaussain process emulators and hierarchical analyses. Webpage and public code supporting arXiv:1806.08365.

https://github.com/stevertaylor/gw_catalog_mining

welovespins: Asymmetries and selection biases in effective-spin measurements
Estimate your own effective-spin posterior with the recipe presented. Supporting arXiv:1805.03046.

---

## Notes


---

## Teaching


---

## Events


---

## Others
### ()