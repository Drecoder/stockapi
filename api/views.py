import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.yahoo_service import get_stock_quote
from .services.sec_service import get_latest_filing
from .services.fred_service import get_fred_series
from .services.gemini_service import generate_watchlist_summary, generate_stock_analysis

try:
    with open("scripts/cik-map.json") as f:
        CIK_MAP = json.load(f)
except Exception as e:
    print(f"❌ Failed to load cik-map.json: {e}")
    CIK_MAP = {}

WATCHLIST = []

def stock_quote(request):
    symbol = request.GET.get("symbol")
    if not symbol:
        return JsonResponse({"error": "Symbol query parameter is required"}, status=400)
    try:
        return JsonResponse(get_stock_quote(symbol))
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def cik_lookup(request, symbol):
    cik = CIK_MAP.get(symbol.upper())
    if not cik:
        return JsonResponse({"error": f"CIK not found for symbol: {symbol}"}, status=404)
    return JsonResponse({"symbol": symbol.upper(), "cik": cik})

def latest_filing(request, cik):
    try:
        data = get_latest_filing(cik)
        if not data:
            return JsonResponse({"error": "No recent accession number found."}, status=404)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def macro_series(request, series_id):
    try:
        return JsonResponse(get_fred_series(series_id))
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def watchlist_get(request):
    return JsonResponse(WATCHLIST, safe=False)

@csrf_exempt
def watchlist_add(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    body = json.loads(request.body)
    symbol = body.get("symbol")
    if not symbol:
        return JsonResponse({"error": "Symbol is required"}, status=400)
    if symbol not in WATCHLIST:
        WATCHLIST.append(symbol)
    return JsonResponse({"success": True})

@csrf_exempt
def watchlist_update(request, old_symbol):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT required"}, status=405)
    body = json.loads(request.body)
    new_symbol = body.get("newSymbol")
    try:
        idx = WATCHLIST.index(old_symbol)
    except ValueError:
        return JsonResponse({"error": "Symbol not found"}, status=404)
    WATCHLIST[idx] = new_symbol
    return JsonResponse({"success": True})

@csrf_exempt
def watchlist_delete(request, symbol):
    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE required"}, status=405)
    try:
        WATCHLIST.remove(symbol)
    except ValueError:
        return JsonResponse({"error": "Symbol not in list"}, status=404)
    return JsonResponse({"success": True})

@csrf_exempt
def gemini_summary(request):
    body = json.loads(request.body)
    symbols = body.get("symbols")
    if not isinstance(symbols, list):
        return JsonResponse({"error": "Invalid request: symbols required"}, status=400)
    return JsonResponse({"summary": generate_watchlist_summary(symbols)})

@csrf_exempt
def gemini_analysis(request):
    body = json.loads(request.body)
    symbols = body.get("symbols")
    if not isinstance(symbols, list):
        return JsonResponse({"error": "Invalid request: symbols required"}, status=400)
    return JsonResponse({"analysis": generate_stock_analysis(symbols)})
