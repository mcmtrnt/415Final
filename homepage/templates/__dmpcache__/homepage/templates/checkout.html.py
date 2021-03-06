# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1566706654.9146547
_enable_loop = True
_template_filename = 'C:/Users/Trent/scraper/homepage/templates/checkout.html'
_template_uri = '/homepage/templates/checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n            <h4>Purchasing a subscription gives you access to:</h4>\r\n            <strong>\r\n            <ul>\r\n                <br>\r\n                <li>View local dirt bike ads side by side with their Kelly Blue Book value</li>\r\n                <br>\r\n                <li>View ads ordered from best value to worst</li>\r\n                <br>\r\n                <li>Access to our "Price my bike" calculator</li>\r\n            </ul>\r\n        </strong>\r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n')
        if request.user.is_authenticated:
            __M_writer('                <div class="wrapper">\r\n                    <div id="formContent">\r\n                            <h2>Checkout</h2>\r\n                            <p>The Pro Account Costs $10</p>\r\n                        <div>\r\n                            <p></p>\r\n                        </div>\r\n\r\n                        <form method="POST">\r\n                            \r\n                                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
            __M_writer('          \r\n\r\n                        <div><p></p></div>\r\n                        \r\n                        <div id="formFooter">\r\n                                <script\r\n                                src="https://checkout.stripe.com/checkout.js" class="stripe-button"\r\n                                data-key="pk_test_CNCYl3Rg3Tfg0QbgsyL9wTAg00kCZhOvs5"\r\n                                data-amount="1000"\r\n                                data-name="Dirt Bike Deals"\r\n                                data-description="Checkout"\r\n                                data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n                                data-locale="auto">\r\n                                </script>\r\n                        </div>\r\n\r\n                    </form>\r\n\r\n                    </div>\r\n                </div>\r\n')
        else:
            __M_writer('                <div class="wrapper">\r\n                    You must be logged in to purchase the Pro Account\r\n                    <a class="btn btn-primary" href="/homepage/login/" role="button">Login</a>\r\n                </div>       \r\n')
        __M_writer('\r\n\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/checkout.html", "uri": "/homepage/templates/checkout.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 23, "60": 24, "61": 34, "62": 34, "63": 54, "64": 55, "65": 60, "71": 65}}
__M_END_METADATA
"""
