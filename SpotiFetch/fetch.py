from SpotiFetch.helpers import *
from SpotiFetch.colors import colors
import random
from rich import print

def fetch_profile(colors, spotify_obj, term='short_term'):
    
    user = get_current_user_info(spotify_obj)

    '''
    Currently Playing is handled differently than any of the others since
    it's the only function that returns a None value
    '''
    current = get_currently_playing_stats(spotify_obj)
    if current is None:
        current = "No currently playing track"
    else:
        current = f"{current['track_name']} - {current['artist_name']}"

    recent = get_user_recently_played(spotify_obj)
    track = get_user_top_tracks(spotify_obj, term)[0]
    artist = get_user_top_artists(spotify_obj, term)[0]
    
    return f"[{colors['colorOne']}]USER[/{colors['colorOne']}]            [{colors['fg']}]{user}[/{colors['fg']}]", \
           f"[{colors['colorTwo']}]NOW PLAYING[/{colors['colorTwo']}]     [{colors['fg']}]{current}[/{colors['fg']}]", \
           f"[{colors['colorThree']}]RECENT TRACK[/{colors['colorThree']}]    [{colors['fg']}]{recent['track_name']} - {recent['artist_name']}[/{colors['fg']}]", \
           f"[{colors['colorFour']}]TOP TRACK[/{colors['colorFour']}]       [{colors['fg']}]{track['track_name']} - {track['artist_name']}[/{colors['fg']}]", \
           f"[{colors['colorFive']}]TOP ARTIST[/{colors['colorFive']}]      [{colors['fg']}]{artist}[/{colors['fg']}]"

def fetch_top_tracks(colors, spotify_obj, term='short_term'):

    top_tracks = get_user_top_tracks(spotify_obj, term)

    return f"[{colors['colorOne']}]{top_tracks[0]['track_name'].upper()} - {top_tracks[0]['artist_name'].upper()}[/{colors['colorOne']}]", \
           f"[{colors['colorTwo']}]{top_tracks[1]['track_name'].upper()} - {top_tracks[1]['artist_name'].upper()}[/{colors['colorTwo']}]", \
           f"[{colors['colorThree']}]{top_tracks[2]['track_name'].upper()} - {top_tracks[2]['artist_name'].upper()}[/{colors['colorThree']}]", \
           f"[{colors['colorFour']}]{top_tracks[3]['track_name'].upper()} - {top_tracks[3]['artist_name'].upper()}[/{colors['colorFour']}]", \
           f"[{colors['colorFive']}]{top_tracks[4]['track_name'].upper()} - {top_tracks[4]['artist_name'].upper()}[/{colors['colorFive']}]" 

def fetch_top_artists(colors, spotify_obj, term='short_term'):

    top_artists = get_user_top_artists(spotify_obj, term)

    return f"[{colors['colorOne']}]{top_artists[0].upper()}[/{colors['colorOne']}]", \
           f"[{colors['colorTwo']}]{top_artists[1].upper()}[/{colors['colorTwo']}]", \
           f"[{colors['colorThree']}]{top_artists[2].upper()}[/{colors['colorThree']}]", \
           f"[{colors['colorFour']}]{top_artists[3].upper()}[/{colors['colorFour']}]", \
           f"[{colors['colorFive']}]{top_artists[4].upper()}[/{colors['colorFive']}]" 

def main(colorscheme="catppuccin", random_color=True, category='profile'):
    Spotipy = create_spotify("user-read-currently-playing user-top-read user-read-recently-played user-read-private")
    
    theme = colors[colorscheme]
    if not random_color:
        logo_color = theme['colorFour']
    else:
        val_list = list(theme.values())
        val_list.pop(5)
        logo_color = random.choice(val_list)

    if category == 'top_tracks':
        field_one, field_two, field_three, field_four, field_five = fetch_top_tracks(theme, Spotipy)
    elif category == 'top_artists':
        field_one, field_two, field_three, field_four, field_five = fetch_top_artists(theme, Spotipy)
    else : 
        field_one, field_two, field_three, field_four, field_five = fetch_profile(theme, Spotipy)

    
    new_art = f"      [{logo_color}]______[/{logo_color}]" \
              f"\n   [{logo_color}];;        ;;[/{logo_color}]" \
              f"\n [{logo_color}];;            ;;[/{logo_color}]      {field_one}" \
              f"\n[{logo_color}];;   _..**.._   ;;[/{logo_color}]     {field_two}" \
              f"\n[{logo_color}];;   _..**.._   ;;[/{logo_color}]     {field_three}" \
              f"\n[{logo_color}];;   _..**.._   ;;[/{logo_color}]     {field_four}" \
              f"\n [{logo_color}];;            ;;[/{logo_color}]      {field_five}" \
              f"\n   [{logo_color}];;        ;;[/{logo_color}]" \
              f"\n      [{logo_color}]------[/{logo_color}]" \

    print(new_art)

if __name__ == "__main__":
    main()