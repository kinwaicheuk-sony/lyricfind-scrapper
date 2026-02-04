import asyncio
from aiohttp import ClientSession
from LyricsFindScrapper import Search, Track

async def test():
    async with ClientSession() as session:
        client = Search(session=session, teritory="us")

        tracks: list[Track] = await client.get_tracks(query="Lemon")

        for track in tracks:
            print(f"\nTrying: {track.artist} - {track.title}")

            try:
                song_data = await client.get_lyrics(track=track)
            except AttributeError:
                print("❌ Lyrics not available (blocked or missing)")
                continue
            except Exception as e:
                print(f"❌ Other error: {e}")
                continue

            if not song_data or not song_data.lyrics:
                print("❌ Empty lyrics")
                continue

            print("✅ LYRICS FOUND")
            print(song_data.lyrics[:500])  # preview only

asyncio.run(test())
