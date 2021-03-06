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


class ProductosClimatologicosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def balance_hdrico_nacional__documento_(self, anio, decena, **kwargs):  # noqa: E501
        """Balance hídrico nacional (documento).  # noqa: E501

        Se obtiene, para la decema y el año pasados por parámetro, el Boletín Hídrico Nacional que se elabora cada diez días. Se presenta información resumida de forma distribuida para todo el territorio nacional de diferentes variables, en las que se incluye informaciones de la precipitación y la evapotranspiración potencial acumuladas desde el 1 de septiembre.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.balance_hdrico_nacional__documento_(anio, decena, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str anio: Año (AAAA) (required)
        :param str decena: Decena de 01 (primera decena) a 36 (última decena) (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.balance_hdrico_nacional__documento__with_http_info(anio, decena, **kwargs)  # noqa: E501
        else:
            (data) = self.balance_hdrico_nacional__documento__with_http_info(anio, decena, **kwargs)  # noqa: E501
            return data

    def balance_hdrico_nacional__documento__with_http_info(self, anio, decena, **kwargs):  # noqa: E501
        """Balance hídrico nacional (documento).  # noqa: E501

        Se obtiene, para la decema y el año pasados por parámetro, el Boletín Hídrico Nacional que se elabora cada diez días. Se presenta información resumida de forma distribuida para todo el territorio nacional de diferentes variables, en las que se incluye informaciones de la precipitación y la evapotranspiración potencial acumuladas desde el 1 de septiembre.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.balance_hdrico_nacional__documento__with_http_info(anio, decena, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str anio: Año (AAAA) (required)
        :param str decena: Decena de 01 (primera decena) a 36 (última decena) (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['anio', 'decena']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method balance_hdrico_nacional__documento_" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'anio' is set
        if ('anio' not in params or
                params['anio'] is None):
            raise ValueError("Missing the required parameter `anio` when calling `balance_hdrico_nacional__documento_`")  # noqa: E501
        # verify the required parameter 'decena' is set
        if ('decena' not in params or
                params['decena'] is None):
            raise ValueError("Missing the required parameter `decena` when calling `balance_hdrico_nacional__documento_`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'anio' in params:
            path_params['anio'] = params['anio']  # noqa: E501
        if 'decena' in params:
            path_params['decena'] = params['decena']  # noqa: E501

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
            '/api/productos/climatologicos/balancehidrico/{anio}/{decena}', 'GET',
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

    def capas_shape_de_estaciones_climatolgicas_(self, tipoestacion, **kwargs):  # noqa: E501
        """Capas SHAPE de estaciones climatológicas de AEMET.  # noqa: E501

        Capas SHAPE de las distintas estaciones climatológicas de AEMET: automáticas, completas, pluviométricas y termométricas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.capas_shape_de_estaciones_climatolgicas_(tipoestacion, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tipoestacion:  | Código | Tipo de Estación | |----------|----------| | automaticas  | Estaciones Automáticas   | | completas  | Estaciones Completas   | | pluviometricas  | Estaciones Pluviométricas   | | termometricas  | Estaciones Termométricas    (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.capas_shape_de_estaciones_climatolgicas__with_http_info(tipoestacion, **kwargs)  # noqa: E501
        else:
            (data) = self.capas_shape_de_estaciones_climatolgicas__with_http_info(tipoestacion, **kwargs)  # noqa: E501
            return data

    def capas_shape_de_estaciones_climatolgicas__with_http_info(self, tipoestacion, **kwargs):  # noqa: E501
        """Capas SHAPE de estaciones climatológicas de AEMET.  # noqa: E501

        Capas SHAPE de las distintas estaciones climatológicas de AEMET: automáticas, completas, pluviométricas y termométricas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.capas_shape_de_estaciones_climatolgicas__with_http_info(tipoestacion, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tipoestacion:  | Código | Tipo de Estación | |----------|----------| | automaticas  | Estaciones Automáticas   | | completas  | Estaciones Completas   | | pluviometricas  | Estaciones Pluviométricas   | | termometricas  | Estaciones Termométricas    (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tipoestacion']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method capas_shape_de_estaciones_climatolgicas_" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tipoestacion' is set
        if ('tipoestacion' not in params or
                params['tipoestacion'] is None):
            raise ValueError("Missing the required parameter `tipoestacion` when calling `capas_shape_de_estaciones_climatolgicas_`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tipoestacion' in params:
            path_params['tipoestacion'] = params['tipoestacion']  # noqa: E501

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
            '/api/productos/climatologicos/capasshape/{tipoestacion}', 'GET',
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

    def resumen_mensual_climatolgico_nacional__documento_(self, anio, mes, **kwargs):  # noqa: E501
        """Resumen mensual climatológico nacional (documento).  # noqa: E501

        Resumen climatológico nacional, para el año y mes pasado por parámetro, sobre el estado del clima y la evolución de las principales variables climáticas, en especial temperatura y precipitación, a nivel mensual, estacional y anual.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resumen_mensual_climatolgico_nacional__documento_(anio, mes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str anio: Año (AAAA) (required)
        :param str mes: Mes (mm) (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resumen_mensual_climatolgico_nacional__documento__with_http_info(anio, mes, **kwargs)  # noqa: E501
        else:
            (data) = self.resumen_mensual_climatolgico_nacional__documento__with_http_info(anio, mes, **kwargs)  # noqa: E501
            return data

    def resumen_mensual_climatolgico_nacional__documento__with_http_info(self, anio, mes, **kwargs):  # noqa: E501
        """Resumen mensual climatológico nacional (documento).  # noqa: E501

        Resumen climatológico nacional, para el año y mes pasado por parámetro, sobre el estado del clima y la evolución de las principales variables climáticas, en especial temperatura y precipitación, a nivel mensual, estacional y anual.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resumen_mensual_climatolgico_nacional__documento__with_http_info(anio, mes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str anio: Año (AAAA) (required)
        :param str mes: Mes (mm) (required)
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['anio', 'mes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resumen_mensual_climatolgico_nacional__documento_" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'anio' is set
        if ('anio' not in params or
                params['anio'] is None):
            raise ValueError("Missing the required parameter `anio` when calling `resumen_mensual_climatolgico_nacional__documento_`")  # noqa: E501
        # verify the required parameter 'mes' is set
        if ('mes' not in params or
                params['mes'] is None):
            raise ValueError("Missing the required parameter `mes` when calling `resumen_mensual_climatolgico_nacional__documento_`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'anio' in params:
            path_params['anio'] = params['anio']  # noqa: E501
        if 'mes' in params:
            path_params['mes'] = params['mes']  # noqa: E501

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
            '/api/productos/climatologicos/resumenclimatologico/nacional/{anio}/{mes}', 'GET',
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
