# -*- coding: utf-8 -*-

import generation_sonnets

def test_constraints_1():
    dates = ['1800-1830']
    constraints = {'date': dates}
    assert generation_sonnets.__compute_constraints__(constraints) == '((date >= 1800) & (date <= 1830) ) '

def test_constraints_2():
    dates = ['1800-1830', '1891-1900']
    constraints = {'date': dates}
    assert generation_sonnets.__compute_constraints__(constraints) == '((date >= 1800) & (date <= 1830) or (date >= 1891) & (date <= 1900) ) '

def test_constraints_3():
    dates = ['1800-1830', '1891-1900']
    authors = ['Arthur Rimbaud', 'Paul Verlaine']
    constraints = {'date': dates, 'auteur': authors}
    assert generation_sonnets.__compute_constraints__(constraints) == f'((date >= 1800) & (date <= 1830) or (date >= 1891) & (date <= 1900) ) & (auteur.isin({authors})) '
