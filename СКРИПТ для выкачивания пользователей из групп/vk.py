version = "7-1"

import time
import re
import requests
from os.path import exists
import locale
import json
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

true = True
false = False
silence = False
data_path = ''


def update(v='last', get=False):
    if v == 'check':
        last_v = update('last', True)
        if last_v == str(version):
            return "Уже установлена актуальная версия"
        else:
            v = 'last'
    print("Rejected!")
    return
    response = requests.post('http://evtn.ru/vk_{0}'.format(v), json={'get': get})
    if get:
        return response.text
    else:
        with open('vk.py', 'wb') as module:
            module.write(response.content)


def drequest(url, data):
    return requests.post(url, data=data)


def auth(token=None, login=None, password=None, client_data=None, app='android', scope=2**28 - 1, respond=False):
    apps = {'android': {'client_id': 2274003, 'client_secret': 'hHbZxrka2uZ6jB1inYsH'}, 'windows': {'client_id': 3697615, 'client_secret': 'AlVXZFMUqyrnABp8ncuU'}}
    if login and password:
        if not client_data:
            if app in apps:
                client_data = apps[app]
            else:
                client_data = apps['android']
        logpass = {**{'username': login, 'password': password,
                      'grant_type': 'password', 'scope': scope}, **client_data}
        response = drequest('https://oauth.vk.com/token', logpass).json()
        if 'error' not in response:
            if not respond:
                print("Success") if silence else None
                auth.default_token = response['access_token']
            else:
                return response['access_token']
        else:
            return response
    elif token:
        auth.default_token = token


class Api:
    def __init__(self, method, token=None, v='5.131', silent=None, **params):
        silent = silence if silent is None else silent
        token = token if token else auth.default_token
        self.silent, self.method, self.token, self.version, self.params = silent, method, token, v, params.copy()
        for key, value in params.items():
            setattr(self, key, value)
        params['access_token'] = token if token else auth.default_token
        params['v'] = v

        self.request = drequest('https://api.vk.com/method/' + method, params)
        self.content = self.request.json()

        if 'response' in self.content:
            self.success = True
            self.visual_success = 'Успех'
            self.content = self.content['response']
        else:
            if not self.silent:
                print('Ошибка: ', self.content['error']['error_msg'])
            self.content = self.content['error']
            self.success = False
            self.visual_success = 'Ошибка'
        if not self.silent:
            print(self)

    def __str__(self):
        return 'Запрос к API по методу ' + str(self.method) + '\n\tПараметры: \n\t\t' + '\n\t\t'.join(['{0}: {1}'.format(i, j) for i, j in self.params.items()]) + '\n\n\tСтатус: ' + str(self.visual_success)


class GLongPoll:
    def __init__(self, group, token=None):
        self.group = group
        if token is None:
            self.token = auth.default_token
        else:
            self.token = token
        self.request = None
        self.updates = []
        connect = Api('groups.getLongPollServer', group_id=group, silent=True, token=self.token)
        if connect.success:
            self.success = True
            if not silence:
                print("Успешно подключено к LongPoll.")
            self.server = connect.content['server']
            self.key = connect.content['key']
            self.ts = connect.content['ts']
        else:
            self.success = False
            if not silence:
                print("Ошибка: " + connect.content['error_msg'])

    def check(self):
        params = {'ts': self.ts, 'key': self.key, 'act': 'a_check', 'wait': 25}
        self.request = drequest(self.server, params)
        if self.request.status_code == 200:
            self.updates = self.request.json()
            if "failed" in self.updates:
                error = self.updates["failed"]
                if error in [2, 3]:
                    print("Переподключение.")
                    self.__init__(self.group, self.token)
                    return self.check()
                elif error == 4:
                    print("(!) Неверная версия")
            if 'ts' in self.updates:
                self.ts = self.updates['ts']
            if 'updates' in self.updates:
                return self.updates['updates']
            return [{'type': "unknown_error", "object": {"msg": "Unknown Error"}}]
        else:
            return [{'type': "request_error", "object": {"msg": "HTTP code said error", "code": self.request.status_code}}]


class ULongPoll:
    def __init__(self, token=None):
        if token is None:
            self.token = auth.default_token
        else:
            self.token = token
        self.request = None
        self.updates = []
        connect = Api('messages.getLongPollServer', lp_version=3, need_pts=1, silent=True, token=self.token)
        if connect.success:
            self.success = True
            if not silence:
                print("Успешно подключено к LongPoll.")
            self.server = connect.content['server']
            self.key = connect.content['key']
            self.ts = connect.content['ts']
        else:
            self.success = False
            if not silence:
                print("Ошибка: " + connect.content['error_msg'])

    def check(self, prettify=False):
        params = {'ts': self.ts, 'key': self.key, 'act': 'a_check', 'wait': 25, "version": 3, "mode": 202}
        self.request = drequest("https://" + self.server, params)
        if self.request.status_code == 200:
            self.updates = self.request.json()
            if "failed" in self.updates:
                error = self.updates["failed"]
                if error in [2, 3]:
                    print("Переподключение.")
                    self.__init__(self.token)
                    return self.check()
                elif error == 4:
                    print("(!) Неверная версия")
            if 'ts' in self.updates:
                self.ts = self.updates['ts']
            if 'updates' in self.updates:
                if prettify:
                    return lp_prettify(self.updates['updates'])
                return self.updates['updates']
            return [{'type': "unknown_error", "object": {"msg": "Unknown Error"}}]
        else:
            return [{'type': "request_error", "object": {"msg": "HTTP code said error", "code": self.request.status_code}}]


def lp_prettify(updates):
    extra_fields = ["peer_id", "timestamp", "text", "from_id", "attachments", "random_id"]
    event_types = {1: "message_flags_replace", 2: "message_flags_install", 3: "message_flags_reset",
                   4: "message_new", 5: "message_edit", 6: "read_incoming", 7: "read_outgoing",
                   8: "friend_online", 9: "friend_offline", 13: "delete_messages", 14: "restore_messages",
                   51: "chat_change", 52: "peer_change", 61: "typing", 62: "chat_typing", 70: "call",
                   80: "counter", 114: "notifications_change"}
    event_schema = {1: ["message_id", "flags"] + extra_fields,
                    2: ["message_id", "mask"] + extra_fields,
                    3: ["message_id", "mask"] + extra_fields,
                    4: ["message_id", "flags"] + extra_fields,
                    5: ["message_id", "mask", "peer_id", "timestamp", "new_text", "from_id", "attachments"],
                    6: ["peer_id", "local_id"],
                    7: ["peer_id", "local_id"],
                    8: ["user_id", "extra", "timestamp"],
                    9: ["user_id", "extra", "timestamp"],
                    13: ["peer_id", "local_id"],
                    14: ["peer_id", "local_id"],
                    51: ["chat_id", "self"],
                    52: ["type_id", "peer_id", "info"],
                    61: ["user_id", "flags"],
                    62: ["user_id", "chat_id"],
                    70: ["user_id", "call_id"],
                    80: ["count"],
                    114: ["peer_id", "sound", "disabled_until"]}
    for i in range(len(updates)):
        event_key = event_id = updates[i][0]
        if event_id in event_types:
            event_key = event_types[event_id]
        ev = updates[i][1:]
        event = {"type": event_key, "object": {"updates": ev}}
        if event_id in event_schema:
            schema = event_schema[event_id][:]
            if event_id in [4, 5] and ev[2] < 2 * 10 ** 9:
                schema.remove("from_id")
            for j in range(len(schema)):
                key = schema[j]
                if j >= len(updates[i]) - 1:
                    break
                event["object"][key] = ev[j]
            if event_id in [8, 9]:
                event["object"]["user_id"] = -event["object"]["user_id"]
        updates[i] = event
    return updates


def check_id(who):
    try:
        return int(who)
    except:
        pass
    if type(who) == str and who:
        if '[' in who and "|" in who:
            who = re.search(r"\[[a-z]+\d+\|", who).group()[1:-1]
        who = who.replace('@', '').replace('https://', '').replace('vk.com/', '')
        obj = Api('utils.resolveScreenName', screen_name=who, silent=silence).content
        if not obj: return 0
        who = obj['object_id']
        if who:
            if obj['type'] != "user":
                return -who
    if who is None: return 0
    return who


def waiter(current_message, token=None):
    if token is None:
        token = auth.default_token
    sample_data = {'text': 'Message_text',
                   'peer_id': 0,
                   'from_id': 0,
                   'id': 0,
                   'fwd_messages': 0}
    current_message += 1
    while True:
        message_data = Api('messages.getById', message_ids=current_message, silent=True, token=token)
        while not message_data.success:
            if 'Too many requests' in message_data.content['error_msg']:
                time.sleep(0.05)
            elif any(error in message_data.content['error_msg'].lower() for error in ['flood', 'access']):
                print('Waiter Auth Error: ' + message_data.content['error_msg'])
                return None
            message_data = Api('messages.getById', message_ids=current_message, silent=True, token=token)
        if message_data.content['items']:
            message_data = message_data.content['items'][0]
            send.destination = message_data['peer_id']
            send.forward = message_data['id']
            if message_data['from_id'] == waiter.ignore:
                current_message += 1
                continue
            return message_data


def start(token=None):
    if token is None:
        token = auth.default_token
    message = Api('messages.getConversations', count=1, silent=True, token=token)
    if message.success:
        print('Успешно авторизован.')
        return int(message.content['items'][0]['last_message']['id'])
    print('Ошибка: ' + message.content['error_msg'])
    return 0


def send(message='', sticker=None, attach=None, forward=None, peer=None, token=None, **params):
    if not token:
        token = auth.default_token
    if not peer:
        peer = send.destination
    elif type(peer) == str:
        peer = check_id(peer)
    if forward == True:
        forward = send.forward
    return Api('messages.send', message=str(message), forward_messages=forward, attachment=attach,
               peer_id=peer, sticker_id=sticker, token=token, **params)


send.forward = 0
send.destination = 0


def users_get(who=None, fields='', token=None, **params):
    if not token:
        token = auth.default_token
    if who:
        if not (type(who) == int or ',' in who) and who:
            who = check_id(who)
    return Api('users.get', user_ids=who, fields=fields, token=token, **params)


def check_token(token=None):
    if token is None:
        token = auth.default_token
    permissions = ['notify', 'friends', 'photos', 'audio', 'video', '',  'stories', 'pages', '', '', 'link', 'status', 'notes',
                   'messages', 'wall', '', 'ads', 'offline', 'docs', 'groups', 'notifications', 'stats', '',
                   'email', '', 'market']
    request = Api('account.getAppPermissions', token=token, silent=True)
    if request.success:
        get_token = ('0000000000000000000000000000'+str(bin(request.content))[2:])[-28:]
        return [i for i in permissions if int(get_token[-permissions.index(i)])]
    return []


def use(name):
    name += ".py"
    print("Включение модуля " + name)
    with open(name, 'rb') as file:
        exec(compile(file.read(), name, 'exec'), globals())


class Data:
    def __init__(self, name):
        self.path = data_path + name + '.json'
        if exists(self.path):
            self.read()
        else:
            self.content = {}
            self.write()

    def __repr__(self):
        return json.dumps(self.content)

    def read(self):
        try:
            with open(self.path) as file:
                self.content = json.load(file)
                return self.content
        except:
            self.content = {}
            return 1

    def write(self):
        try:
            with open(self.path, 'w') as file:
                json.dump(self.content, file)
        except:
            return 2

    def __call__(self, obj=None):
        self.content = obj
        return self.write()

    def get(self):
        return self.content


waiter.ignore = 0
auth.default_token = None
#last_v = update(get=True)
#if version != last_v:
#    need_update = "Доступна версия {0}".format(last_v)
#else:
#    need_update = "Установлена последняя версия"
#print('vkPy {0} ({1})'.format(version, need_update))
