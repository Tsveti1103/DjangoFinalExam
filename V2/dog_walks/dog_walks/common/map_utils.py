import folium
from dog_walks.common.utils import get_all_places
from folium.plugins import Search, LocateControl


# ?next={{ request.path }}
def create_map():
    # f = folium.Figure(width=1200, height=700)
    the_map = folium.Map(location=[42.76686028599908, 25.238436899999996], zoom_start=8, tiles='OpenStreetMap') \
        # .add_to(f)
    places = get_all_places()
    all_places = folium.FeatureGroup(name='Всички')
    night_places = folium.plugins.FeatureGroupSubGroup(all_places, name='Нощувки')
    eat_places = folium.plugins.FeatureGroupSubGroup(all_places, name='Заведения за хранене')
    walk_places = folium.plugins.FeatureGroupSubGroup(all_places, name='Места за разходка')
    for place in places:
        marker = folium.Marker(
            location=[place.latitude, place.longitude],
            tooltip=place.name,
            popup=folium.Popup(
                f"<a href='http://127.0.0.1:8000/places/{place.PLACE_TYPE}/{place.pk}/details/' target='_blank'>{place.name}</a>",
                min_width=50, max_width=300),
            icon=folium.Icon(),
            name=place.name,
        )
        if place.PLACE_TYPE == 'night':
            night_places.add_child(marker)
            marker.icon.options['prefix'] = 'fa'
            marker.icon.options['icon'] = 'bed'
            marker.icon.options['markerColor'] = 'lightblue'
            if place.dog_fee:
                marker.icon.options['iconColor'] = 'yellow'
        elif place.PLACE_TYPE == 'eat':
            eat_places.add_child(marker)
            marker.icon.options['icon'] = 'glyphicon glyphicon-cutlery'
            marker.icon.options['markerColor'] = 'lightred'
        elif place.PLACE_TYPE == 'walk':
            walk_places.add_child(marker)
            marker.icon.options['prefix'] = 'fa'
            marker.icon.options['icon'] = 'tree'
            marker.icon.options['markerColor'] = 'green'
            if place.dogs_are_welcome == 'NO':
                marker.icon.options['iconColor'] = 'red'
            elif place.dogs_are_welcome == 'MAYBE':
                marker.icon.options['iconColor'] = 'yellow'

    the_map.add_child(all_places)
    the_map.add_child(eat_places)
    the_map.add_child(night_places)
    the_map.add_child(walk_places)
    Search(
        search_zoom=10,
        layer=all_places,
        search_label="name",
        placeholder='Търси място',
        collapsed=False,
    ).add_to(the_map)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Satellite',
        overlay=False,
        control=True
    ).add_to(the_map)
    LocateControl(keepCurrentZoomLevel=True, strings={
        'title': "Моето местоположение"}).add_to(the_map)
    folium.LayerControl().add_to(the_map)
    return the_map
