import folium
import pandas as pd
import polyline
import requests
from django.shortcuts import render


def base_map(request):
    # Make your map object
    main_map = folium.Map(location=[18.77, -19.16], zoom_start=3)  # Create base map
    main_map_html = main_map._repr_html_()  # Get HTML for website
    context = {
        'main_map': main_map_html
    }

    return render(request, 'index.html', context)


def connected_map(request):
    # Make your map object
    main_map = folium.Map(location=[18.77, -19.16], zoom_start=3)  # Create base map
    user = request.user  # Pulls in the Strava User data
    strava_login = user.social_auth.get(provider='strava')  # Strava login
    access_token = strava_login.extra_data['access_token']  # Strava Access token
    activites_url = 'https://www.strava.com/api/v3/athlete/activities'

    # Get activity data
    header = {'Authorization': 'Bearer ' + str(access_token)}
    activity_df_list = []
    for n in range(5):  # Change this to be higher if you have more than 1000 activities
        param = {'per_page': 200, 'page': n + 1}

        activities_json = requests.get(activites_url, headers=header, params=param).json()
        if not activities_json:
            break
        activity_df_list.append(pd.json_normalize(activities_json))

    # Get polyline data
    activities_df = pd.concat(activity_df_list)
    activities_df = activities_df.dropna(subset=['map.summary_polyline'])
    activities_df['polylines'] = activities_df['map.summary_polyline'].apply(polyline.decode)

    # Plot polylines onto Folium Map
    for pl in activities_df['polylines']:
        if len(pl) > 0:  # Ignore polylines with length zero
            folium.PolyLine(locations=pl, color='red').add_to(main_map)

    # Return HTML version of map
    main_map_html = main_map._repr_html_()  # Get HTML for website
    context = {
        'main_map': main_map_html
    }

    return render(request, 'index.html', context)
