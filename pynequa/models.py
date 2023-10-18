from typing import Dict, List, Optional
from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from loguru import logger


class AbstractParams(ABC):
    """
    Abstract base class for all Sinequa models.
    """

    @abstractmethod
    def generate_payload(self, **kwargs) -> Dict:
        """
        This is abstract method for AbstractParams.
        Every child class should implement this method.
        """
        raise NotImplementedError()


@dataclass
class TreeParams(AbstractParams):
    """
    Represents the parameters for configuring a tree parameters.

    Attributes:
        box (str): The name of the relevant tree navigation box (required).
        column (str): The name of the index column associated with the
                        navigation box (required).
        op (str, optional): The relational operator. Default is 'eq'.
            Possible values: '=', '!=', '<', '<=', '>=', '>', 'between', 'not between'.
        value (str): The filter value (required).
    """
    box: str = ""
    column: str = ""
    op: str = ""
    value: str = ""

    def generate_payload(self, **kwargs) -> Dict:
        """
        This method generates payload for
        TreeParams.
        """
        return {
            "box": self.box,
            "column": self.column,
            "op": self.op,
            "value": self.value,
        }


@dataclass
class SelectParams(AbstractParams):
    expression: str = ""
    facet: str = ""

    def generate_payload(self, **kwargs) -> Dict:
        """
        This method generates payload for
        SelectParams.
        """
        return {
            "expression": self.expression,
            "facet": self.facet,
        }


@dataclass
class OpenParams(AbstractParams):
    expression: str = ""
    facet: str = ""

    def generate_payload(self, **kwargs) -> Dict:
        """
        This method generates payload for
        OpenParams.
        """
        return {
            "expression": self.expression,
            "facet": self.facet,
        }


@dataclass
class AdvancedParams(AbstractParams):
    col_name: str = ""
    col_value: str = None
    value:  str or int = None
    operator: str = None
    debug: bool = False

    def generate_payload(self, **kwargs) -> Dict:
        """
        This method generates payload for
        AdvancedParams.
        """
        payload = {
            self.col_name: self.col_value,
            "value": self.value,
            "operator": self.operator
        }

        if self.debug:
            logger.debug(payload)

        return payload


@dataclass
class QueryParams(AbstractParams):
    name: str = ""  # required
    action: Optional[str] = None
    search_text: str = ""  # required
    select_params: Optional[List[SelectParams]
                            ] = field(default_factory=lambda: [])
    additional_select_clause: Optional[str] = None
    additional_where_clause: Optional[str] = None
    open_params: Optional[List[OpenParams]] = field(default_factory=lambda: [])
    page: Optional[int] = 1
    page_size: Optional[int] = 10
    tab: Optional[str] = None
    scope: Optional[str] = None
    basket: Optional[str] = None
    is_first_page: Optional[bool] = False
    strict_refine: Optional[bool] = False
    global_relevance: Optional[int] = None
    question_language: Optional[str] = None
    question_default_language: Optional[str] = None
    spelling_correction_mode: Optional[str] = None
    spelling_correction_filter: Optional[str] = None
    document_weight: Optional[str] = None
    text_part_weights: Optional[str] = None
    relevance_transforms: Optional[str] = None
    remove_duplicates: Optional[bool] = False
    aggregations: Optional[List[str]] = field(default_factory=lambda: [])
    order_by: Optional[str] = None
    group_by: Optional[str] = None
    advanced: Optional[AdvancedParams] = None
    debug: bool = False

    def _prepare_query_args(self, query_name: str) -> Dict:
        params = {
            "name": query_name,
            "text": self.search_text,
            "isFirstpage": self.is_first_page,
            "strictRefine": self.strict_refine,
            "removeDuplicates": self.remove_duplicates,
        }

        if self.action is not None:
            params["action"] = self.action
        else:
            params["action"] = "search"

        if len(self.select_params) > 0:
            select_params = []
            for item in self.select_params:
                select_params.append(item.generate_payload())
            params["select"] = self.select_params

        if self.additional_select_clause is not None:
            params["additionalSelectClause"] = self.additional_select_clause

        if self.additional_where_clause is not None:
            params["additionalWhereClause"] = self.additional_where_clause

        if len(self.open_params) > 0:
            open_params = []
            for item in self.open_params:
                open_params.append(item.generate_payload())
            params["open"] = self.open_params

        if self.page is not None:
            params["page"] = self.page
        else:
            params["page"] = 1

        if self.page_size is not None:
            params["pageSize"] = self.page_size
        else:
            params["pageSize"] = self.page_size

        if self.tab is not None:
            params["tab"] = self.tab

        if self.scope is not None:
            params["scope"] = self.scope

        if self.basket is not None:
            params["basket"] = self.basket

        if self.global_relevance is not None:
            params["globalRelevance"] = self.global_relevance

        if self.question_language is not None:
            params["questionLanguage"] = self.question_language

        if self.question_default_language is not None:
            params["questionDefaultLanguage"] = self.question_default_language

        if self.spelling_correction_mode is not None:
            params["spellingCorrectionMode"] = self.spelling_correction_mode

        if self.spelling_correction_filter is not None:
            params["spellingCorrectionFilter"] = self.spelling_correction_filter

        if self.document_weight is not None:
            params["documentWeight"] = self.document_weight

        if self.text_part_weights is not None:
            params["textPartWeights"] = self.text_part_weights

        if self.relevance_transforms is not None:
            params["relevanceTransforms"] = self.relevance_transforms

        if len(self.aggregations) > 0:
            params["aggregations"] = self.aggregations

        if self.order_by is not None:
            params["orderBy"] = self.order_by

        if self.group_by is not None:
            params["groupBy"] = self.group_by

        if self.advanced is not None:
            params["advanced"] = self.advanced.generate_payload()

        return params

    def generate_payload(self, **kwargs) -> Dict:
        """
        This method generates payload for
        QueryParams.

        Args:
            query_name(str): Name of query service to query for
        """
        query_name = kwargs.get("query_name")
        payload = self._prepare_query_args(query_name)
        if self.debug:
            logger.debug(payload)

        return payload
