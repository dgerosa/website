---
title: "“LHS in LHS”: a new expansion strategy for Latin hypercube sampling in simulation design"
date: 2025-09-03
permalink: /posts/2025-09-03-lhs-in-lhs-a-new-expansion-strategy-for-latin-hypercube-sampling-in-simulation-design
tags:
  - Papers
  - Milano
  - SoftwareX
---

Happy to share this super fun paper. The nice story here is that we had two BSc students working on this, Alessandro Crespi who was majoring in computer science but wanted to to physics, and Matteo Falcone who was majoring in physics but wanted to do computer science (and the whole thing was then wrapped up by Phd student Matteo Boschini). Anyway, I somehow got interested in the development of Latin Hypercube sampling, which is a smart way to distribute points in a given parameter space, in a way that is "maximally filling" (where this notion is appropriately defined). Steve Taylor and I used it [in this paper](https://arxiv.org/abs/1806.08365) some years ago, and one of the limitations we faced was that one had to specify the number of points beforehand. What if you want to add additional samples? Say because you found out you have the computational resources to run a few more simulations, or because you want to improve your model. This paper is a new "nested" strategy to add points to an existing Latin Hypercube such that the space filling properties are approximately preserved. Our implementation is at [github.com/m-boschini/expandLHS](https://github.com/m-boschini/expandLHS).


M. Boschini, **D. Gerosa**, A. Crespi, M. Falcone.\
[SoftwareX 31 (2025) 102294](https://authors.elsevier.com/sd/article/S2352-7110(25)00260-2). [arXiv:2509.00159 [stat.ME]](https://arxiv.org/abs/2509.00159).\
Open source code.