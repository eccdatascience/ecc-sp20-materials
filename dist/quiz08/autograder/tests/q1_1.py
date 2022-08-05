test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(one_resampled_percentage(votes)) in set([float, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 35 <= one_resampled_percentage(votes) <= 65\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> votes = Table.read_table('votes.csv')\n>>> np.random.seed(123)\n>>> one_resampled_percentage(votes) == 51.6\nTrue", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
