#!/usr/bin/env python3

# Copyright 2020-present Daniel Burkhardt

import json
import requests
import argparse

parser = argparse.ArgumentParser(description="Send messages to Slack!")

parser.add_argument('-m', type=str, dest='message',
                    help='Message to Post to Slack')
parser.add_argument('--log-file', type=str, dest='log_file', default=None,
                    help='Path to logfile to be sent to slack.')
parser.add_argument('--webhook-url', type=str, dest='webhook',
                    help='Webhook for Slack App. Create one at "https://api.slack.com/apps"')


def post_to_slack(webhook_url, message, log_file=None):
    # https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784

    msg_block = {"type": "section",
    "text": {
        "type": "mrkdwn",
        "text": message
        }
    }
    message_blocks = [msg_block]
    if log_file is not None:
        with open(log_file, 'r') as f:
            log_text = f.readlines()
        header = {
    		"type": "section",
    		"text": {
    			"type": "mrkdwn",
    			"text": "Dumping text from {}. Please consult the log to determine the nature of the issue:".format(log_file)
    		}
    	}
        body = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "```" + " ".join(log_text) + "```"
                }
        }
        message_blocks.append(header)
        message_blocks.append(body)
    json = {"blocks":message_blocks}
    response = requests.post(
        webhook_url, json=json
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
            )

if __name__ == '__main__':
    args = parser.parse_args()
    post_to_slack(args.webhook, args.message, args.log_file)
