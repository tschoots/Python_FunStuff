import soco
from soco.core import SoCo



def main():

    print ("Sonos players:")
    zone_list = list(soco.discover())
    for zone in zone_list:
        print (zone.player_name)

    zone_list[0].play_uri('http://ia801402.us.archive.org/20/items/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy.mp3')
    #zone_list[0].play_uri('https://www.youtube.com/watch?v=u1OyF1Gkz-A')



if __name__ == "__main__":
    main()