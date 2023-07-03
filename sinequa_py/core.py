from sinequa_py.api import API
from typing import Optional, List, Dict


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

    def search_dataset(self, parameters: Optional[Dict], datasets: Optional[List[str]]) -> Dict:
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

    def search_query(self, search_text: str, page_size: int = 10, page: int = 1, **kwargs) -> Dict:
        '''
        This method performs search query.

        Args:
            search_text(str): text to search
            page_size(int): number of results in a page
            page(int): page number 

        Returns:
            Dict: response data of this request 
        '''
        endpoint = "search.query"

        query_parameters = {
            "name": self.query_name,
            "action": "search",
            "text": search_text,
            "pageSize": page_size,
            "page": page
        }

        payload = {
            "app": self.app_name,
            "query": self._prepare_kwargs(query_parameters, kwargs=kwargs),
        }
        return self.post(endpoint=endpoint, payload=payload)

    def query_intent(self, intent_text: str, **kwargs):
        endpoint = "queryintent"

        query_parameters = {
            "name": self.query_name,
            "text": intent_text
        }
        payload = {
            "app": self.app_name,
            "name": self.query_name,
            "query": self._prepare_kwargs(query_parameters, kwargs=kwargs),
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_profile(self, profile_name: str, response_type: str = "SearchCursor", **kwargs) -> Dict:
        '''
        This method searches for Sienequa profile. 

        Args:
            profile_name(str): profile name
            response_type(str): default will be SearchCursor 
            kwargs: will carry optional query parameters in payload

        Returns: 
            Dict: response data for Sinequa profile search.
        '''
        endpoint = "search.profile"

        payload = {
            "profile": profile_name,
            "responsetype": response_type,
            "query": self._prepare_kwargs({}, kwargs=kwargs),
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_user_settings(self, app_name: str, action: str = "load", user_settings: Dict = {}) -> Dict:
        '''
        This method provides user settings 

        Args:
            app_name(str): name of application for which user setting should be handled
            action(str): search action (load|save|patch)
            user_settings(Dict): user settings to be saved or patched (see official documentation for more info)

        Returns: 
            Dict: search response based upon action 
        '''
        endpoint = "search.usersettings"
        payload = {
            "app": app_name,
            "action": action,
            "userSettings": user_settings,
        }

        return self.post(endpoint=endpoint, payload=payload)

    def search_preview(self):
        '''
        '''
        endpoint = "search.preview"
        pass

    def search_query_export(self):
        '''
        '''
        endpoint = "search.queryexport"
        pass

    def search_recent_queries(self):
        '''
        '''
        endpoint = "search.recentqueries"
        pass

    def search_similardocuments(self):
        '''
        '''
        endpoint = "search.similardocuments"
        pass

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
