# -*- encoding:UTF-8 -*-
#
# Splunk UI module python renderer
# This module is imported by the module loader (lib.module.ModuleMapper) into
# the splunk.appserver.mrsparkle.controllers.module.* namespace.
#

import controllers.module as module

import splunk, splunk.search, splunk.util, splunk.entity
import lib.util as util
import lib.i18n as i18n

import logging
logger = logging.getLogger('splunk.module.CustomResultsTable')

import math
import cgi

class CustomResultsTable(module.ModuleHandler):
    
    def generateResults(self, host_app, client_app, sid, count=1000, 
            offset=0, entity_name='results'):

        count = max(int(count), 0)
        offset = max(int(offset), 0)
        if not sid:
            raise Exception('CustomResultsTable.generateResults - sid not passed!')

        try:
            job = splunk.search.getJob(sid)
        except splunk.ResourceNotFound, e:
            logger.error('CustomResultsTable could not find job %s.' % sid)
            return _('<p class="resultStatusMessage">Could not retrieve search data.</p>')
        
        # output = []
        # output.append('<div class="CustomResultsTableWrapper">')
        # output.append('<table class="CustomResultsTable splTable">')
  
        # fieldNames = [x for x in getattr(job, entity_name).fieldOrder if (not x.startswith('_'))]
        
        # dataset = getattr(job, entity_name)[offset: offset+count]
        
        # for i, result in enumerate(dataset):
        #     output.append('<tr>')
        #     for field in fieldNames:
        #         output.append('<td')
        #         fieldValues = result.get(field, None)
        #         if fieldValues:
        #             output.append('>%s</td>' % fieldValues)
        #         else:
        #             output.append('></td>')
        #     output.append('</tr>')
        # output.append('</table></div>')

        # output = ''.join(output)

        # return output

        output = []
         
        output.append('''  {
        "tooltip" : {
            "trigger": "axis"
        },
        "legend": {
            "data":["蒸发量","降水量"]
        },
        "toolbox": {
            "show" : true,
            "feature" : {
                "mark" : {"show": true},
                "dataView" : {"show": true, "readOnly": false},
                "magicType" : {"show": true, "type": ["line", "bar"]},
                "restore" : {"show": true},
                "saveAsImage" : {"show": true}
            }
        },
        "calculable" : true,
        "xAxis" : [
            {
                "type" : "category",
                "data" : ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
            }
        ],
        "yAxis" : [
            {
                "type" : "value",
                "splitArea" : {"show" : true}
            }
        ],
        "series" : [
            {
                "name":"蒸发量",
                "type":"bar",
                "data":[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
            },
            {
                "name":"降水量",
                "type":"bar",
                "data":[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
            }
        ]
    } ''')
        output = ''.join(output)

        return output
      