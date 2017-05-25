#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import json
import subprocess

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file


def playSound(filename):
    """Plays a sound file.

       Uses sox file to play the sound file, the file needs to be in the sounds folder.

       Args:
           filename (String): The filename of the file in the sounds folder.
    """
    FNULL = open(os.devnull, 'w')
    path = os.path.dirname(os.path.realpath(__file__)) + "/sounds/" + filename
    subprocess.call(["play", path], stdout=FNULL, stderr=subprocess.STDOUT)


def process_event(event):
    """Pretty prints events.

    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.

    Args:
        event(event.Event): The current event to process.
    """
    if event.type == EventType.ON_START_FINISHED:
        playSound('prompt.mp3') # Need a new sound for start.

    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        playSound('prompt.mp3') # Prompt when conversation started.

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        playSound('finished.aiff') # Everything ended, let the user know!

    if (event.type == EventType.ON_ASSISTANT_ERROR or
            event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT):
        playSound('error.aiff') # Failure of any kind.


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            print(event)
            process_event(event)


if __name__ == '__main__':
    main()
