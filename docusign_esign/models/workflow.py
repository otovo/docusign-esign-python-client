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


class Workflow(object):
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
        'current_workflow_step_id': 'str',
        'workflow_status': 'str',
        'workflow_steps': 'list[WorkflowStep]'
    }

    attribute_map = {
        'current_workflow_step_id': 'currentWorkflowStepId',
        'workflow_status': 'workflowStatus',
        'workflow_steps': 'workflowSteps'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Workflow - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_workflow_step_id = None
        self._workflow_status = None
        self._workflow_steps = None
        self.discriminator = None

        setattr(self, "_{}".format('current_workflow_step_id'), kwargs.get('current_workflow_step_id', None))
        setattr(self, "_{}".format('workflow_status'), kwargs.get('workflow_status', None))
        setattr(self, "_{}".format('workflow_steps'), kwargs.get('workflow_steps', None))

    @property
    def current_workflow_step_id(self):
        """Gets the current_workflow_step_id of this Workflow.  # noqa: E501

          # noqa: E501

        :return: The current_workflow_step_id of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._current_workflow_step_id

    @current_workflow_step_id.setter
    def current_workflow_step_id(self, current_workflow_step_id):
        """Sets the current_workflow_step_id of this Workflow.

          # noqa: E501

        :param current_workflow_step_id: The current_workflow_step_id of this Workflow.  # noqa: E501
        :type: str
        """

        self._current_workflow_step_id = current_workflow_step_id

    @property
    def workflow_status(self):
        """Gets the workflow_status of this Workflow.  # noqa: E501

          # noqa: E501

        :return: The workflow_status of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """Sets the workflow_status of this Workflow.

          # noqa: E501

        :param workflow_status: The workflow_status of this Workflow.  # noqa: E501
        :type: str
        """

        self._workflow_status = workflow_status

    @property
    def workflow_steps(self):
        """Gets the workflow_steps of this Workflow.  # noqa: E501

          # noqa: E501

        :return: The workflow_steps of this Workflow.  # noqa: E501
        :rtype: list[WorkflowStep]
        """
        return self._workflow_steps

    @workflow_steps.setter
    def workflow_steps(self, workflow_steps):
        """Sets the workflow_steps of this Workflow.

          # noqa: E501

        :param workflow_steps: The workflow_steps of this Workflow.  # noqa: E501
        :type: list[WorkflowStep]
        """

        self._workflow_steps = workflow_steps

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
        if issubclass(Workflow, dict):
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
        if not isinstance(other, Workflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Workflow):
            return True

        return self.to_dict() != other.to_dict()