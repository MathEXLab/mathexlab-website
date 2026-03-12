---
title: "Publications"
layout: "publications"
description: "Publications from MathEXLab."
menu:
  main:
    weight: 4

sections:

  - id: "selected"
    title: "Featured Publications"

    projects:

      - id: " condensnet"
        title: "CondensNet: enabling stable long-term climate simulations via hybrid deep learning models with adaptive physical constraints"
        featured: true
        poster: "/images/projects/condensnet.png"
        summary: "Deep learning is increasingly being used to emulate cloud and convection processes in climate models, offering a faster alternative to computationally intensive cloud-resolving simulations. However, because these processes unfold at kilometre scales or smaller — far below the resolution of global climate models — hybrid AI–physics approaches often become unstable when run over long time horizons. Researchers from the National University of Singapore (NUS)’s College of Design and Engineering (CDE), in collaboration with Tsinghua University, NVIDIA and the Centre for Climate Research Singapore, have traced a key instability to a moisture imbalance during condensation. They developed CondensNet, an adaptive, physics-constrained neural-network that can correct physically inconsistent behaviour. Integrated into a global climate model, it enables stable, accurate long-term simulations while running far faster than cloud-resolving approaches."
        link: "https://www.nature.com/articles/s41612-025-01269-5"

      - id: "omnisapiens"
        title: "OmniSapiens: A Foundation Model for Social Behavior Processing via Heterogeneity-Aware Relative Policy Optimization"
        featured: true
        poster: "/images/projects/omnisapiens.png"
        summary: "Building a first-of-its kind multimodal foundation model for understanding and recognising human behaviors via reasoning RL methods. 🤖 A longstanding goal of artificial intelligence has been to build systems that can genuinely understand human behavior, interpreting emotions, intentions, and social signals in a grounded and context-aware manner. This vision of socially intelligent AI is central to applications ranging from human-AI collaboration to healthcare and finance. ⚠️ Yet, it is often difficult for AI models to learn diverse social intelligence capabilities, given the intrinsic complexity and ambiguity of human social cues. State-of-the art learning algorithms (including DeepSeek’s GRPO) are primarily optimized for standard benchmarks (i.e. coding/ math) often overlooking unique challenges to learning optimization in social settings, such as heterogeneous reward signals.🚀 Building on our ICLR 2026 work (Human Behavior Atlas), we develop a new core reasoning-reinforcement learning algorithm, Heterogeneity-Aware Relative Policy Optimization (HARPO), designed to enable balanced optimization across diverse social intelligence tasks. Leveraging HARPO, we develop OmniSapiens 2.0, a second iteration of a unified foundation model for social intelligence. We intend to make the model publicly available to support future AI research!"
        link: "https://lnkd.in/gjXTHKv6"

      - id: "tlr"
        title: "Time-lagged recurrence: A data-driven method to estimate the predictability of dynamical systems"
        featured: true
        poster: "/images/projects/tlr.png"
        summary: "This work contributes to better understand the state-dependent predictability of complex dynamicalsystems across different disciplines, including physics and  engineering. This is an inderdisplinary project between MathExLab PhD student Chenyu Dong and collaborators: Davide Faranda (CNRS), Adriano Gualandi (University of Cambridge), and Valerio Lucarini (University of Leicester)!"
        link: "https://www.pnas.org/doi/10.1073/pnas.2420252122"

---
## Full publication list
{{< scholar-feed user="all_publications" limit="20" sort="year_desc" title="All Publications" >}}