CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): 'http://10.102.{}.60'.format(i)
              for i in range(1, 12)},
    'FLAG_FORMAT': r'EOF\{.*\}',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    'SYSTEM_PROTOCOL': 'eof',
    'SYSTEM_HOST': 'http://35.221.181.38:8888/challenge/5/flagsubmit',
    'SYSTEM_PORT': 8888,
    'TEAM_TOKEN': 'e3bbf42227b370d0cbf8253b9d947ff7',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 10,
    'FLAG_LIFETIME': 5 * 60,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': '8dbc01561823acc3702dd7e2cdb89cfbe5ac2f5e54f4eb00',

    # Use authorization for API requests
    'ENABLE_API_AUTH': True,
    'API_TOKEN': 'f240a55420c0364b0286d20714143f5288530880ae68d972'
}
