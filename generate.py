import os
import re

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Direct-Preference-Optimization"
details_dir = os.path.join(base_dir, "details")
if not os.path.exists(details_dir):
    os.makedirs(details_dir)

files = [
    ("actor_critic_rlhf.md", "The Actor-Critic RLHF Era (PPO Baseline, ~2019–2023)"),
    ("dpo_breakthrough.md", "The Direct Mathematical Parameterization Breakthrough (DPO, 2023)"),
    ("reference_free_online.md", "The Reference-Free & Iterative Online Era (~2024–Present)"),
    ("standard_dpo.md", "A. Standard DPO (Bradley-Terry Formulation)"),
    ("ipo.md", "B. Identity Preference Optimization (IPO)"),
    ("kto.md", "C. Kahneman-Tversky Optimization (KTO)"),
    ("orpo.md", "D. Odds Ratio Preference Optimization (ORPO)"),
    ("offline_dpo.md", "Offline DPO (The Static Framework)"),
    ("online_dpo.md", "Online / Iterative DPO"),
    ("rejection_sampling_dpo.md", "Rejection-Sampling DPO"),
    ("likelihood_saturation.md", "The Likelihood Saturation and Capability Collapse Wall"),
    ("reference_model_memory.md", "The Reference Model Memory-Overhead Barrier"),
    ("conversational_persona.md", "Conversational Persona and Formatting Alignment for LLMs"),
    ("safety_guardrail.md", "Safety Guardrail Hardening and Red-Teaming Defense"),
    ("multi_step_reasoning.md", "Multi-Step Reasoning Refinement & Distillation"),
]

for filename, title in files:
    content = f"""# {title}

This page provides detailed information about **{title}**.

## Overview
{title} is a critical component in the evolution of Direct Preference Optimization and Large Language Model alignment.

## Diagram
```mermaid
graph TD;
    A[Start: {title.split()[0]}] --> B[Processing];
    B --> C[Optimization];
    C --> D[Result];
```

[Back to main README](../README.md)
"""
    with open(os.path.join(details_dir, filename), "w") as f:
        f.write(content)

readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

for filename, title in files:
    # First make sure we don't double replace if we run multiple times
    link = f"[{title}](details/{filename})"
    readme = readme.replace(f"**{title}**", f"**{link}**")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)
