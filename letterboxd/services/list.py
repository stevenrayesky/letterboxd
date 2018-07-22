import logging

logging.getLogger(__name__)


class List(object):
    """
    /list/* services for the Letterboxd API
    """

    def __init__(self, api, list_id=None):
        """
        Initializes a Film object with a specific film.

        :param api: API object
        :param list_id: str - LID for the film on Letterboxd
        """
        self._api = api
        self._list_id = list_id

    def details(self, list_id=None):
        """
        /list/{id}

        Get details of a list by LID. If no list ID passed, uses the
        initialized list.

        :param list_id: str - LID of the film
        :return: dict - Film
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(path=f"list/{list_id}")
        return response.json()

    def comments(self, list_id=None, comments_request=None):
        """
        /list/{id}/comments

        A cursored window over the comments for a list.
        Use the ‘next’ cursor to move through the comments.

        :param list_id: str - LID of the list
        :param comments_request: dict - CommentsRequest
        :return:
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(path=f"list/{list_id}/comments")
        list_comments_response = response.json()
        return list_comments_response

    def create_comment(self, list_id=None, comment_creation_request=None):
        """
        /list/{id}/comments

        Create a comment on a list.

        Calls to this endpoint must include the access token for an authenticated member.

        :param list_id: str - LID for the list
        :param comment_creation_request: dict - CommentCreationRequest
        :return: dict - ListComment
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(
            path=f"list/{list_id}/comments",
            method="POST",
            params=comment_creation_request,
        )
        list_comment = response.json()
        return list_comment

    # TODO: Implement the rest of /list/* endpoints


class Lists(object):
    """
    /lists service for the Letterboxd API
    """

    def __init__(self, api):
        """

        :param api: API object
        """
        self._api = api

    def lists(self, lists_request=None):
        """
        [GET] /lists

        A cursored window over a list of lists.

        Use the ‘next’ cursor to move through the list.

        :param lists_request: dict - ListsRequest
        :return: dict - ListsResponse
        """
        response = self._api.api_call(path="lists", params=lists_request)
        lists_response = response.json()
        logging.debug(lists_response)
        return lists_response

    def create_list(self, list_creation_request=None):
        """
        [POST] /lists

        Create a list.

        Calls to this endpoint must include the access token
        for an authenticated member.

        :param list_creation_request: dict - ListCreationRequest
        :return: dict - ListCreateResponse
        """
        response = self._api.api_call(
            path="lists", params=list_creation_request, method="POST"
        )
        list_create_response = response.json()
        logging.debug(list_create_response)
        return list_create_response
