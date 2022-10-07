```
import json    

def getObjects():
   objects = ...
   return JsonResponse(json.loads(objects))
   ```