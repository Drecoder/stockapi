from django.urls import path
from . import views

urlpatterns = [
    path("api/stock", views.stock_quote),
    path("api/cik/<str:symbol>", views.cik_lookup),
    path("api/edgar/latest-filing/<str:cik>", views.latest_filing),
    path("macro/<str:series_id>", views.macro_series),

    path("api/watchlist", views.watchlist_get),
    path("api/watchlist", views.watchlist_add),  # POST same URL
    path("api/watchlist/<str:old_symbol>", views.watchlist_update),  # PUT
    path("api/watchlist/<str:symbol>", views.watchlist_delete),      # DELETE

    path("api/gemini/summary", views.gemini_summary),
    path("api/gemini/analysis", views.gemini_analysis),
]
