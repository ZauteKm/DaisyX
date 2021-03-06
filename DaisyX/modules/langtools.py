# Copyright (C) 2021 TeamDaisyX


# This file is part of Daisy (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from google_trans_new import google_translator

from DaisyX.services.events import register

API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


@register(pattern="^/tr ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply(
            "`/tr <LanguageCode>` as reply to a message or `/tr <LanguageCode> | <text>`"
        )
        return
    text = text.strip()
    lan = lan.strip()
    translator = google_translator()
    try:
        translated = translator.translate(text, lang_tgt=lan)
        after_tr_text = translated
        detect_result = translator.detect(text)
        output_str = ("**TRANSLATED Succesfully** from {} to {}\n\n" "{}").format(
            detect_result[0], lan, after_tr_text
        )
        await event.reply(output_str)
    except Exception as exc:
        await event.reply(str(exc))
