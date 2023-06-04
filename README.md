# pyscord-storage | ![Uptime Robot status](https://img.shields.io/uptimerobot/status/m788953682-d9a508d14b27c021c836b4aa?style=flat-square) ![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m788953682-d9a508d14b27c021c836b4aa?style=flat-square)

Free unlimited file hosting 😁👍

---

## API

- [Upload From URL](https://discord-storage.animemoe.us/api/upload-from-url/)
- [Upload From File](https://discord-storage.animemoe.us/api/upload-from-file/)

---

## Usage

```python
import pyscord_storage

result = pyscord_storage.upload_from_file("path/to/your.file")

print(result)
```

```python
import pyscord_storage

result = pyscord_storage.upload_from_url("waifu.jpg","https://github.com/animemoeus/pyscord-storage/raw/master/tests/temp/takagi.png")

print(result)
```

---

## About

- Max upload file size limit is ~~[8MB](https://support.discord.com/hc/en-us/community/posts/360031101592-Increase-max-file-size-for-free-accounts)~~ [25MB](https://twitter.com/discord/status/1645522780337885184) 🥳🎉.
- media.discordapp.net & cdn.discordapp.com. [Click here for detail](https://www.reddit.com/r/discordapp/comments/e8lgj2/mediadiscordappnet_cdndiscordappcom/).
- proxy_url. [Click here for detail](https://www.reddit.com/r/discordapp/comments/f1ixly/.discord_adding_lower_width_and_height_to_linked/).
- How long my Discord file link will work? [Click here for detail](https://support.discord.com/hc/en-us/community/posts/360061593771-Privacy-for-CDN-attachements).

---

## Increase Upload Limit

- I don't know if this will work, but I think if the server gets a boost, we can increase the upload limit up to 50 MB or 100MB.
- [https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ-](https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ-)
- Discord Server [https://discord.gg/kZuWeKzgkq](https://discord.gg/kZuWeKzgkq)

### Example Implementation

- <https://api.animemoe.us/waifu/>
- <https://waifu.animemoe.us/>
