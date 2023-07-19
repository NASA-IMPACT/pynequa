from typing import Dict, List


class TreeParams:
    box: str = ""
    column: str = ""
    op: str = ""
    value: str = ""

    def _generate_tree_params_payload(self) -> Dict:
        return {
            "box": self.box,
            "column": self.column,
            "op": self.op,
            "value": self.value,
        }


class SelectParams:
    expression: str = ""
    facet: str = ""

    def _generate_select_params_payload(self) -> Dict:
        return {
            "expression": self.expression,
            "facet": self.facet,
        }


class OpenParams:
    expression: str = ""
    facet: str = ""

    def _generate_open_params_payload(self) -> Dict:
        return {
            "expression": self.expression,
            "facet": self.facet,
        }


class AdvancedParams:
    col_name: str = ""
    col_value: str = ""
    value: str = ""
    operator: str = ""

    def _generate_advanced_params_payload(self) -> Dict:
        return {
            self.col_name: self.col_value,
            "value": self.value,
            "operator": self.operator
        }


class QueryParams:
    name: str = ""  # required
    action: str = ""
    search_text: str = ""  # required
    select_params: List[SelectParams] = []
    additional_select_clause: str = ""
    additional_where_clause: str = ""
    open_params: List[OpenParams] = []
    page: int = 0
    page_size: int = 0
    tab: str = ""
    scope: str = ""
    basket: str = ""
    is_first_page: bool = False
    strict_refine: bool = False
    global_relevance: int = 0
    question_language: str = ""
    question_default_language: str = ""
    spelling_correction_mode: str = ""
    spelling_correction_filter: str = ""
    document_weight: str = ""
    text_part_weights: str = ""
    relevance_transforms: str = ""
    remove_duplicates: bool = False
    aggregations: List[str] = []
    order_by: str = ""
    group_by: str = ""
    advanced: AdvancedParams = AdvancedParams()

    def __init__(self) -> None:
        pass

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
                select_params.append(item._generate_select_params_payload())
            params["select"] = self.select_params

        if self.additional_select_clause is not None:
            params["additionalSelectClause"] = self.additional_select_clause

        if self.additional_where_clause is not None:
            params["additionalWhereClause"] = self.additional_where_clause

        if len(self.open_params) > 0:
            open_params = []
            for item in self.open_params:
                open_params.append(item._generate_open_params_payload())
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
            params["advanced"] = self.advanced._generate_advanced_params_payload()

        return params
