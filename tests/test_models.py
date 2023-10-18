from pynequa.models import QueryParams
import unittest
import logging


class TestQueryParams(unittest.TestCase):

    def test_query_params_payload(self):
        """
            Test if query params payload is correctly
            generated or not.
        """
        qp = QueryParams(
            name="query",
            search_text="What was Landsat-9 launched?"
        )

        payload = qp.generate_payload()
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


if __name__ == '__main__':
    unittest.main()
