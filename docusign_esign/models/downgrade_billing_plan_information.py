# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class DowngradeBillingPlanInformation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'downgrade_event_type': 'str',
        'plan_information': 'PlanInformation',
        'promo_code': 'str',
        'sale_discount': 'str',
        'sale_discount_periods': 'str',
        'sale_discount_type': 'str'
    }

    attribute_map = {
        'downgrade_event_type': 'downgradeEventType',
        'plan_information': 'planInformation',
        'promo_code': 'promoCode',
        'sale_discount': 'saleDiscount',
        'sale_discount_periods': 'saleDiscountPeriods',
        'sale_discount_type': 'saleDiscountType'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DowngradeBillingPlanInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._downgrade_event_type = None
        self._plan_information = None
        self._promo_code = None
        self._sale_discount = None
        self._sale_discount_periods = None
        self._sale_discount_type = None
        self.discriminator = None

        setattr(self, "_{}".format('downgrade_event_type'), kwargs.get('downgrade_event_type', None))
        setattr(self, "_{}".format('plan_information'), kwargs.get('plan_information', None))
        setattr(self, "_{}".format('promo_code'), kwargs.get('promo_code', None))
        setattr(self, "_{}".format('sale_discount'), kwargs.get('sale_discount', None))
        setattr(self, "_{}".format('sale_discount_periods'), kwargs.get('sale_discount_periods', None))
        setattr(self, "_{}".format('sale_discount_type'), kwargs.get('sale_discount_type', None))

    @property
    def downgrade_event_type(self):
        """Gets the downgrade_event_type of this DowngradeBillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The downgrade_event_type of this DowngradeBillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_event_type

    @downgrade_event_type.setter
    def downgrade_event_type(self, downgrade_event_type):
        """Sets the downgrade_event_type of this DowngradeBillingPlanInformation.

          # noqa: E501

        :param downgrade_event_type: The downgrade_event_type of this DowngradeBillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._downgrade_event_type = downgrade_event_type

    @property
    def plan_information(self):
        """Gets the plan_information of this DowngradeBillingPlanInformation.  # noqa: E501


        :return: The plan_information of this DowngradeBillingPlanInformation.  # noqa: E501
        :rtype: PlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """Sets the plan_information of this DowngradeBillingPlanInformation.


        :param plan_information: The plan_information of this DowngradeBillingPlanInformation.  # noqa: E501
        :type: PlanInformation
        """

        self._plan_information = plan_information

    @property
    def promo_code(self):
        """Gets the promo_code of this DowngradeBillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The promo_code of this DowngradeBillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._promo_code

    @promo_code.setter
    def promo_code(self, promo_code):
        """Sets the promo_code of this DowngradeBillingPlanInformation.

          # noqa: E501

        :param promo_code: The promo_code of this DowngradeBillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._promo_code = promo_code

    @property
    def sale_discount(self):
        """Gets the sale_discount of this DowngradeBillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount of this DowngradeBillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount

    @sale_discount.setter
    def sale_discount(self, sale_discount):
        """Sets the sale_discount of this DowngradeBillingPlanInformation.

          # noqa: E501

        :param sale_discount: The sale_discount of this DowngradeBillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount = sale_discount

    @property
    def sale_discount_periods(self):
        """Gets the sale_discount_periods of this DowngradeBillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_periods of this DowngradeBillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_periods

    @sale_discount_periods.setter
    def sale_discount_periods(self, sale_discount_periods):
        """Sets the sale_discount_periods of this DowngradeBillingPlanInformation.

          # noqa: E501

        :param sale_discount_periods: The sale_discount_periods of this DowngradeBillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_periods = sale_discount_periods

    @property
    def sale_discount_type(self):
        """Gets the sale_discount_type of this DowngradeBillingPlanInformation.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_type of this DowngradeBillingPlanInformation.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_type

    @sale_discount_type.setter
    def sale_discount_type(self, sale_discount_type):
        """Sets the sale_discount_type of this DowngradeBillingPlanInformation.

          # noqa: E501

        :param sale_discount_type: The sale_discount_type of this DowngradeBillingPlanInformation.  # noqa: E501
        :type: str
        """

        self._sale_discount_type = sale_discount_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DowngradeBillingPlanInformation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DowngradeBillingPlanInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DowngradeBillingPlanInformation):
            return True

        return self.to_dict() != other.to_dict()