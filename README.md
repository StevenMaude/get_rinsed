# get_rinsed

Like [`get_iplayer`](https://github.com/dinkypumpkin/get_iplayer) but
for Rinse FM podcasts.

(I wrote a downloader for Rinse FM podcasts ages ago, then they
redesigned their site, breaking it entirely. Hopefully this one will
work for longer.)

## Desirable features
* Search for artist, show all shows, option to download show(s)
* Track what's been downloaded; force override to redownload
* Download resuming

## Quick research
Link: http://rinse.fm/podcasts/

Filenames are `ArtistDDMMYY.mp3` (Artist can also be show name instead.)

### Sample data
Infinite scrolling site; data obtained by e.g.
http://rinse.fm/podcasts/?page=2

Currently goes to a maximum page number of 19.

Higher page numbers work, but return no podcasts (so easy way to check
when we're done).

In `sample_data`:
* `page_with_podcasts.html` contains download links;
* `page_with_no_podcasts.html` is an empty podcast page (retrieved by
grabbing page 1000).

### xPath
Download links: `//div[@class="download icon"]/a/@href`

Time of broadcast: `//div[@class="date monobold grey px11 mt4"]`
