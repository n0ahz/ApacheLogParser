from django.shortcuts import render
#import apache_log_parser
from pprint import pprint
from .models import ApacheLog,Site
from log_formats.models import LogFormats
import datetime
from django.http import HttpResponse, HttpResponseRedirect

#from django.db import connection
from django.db import transaction,connection
import apache_log_parser
def create(request):
    siteObj = Site.objects.order_by("-id")
    siteList = list(siteObj)
    return render(request, 'upload_log.html', {'sites':siteList})

def parseLog(request):
    siteId = int(request.POST.get('site_id'))
    log_formatObg = LogFormats.objects.filter(site_id=siteId)
    logFormat = str(log_formatObg[0].log_format)

    #% h % l % u % t \"%r\" %>s %b
    print logFormat
    line_parser = apache_log_parser.make_parser(""+logFormat)


    fileitem=request.FILES.get('ufile')
    flag = True
    # Insert into table (r1,r2....rn) values (v1,v2,v3...vn),(v1,v2,v3...vn),(v1,v2,v3...vn)....
    strQuery = "INSERT INTO "+ str(ApacheLog._meta.db_table) +" (status,request_first_line,response_bytes_clf,remote_host,request_http_ver,request_url_port,remote_logname,request_method,site_id) VALUES "
    for line in fileitem.file:
        if(flag == True):
            strQuery += ' ('
        else:
            strQuery += ', ('

        try:
            data=line_parser(line.strip())
            pprint(data)
            break
        except apache_log_parser.LineDoesntMatchException:
            return HttpResponse("Formet Doesnt Match ......!")

        strQuery+='"'+str(data.get('status'))+'","'+str(data.get('request_first_line'))+'","'+str(data.get('response_bytes_clf'))+'","'+str(data.get('remote_host'))+'","';
        strQuery+=str(data.get('request_http_ver'))+'","'+str(data.get('request_url_port'))+'","'+str(data.get('remote_logname'))+'","'+str(data.get('request_method'))+'",'+ str(siteId) +')';
        flag = False

        #orm query
        #     db = ApacheLog(
        #         status=data.get('status'),request_first_line=data.get('request_first_line'),
        #         response_bytes_clf=data.get('response_bytes_clf'),remote_host=data.get('remote_host'),
        #         request_http_ver=data.get('request_http_ver'),request_url_port=data.get('request_url_port'),
        #         remote_logname=data.get('remote_logname'),request_method=data.get('request_method')
        #     )
        #     db.save()

    cursor = connection.cursor()
    #print "----------------------------------------"
    #t1= time.time()
    cursor.execute(strQuery)
    #t2=time.time()
    #print t2-t1
    #print "-----------------------------------"
    return HttpResponseRedirect('/home')
