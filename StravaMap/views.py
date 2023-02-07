from django.shortcuts import render
import folium

# Create your views here.
def base_map(request):
    # Make your map object
    main_map = folium.Map(location=[-8.0259, -34.9107], zoom_start=12) # Create base map
    main_map_html = main_map._repr_html_() # Get HTML for website

    context = {
        'main_map': main_map_html
    }
    return render(request, 'index.html', context)
