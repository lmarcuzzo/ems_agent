# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Metric(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, value: int=None):  # noqa: E501
        """Metric - a model defined in Swagger

        :param id: The id of this Metric.  # noqa: E501
        :type id: int
        :param name: The name of this Metric.  # noqa: E501
        :type name: str
        :param value: The value of this Metric.  # noqa: E501
        :type value: int
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'value': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'value': 'value'
        }

        self._id = id
        self._name = name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Metric':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Metric of this Metric.  # noqa: E501
        :rtype: Metric
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Metric.

        Unique identifier for each metric  # noqa: E501

        :return: The id of this Metric.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Metric.

        Unique identifier for each metric  # noqa: E501

        :param id: The id of this Metric.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Metric.

        Metric name  # noqa: E501

        :return: The name of this Metric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Metric.

        Metric name  # noqa: E501

        :param name: The name of this Metric.
        :type name: str
        """

        self._name = name

    @property
    def value(self) -> int:
        """Gets the value of this Metric.

        Value of current metric  # noqa: E501

        :return: The value of this Metric.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Sets the value of this Metric.

        Value of current metric  # noqa: E501

        :param value: The value of this Metric.
        :type value: int
        """

        self._value = value
