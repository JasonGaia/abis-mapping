"""Provides Mapper Base Class for the Package"""


# Standard
import abc

# Third-Party
import rdflib

# Local
from . import types

# Typing
from typing import Optional, final


class ABISMapper(abc.ABC):
    """ABIS Mapper Base Class"""

    # ABIS Mapper Registry
    registry: dict[str, type["ABISMapper"]] = {}

    @abc.abstractmethod
    def apply_mapping(
        self,
        data: types.CSVType,
        ) -> rdflib.Graph:
        """Applies mapping from csv to ABIS conformant rdf

        Args:
            data (CSVType): Pandas readable CSV type.

        Returns:
            rdflib.Graph: ABIS conformant rdf graph
        """

    @final
    @classmethod
    def register_mapper(
        cls,
        mapper: type["ABISMapper"],
        template_id: str,
        ) -> None:
        """Registers a concrete ABIS Mapper with the Base Class

        Args:
            mapper (type[ABISMapper]): Mapper to be registered.
            template_id (str): Template ID to associate with the mapper.
        """
        # Register the mapper
        cls.registry[template_id] = mapper


def get_mapper(template_id: str) -> Optional[type[ABISMapper]]:
    """Retrieves ABIS Mapper class for the specified template ID.

    Args:
        template_id (str): Template ID to retrieve the mapper for.

    Returns:
        Optional[type[ABISMapper]]: ABIS mapper class associated with the
            specified template ID if found, otherwise `None`.
    """
    # Retrieve and return the mapper
    return ABISMapper.registry.get(template_id)


def get_mappers() -> dict[str, type[ABISMapper]]:
    """Retrieves the full registry of ABIS Mappers.

    Returns:
        dict[str, type[ABISMapper]]: Dictionary of template ID to ABIS Mapper.
    """
    # Retrieve and return the mappers
    return ABISMapper.registry