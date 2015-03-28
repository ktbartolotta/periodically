define(
    ['jquery', 'knockout', 'elementModel'], 
    function ($, ko, ElementModel, PeriodicsCompViewModel) {

        function PeriodicalViewModel () {
            var self = this;

            // Data
            self.periodics = ko.observableArray();
            self.word = ko.observable();

            self.responseComp = ko.observable('emptyComp');
            self.resp = {};

            // Helpers
            self.ajax = function (uri, method, data) {
                var request = {
                    url: uri,
                    type: method,
                    dataType: 'json',
                    contentType: 'application/json',
                    data: data ? ko.toJSON(data) : {}
                };
                return $.ajax(request);
            };

            self.get_periodics = function () {
                self.ajax(
                    "/periodic/" + self.word(),
                    'GET'
                )
                .done(function (data) {
                    console.log(JSON.stringify(data));

                    if (data.periodics) {
                        self.resp = data;
                        self.responseComp('emptyComp');
                        self.responseComp('periodicsComp');
                    }
                    else if (data.no_periodics) {
                        self.resp = data;
                        self.responseComp('emptyComp');
                        self.responseComp('noPeriodicsComp');
                    }
                })
                .fail(function (xhr, status, error) {
                    console.log(status + ' ' + error);
                });
            };

           
        };

         // Components
        ko.components.register('emptyComp' , {
            template: '<div></div>'
        });

        ko.components.register('periodicsComp', {

            viewModel: { require: "periodicsComp"},
            template: { require: "text!../templates/periodics.html"}

        });

        ko.components.register('noPeriodicsComp', {

            viewModel: { require: "noPeriodicsComp"},
            template: { require: "text!../templates/noPeriodics.html"}

        });

        ko.applyBindings(new PeriodicalViewModel(), $('#main')[0]);
});
