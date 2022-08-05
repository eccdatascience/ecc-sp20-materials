test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> final_scores.num_columns == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> set(['Opponent', 'Cal Score', 'Opponent Score']) == set(final_scores.labels)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> final_scores.take(range(5, 11)).column(0).item(0) == "Oregon"\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
