// A simple results table
Splunk.Module.CustomResultsTable = $.klass(Splunk.Module.DispatchingModule, {

    /*
     * overriding initialize to set up references and event handlers.
     */
    initialize: function($super, container) {
        $super(container);
        this.myParam = this.getParam("myParam");
        this.resultsContainer = this.container;
    },

    onJobDone: function(event) {
        this.getResults();
    },

    getResultParams: function($super) {
        var params = $super();
        var context = this.getContext();
        var search = context.get("search");
        var sid = search.job.getSearchId();

        if (!sid) this.logger.error(this.moduleType, "Assertion Failed.");

        params.sid = sid;
        return params;
    },

    renderResults: function($super, htmlFragment) {
        if (!htmlFragment) {
            this.resultsContainer.html('No content available.');
            return;
        }
        require.config({
            paths:{ 
                echarts:'./js/echarts',
                'echarts/chart/bar' : './js/echarts-map',
                'echarts/chart/line': './js/echarts-map',
                'echarts/chart/map' : './js/echarts-map'
            }
        });
    
        // Step:4 require echarts and use it in the callback.
        // Step:4 动态加载echarts然后在回调函数中开始使用，注意保持按需加载结构定义图表路径
        require(
            [
                'echarts',
                'echarts/chart/bar',
                'echarts/chart/line',
                'echarts/chart/map'
            ],
            function (ec) {
                //--- 折柱 ---
                var myChart = ec.init(document.getElementById('main'));
                var jsonObj = eval("(" + htmlFragment + ")")
                myChart.setOption(jsonObj);
                
         
            }
        );
    }
})
