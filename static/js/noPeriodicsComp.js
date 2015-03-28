define(["knockout"], function (ko) {

    function NoPeriodicsCompViewModel (params) {
        var self = this;

        self.resp = params.resp;
        self.input = params.input;
        self.words = ko.observableArray(self.resp.no_periodics.suggestions);

        self.get_periodics = function (word) {
            self.input(word);
        }
    };

    return NoPeriodicsCompViewModel;

});