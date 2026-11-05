---
title: "Latin hypercube sampling to reduce the variance in Monte Carlo integration: a practical guide and an application to gravitational-wave astronomy"
date: 2026-11-05
permalink: /posts/2026-11-05-latin-hypercube-sampling-to-reduce-the-variance-in-monte-carlo-integration-a-practical-guide-and-an-application-to-gravitational-wave-astronomy
tags:
  - Papers
  - Milano
---

We're [back to](https://davidegerosa.com/posts/2025-09-03-lhs-in-lhs-a-new-expansion-strategy-for-latin-hypercube-sampling-in-simulation-design) Latin hypercubes! That's an amazing mathematical construction to fill the space evenly with points (which might sound trivial, it's really not!). One of the things Latin hypercubes are good at is making integrals more accurate. That is, the variance of an integral estimated with random samples can be brought down by drawing these samples on a Latin hypercube. This paper provides a gentle (hopefully) introduction to this idea, using both "vanilla" Latin hypercubes and more complex ones based on something called orthogonal arrays. There's also an application to selection effects in gravitational-wave astronomy, which turns out to be a hard problem even for Latin hypercubes. 


M. Boschini, **D. Gerosa**.\
[arXiv:2611.04045 [astro-ph.IM]](https://arxiv.org/abs/2611.04045).