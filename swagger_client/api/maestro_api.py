# coding: utf-8

"""
    AEMET OpenData

    AEMET OpenData es una API REST desarrollado por AEMET que permite la difusión y la reutilización de la información meteorológica y climatológica de la Agencia, en el sentido indicado en la Ley 18/2015, de 9 de julio, por la que se modifica la Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público. (IMPORTANTE: Para poder realizar peticiones, es necesario introducir en API Key haciendo clic en el círculo rojo de recurso REST).  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MaestroApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_municipio_using_get(self, municipio, **kwargs):  # noqa: E501
        """getMunicipio  # noqa: E501

        Retorna información específica del municipio de España que se le pasa como parámetro.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_municipio_using_get(municipio, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str municipio: Municipio (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_municipio_using_get_with_http_info(municipio, **kwargs)  # noqa: E501
        else:
            (data) = self.get_municipio_using_get_with_http_info(municipio, **kwargs)  # noqa: E501
            return data

    def get_municipio_using_get_with_http_info(self, municipio, **kwargs):  # noqa: E501
        """getMunicipio  # noqa: E501

        Retorna información específica del municipio de España que se le pasa como parámetro.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_municipio_using_get_with_http_info(municipio, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str municipio: Municipio (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['municipio']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_municipio_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'municipio' is set
        if ('municipio' not in params or
                params['municipio'] is None):
            raise ValueError("Missing the required parameter `municipio` when calling `get_municipio_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'municipio' in params:
            path_params['municipio'] = params['municipio']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/maestro/municipio/{municipio}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Model200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_municipios_using_get(self, **kwargs):  # noqa: E501
        """getMunicipios  # noqa: E501

        Retorna todos los municipios de España. Este servicio es útil para obtener información para utilizar otros elementos de AEMET OpenData, como por ejemplo, la predicción de municipios para 7 días o por  horas ya que nos retorna el id del municipio que necesitamos.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_municipios_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_municipios_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_municipios_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_municipios_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getMunicipios  # noqa: E501

        Retorna todos los municipios de España. Este servicio es útil para obtener información para utilizar otros elementos de AEMET OpenData, como por ejemplo, la predicción de municipios para 7 días o por  horas ya que nos retorna el id del municipio que necesitamos.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_municipios_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_municipios_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/maestro/municipios', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Model200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
