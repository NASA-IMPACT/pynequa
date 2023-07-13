from sinequa_py.api import API
from typing import Optional, List, Dict
from sinequa_py.models import QueryParams


class Sinequa(API):
    '''
        Sinequa API Client for Python

        Attributes:
            app_name(str): name of Sinequa app
            query_name(str): name of search query web service 
    '''
    app_name: str
    query_name: str

    def __init__(self, config: Dict) -> None:
        super().__init__(config)
        self.app_name = config["app_name"]  # name of application
        # name of search query web service
        self.query_name = config["query_name"]

    @staticmethod
    def _prepare_kwargs(payload: Dict, kwargs: Dict) -> Dict:
        for key, value in kwargs.items():
            payload[key] = value
        return payload

    def search_app(self, pre_login: bool = False, mode: str = "debug") -> Dict:
        '''
            This method retrieves SBA configuration before and after login. 

            Args: 
                pre_login(bool): false by default. 
                mode(str): debug by default (debug|release)
        '''
        endpoint = "search.app"
        payload = {
            "app": self.app_name,
            "preLogin": pre_login,
            "mode": mode,
        }
        return self.post(endpoint=endpoint, payload=payload)

    def search_dataset(self, parameters: Optional[Dict],
                       datasets: Optional[List[str]]) -> Dict:
        '''
        This method retrieves datasets through SQL queries. The response is a
        list of available datasets with their respective names and descriptions. 

        Args:
            parameters(dict): dictionary of parameters that can be used in SQL fragments
            datasets(list): list of datasets
        Returns:
            Dict: search dataset response  

        '''
        endpoint = "search.dataset"
        payload = {}
        if parameters is not None:
            payload["parameters"] = parameters

        if len(datasets) > 0:
            payload["datasets"] = datasets

        return self.post(endpoint=endpoint, payload=payload)

    def search_query(self, query_params: QueryParams) -> Dict:
        '''
        This method performs search query.

        Args:
            query_params(QueryParams): query parameters as defined in QueryParams class 

        Returns:
            Dict: response data of this request 
        '''
        endpoint = "search.query"

        payload = {
            "app": self.app_name,
            "query": query_params._prepare_query_args(
                query_name=self.query_name)
        }

        return self.post(endpoint=endpoint, payload=payload)

    def query_intent(self, intent_text: str) -> Dict:
        '''
        This method evaluates SBA query intents from query intent sets. 

        Args:
            intent_text(str): indicates the text that should trigger query intent

        Returns:
            Dict: Query Intent response 

        '''
        endpoint = "queryintent"

        query_parameters = {
            "name": self.query_name,
            "text": intent_text
        }
        payload = {
            "app": self.app_name,
            "name": self.query_name,
            "query": query_parameters,
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_profile(self, profile_name: str,
                       query_params: QueryParams, response_type: str = "SearchCursor") -> Dict:
        '''
        This method searches for Sienequa profile. 

        Args:
            profile_name(str): profile name
            response_type(str): default will be SearchCursor 
            query_params(QueryParams): will carry  query parameters in payload

        Returns: 
            Dict: response data for Sinequa profile search.
        '''
        endpoint = "search.profile"

        payload = {
            "profile": profile_name,
            "responsetype": response_type,
            "query": query_params._prepare_query_args(query_name=self.query_name),
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_user_settings(self, action: str = "load", user_settings: Dict = {}) -> Dict:
        '''
        This method provides user settings 

        Args:
            app_name(str): name of application for which user setting should be handled
            action(str): search action (load|save|patch)
            user_settings(Dict): user settings to be saved or patched (see official 
            documentation for more info)

        Returns: 
            Dict: search response based upon action 
        '''
        endpoint = "search.usersettings"
        payload = {
            "app": self.app_name,
            "action": action,
            "userSettings": user_settings,
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_preview(self,   query_params: QueryParams, action: str = "get", origin: str = "", id: str = "",
                       **kwargs) -> Dict:
        '''
        This method retrieves preview data for a product. 

        Args:
            query_params(QueryParams): query params with text to be searched
            action(str): retrieves a preview object
            origin(str): server address of the SBA in browser used to load CSS
            id(str): id of document for which to retrieve the preview

        Returns:
            Dict: response for for Search Preview
        '''
        endpoint = "search.preview"

        payload = {
            "app": self.app_name,
            "action": action,
            "id": id,
            "origin": origin,
            "query": query_params._prepare_query_args(
                query_name=self.query_name)
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_query_export(self, web_service: str, type: str, format: str,
                            name: str, max_count: int) -> Dict:
        '''
        This method allows exporting of search results in different formats.

        Args:
            web_service(str): name of query export web service
            type(str): type of export to perform
            format(str): output format of export
            name(str): name of saved query to be exported (optional)
            max_count(int): maximum of number of documents to include in export (optional)

        Returns:
            Dict: response for search export 
        '''
        endpoint = "search.queryexport"
        payload = {
            "app": self.app_name,
            "webService": web_service,
            "type": type,
            "format": format,
        }

        if name != "":
            payload["name"]: name

        if max_count > 0:
            payload["maxCount"] = max_count

        return self.post(endpoint=endpoint, payload=payload)

    def search_recent_queries(self, action: str = "load") -> Dict:
        '''
        This method retrieves the current recent queries.

        Args:
            action(str): Retrieve recent queries, default=load

        Returns:
            Dict: response for recent queries
        '''
        endpoint = "search.recentqueries"

        payload = {
            "app": self.app_name,
            "action": action,
        }
        return self.post(endpoint=endpoint, payload=payload)

    def search_similardocuments(self, source_doc_id: str, query_params: QueryParams) -> Dict:
        '''
        This method retrieves similar documents to a given document

        Args:
            source_doc_id(str): identifier of document for which to retrieve similar documents
            query_params(QueryParams): query params 
        '''
        endpoint = "search.similardocuments"

        payload = {
            "app": self.app_name,
            "sourceDocumentId": source_doc_id,
            "query": query_params._prepare_query_args(
                query_name=self.query_name)
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_query_links(self):
        '''
        '''
        endpoint = "search.querylinks"
        pass

    def search_ratings(self):
        '''
        '''
        endpoint = "search.ratings"
        pass

    def search_profile_subtree(self):
        '''
        '''
        endpoint = "search.profile.subtree"
        pass

    def search_alerts(self):
        '''
        '''
        endpoint = "search.alerts"
        pass

    def search_baskets(self):
        '''
        '''
        endpoint = "search.baskets"
        pass

    def search_labels(self):
        '''
        '''
        endpoint = "search.labels"
        pass

    def search_saved_queries(self):
        '''
        '''
        endpoint = "search.savedQueries"
        pass

    def search_suggest(self):
        '''
        '''
        endpoint = "search.suggest"
        pass

    def search_custom(self):
        '''
        '''
        endpoint = "search.custom"
        pass

    def suggest_field(self):
        '''
        '''
        endpoint = "suggestField"
        pass

    def engine_sql(self):
        '''
        '''
        endpoint = "engine.sql"
        pass
