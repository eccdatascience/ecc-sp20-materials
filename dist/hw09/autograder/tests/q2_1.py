test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Your resample should have the same number of rows as the original sample;\n>>> simulate_resample(observations).num_rows == 17\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Your resample should only have the same first label;\n>>> simulate_resample(observations).labels[0] == observations.labels[0]\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This is a little magic to make sure that you see the same results we did.;\n'
                                               '>>> np.random.seed(123);\n'
                                               '>>> \n'
                                               '>>> one_resample = simulate_resample(observations);\n'
                                               '>>> ten_rows = one_resample.take(np.arange(10));\n'
                                               '>>> ten_rows.column(0).item(0) == 108\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
