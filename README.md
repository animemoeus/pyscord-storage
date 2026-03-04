# pyscord-storage | ![Uptime Robot status](https://img.shields.io/uptimerobot/status/m788953682-d9a508d14b27c021c836b4aa?style=flat-square) ![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m788953682-d9a508d14b27c021c836b4aa?style=flat-square)

Because paying for actual file storage is for people with money. Why use S3, GCS, or literally any purpose-built storage service when you can just... use Discord? A chat app. For teenagers. As your CDN.

You're welcome.


## Refresh Expired URL

Discord, in its infinite wisdom, decided that CDN URLs should expire. Because nothing says "reliable file hosting" like links that stop working. Anyway, here's how you unfail them:

```text
https://bypass-discord.animemoe.us/DISCORD_FILE_URL_HERE
```
```text
https://bypass-discord.animemoe.us/https://media.discordapp.net/attachments/858938620425404426/1478701777837621259/animemoeus-waifu.jpg
```

Groundbreaking infrastructure, truly.


## Installation

Shockingly straightforward:

```bash
pip install pyscord-storage
```

Congratulations. You are now a cloud architect.


## Usage

Upload a local file, like a person who has completely given up on conventional DevOps:

```python
import pyscord_storage

result = pyscord_storage.upload_from_file("path/to/your.file")

print(result)
```

Or, if you're feeling extra chaotic, make the backend fetch a file from a URL for you:

```python
import pyscord_storage

result = pyscord_storage.upload_from_url("waifu.jpg", "https://github.com/animemoeus/pyscord-storage/raw/master/tests/temp/takagi.png")

print(result)
```

Both functions return a dict. You're not getting a proper SDK response object. This is Discord storage. Manage your expectations accordingly.


## CLI

For those who prefer their existential dread served directly in the terminal:

```bash
pip install pyscord-storage
```

```bash
# Upload a local file
pyscord-storage --file path/to/your.file

# Upload from a remote URL
pyscord-storage --url https://example.com/your.file
```

On success, it prints the URL. On failure, it prints the error to stderr and exits with code 1. Professional.


## Async Support

Yes, we also have async versions — because if you're going to do something ridiculous, you might as well do it non-blockingly.

```python
import asyncio
import pyscord_storage

async def main():
    result = await pyscord_storage.async_upload_from_file("path/to/your.file")
    print(result)

asyncio.run(main())
```

```python
import asyncio
import pyscord_storage

async def main():
    result = await pyscord_storage.async_upload_from_url("waifu.jpg", "https://github.com/animemoeus/pyscord-storage/raw/master/tests/temp/takagi.png")
    print(result)

asyncio.run(main())
```


## About

- Max upload file size is ~~[8MB](https://support.discord.com/hc/en-us/community/posts/360031101592-Increase-max-file-size-for-free-accounts)~~ [25MB](https://twitter.com/discord/status/1645522780337885184) — an upgrade celebrated with an enthusiasm that says a lot about the alternatives we were previously working with.
- There are two CDN domains: `media.discordapp.net` and `cdn.discordapp.com`. [Click here for the explanation](https://www.reddit.com/r/discordapp/comments/e8lgj2/mediadiscordappnet_cdndiscordappcom/) you didn't ask for but definitely need.
- There's also a `proxy_url` thing. [Here's more than you wanted to know about it](https://www.reddit.com/r/discordapp/comments/f1ixly/.discord_adding_lower_width_and_height_to_linked/).
- Discord CDN links expire. As in, your files disappear. [More details here](https://support.discord.com/hc/en-us/community/posts/360061593771-Privacy-for-CDN-attachements), in case you'd like to really sit with that fact before deploying to production.


## Increase Upload Limit

Here's the part where I tell you that to get more storage out of a chat app, you need to pay to "boost" a Discord server. No, I'm not joking.

- Boosting may push the limit to 50MB or 100MB. Allegedly.
- [Discord Server Boosting FAQ](https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ-)
- Join our Discord Server (of course there's a Discord server): [https://discord.gg/kZuWeKzgkq](https://discord.gg/kZuWeKzgkq)


## Example Implementations

These are real. Deployed. In the wild.

- <https://api.animemoe.us/waifu/>
- <https://waifu.animemoe.us/>
