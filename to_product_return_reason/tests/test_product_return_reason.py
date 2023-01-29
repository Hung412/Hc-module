from psycopg2 import IntegrityError

from odoo import tools, exceptions
from odoo.tests.common import tagged


from .common import ProductReturnReasonCommon


@tagged('post_install', '-at_install')
class TestProducReturnReason(ProductReturnReasonCommon):
    def test_01_sql_constraints_name(self):
        with tools.mute_logger('odoo.sql_db'):
            with self.assertRaises(IntegrityError):
                self.env['product.return.reason'].create({
                    'name': 'reason_1',
                    'description': 'description',
                })

    def test_01_sql_constraints_description(self):
        with tools.mute_logger('odoo.sql_db'):
            with self.assertRaises(IntegrityError):
                self.env['product.return.reason'].create({
                    'name': 'reason_error_test',
                    'description': 'reason_error_test',
                })
                
    def test_copy_reason(self):
        self.reason_2 = self.reason_1.copy()
        reason_2_name = self.reason_1.name + ' (copy)'
        self.assertRecordValues(self.reason_2, [{
                'name': reason_2_name,
                'description': 'description'
            }])
