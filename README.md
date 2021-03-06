# pyscord-storage

Free unlimited file hosting using Discord server

---

## Installation

```bash
pip install pyscord-storage --upgrade
```

## Example

## Code

```python
import pyscord_storage

filename = "example.jpg"
file = "https://cdn.discordapp.com/attachments/858938620425404426/980409229393395722/waifu-animemoeus.jpg"
# file = '/path/to/your/file'

data = pyscord_storage.upload(filename, file)
```

### Result

```json
{
  "status": 200,
  "data": {
    "id": "860049950065819658",
    "filename": "ynm.jpg",
    "size": 130407,
    "url": "https://cdn.discordapp.com/attachments/858938620425404426/860049950065819658/ynm.jpg",
    "proxy_url": "https://media.discordapp.net/attachments/858938620425404426/860049950065819658/ynm.jpg",
    "width": 537,
    "height": 954,
    "content_type": "image/jpeg"
  }
}
```

### API

- [Upload From URL](https://discord-storage.animemoe.us/upload-from-url/)
- [Upload From File](https://discord-storage.animemoe.us/upload-from-file/)

### About

- Max upload size limit is 8MB. [Click here for detail](https://support.discord.com/hc/en-us/community/posts/360031101592-Increase-max-file-size-for-free-accounts).
- media.discordapp.net & cdn.discordapp.com. [Click here for detail](https://www.reddit.com/r/discordapp/comments/e8lgj2/mediadiscordappnet_cdndiscordappcom/).
- proxy_url. [Click here for detail](https://www.reddit.com/r/discordapp/comments/f1ixly/.discord_adding_lower_width_and_height_to_linked/).
- How long my Discord file link will work? [Click here for detail](https://support.discord.com/hc/en-us/community/posts/360061593771-Privacy-for-CDN-attachements).

### Increase Upload Limit

- I don't know if this will work, but I think if the server gets a boost, we can increase the upload limit up to 50 MB or 100MB.
- [https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ-](https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ-)
- Discord Server [https://discord.gg/kZuWeKzgkq](https://discord.gg/kZuWeKzgkq)

### Example Implementation

- <https://api.animemoe.us/waifu/>
- <https://waifu.animemoe.us/>
