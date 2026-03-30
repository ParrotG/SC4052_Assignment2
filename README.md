# SC4052 Assignment 2

This project is a code implementation for SC4052 Cloud Computing Tutorial 3 Question 6(i). It demonstrates how PageRank can be used as the core signal in a crawler strategy, and how additional page-level metadata can improve the selection of high-quality pages to crawl first.

## Design Purpose

The goal of this project is to show a simple crawl-priority pipeline:

- Model a small directed web graph with URLs and PageMetadata.
- Compute PageRank scores from the link structure.
- Extract the top-k URLs based on authority.
- Extend the ranking with heuristic signals from page metadata to prioritize higher-value pages for crawling.

This keeps PageRank as the main authority signal while also considering practical crawler concerns such as crawl permissions, page quality, trust, and freshness.

## Included Functionality

The demo contains the following components:

- A manually constructed sample directed web graph in `build_sample_web_graph()`.
- A `PageMetadata` data model for describing crawl-related quality signals.
- PageRank score computation using `networkx.pagerank`.
- Top-k URL extraction based only on PageRank authority.
- A heuristic-enhanced crawl policy that combines PageRank with metadata such as:
  - crawl permission
  - content length
  - login-page penalties
  - query-parameter penalties
  - trusted-domain bonuses
  - freshness bonuses
- Console output for both pure PageRank ranking and heuristic-enhanced ranking.
- Graph visualization with the selected top-k nodes highlighted for each ranking strategy.

## Installation

It is recommended to use `uv`, although plain `pip` also works.

Install the required dependencies with one of the following options:

```bash
uv pip install -e .
```

or

```bash
pip install -e .
```

If you prefer installing packages directly instead of editable mode, you may also run:

```bash
uv pip install matplotlib networkx numpy scipy
```

or

```bash
pip install matplotlib networkx numpy scipy
```

## How to Run

Run the demo from the project root with:

```bash
python -m crawl_strategy_demo
```

You may also override the number of selected URLs with the optional `k` argument:

```bash
python -m crawl_strategy_demo --top-k 3
```

The program will:

- build the sample web graph,
- compute PageRank scores,
- print the top-k URLs by PageRank,
- compute heuristic-enhanced crawl scores,
- print the top-k URLs selected by the heuristic strategy,
- generate graph images with highlighted selected nodes for both ranking methods.

The generated image files are saved to:

- `outputs/pagerank_topk_graph.png`
- `outputs/heuristic_topk_graph.png`

## Customizing the Graph

If you want to test a different web structure, you can edit `build_sample_web_graph()` in `crawl_strategy_demo.py`.

You may customize:

- the directed link structure in `graph_definition`,
- the page metadata values in `metadata`.

This is optional, but it is useful if you want to experiment with how different link patterns and metadata signals affect PageRank and crawl priority.
