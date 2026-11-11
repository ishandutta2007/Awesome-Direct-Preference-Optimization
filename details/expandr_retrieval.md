# Dense Retrieval with ExpandR

## Detailed Description

ExpandR uses an LLM to generate query expansions and jointly optimizes it with a dense retriever. The LLM is trained with Direct Preference Optimization using feedback that combines retrieval effectiveness and generation consistency.

## Workflow / Architecture

```mermaid
flowchart LR
    Query --> LLM[LLM query expander] --> Expansion[Query expansion] --> Retriever[Dense retriever]
    Retriever --> Feedback[Ranking-aware preference feedback] --> DPO[LLM DPO update]
```

## Sources

- [Official paper](https://aclanthology.org/2025.emnlp-main.963/)
- [Author code](https://github.com/NEUIR/ExpandR)

[Back to README](../README.md)
