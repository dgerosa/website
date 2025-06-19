---
title: "Efficient multi-timescale dynamics of precessing black-hole binaries"
date: 2023-04-12
permalink: /posts/2023-04-12-efficient-multi-timescale-dynamics-of-precessing-black-hole-binaries
tags:
  - Milano
  - Papers
  - PRD
---

It’s out! The notorious (ask my students…) “ _precession v2_ ” paper is finally out! This took a veeeery long time; we checked and the first commit for this paper is from May 2020 (!). But the result is an exhilarating tour of spin precession at 2PN with 27 pages and 183 (!!!) numbered equations. We rewrote the entire formalism, change how we parametrize things, compute all we could in closed forms, and speed up the computational implementation. It’s cool, now performing a precession-averaged evolution is a <0.1s operation. If you’re into BH binary spin precession, this is the paper for you. All of this is now part v2 of our [PRECESSION](https://github.com/dgerosa/precession) python module. So long, and thanks for all the spin.

**D. Gerosa**, G. Fumagalli, M. Mould, G. Cavallotto, D. Padilla Monroy, D. Gangardt, V. De Renzis.\
[Physical Review D 108 (2023) 024042](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.024042). [arXiv:2304.04801 [gr-qc]](https://arxiv.org/abs/2304.04801).\
Open source code.