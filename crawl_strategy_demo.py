from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Iterable, Tuple
from urllib.parse import urlparse
import networkx as nx


@dataclass(frozen=True)
class PageMetadata:
    """Metadata used by the heuristic-enhanced crawler policy."""
    allows_crawling: bool
    content_length: int
    is_login_page: bool
    has_many_query_params: bool
    is_trusted_domain: bool
    freshness_days: int


def build_sample_web_graph() -> Tuple[nx.DiGraph, Dict[str, PageMetadata]]:
    """
    Build a small directed web graph with human-readable URLs.

    Returns:
        A tuple containing:
        1) A directed graph whose nodes are URLs.
        2) A metadata dictionary for heuristic-enhanced ranking.
    """
    graph_definition: Dict[str, List[str]] = {
        "https://research.example.edu/": [
            "https://research.example.edu/papers/ai-survey",
            "https://research.example.edu/labs/ml",
            "https://open-data.example.org/datasets/health-ai",
            "https://news.example.com/ai-breakthrough",
        ],
        "https://research.example.edu/papers/ai-survey": [
            "https://research.example.edu/labs/ml",
            "https://open-data.example.org/datasets/health-ai",
            "https://journal.example.org/article/rag-overview",
        ],
        "https://research.example.edu/labs/ml": [
            "https://research.example.edu/papers/ai-survey",
            "https://open-data.example.org/datasets/health-ai",
            "https://journal.example.org/article/rag-overview",
        ],
        "https://open-data.example.org/": [
            "https://open-data.example.org/datasets/health-ai",
            "https://open-data.example.org/datasets/climate",
            "https://journal.example.org/article/rag-overview",
        ],
        "https://open-data.example.org/datasets/health-ai": [
            "https://research.example.edu/papers/ai-survey",
            "https://journal.example.org/article/rag-overview",
        ],
        "https://open-data.example.org/datasets/climate": [
            "https://journal.example.org/article/rag-overview",
        ],
        "https://journal.example.org/": [
            "https://journal.example.org/article/rag-overview",
            "https://journal.example.org/article/medical-imaging",
        ],
        "https://journal.example.org/article/rag-overview": [
            "https://research.example.edu/papers/ai-survey",
            "https://journal.example.org/article/medical-imaging",
        ],
        "https://journal.example.org/article/medical-imaging": [
            "https://research.example.edu/papers/ai-survey",
        ],
        "https://news.example.com/": [
            "https://news.example.com/ai-breakthrough",
            "https://news.example.com/ai-opinion",
        ],
        "https://news.example.com/ai-breakthrough": [
            "https://research.example.edu/papers/ai-survey",
            "https://open-data.example.org/datasets/health-ai",
        ],
        "https://news.example.com/ai-opinion": [
            "https://news.example.com/ai-breakthrough",
        ],
        "https://spam.example.net/": [
            "https://spam.example.net/free-traffic",
            "https://spam.example.net/login",
        ],
        "https://spam.example.net/free-traffic": [
            "https://spam.example.net/login",
            "https://news.example.com/ai-opinion",
        ],
        "https://spam.example.net/login": [
            "https://spam.example.net/free-traffic",
        ],
        "https://portal.example.com/search?q=ai": [
            "https://news.example.com/ai-breakthrough",
            "https://research.example.edu/",
        ],
        "https://accounts.example.com/login": [
            "https://research.example.edu/",
        ],
    }

    metadata: Dict[str, PageMetadata] = {
        "https://research.example.edu/": PageMetadata(
            allows_crawling=True,
            content_length=3000,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=5,
        ),
        "https://research.example.edu/papers/ai-survey": PageMetadata(
            allows_crawling=True,
            content_length=8500,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=10,
        ),
        "https://research.example.edu/labs/ml": PageMetadata(
            allows_crawling=True,
            content_length=2500,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=20,
        ),
        "https://open-data.example.org/": PageMetadata(
            allows_crawling=True,
            content_length=2200,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=8,
        ),
        "https://open-data.example.org/datasets/health-ai": PageMetadata(
            allows_crawling=True,
            content_length=6200,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=3,
        ),
        "https://open-data.example.org/datasets/climate": PageMetadata(
            allows_crawling=True,
            content_length=5000,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=30,
        ),
        "https://journal.example.org/": PageMetadata(
            allows_crawling=True,
            content_length=2000,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=15,
        ),
        "https://journal.example.org/article/rag-overview": PageMetadata(
            allows_crawling=True,
            content_length=9000,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=7,
        ),
        "https://journal.example.org/article/medical-imaging": PageMetadata(
            allows_crawling=True,
            content_length=7600,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=True,
            freshness_days=40,
        ),
        "https://news.example.com/": PageMetadata(
            allows_crawling=True,
            content_length=1800,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=2,
        ),
        "https://news.example.com/ai-breakthrough": PageMetadata(
            allows_crawling=True,
            content_length=3500,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=1,
        ),
        "https://news.example.com/ai-opinion": PageMetadata(
            allows_crawling=True,
            content_length=1600,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=4,
        ),
        "https://spam.example.net/": PageMetadata(
            allows_crawling=True,
            content_length=500,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=100,
        ),
        "https://spam.example.net/free-traffic": PageMetadata(
            allows_crawling=True,
            content_length=350,
            is_login_page=False,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=120,
        ),
        "https://spam.example.net/login": PageMetadata(
            allows_crawling=False,
            content_length=200,
            is_login_page=True,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=5,
        ),
        "https://portal.example.com/search?q=ai": PageMetadata(
            allows_crawling=False,
            content_length=900,
            is_login_page=False,
            has_many_query_params=True,
            is_trusted_domain=False,
            freshness_days=1,
        ),
        "https://accounts.example.com/login": PageMetadata(
            allows_crawling=False,
            content_length=300,
            is_login_page=True,
            has_many_query_params=False,
            is_trusted_domain=False,
            freshness_days=2,
        ),
    }

    graph = nx.DiGraph()

    for source_url, target_urls in graph_definition.items():
        graph.add_node(source_url)
        for target_url in target_urls:
            graph.add_edge(source_url, target_url)

    for url in metadata:
        if url not in graph:
            graph.add_node(url)

    return graph, metadata


def compute_pagerank_scores(graph: nx.DiGraph, alpha: float = 0.85) -> Dict[str, float]:
    """
    Compute PageRank scores using NetworkX.

    Args:
        graph: The directed web graph.
        alpha: The damping factor used by PageRank.

    Returns:
        A dictionary mapping URL to PageRank score.
    """
    return nx.pagerank(graph, alpha=alpha)


def get_top_k_by_authority(
    pagerank_scores: Dict[str, float],
    k: int,
) -> List[Tuple[str, float]]:
    """
    Return the top-k URLs ranked only by authority (PageRank).

    Args:
        pagerank_scores: Precomputed PageRank scores.
        k: Number of URLs to return.

    Returns:
        A list of (URL, score) tuples.
    """
    ranked = sorted(
        pagerank_scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )
    return ranked[:k]


def normalize_content_length(content_length: int) -> float:
    """
    Convert content length into a bounded quality signal.

    The value is clipped to [0.0, 1.0].
    """
    return min(content_length / 8000.0, 1.0)


def freshness_bonus(freshness_days: int) -> float:
    """
    Convert freshness into a bounded bonus.

    Newer pages receive a larger bonus.
    """
    if freshness_days <= 3:
        return 1.0
    if freshness_days <= 14:
        return 0.8
    if freshness_days <= 30:
        return 0.5
    if freshness_days <= 90:
        return 0.2
    return 0.0


def compute_heuristic_score(
    url: str,
    pagerank_score: float,
    metadata: PageMetadata,
) -> float:
    """
    Compute a heuristic-enhanced crawl priority score.

    Strategy:
    - Disallow crawling if the page is blocked.
    - Penalize login pages and parameter-heavy search pages.
    - Reward trusted domains, richer content, and freshness.
    - Keep PageRank as the central authority signal.

    Args:
        url: The page URL.
        pagerank_score: The PageRank authority score.
        metadata: The metadata for the page.

    Returns:
        A float crawl priority score.
    """
    if not metadata.allows_crawling:
        return -1.0

    score = pagerank_score

    if metadata.is_trusted_domain:
        score += 0.020

    score += 0.015 * normalize_content_length(metadata.content_length)
    score += 0.010 * freshness_bonus(metadata.freshness_days)

    if metadata.is_login_page:
        score -= 0.050

    if metadata.has_many_query_params:
        score -= 0.030

    parsed = urlparse(url)
    path_lower = parsed.path.lower()

    low_value_keywords = ("login", "signin", "signup", "account", "search", "tag", "filter")
    if any(keyword in path_lower for keyword in low_value_keywords):
        score -= 0.030

    return score


def get_top_k_with_heuristics(
    pagerank_scores: Dict[str, float],
    metadata_map: Dict[str, PageMetadata],
    k: int,
) -> List[Tuple[str, float, float]]:
    """
    Return the top-k URLs using PageRank plus heuristic signals.

    Args:
        pagerank_scores: Precomputed PageRank scores.
        metadata_map: Metadata used by the heuristic policy.
        k: Number of URLs to return.

    Returns:
        A list of tuples:
        (URL, heuristic_score, pagerank_score)
    """
    scored_urls: List[Tuple[str, float, float]] = []

    for url, pr_score in pagerank_scores.items():
        metadata = metadata_map[url]
        heuristic_score = compute_heuristic_score(url, pr_score, metadata)
        scored_urls.append((url, heuristic_score, pr_score))

    ranked = sorted(
        scored_urls,
        key=lambda item: item[1],
        reverse=True,
    )
    return ranked[:k]


def print_ranked_results(
    title: str,
    results: Iterable[Tuple],
) -> None:
    """Print ranked results in a readable format."""
    print(f"\n{title}")
    print("-" * len(title))
    for index, row in enumerate(results, start=1):
        print(f"{index}. {row}")


def main() -> None:
    """Run the full demo."""
    graph, metadata = build_sample_web_graph()

    print(f"Number of nodes: {graph.number_of_nodes()}")
    print(f"Number of edges: {graph.number_of_edges()}")

    pagerank_scores = compute_pagerank_scores(graph, alpha=0.85)

    top_k = 5

    top_by_authority = get_top_k_by_authority(pagerank_scores, top_k)
    print_ranked_results("Top-k URLs by PageRank authority", top_by_authority)

    top_by_heuristics = get_top_k_with_heuristics(pagerank_scores, metadata, top_k)
    print_ranked_results("Top-k URLs by heuristic-enhanced policy", top_by_heuristics)

    print("\nMetadata snapshot for top heuristic-ranked URLs")
    print("----------------------------------------------")
    for url, heuristic_score, pr_score in top_by_heuristics:
        print(
            {
                "url": url,
                "heuristic_score": round(heuristic_score, 6),
                "pagerank_score": round(pr_score, 6),
                "metadata": metadata[url],
            }
        )


if __name__ == "__main__":
    main()