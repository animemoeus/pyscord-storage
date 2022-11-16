import json,orjson,pyscord_storage,asyncio

print(
    json.dumps(
        pyscord_storage.upload(
            "test.jpg",
            "https://cdn.discordapp.com/attachments/858938620425404426/980409229393395722/waifu-animemoeus.jpg",
        ),
        indent=1,
    )
)
print(orjson.dumps(asyncio.run(pyscord_storage.async_upload("test.jpg","https://cdn.discordapp.com/attachments/858938620425404426/980409229393395722/waifu-animemoeus.jpg",),indent=1,)))
