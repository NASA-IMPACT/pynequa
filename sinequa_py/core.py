from sinequa_py.api import API

class Sinequa(API):
    '''
        Sinequa API Client for Python

        Attributes:
            app_name(string): name of Sinequa app
            query_name(string): name of search query web service 
    '''
    app_name: str
    query_name: str 

    def __init__(self, config: dict) -> None:
        super().__init__(config)
        self.app_name=config["app_name"] # name of application
        self.query_name=config["query_name"] # name of search query web service

    @staticmethod
    def _prepare_kwargs(payload: dict, kwargs: dict)->dict:
        for key, value in kwargs.items():
            payload[key]=value
        return payload

    def search_app(self, pre_login: bool= false, mode: str = "debug")-> dict:
        '''
            This method retrieves SBA configuration before and after login. 
            
            Args: 
                pre_login(bool): false by default. 
                mode(str): debug by default (debug|release)
        '''
        endpoint="search.app"
        payload={
            "app": self.app_name,
            "preLogin": pre_login,
            "mode": mode,
        }
        return self.post(endpoint=endpoint, payload=payload)

    def search_dataset(self, parameters:dict, datasets: list) -> dict:
        '''
            This method retrieves datasets through SQL queries. The response is a
            list of available datasets with their respective names and descriptions. 
        '''
        endpoint="search.dataset"
        payload={}
        if parameters is not None:
            payload["parameters"]=parameters
        
        if len(datasets)>0:
            payload["datasets"]=datasets

        return self.post(endpoint=endpoint, payload=payload)

    def search_query(self, search_text, page_size= 10, page= 1, **kwargs) -> dict:
        '''
        This method performs search query.

        Args:
            search_text(string): text to search
            page_size(int): number of results in a page
            page(int): page number 
        
        Returns:
            dict: response data of this request 
        '''
        endpoint="search.query"

        query_parameters={
                "name":self.query_name,
                "action":"search",
                "text":search_text,
                "pageSize":page_size,
                "page":page 
        }
        
        payload={
            "app": self.app_name,
            "query": self._prepare_kwargs(query_parameters,kwargs=kwargs),
        }
        return self.post(endpoint=endpoint, payload=payload) 

    def query_intent(self, intent_text: str,**kwargs):
        endpoint="queryintent"

        query_parameters={
            "name": self.query_name,
            "text":intent_text
        }
        payload={
            "app": self.app_name,
            "name": self.query_name,
            "query": self._prepare_kwargs(query_parameters, kwargs=kwargs),
        }

        return self.post(endpoint=endpoint, payload=payload) 

    def search_profile(self):
        endpoint="search.profile"
        pass 

    def search_user_settings(self):
        endpoint="search.usersettings"
        pass 

    def search_preview(self):
        endpoint="search.preview"
        pass

    def search_query_export(self):
        endpoint="search.queryexport"
        pass 

    def search_recent_queries(self):
        endpoint="search.recentqueries"
        pass 

    def search_similardocuments(self):
        endpoint="search.similardocuments"
        pass 

    def search_query_links(self):
        endpoint="search.querylinks"
        pass 

    def search_ratings(self):
        endpoint="search.ratings"
        pass 



