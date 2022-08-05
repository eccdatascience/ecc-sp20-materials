test = {   'name': 'q1_15',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure to input `smooth = True` as the second argument to the `minimize` function\n'
                                               '>>> # i.e. minimize(..., smooth = True)\n'
                                               '>>> (1 <= minimized_parameters.item(0) <= 2 and (-7 <= minimized_parameters.item(1) <= -6))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.allclose(minimized_parameters, [ 1.0711393, -6.4542809])\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
