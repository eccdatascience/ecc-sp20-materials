test = {   'name': 'q1_11',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> all([type(lower_bound_sal) in set([float, np.float32, np.float64]), type(upper_bound_sal) in set([float, np.float32, np.float64]), '
                                               'type(reject_sal) == bool])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([lower_bound_sal == percentile(2.5, resampled_correlations_salary), upper_bound_sal == percentile(97.5, resampled_correlations_salary), '
                                               'reject_sal == True])\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
