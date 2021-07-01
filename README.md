# pyscord-storage

Upload file to the Discord server

---

### Installation

```
pip install pyscord-storage --upgrade
```

### Example

```python
import pyscord_storage

filename = 'ynm.jpg'
url = 'https://github.com/animemoeus/pyscord-storage/raw/master/sample.jpg'


data = pyscord_storage.upload(filename,url)
```

### Result

```
{
    'status': 200,
    'data':
        {
            'id': '860049950065819658',
            'filename': 'ynm.jpg',
            'size': 130407,
            'url': 'https://cdn.discordapp.com/attachments/858938620425404426/860049950065819658/ynm.jpg',
            'proxy_url': 'https://media.discordapp.net/attachments/858938620425404426/860049950065819658/ynm.jpg',
            'width': 537,
            'height': 954,
            'content_type': 'image/jpeg'
        }
}
```

### About

- Max upload size limit is 8MB. [Click here for detail](https://support.discord.com/hc/en-us/community/posts/360031101592-Increase-max-file-size-for-free-accounts).
- url vs proxy_url. [Click here for detail](https://www.reddit.com/r/discordapp/comments/e8lgj2/mediadiscordappnet_cdndiscordappcom/).
- proxy_url. [Click here for detail](https://www.reddit.com/r/discordapp/comments/f1ixly/.discord_adding_lower_width_and_height_to_linked/)
- Attachments URL. [Click here for detail](https://support.discord.com/hc/en-us/community/posts/360061593771-Privacy-for-CDN-attachements).

### Example Implementation

- https://api.animemoe.us/waifu/
- https://waifu.animemoe.us/
