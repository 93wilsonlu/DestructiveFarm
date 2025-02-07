# Based on https://gist.github.com/xmikasax/90a0ce5736a4274e46b9958f836951e7

import socket

from server import app
from server.models import FlagStatus, SubmitResult
import requests


RESPONSES = {
    FlagStatus.QUEUED: ['Please submit the flag when round is running.', 'submit too frequently.'],
    FlagStatus.ACCEPTED: ['correct'],
    FlagStatus.REJECTED: ['incorrect'],
}

READ_TIMEOUT = 5
APPEND_TIMEOUT = 0.05
BUFSIZE = 4096


def recvall(sock):
    sock.settimeout(READ_TIMEOUT)
    chunks = [sock.recv(BUFSIZE)]

    sock.settimeout(APPEND_TIMEOUT)
    while True:
        try:
            chunk = sock.recv(BUFSIZE)
            if not chunk:
                break

            chunks.append(chunk)
        except socket.timeout:
            break

    sock.settimeout(READ_TIMEOUT)
    return b''.join(chunks)


def submit_flags(flags, config):
    unknown_responses = set()
    session = requests.Session()
    for item in flags:
        response = session.post(config['SYSTEM_HOST'], json={'flag': item}, headers={
                                'Authorization': config['TEAM_TOKEN']})

        try:
            response_lower = response.json()['res'].lower()
            if response_lower == '':
                response_lower = response.json()['message'].lower()
        except:
            response_lower = response.text.lower()
        print('Flag: ',response_lower)
        for status, substrings in RESPONSES.items():
            if any(s in response_lower for s in substrings):
                found_status = status
                break
        else:
            found_status = FlagStatus.QUEUED
            if response not in unknown_responses:
                unknown_responses.add(response)
                app.logger.warning(
                    'Unknown checksystem response (flag will be resent): %s', response)
        
        print(found_status)
        print(SubmitResult(item.flag, found_status, response.status_code))


        yield SubmitResult(item.flag, found_status, response.status_code)

    session.close()
