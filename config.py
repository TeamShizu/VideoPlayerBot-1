"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "7635212"))
API_HASH = getenv("API_HASH", "d2ff99e45bef6b7f94628277f888a644")
BOT_TOKEN = getenv("BOT_TOKEN", "1990794700:AAE_QAKNHbZB9RQoCmFPDGHErEqoWtUHq0Q")
SESSION_STRING = getenv("SESSION_STRING", "BQBM24AXRGME-p0tcr5j5hxFw3wzRWf7af4CrQHqdS1zGtzopjn3E6_3t8Um9uIwjsFAZeU10JaXyQ15Anye-N-aK8h-0LwSNeuPfbqW2Eq8qSsnuVLZzV4ngR903vI1FhBycvO95g8Wxst0yo0TjjSxxEavAfkPz6y3TZuAmRUNBZe0OU98CTwcTJwMM44aZ8qSUDFvne9_JWkfzDhHA6Xe39-SnWWaDPNAUwy6Myxb1fFXNW6Ay0UY72hRt085P0_-EWsHwd6qQ7VnAAjkCqzUKYtHUKVun0f8uk-3Mq-qpBQxKKugPTz-KM10c9zAN-k7heLBVbP-iljglDhCHaTjabm5JwA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kingdom_family")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kingdom_family_chanel")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kingdom music")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","1985638127").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "Hi there i am kingdom family music play bot")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
