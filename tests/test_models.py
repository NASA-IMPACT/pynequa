from pynequa.models import QueryParams, AdvancedParams, AlertParams
import unittest
import logging
import json


class TestQueryParams(unittest.TestCase):

    def test_query_params_payload(self):
        """
            Test if query params payload is correctly
            generated or not.
        """
        qp = QueryParams(
            name="query",
            search_text="What was Landsat-9 launched?",
            page_size=20,
        )

        payload = qp.generate_payload()
        print(payload)
        logging.debug(payload)

        keys_which_must_be_in_payload = [
            "name",
            "text",
            "isFirstpage",
            "strictRefine",
            "removeDuplicates"
        ]

        for key in keys_which_must_be_in_payload:
            if key not in payload:
                self.assertEqual(key, "test", f"{key} is mising in payload")

    def test_query_params_with_advanced_params(self):
        """
            Test if advanced params are correctly
            generated in query param payload or not.
        """

        ap1 = AdvancedParams(
            col_name="collection",
            col_value="accounting"
        )

        ap2 = AdvancedParams(
            col_name="docformat",
            col_value=["pdf", "docx"]
        )

        ap3 = AdvancedParams(
            col_name="modified",
            value="2019-01-01",
            operator=">="
        )

        ap4 = AdvancedParams(
            col_name="modified",
            value="2019-12-31",
            operator="<="
        )

        qp = QueryParams(
            name="query",
            search_text="What was Landsat-9 launched?",
            advanced=[
                ap1,
                ap2,
                ap3,
                ap4
            ]
        )

        payload = qp.generate_payload()

        expected_payload = {
            "collection": "accounting",
            "docformat": ["pdf", "docx"],
            "modified": [
                {"value": "2019-01-01", "operator": ">="},
                {"value": "2019-12-31", "operator": "<="}
            ]
        }

        assert payload["advanced"] == expected_payload


class TestAlertParams(unittest.TestCase):

    def test_alert_params_payload(self):
        """
            Test if alert params payload is correctly
            generated or not.
        """
        ap = AlertParams(
            name="TestAlert",
            description="This is a test alert",
            frequency="hourly",
            combine_with_other_alerts=True,
            respect_tab_selection=True,
        )

        generated_payload = ap.generate_payload()

        expected_payload = {
            "name": "TestAlert",
            "description": "This is a test alert",
            "frequency": "hourly",
            "active": False,
            "combineWithOtherAlerts": True,
            "respectTabSelection": True
        }

        assert generated_payload == expected_payload


if __name__ == '__main__':
    unittest.main()
