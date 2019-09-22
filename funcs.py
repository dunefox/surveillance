#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config as cfg

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!") 

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.message.chat_id, text=text_caps)

