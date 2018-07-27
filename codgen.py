
import os

from sympy.core.expr import Basic
from sympy.integrals.rubi.rubi import rubi_object
from sympy.integrals.rubi.rubi import *
from sympy import *
from sympy.core.singleton import Singleton

from matchpy.utils import get_short_lambda_source
from matchpy.matching.code_generation import CodeGenerator
import re
rubi = rubi_object()[0]

    
GENERATED_TEMPLATE = '''
# -*- coding: utf-8 -*-
from matchpy import *
from sympy import *
from sympy.integrals.rubi.utility_function import *
from sympy.integrals.rubi.constraints import *
from sympy.integrals.rubi.symbol import *
{}
{}
    '''.strip()

generator = CodeGenerator(rubi.matcher)
global_code, code = generator.generate_code()
code = GENERATED_TEMPLATE.format(global_code, code)

with open('generated.py', 'w', encoding='utf-8') as f:
    f.write(code)

from generated import match_root

x = symbols('x')
for r, p in match_root(Integral(S(1)/x, x)):
    print(r, p)
