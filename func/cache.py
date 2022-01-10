import json
import random


def get_random_member(guild_id, member_id):
    with open('./db/members.json') as f:
        data = json.load(f)
    if guild_id in data.keys():
        members = data[guild_id]
        if member_id in members:
            members.remove(member_id)
            if len(members) > 0:
                return random.choice(members)


def update_members_list(guild_id, member_id):
    with open('./db/members.json') as f:
        data = json.load(f)

    if not guild_id in data.keys():
        data[guild_id] = []
    if not member_id in data[guild_id]:
        data[guild_id].append(member_id)

    with open('./db/members.json', 'w+') as f:
        json.dump(data, f, indent=4)


def remove_member(guild_id, member_id):
    with open('./db/members.json') as f:
        data = json.load(f)

    if guild_id in data.keys():
        if member_id in data[guild_id]:
            data[guild_id].remove(member_id)

            with open('./db/members.json', 'w') as f:
                json.dump(data, f, indent=4)

            return True

    return False
