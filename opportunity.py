# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['SaleOpportunity']
__metaclass__ = PoolMeta


class SaleOpportunity:
    __name__ = 'sale.opportunity'

    next_action_date = fields.DateTime('Next Action Date')
    next_action = fields.Char('Next Action')
