test = {   'name': 'q1_7',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> all([type(lower_bound_pc) in set([float, np.float32, np.float64]), type(upper_bound_pc) in set([float, np.float32, np.float64]), type(reject) == '
                                               'bool])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([lower_bound_pc == percentile(2.5, resampled_correlations_pc), upper_bound_pc == percentile(97.5, resampled_correlations_pc), reject == '
                                               'True])\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
