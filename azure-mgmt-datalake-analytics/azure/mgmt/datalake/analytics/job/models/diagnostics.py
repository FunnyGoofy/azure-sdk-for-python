# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Diagnostics(Model):
    """Error diagnostic information for failed jobs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar column_number: the column where the error occured.
    :vartype column_number: int
    :ivar end: the ending index of the error.
    :vartype end: int
    :ivar line_number: the line number the error occured on.
    :vartype line_number: int
    :ivar message: the error message.
    :vartype message: str
    :ivar severity: the severity of the error. Possible values include:
     'Warning', 'Error', 'Info'
    :vartype severity: str or :class:`SeverityTypes
     <azure.mgmt.datalake.analytics.job.models.SeverityTypes>`
    :ivar start: the starting index of the error.
    :vartype start: int
    """ 

    _validation = {
        'column_number': {'readonly': True},
        'end': {'readonly': True},
        'line_number': {'readonly': True},
        'message': {'readonly': True},
        'severity': {'readonly': True},
        'start': {'readonly': True},
    }

    _attribute_map = {
        'column_number': {'key': 'columnNumber', 'type': 'int'},
        'end': {'key': 'end', 'type': 'int'},
        'line_number': {'key': 'lineNumber', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'start': {'key': 'start', 'type': 'int'},
    }

    def __init__(self):
        self.column_number = None
        self.end = None
        self.line_number = None
        self.message = None
        self.severity = None
        self.start = None
