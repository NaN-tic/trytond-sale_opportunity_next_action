# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .opportunity import *


def register():
    Pool.register(
        SaleOpportunity,
        module='sale_opportunity_next_action', type_='model')
