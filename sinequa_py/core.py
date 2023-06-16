from sinequa_py.api import API

class Sinequa(API):
    def __init__(self, config) -> None:
        """
            This method expects following: 
            {
                "access_token": "security token for Sinequa authentication",
                "base_url":"URL of Sinequa instance",
                "app_name": "name of sinequa app",
                "query_name": "name of query service"
            }
        """
        super().__init__(config)
        pass

    def search_app(self):
        endpoint="search.app"
        pass 

    def search_dataset(self):
        endpoint="search.dataset"
        print("hello world")

    def search_query(self):
        endpoint="search.query"
        pass 

    def query_intent(self):
        endpoint="queryintent"
        pass 

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



