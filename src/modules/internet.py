import http


class Internet:
    def __init__(self):
        pass

    @staticmethod
    def withInternetConnected():
        print("""@VER:1.1 withInternetConnected""")
        conn = http.client.HTTPSConnection("8.8.8.8", timeout=5)
        try:
            conn.request("HEAD", "/")
            returnValue = True
        except Exception:
            returnValue = False
        finally:
            conn.close()
        return returnValue