# import requests
# import json
# from elasticsearch import Elasticsearch
# import base64


# ES_URL = "http://dev01.animaker.com:65530/"

# def connect_elasticsearch(url):
#         es = None

#         es = Elasticsearch(url)

#         if es.ping():
#             print('Yay Connect')
#         else:
#             print('Awww it could not connect!')
#         return es


# es = connect_elasticsearch(ES_URL)

# query =  {
#                "query": {
#                   "bool": {
#                      "must": [{
#                      "match": {
#                            "type": "BG"
#                      }
#                      }],
#                      "must_not": [{
#                      "exists": {
#                            "field": "subtype"
#                      }
#                      }]
#                   }
#                },
#                "from" : 0,
#                "size": 1000
# }
# res = es.search(index="animadminlibrary",body=query)

# from datetime import datetime, timedelta, time
# from dateutil.relativedelta import relativedelta

# def leapyear(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 days = 29
#             else:
#                 days = 28
#         else:
#             days = 29
#     else:
#         days = 28
#     return days

# def getrange(substart, subend):
#     # get the start date and end date of current subscription
#     # counts will get reset for each month even for yearly plans
#     exportdate = datetime.utcnow()
#     a_month = relativedelta(months=1)
#     # r = relativedelta.relativedelta(exportdate, substart)
#     # monthdiff = r.months + (r.years * 12)
#     # months = (substart.month + monthdiff) % 12
#     # startdate = datetime.utcnow().replace(month = months, day = substart.day, hour = substart.hour, minute = substart.minute)
#     # enddate = startdate + timedelta(days = 30)
#     if substart.day <= exportdate.day:
#         try:
#             startdate = datetime.utcnow().replace(day = substart.day, hour = substart.hour, minute = substart.minute, second = substart.second)
#         except ValueError:
#             if datetime.utcnow().month == 2:
#                 day = leapyear(datetime.utcnow().year)
#             else:
#                 day = 30
#             startdate = datetime.utcnow().replace(day = day, hour = substart.hour, minute = substart.minute, second = substart.second)
#         enddate = startdate + a_month
#     else:
#         try:
#             enddate = datetime.utcnow().replace(day = substart.day, hour = substart.hour, minute = substart.minute, second = substart.second)
#         except ValueError:
#             if datetime.utcnow().month == 2:
#                 day = leapyear(datetime.utcnow().year)
#             else:
#                 day = 30
#             enddate = datetime.utcnow().replace(day = day, hour = substart.hour, minute = substart.minute, second = substart.second)
#         startdate = enddate - a_month
#     return startdate, enddate



prev_exported_asset_list =list(AnimtrnMarketplace.objects.values_list('assetid',flat=True).filter(assetid__in=self.project_asset_list).filter(downloaddate__lte=end,teamid=teamid,projectid = projectid,productname =settings.APP_NAME).distinct())
image_credit_used = AnimtrnMarketplace.objects.filter(source = 'ISESS',downloaddate__gte=start,downloaddate__lte=end,teamid=teamid,iscredited = 1,productname =settings.APP_NAME).distinct().count()
exclusive_image_credit_used = AnimtrnMarketplace.objects.filter(Q(source = 'ISSIG') | Q(source = 'GETTY'),downloaddate__gte=start,downloaddate__lte=end,teamid=teamid,iscredited = 1,productname =settings.APP_NAME).distinct().count()
export_credit_used = PictrnExport.objects.filter(teamid = teamid,created__gte = start,created__lte = end).count()






