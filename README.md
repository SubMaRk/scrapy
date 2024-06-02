# scrapy
Download any Manga Manhwa Manhua from online website with Custom Extension.

# Installation

To install the required dependencies for this project, follow these steps:

1. **Clone the Repository:**

```bash
git clone https://github.com/SubMaRk/scrapy.git
cd scrapy
```
2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Enjoy!**


# Usage

```bash
python manga_downloader.py [-h] [--murl MURL] [--start START] [--end END] [--output OUTPUT] [--workthreads WORKTHREADS] [--imagethreads IMAGETHREADS] [--wait WAIT] [--list] [--debug]
```

**Arguments**

- `--help`, `-h`: display this help.
- `--murl`, `-m MURL`: Enter Manga URL to process.
- `--start`, `-s START`: Specify chapter number to start download. (default: 0)
- `--end`, `-e END`: Specify chapter number to stop download.
- `--output`, `-o OUTPUT`: Enter output path to save downloaded.
- `--workthreads`, `-t WORKTHREADS`: Enter amount of threads to run.
- `--imagethreads`, `-t IMAGETHREADS`: Enter amount of threads to download image(s).
- `--wait`, `-d WAIT`: Enter time to delay read page until loaded (In seconds; Use for images encrypted in readpage).
- `--list`, `-l`: Display Chapter list only.
- `--debug`, `-d`: Start with debug mode.

# Example

Full code

```bash
python scrapy.py -m <manga_url> -s <start> -e <end> -o <output_folder> -wt <work_threads> -it <image_threads> -d <time_delay(s)> -l -d
```

Download chapters 1 to 10 of a manga from a given URL with 4 work threads and 4 image threads:

```bash
python scrapy.py -m <manga_url> -e 10 -o <output_folder> -wt 4 -it 4
```

Display the chapter list from the specified manga URL only:

```bash
python scrapy.py -m <manga_url> -l
```

Start with debug mode

```bash
python scrapy.py -m <manga_url> -d
```

or

```bash
python scrapy.py -m <manga_url> -e 10 -o <output_folder> -wt 1 -it 4 -d
```

# Support Website

**MangaReader Template Sites**

| **No.** | **Type**  | **Domain**              |          **Name**          | **LANGUAGE** | **Status** |
|---------|-----------|-------------------------|----------------------------|--------------|------------|
|   001   |  General  | thaimanga.net           | ThaiManga                  |     Thai     |    [✅]    |
|   002   |  General  | manga689.com            | Manga689                   |     Thai     |    [✅]    |
|   003   |  General  | manga168.com            | Manga168                   |     Thai     |    [✅]    |
|   004   |  General  | tamamanga.com           | TAMAMANGA                  |     Thai     |    [✅]    |
|   005   |  General  | xn--l3c0azab5a2gta.com  | สดใสเมะ                    |     Thai     |    [✅]    |
|   006   |  General  | ped-manga.com           | Ped-Manga                  |     Thai     |    [✅]    |
|   007   |  General  | sing-manga.com          | SING-MANGA                 |     Thai     |    [✅]    |
|   008   |  General  | mangakimi.com           | MangaKimi                  |     Thai     |    [✅]    |
|   009   |  General  | reapertrans.com         | Reapertrans                |     Thai     |    [✅]    |
|   010   |  General  | dragon-manga.com        | Dragon-Manga               |     Thai     |    [✅]    |
|   011   |  General  | moodtoon.com            | moodtoon                   |     Thai     |    [✅]    |
|   012   |  General  | toomtam-manga.com       | Toomtam-Manga              |     Thai     |    [✅]    |
|   013   |  General  | miku-manga.com          | Miku-manga                 |     Thai     |    [✅]    |
|   014   |  General  | asurahunter.com         | Asurahunter                |     Thai     |    [✅]    |
|   015   |  General  | 108-manga.com           | 108-Manga                  |     Thai     |    [✅]    |
|   016   |  General  | joji-manga.com          | Joji-Manga                 |     Thai     |    [✅]    |
|   017   |  General  | spy-manga.com           | Spy-Manga                  |     Thai     |    [✅]    |
|   018   |  General  | murim-manga.com         | Murim-Manga                |     Thai     |    [✅]    |
|   019   |  General  | kumomanga.net           | kumomanga                  |     Thai     |    [✅]    |
|   020   |  General  | mangastep.com           | MANGASTEP                  |     Thai     |    [✅]    |
|   021   |  General  | hippomanga.com          | Hippomanga                 |     Thai     |    [✅]    |
|   022   |  General  | popsmanga.com           | PopsManga                  |     Thai     |    [✅]    |
|   023   |  General  | tanuki-manga.com        | Tanuki-Manga               |     Thai     |    [✅]    |
|   024   |  General  | inu-manga.com           | Inu Manga                  |     Thai     |    [✅]    |
|   025   |  General  | lami-manga.com          | Lami-Manga                 |     Thai     |    [✅]    |
|   026   |  General  | weimanga.com            | Weimanga                   |     Thai     |    [✅]    |
|   027   |  General  | slow-manga.com          | SLOW-MANGA                 |     Thai     |    [✅]    |
|   028   |  General  | makimaaaaa.com          | makimaaaaa                 |     Thai     |    [✅]    |
|   029   |  General  | kazetori-manga.com      | Kazetori Manga             |     Thai     |    [✅]    |
|   030   |  General  | flash-manga.com         | Flash-Manga                |     Thai     |    [✅]    |
|   031   |  General  | manga-za.net            | MANGA-ZA                   |     Thai     |    [✅]    |
|   032   |  General  | oremanga.net            | Oremanga                   |     Thai     |    [✅]    |
|   033   |  General  | manhwathailand.com      | Manhwa Thailand            |     Thai     |    [✅]    |
|   034   |  General  | romance-manga.com       | Romance-manga              |     Thai     |    [✅]    |
|   035   |  General  | germa-66.com            | Germa-66                   |     Thai     |    [✅]    |
|   036   |  General  | skoiiz-manga.com        | SKOIIZ-MANGA               |     Thai     |    [✅]    |
|   037   |  General  | xn--72ca2cvbi6fe9m.com  | มังงะไทย                    |     Thai     |    [✅]    |
|   038   |  General  | go-manga.com            | Go-Manga                   |     Thai     |    [✅]    |
|   039   |  General  | up-manga.com            | Up-Manga                   |     Thai     |    [✅]    |
|   040   |  General  | god-manga.com           | God-manga                  |     Thai     |    [✅]    |
|   041   |  General  | rose-manga.com          | Rose-manga                 |     Thai     |    [✅]    |
|   042   |  General  | xn--72cas2cj6a4hf4b5a8oc.com | มังงะญี่ปุ่น               |     Thai     |    [✅]    |
|   043   |  General  | seetoon.net             | SEETOON                    |     Thai     |    [✅]    |
|   044   |  General  | manga-sugoi.com         | Manga sugoi                |     Thai     |    [✅]    |
|   045   |  General  | manga-i.com             | Manga-i                    |     Thai     |    [✅]    |
|   046   |  General  | ranker-manga.com        | Ranker-Manga               |     Thai     |    [✅]    |
|   047   |  General  | manga248.com            | manga248                   |     Thai     |    [✅]    |
|   048   |  General  | haremmanga.net          | Haremmanga                 |     Thai     |    [✅]    |
|   049   |  General  | one-manga.com           | ONE-MANGA                  |     Thai     |    [✅]    |
|   050   |   Adult   | god-doujin.com          | God-Doujin                 |     Thai     |    [✅]    |
|   051   |   Adult   | doujin69.com            | Doujin69                   |     Thai     |    [✅]    |
|   052   |   Adult   | doujin-new.com          | Doujin-New                 |     Thai     |    [✅]    |
|   053   |   Adult   | oredoujin.com           | Oredoujin                  |     Thai     |    [✅]    |
|   054   |   Adult   | doujin-y.com            | Doujin-Y                   |     Thai     |    [✅]    |
|   055   |   Adult   | toonhunter.com          | Toonhunter                 |     Thai     |    [✅]    |
|   056   |   Adult   | doujinmoon.com          | Doujinmoon                 |     Thai     |    [✅]    |
|   057   |   Adult   | ecchi-doujin.com        | Ecchi-Doujin               |     Thai     |    [✅]    |
|   058   |   Adult   | doujin4u.com            | Doujin4u                   |     Thai     |    [✅]    |
|   059   |   Adult   | xn--69-uqi5m9an.com     | อิคึ69                       |     Thai     |    [✅]    |
|   060   |   Adult   | 108read.com             | 108Read                    |     Thai     |    [✅]    |
|   061   |   Adult   | ped-doujin.com          | Ped doujin                 |     Thai     |    [✅]    |
|   062   |   Adult   | eye-manga.com           | EYE-Manga                  |     Thai     |    [✅]    |
|   063   |   Adult   | manga-20.com            | Manga-20                   |     Thai     |    [✅]    |
|   064   |   Adult   | manga-yuri.com          | Manga-Yuri                 |     Thai     |    [✅]    |
|   065   |   Adult   | tora-manga.com          | Tora-manga                 |     Thai     |    [✅]    |
|   066   |   Adult   | manga-bl.com            | Manga-BL                   |     Thai     |    [✅]    |
|   067   |   Adult   | manga-yaoi.com          | Manga-Yaoi                 |     Thai     |    [✅]    |
|   068   |   Adult   | xn--72ca0fgy7cem.com    | มังงะวาย                    |     Thai     |    [✅]    |
|   069   |   Adult   | ntr-manga.com           | NTR-Manga                  |     Thai     |    [✅]    |
|   070   |   Adult   | 18ntr.com               | 18NTR                      |     Thai     |    [✅]    |
|   071   |   Adult   | godhman.net             | GODHMAN                    |     Thai     |    [✅]    |

**Madara Template Sites**

| **No.** | **Type**  | **Domain**              |          **Name**          | **LANGUAGE** | **Status** |
|---------|-----------|-------------------------|----------------------------|--------------|------------|
|   001   |  General  | nabee-manga.com         | Nabee-Manga                |     Thai     |    [✅]    |
|   002   |  General  | manga-post.com          | Manga-Post                 |     Thai     |    [✅]    |
|   003   |  General  | sixmanga.com            | Sixmanga                   |     Thai     |    [✅]    |
|   004   |  General  | snap-manga.com          | Snap-Manga                 |     Thai     |    [✅]    |
|   005   |  General  | manga-lc.net            | Manga-LC                   |     Thai     |    [✅]    |
|   006   |  General  | mangaisekaithai.com     | MangaIsekaiThai            |     Thai     |    [✅]    |
|   007   |  General  | cats-translator.com     | Cats-Translator            |     Thai     |    [✅]    |
|   008   |  General  | manga191.com            | Manga191                   |     Thai     |    [✅]    |
|   009   |  General  | rh2plusmanga.com        | RH2PlusManga               |     Thai     |    [✅]    |
|   010   |  General  | mangasuper.com          | Manga Super                |     Thai     |    [🔴]    |
|   011   |  General  | doodmanga.com           | DoodManga                  |     Thai     |    [✅]    |
|   012   |  General  | catzaa.com              | Catzaa                     |     Thai     |    [🔴]    |
|   013   |  General  | moritoon.com            | Moritoon                   |     Thai     |    [✅]    |
|   014   |  General  | nano-manga.com          | Nano-Manga                 |     Thai     |    [🔴]    |
|   015   |  General  | manga-uptocats.com      | Manga-Uptocats             |     Thai     |    [🔴]    |
|   016   |  General  | haremmanhua.com         | HaremManhua                |     Thai     |    [✅]    |
|   017   |  General  | manghaha.com            | Manghaha                   |     Thai     |    [🔴]    |
|   018   |  General  | dokimori.com            | Dokimori                   |     Thai     |    [🔴]    |
|   019   |  General  | kuro-manga.com          | Kuro-Manga                 |     Thai     |    [🔴]    |
|   020   |  General  | manhwabreakup.com       | ManhwaBreakup              |     Thai     |    [🔴]    |
|   021   |  General  | manhuabug.com           | ManhuaBug                  |     Thai     |    [✅]    |
|   022   |  General  | thaitoon.net            | Thaitoon                   |     Thai     |    [🔴]    |
|   023   |  General  | zurushin.com            | Zurushin                   |     Thai     |    [🔴]    |
|   024   |  General  | manhuathai.com          | ManhuaThai                 |     Thai     |    [✅]    |
|   025   |  General  | chocomanga.com          | ChocoManga                 |     Thai     |    [✅]    |
|   026   |  General  | wasabith.com            | WasabiTh                   |     Thai     |    [🔴]    |
|   027   |  General  | kapimanga.com           | KapiManga                  |     Thai     |    [✅]    |
|   028   |  General  | kumotran.com            | KumoTran                   |     Thai     |    [✅]    |
|   029   |  General  | manhuakey.com           | ManhuaKey                  |     Thai     |    [✅]    |
|   030   |   Adult   | doujinfast.com          | DoujinFast                 |     Thai     |    [🔴]    |
|   031   |   Adult   | doujinx-h.com           | Doujinx-H                  |     Thai     |    [🔴]    |
|   032   |   Adult   | doujinza.com            | DoujinZa                   |     Thai     |    [🔴]    |
|   033   |   Adult   | kuro-doujin.com         | Kuro-Doujin                |     Thai     |    [🔴]    |
|   034   |   Adult   | doujin-lc.net           | Doujin-LC                  |     Thai     |    [🔴]    |
|   035   |   Adult   | doujinsuki.com          | DoujinSuki                 |     Thai     |    [🔴]    |
|   036   |   Adult   | superdoujin.org         | SuperDoujin                |     Thai     |    [🔴]    |
|   037   |   Adult   | yaoi-y.com              | Yaoi-Y                     |     Thai     |    [🔴]    |
|   038   |   Adult   | ok-doujinx.com          | OK-Doujinx                 |     Thai     |    [🔴]    |

**Other Sites**

| **No.** | **Type**  | **Domain**              |          **Name**          | **LANGUAGE** | **Status** |
|---------|-----------|-------------------------|----------------------------|--------------|------------|
|   001   |  General  | loli-manga.com          | Loli Manga                 |     Thai     |    [🔴]    |
|   002   |  General  | mangasleep.com          | Manga Sleep                |     Thai     |    [🔴]    |
|   003   |  General  | kaichan.co              | Kai Chan                   |     Thai     |    [🔴]    |
|   004   |  General  | manga00.com             | Manga 00                   |     Thai     |    [🔴]    |
|   005   |  General  | toonsmanga.com          | Toons Manga                |     Thai     |    [🔴]    |