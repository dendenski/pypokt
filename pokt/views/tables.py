from typing import Union, List, Tuple

from tabulate import tabulate

from .interfaces import SupportedChain
from .utils import chain_ids_to_details


def _supported_chains_to_table_data(
    supported_chains: List[SupportedChain],
) -> List[Tuple[str, str, str, str]]:
    return [
        (
            chain.name,
            chain.portal_prefix,
            chain.chainID,
            "Y" if chain.revenue_generating else "-",
        )
        for chain in supported_chains
    ]


def make_supported_chains_table(
    supported_chains: Union[List[str], List[SupportedChain]], tablefmt="github"
) -> str:
    if not supported_chains:
        return ""
    if isinstance(supported_chains[0], str):
        supported_chains = chain_ids_to_details(supported_chains)
    table = _supported_chains_to_table_data(supported_chains)
    headers = ("Name", "Portal API Prefix", "RelayChainID", "Generates Revenue")
    return tabulate(table, headers, tablefmt=tablefmt)
