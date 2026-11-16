---
title: "Gravitational-wave hierarchical inference from population samples"
date: 2026-11-16
permalink: /posts/2026-11-16-gravitational-wave-hierarchical-inference-from-population-samples
tags:
  - Papers
  - Milano
---

When doing gravitational-wave population fits (the notorious Bayesian hierarchical analyses), one typically relies on models that can be evaluated. That means I have the PDF of the model. This seems fair—what's wrong with that? But in practice, it prevents a lot of applications. My stellar physics friends who run state-of-the-art simulations don't really have a PDF, but rather a numerical generative model. In practice, they can give me a table of simulated sources; that is, they have "samples" from a PDF, but the PDF itself is not easily evaluable. Great work by Federico here, who in this paper has rewritten the GW population problem in a way that can make use of these samples, rather than PDF evaluations. This opens the door to so many applications!


F. De Santi, **D. Gerosa**, M. Mould.\
[arXiv:2611.17428 [[astro-ph.HE]]](https://arxiv.org/abs/2611.17428).